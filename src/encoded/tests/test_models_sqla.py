def test_db_creation(sqla_engine):
    import encoded.models.sqla as sqla
    from encoded.models.sqla import (
        source,
        organism,
        protocol,
        antibody,
        biosample
        )
    sqla.Base.metadata.drop_all(sqla_engine)
    sqla.Base.metadata.create_all(sqla_engine)

