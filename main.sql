CREATE TABLE temperatures (
   id INTEGER  PRIMARY KEY AUTOINCREMENT,
   value FLOAT NOT NULL,
   type TEXT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE isolations (
   id INTEGER  PRIMARY KEY AUTOINCREMENT,
   value FLOAT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE resistances (
   id INTEGER  PRIMARY KEY AUTOINCREMENT,
   value FLOAT NOT NULL,
   type TEXT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vibrations (
   id INTEGER  PRIMARY KEY AUTOINCREMENT,
   value FLOAT NOT NULL,
   type TEXT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pressures (
   id INTEGER  PRIMARY KEY AUTOINCREMENT,
   value FLOAT NOT NULL,
   type TEXT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE alarms (
   id INTEGER  PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/** TEST **/

INSERT INTO alarms (id, name) VALUES (
    1, 'Test Alarm'
);

CREATE TABLE configurations (
   id INTEGER  PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL UNIQUE,
   value TEXT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/** ISOLATION **/

INSERT INTO configurations(name, value) VALUES (
   'isolationCron', ''
);
INSERT INTO configurations(name, value) VALUES (
   'isolationPeriod', ''
);
INSERT INTO configurations(name, value) VALUES (
   'isolationDuration', '10'
);


/** RESISTANCE **/

INSERT INTO configurations(name, value) VALUES (
   'resistanceCron', ''
);
INSERT INTO configurations(name, value) VALUES (
   'resistancePeriod', ''
);
INSERT INTO configurations(name, value) VALUES (
   'resistanceDuration', '10'
);

/** WELL SENSOR **/

INSERT INTO configurations(name, value) VALUES (
   'wellCron', ''
);
INSERT INTO configurations(name, value) VALUES (
   'wellPeriod', ''
);
INSERT INTO configurations(name, value) VALUES (
   'wellEnabled', 'True'
);
INSERT INTO configurations(name, value) VALUES (
   'wellDuration', '10'
);

/** ALARMS **/

INSERT INTO configurations(name, value) VALUES (
   'isolationAlarmValue', '0'
);

INSERT INTO configurations(name, value) VALUES (
   'isolationVoltage', '500'
);

/** NUEVOS SCRIPTS **/

INSERT INTO configurations(name, value) VALUES (
   'loopDuration', '5'
);

INSERT INTO configurations(name, value) VALUES (
   'measure1', 'ISO'
);
INSERT INTO configurations(name, value) VALUES (
   'leadTime1', '1'
);
INSERT INTO configurations(name, value) VALUES (
   'periodMeasure1', '25'
);
INSERT INTO configurations(name, value) VALUES (
   'durationMeasure1', '1'
);


INSERT INTO configurations(name, value) VALUES (
   'measure2', 'ISO'
);
INSERT INTO configurations(name, value) VALUES (
   'leadTime2', '1'
);
INSERT INTO configurations(name, value) VALUES (
   'periodMeasure2', '25'
);
INSERT INTO configurations(name, value) VALUES (
   'durationMeasure2', '1'
);


INSERT INTO configurations(name, value) VALUES (
   'measure3', 'ISO'
);
INSERT INTO configurations(name, value) VALUES (
   'periodMeasure3', '25'
);
INSERT INTO configurations(name, value) VALUES (
   'durationMeasure3', '1'
);
