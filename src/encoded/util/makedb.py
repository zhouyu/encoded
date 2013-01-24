from sqlalchemy import *
from encoded.models.sqla import *
import encoded.models.sqla as sqla

e = create_engine('postgresql://hitz@localhost/dcc',echo=True)
sqla.Base.metadata.create_all(e)

