from pyramid.settings import asbool
from pyramid.config import Configurator
from pyramid.decorator import reify
from pyramid.request import Request as BaseRequest
from pyramid.security import authenticated_userid

from sqlalchemy import engine_from_config
from .storage import (
    Base,
    DBSession,
    )
STATIC_MAX_AGE = 0


class Request(BaseRequest):
    """
    Custom request class
    """

    @reify
    def es(self):
        """
        Get the Elastic Search connection
        """
        settings = self.registry.settings
        return settings['elasticsearch']

    @reify
    def user(self):
        """
        Get the logged in user
        """
        email = authenticated_userid(self)
        if email is not None:
            pass
            # get email out of db rs =...
            res = [email]
            if len(res) == 0:
                pass
                ## create new user doc
                '''
                doc = {
                    'id': str(uuid4()),
                    'email': email,
                    'registered': datetime.datetime.utcnow(),
                }
                # store in DB
                res = self.es.index(doc, 'users', 'usertype', doc['id'])
                if res['ok'] == False:
                    logger.error("Signup failure")
                    logger.error(res)
                    raise HTTPServerError()
                self.db.refresh()
                res = [namedtuple('User', doc.keys())(**doc)]
                '''

            if len(res) > 0:
                return res[0]

        return None


def static_resources(config):
    config.add_static_view('static', 'static', cache_max_age=STATIC_MAX_AGE)

    favicon_path = '/static/img/favicon.ico'
    if config.route_prefix:
        favicon_path = '/%s%s' % (config.route_prefix, favicon_path)
    config.add_route('favicon.ico', 'favicon.ico')

    def favicon(request):
        subreq = request.copy()
        subreq.path_info = favicon_path
        response = request.invoke_subrequest(subreq)
        return response

    config.add_view(favicon, route_name='favicon.ico')


def tests_js(config):
    config.add_static_view('tests/js', 'tests/js', cache_max_age=STATIC_MAX_AGE)


def configure_engine(settings):
    engine_url = settings.get('sqlalchemy.url')
    engine_opts = {}
    # http://docs.sqlalchemy.org/en/rel_0_8/dialects/sqlite.html#using-a-memory-database-in-multiple-threads
    if engine_url == 'sqlite://':
        from sqlalchemy.pool import StaticPool
        engine_opts.update(
            connect_args={'check_same_thread': False},
            poolclass=StaticPool,
            )
    engine = engine_from_config(settings, 'sqlalchemy.', **engine_opts)
    Base.metadata.create_all(engine)
    DBSession.configure(bind=engine)
    return engine


def load_sample_data(app):
    from .tests.sample_data import load_sample
    from webtest import TestApp
    testapp = TestApp(app)
    load_sample(testapp)


def load_workbook(app, workbook_filename):
    from .loadxl import load_all
    from webtest import TestApp
    testapp = TestApp(app)
    load_all(testapp, workbook_filename)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(
        settings=settings,
    )

    config.include('pyramid_tm')
    configure_engine(settings)

    # Render an HTML page to browsers and a JSON document for API clients
    config.add_renderer(None, 'encoded.renderers.PageOrJSON')
    config.add_renderer('null_renderer', 'encoded.renderers.NullRenderer')
    config.scan('encoded.renderers')
    config.set_request_factory(Request)
    config.include('.api')
    config.include('.authz')
    config.include('.elasticsearch')

    config.include(static_resources)
    config.include(tests_js)

    app = config.make_wsgi_app()

    if asbool(settings.get('load_sample_data', False)):
        load_sample_data(app)

    workbook_filename = settings.get('load_workbook', '')
    if workbook_filename:
        load_workbook(app, workbook_filename)

    return app
