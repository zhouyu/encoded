import pyes

from api import collections

import logging
log = logging.getLogger(__name__)


def includeme(config):

    settings = config.registry.settings

    # Elastic Search connection
    connection_string = '%(host)s:%(port)s' % {
        'host': settings['elasticsearch.host'],
        'port': settings['elasticsearch.port'],
    }
    log.info("Connecting to Elastic Search on %s", connection_string)
    connection = pyes.ES(connection_string)
    settings['elasticsearch'] = connection

    # Create indexes and mappings
    create_indexes(connection)

''' mapping example'''
USER_MAPPING = {
    'id': {
        'type': 'string',
        'store': 'yes',
        'index': 'not_analyzed',
    },
    'email': {
        'type': 'string',
        'store': 'yes',
        'index': 'not_analyzed',
    },
    'registered': {
        'type': 'date',
        'store': 'yes',
    },
}


def create_indexes(es):

    for collection in collections.keys():
        es.create_index_if_missing(collection)
        if collection == 'users':  #hack
            es.put_mapping('usertype', {'properties': USER_MAPPING},
            [collection])

    '''
    es.create_index_if_missing('plants')
    es.put_mapping('planttype', {'properties': PLANT_MAPPING}, ['plants'])

    es.create_index_if_missing('snaps')
    es.put_mapping('snaptype', {'properties': SNAP_MAPPING}, ['snaps'])
    '''