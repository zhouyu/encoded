select version()
select current_schema()
select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s


DROP TABLE ipstemcell_line
COMMIT

DROP TABLE single_cell
COMMIT

DROP TABLE validation_document
COMMIT

DROP TABLE biosample_relationship
COMMIT

DROP TABLE tissue
COMMIT

DROP TABLE cell_line
COMMIT

DROP TABLE validation
COMMIT

DROP TABLE human_donor
COMMIT

DROP TABLE mouse_donor
COMMIT

DROP TABLE biosample
COMMIT

DROP TABLE antibody
COMMIT

DROP TABLE protocol
COMMIT
SELECT relname FROM pg_class c join pg_namespace n on n.oid=c.relnamespace where relkind='S' and n.nspname=current_schema() and relname=%(name)s

DROP SEQUENCE source_no_seq
COMMIT

DROP TABLE source
COMMIT

DROP TABLE treat_treat_details
COMMIT

DROP TABLE target
COMMIT

DROP TABLE donor
COMMIT

DROP TABLE document
COMMIT

DROP TABLE treatment
COMMIT

DROP TABLE organism
COMMIT

DROP TABLE modification
COMMIT

DROP TABLE treatment_details
COMMIT
SELECT relname FROM pg_class c join pg_namespace n on n.oid=c.relnamespace where relkind='S' and n.nspname=current_schema() and relname=%(name)s

DROP SEQUENCE url_no_seq
COMMIT

DROP TABLE url
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE biosample_ontologies
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE treatment_ontologies
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE conc_units
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE time_units
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE genders
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE protocol_types
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE document_file_types
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE antibody_clonality
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE modification_types
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE modifiable_amino_acids
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE validation_states
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE antibody_validation_methods
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


DROP TYPE review_states
COMMIT
select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where n.nspname=current_schema() and relname=%(name)s

SELECT relname FROM pg_class c join pg_namespace n on n.oid=c.relnamespace where relkind='S' and n.nspname=current_schema() and relname=%(name)s

CREATE SEQUENCE url_no_seq
COMMIT

