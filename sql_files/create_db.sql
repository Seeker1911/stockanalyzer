-- noinspection SqlNoDataSourceInspectionForFile

drop database if exists tutorial;
CREATE database tutorial owner postgres;
\connect tutorial
-- Extend the database with TimescaleDB
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;
-- We start by creating a regular SQL table

CREATE TABLE conditions (
  time        TIMESTAMPTZ       NOT NULL,
  location    TEXT              NOT NULL,
  temperature DOUBLE PRECISION  NULL,
  humidity    DOUBLE PRECISION  NULL
);
-- This creates a hypertable that is partitioned by time
--   using the values in the `time` column.

SELECT create_hypertable('conditions', 'time');
INSERT INTO conditions(time, location, temperature, humidity)
  VALUES (NOW(), 'office', 70.0, 50.0);
