CREATE TYPE conc_units AS ENUM ('mM','uM','nM','pm','mg/ml','ug/ml','ng/ml','U/ml','percent')
CREATE TYPE time_units AS ENUM ('s','m','hr','d')

CREATE TABLE treatment (
    date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    created_by VARCHAR NOT NULL,
    is_current BOOLEAN NOT NULL,
    treatment_id SERIAL NOT NULL,
    treatment_name VARCHAR NOT NULL,
    chebi_id VARCHAR NOT NULL,
    concentration FLOAT,
    concentration_units conc_units,
    duration FLOAT,
    duration_units time_units,
    submitted_by VARCHAR NOT NULL,
    PRIMARY KEY (treatment_id)
)

CREATE TABLE source (
    date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    created_by VARCHAR NOT NULL,
    is_current BOOLEAN NOT NULL,
    source_id SERIAL NOT NULL,
    source_name VARCHAR NOT NULL,
    url_id INTEGER,
    PRIMARY KEY (source_id),
    FOREIGN KEY(url_id) REFERENCES url (url_id)
)


CREATE TYPE protocol_types AS ENUM ('growth','extraction','excision','purification')

CREATE TABLE protocol (
    date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    created_by VARCHAR NOT NULL,
    is_current BOOLEAN NOT NULL,
    protocol_id SERIAL NOT NULL,
    protocol_name VARCHAR NOT NULL,
    protocol_type protocol_types NOT NULL,
    protocol_description VARCHAR,
    document_id INTEGER NOT NULL,
    submitted_by VARCHAR NOT NULL,
    PRIMARY KEY (protocol_id),
    FOREIGN KEY(document_id) REFERENCES document (document_id)
)

 CREATE TYPE genders AS ENUM ('Male','Female','Unknown')

CREATE TABLE donor (
    date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    created_by VARCHAR NOT NULL,
    is_current BOOLEAN NOT NULL,
    donor_id SERIAL NOT NULL,
    organism_id INTEGER,
    age VARCHAR,
    gender genders,
    PRIMARY KEY (donor_id),
    FOREIGN KEY(organism_id) REFERENCES organism (organism_id)
)


CREATE TABLE human_donor (
    donor_id INTEGER NOT NULL,
    ethnicity VARCHAR,
    health_status VARCHAR,
    external_donor_id INTEGER,
    PRIMARY KEY (donor_id),
    FOREIGN KEY(donor_id) REFERENCES donor (donor_id)
)

CREATE TABLE mouse_donor (
    donor_id INTEGER NOT NULL,
    strain VARCHAR,
    PRIMARY KEY (donor_id),
    FOREIGN KEY(donor_id) REFERENCES donor (donor_id)
)

 CREATE TYPE ontologies AS ENUM ('UBERON','CLO','EFO')

CREATE TABLE biosample (
    date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    created_by VARCHAR NOT NULL,
    is_current BOOLEAN NOT NULL,
    biosample_id SERIAL NOT NULL,
    biosample_type VARCHAR NOT NULL,
    source_id INTEGER,
    product_id VARCHAR NOT NULL,
    lot_id VARCHAR,
    submitted_by VARCHAR NOT NULL,
    ontology ontologies NOT NULL,
    ontology_id VARCHAR NOT NULL,
    ontology_term VARCHAR NOT NULL,
    PRIMARY KEY (biosample_id),
    FOREIGN KEY(source_id) REFERENCES source (source_id)
)

CREATE TABLE tissue (
    biosample_id INTEGER NOT NULL,
    date_obtained DATE NOT NULL,
    donor_id INTEGER,
    extraction_protocol_id INTEGER,
    PRIMARY KEY (biosample_id),
    FOREIGN KEY(biosample_id) REFERENCES biosample (biosample_id),
    FOREIGN KEY(donor_id) REFERENCES human_donor (donor_id),
    FOREIGN KEY(extraction_protocol_id) REFERENCES protocol (protocol_id)
)

CREATE TABLE biosample_treatment (
    biosample_id INTEGER,
    treatment_id INTEGER,
    FOREIGN KEY(biosample_id) REFERENCES biosample (biosample_id),
    FOREIGN KEY(treatment_id) REFERENCES treatment (treatment_id)
)

CREATE TABLE cell_line (
    biosample_id INTEGER NOT NULL,
    organism_id INTEGER,
    growth_protocol_id INTEGER,
    is_stable BOOLEAN NOT NULL,
    PRIMARY KEY (biosample_id),
    FOREIGN KEY(biosample_id) REFERENCES biosample (biosample_id),
    FOREIGN KEY(organism_id) REFERENCES organism (organism_id),
    FOREIGN KEY(growth_protocol_id) REFERENCES protocol (protocol_id)
)

CREATE TABLE biosample_relationship (
    date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    created_by VARCHAR NOT NULL,
    is_current BOOLEAN NOT NULL,
    biosample_rel_id SERIAL NOT NULL,
    biosample_type VARCHAR,
    biosample_id INTEGER,
    related_biosample_id INTEGER,
    PRIMARY KEY (biosample_rel_id),
    FOREIGN KEY(biosample_id) REFERENCES biosample (biosample_id),
    FOREIGN KEY(related_biosample_id) REFERENCES biosample (biosample_id)
)

CREATE TABLE ipstemcell_line (
    biosample_id INTEGER NOT NULL,
    PRIMARY KEY (biosample_id),
    FOREIGN KEY(biosample_id) REFERENCES cell_line (biosample_id)
)

CREATE TABLE single_cell (
    biosample_id INTEGER NOT NULL,
    purification_protocol_id INTEGER,
    excision_protocol_id INTEGER,
    PRIMARY KEY (biosample_id),
    FOREIGN KEY(biosample_id) REFERENCES tissue (biosample_id),
    FOREIGN KEY(purification_protocol_id) REFERENCES protocol (protocol_id),
    FOREIGN KEY(excision_protocol_id) REFERENCES protocol (protocol_id)
)

