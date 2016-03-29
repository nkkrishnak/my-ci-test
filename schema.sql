CREATE TABLE journal (
	eraid integer not null,
	title varchar2(2000) not null,
	foreign_title varchar2(2000),
	rank char(2) check (rank in ('A*', 'A', 'B', 'C')),
	multidisciplinary_ind char(1) default 'N' check (multidisciplinary_ind in ('Y', 'N')),
	peer_reviewed_ind char(1),
	scholarly_ind char(1),
	CONSTRAINT journal_pk PRIMARY KEY (eraid)
);

CREATE TABLE journal_for (
	eraid integer not null,
	-- a era discipline is only four sigificant figures, however we will link it to
	-- CR table 'classification_code' which has all six digits, so we will record it
	-- here with six for easy linkage
	discipline char(6) not null check (SUBSTR(discipline,5,2) = '00'),
	column_id integer not null check (column_id > 0),
	CONSTRAINT journal_for_pk PRIMARY KEY (eraid, discipline),
	CONSTRAINT journal_for_fk FOREIGN KEY (eraid) REFERENCES journal (eraid)
);

CREATE TABLE journal_issn (
	eraid integer not null,
	issn varchar2(20) not null,
	column_id integer not null check (column_id > 0),
	valid_ind char(1) default 'N' check (valid_ind in ('Y', 'N')),
	CONSTRAINT journal_issn_pk PRIMARY KEY (issn),
	CONSTRAINT journal_issn_fk FOREIGN KEY (eraid) REFERENCES journal (eraid)
);