CREATE TABLE url (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	url_no INTEGER NOT NULL,
	url_type VARCHAR NOT NULL,
	url VARCHAR NOT NULL,
	PRIMARY KEY (url_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE treatment_ontologies AS ENUM ('ChEBI','Protein')
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE conc_units AS ENUM ('mM','uM','nM','pm','mg/ml','ug/ml','ng/ml','U/ml','percent')
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE time_units AS ENUM ('s','m','hr','d')
COMMIT

CREATE TABLE treatment_details (
	treatment_details_no SERIAL NOT NULL,
	ontology treatment_ontologies NOT NULL,
	ontology_no VARCHAR NOT NULL,
	ontology_term VARCHAR NOT NULL,
	concentration FLOAT,
	concentration_units conc_units,
	duration FLOAT,
	duration_units time_units,
	PRIMARY KEY (treatment_details_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE modification_types AS ENUM ('GFP-fusion','acetylation','phosphoryation','ubiquitinylation','monomethlyation','dimethylation','trimethlyation')
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE modifiable_amino_acids AS ENUM ('E','K','R','D','S','T','C','H')
COMMIT

CREATE TABLE modification (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	modification_no SERIAL NOT NULL,
	modification_type modification_types NOT NULL,
	position INTEGER,
	residue modifiable_amino_acids,
	PRIMARY KEY (modification_no)
)


COMMIT

CREATE TABLE organism (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	organism_no SERIAL NOT NULL,
	organism_name VARCHAR NOT NULL,
	taxon_no INTEGER NOT NULL,
	PRIMARY KEY (organism_no)
)


COMMIT

CREATE TABLE treatment (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	treatment_no SERIAL NOT NULL,
	treatment_name VARCHAR NOT NULL,
	treatment_description VARCHAR,
	submitted_by VARCHAR NOT NULL,
	PRIMARY KEY (treatment_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE document_file_types AS ENUM ('pdf','doc','docx','rtf','txt','rst')
COMMIT

CREATE TABLE document (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	document_no SERIAL NOT NULL,
	document_type document_file_types NOT NULL,
	submitted_by VARCHAR NOT NULL,
	file_location VARCHAR,
	document BYTEA,
	PRIMARY KEY (document_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE genders AS ENUM ('Male','Female','Unknown')
COMMIT

CREATE TABLE donor (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	donor_no SERIAL NOT NULL,
	organism_no INTEGER NOT NULL,
	age VARCHAR,
	gender genders,
	PRIMARY KEY (donor_no),
	FOREIGN KEY(organism_no) REFERENCES organism (organism_no)
)


COMMIT

CREATE TABLE target (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	target_no SERIAL NOT NULL,
	target_label VARCHAR NOT NULL,
	lable_stem VARCHAR,
	symbol VARCHAR NOT NULL,
	organism_no INTEGER NOT NULL,
	target_class VARCHAR,
	modification_no INTEGER,
	PRIMARY KEY (target_no),
	FOREIGN KEY(organism_no) REFERENCES organism (organism_no),
	FOREIGN KEY(modification_no) REFERENCES modification (modification_no)
)


COMMIT

CREATE TABLE treat_treat_details (
	treat_treat_details_no SERIAL NOT NULL,
	details_no INTEGER,
	treatment_no INTEGER,
	PRIMARY KEY (treat_treat_details_no),
	FOREIGN KEY(details_no) REFERENCES treatment_details (treatment_details_no),
	FOREIGN KEY(treatment_no) REFERENCES treatment (treatment_no)
)


COMMIT
SELECT relname FROM pg_class c join pg_namespace n on n.oid=c.relnamespace where relkind='S' and n.nspname=current_schema() and relname=%(name)s

CREATE SEQUENCE source_no_seq
COMMIT

CREATE TABLE source (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	source_no INTEGER NOT NULL,
	source_name VARCHAR NOT NULL,
	url_no INTEGER,
	PRIMARY KEY (source_no),
	FOREIGN KEY(url_no) REFERENCES url (url_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE protocol_types AS ENUM ('growth','extraction','excision','purification')
COMMIT

CREATE TABLE protocol (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	protocol_no SERIAL NOT NULL,
	protocol_name VARCHAR NOT NULL,
	protocol_type protocol_types NOT NULL,
	protocol_description VARCHAR,
	document_no INTEGER NOT NULL,
	submitted_by VARCHAR NOT NULL,
	PRIMARY KEY (protocol_no),
	FOREIGN KEY(document_no) REFERENCES document (document_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE antibody_clonality AS ENUM ('monoclonal','polyclonal')
COMMIT

CREATE TABLE antibody (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	antibody_no SERIAL NOT NULL,
	antibody_acc VARCHAR NOT NULL,
	source_no INTEGER,
	product_no VARCHAR NOT NULL,
	lot_no VARCHAR,
	submitted_by VARCHAR NOT NULL,
	isotype VARCHAR,
	clonality antibody_clonality,
	purification VARCHAR,
	antigen_description VARCHAR,
	epitope VARCHAR,
	host_organism_no INTEGER,
	PRIMARY KEY (antibody_no),
	FOREIGN KEY(source_no) REFERENCES source (source_no),
	FOREIGN KEY(host_organism_no) REFERENCES organism (organism_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE biosample_ontologies AS ENUM ('UBERON','CLO','EFO')
COMMIT

CREATE TABLE biosample (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	biosample_no SERIAL NOT NULL,
	biosample_acc VARCHAR NOT NULL,
	biosample_type VARCHAR NOT NULL,
	source_no INTEGER NOT NULL,
	product_no VARCHAR NOT NULL,
	lot_no VARCHAR,
	submitted_by VARCHAR NOT NULL,
	treatment_no INTEGER,
	ontology biosample_ontologies NOT NULL,
	ontology_no VARCHAR NOT NULL,
	ontology_term VARCHAR NOT NULL,
	PRIMARY KEY (biosample_no),
	FOREIGN KEY(source_no) REFERENCES source (source_no),
	FOREIGN KEY(treatment_no) REFERENCES treatment (treatment_no)
)


COMMIT

CREATE TABLE mouse_donor (
	donor_no INTEGER NOT NULL,
	strain VARCHAR,
	PRIMARY KEY (donor_no),
	FOREIGN KEY(donor_no) REFERENCES donor (donor_no)
)


COMMIT

CREATE TABLE human_donor (
	donor_no INTEGER NOT NULL,
	ethnicity VARCHAR,
	health_status VARCHAR,
	external_donor_no INTEGER,
	PRIMARY KEY (donor_no),
	FOREIGN KEY(donor_no) REFERENCES donor (donor_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE validation_states AS ENUM ('validated','not validated','invalid')
COMMIT

CREATE TABLE validation (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	validation_no SERIAL NOT NULL,
	antibody_no INTEGER NOT NULL,
	target_no INTEGER NOT NULL,
	validation_status validation_states,
	PRIMARY KEY (validation_no),
	FOREIGN KEY(antibody_no) REFERENCES antibody (antibody_no),
	FOREIGN KEY(target_no) REFERENCES target (target_no)
)


COMMIT

CREATE TABLE cell_line (
	biosample_no INTEGER NOT NULL,
	organism_no INTEGER,
	growth_protocol_no INTEGER,
	is_stable BOOLEAN NOT NULL,
	PRIMARY KEY (biosample_no),
	FOREIGN KEY(biosample_no) REFERENCES biosample (biosample_no),
	FOREIGN KEY(organism_no) REFERENCES organism (organism_no),
	FOREIGN KEY(growth_protocol_no) REFERENCES protocol (protocol_no)
)


COMMIT

CREATE TABLE tissue (
	biosample_no INTEGER NOT NULL,
	date_obtained DATE NOT NULL,
	donor_no INTEGER,
	extraction_protocol_no INTEGER,
	PRIMARY KEY (biosample_no),
	FOREIGN KEY(biosample_no) REFERENCES biosample (biosample_no),
	FOREIGN KEY(donor_no) REFERENCES donor (donor_no),
	FOREIGN KEY(extraction_protocol_no) REFERENCES protocol (protocol_no)
)


COMMIT

CREATE TABLE biosample_relationship (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	biosample_rel_no SERIAL NOT NULL,
	biosample_type VARCHAR,
	biosample_no INTEGER,
	related_biosample_no INTEGER,
	PRIMARY KEY (biosample_rel_no),
	FOREIGN KEY(biosample_no) REFERENCES biosample (biosample_no),
	FOREIGN KEY(related_biosample_no) REFERENCES biosample (biosample_no)
)


COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE antibody_validation_methods AS ENUM ('ENCODE2','To be added','Immunoflurescense','Immunoprecipitation','Western Blot','Correlation','Mass-Spec')
COMMIT

            SELECT EXISTS (
                SELECT * FROM pg_catalog.pg_type t
                WHERE t.typname = %(typname)s
                AND pg_type_is_visible(t.oid)
                )


CREATE TYPE review_states AS ENUM ('submitted','change_request','approved','rejected')
COMMIT

CREATE TABLE validation_document (
	gid UUID NOT NULL,
	date_created TIMESTAMP WITHOUT TIME ZONE NOT NULL,
	created_by VARCHAR NOT NULL,
	is_current BOOLEAN NOT NULL,
	validation_document_no SERIAL NOT NULL,
	validation_no INTEGER,
	method antibody_validation_methods NOT NULL,
	document_no INTEGER,
	review_status review_states NOT NULL,
	reviewed_by VARCHAR,
	PRIMARY KEY (validation_document_no),
	FOREIGN KEY(validation_no) REFERENCES validation (validation_no),
	FOREIGN KEY(document_no) REFERENCES document (document_no)
)


COMMIT

CREATE TABLE single_cell (
	biosample_no INTEGER NOT NULL,
	purification_protocol_no INTEGER,
	excision_protocol_no INTEGER,
	PRIMARY KEY (biosample_no),
	FOREIGN KEY(biosample_no) REFERENCES tissue (biosample_no),
	FOREIGN KEY(purification_protocol_no) REFERENCES protocol (protocol_no),
	FOREIGN KEY(excision_protocol_no) REFERENCES protocol (protocol_no)
)


COMMIT

CREATE TABLE ipstemcell_line (
	biosample_no INTEGER NOT NULL,
	PRIMARY KEY (biosample_no),
	FOREIGN KEY(biosample_no) REFERENCES cell_line (biosample_no)
)


COMMIT
