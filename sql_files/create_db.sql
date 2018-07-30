-- noinspection SqlNoDataSourceInspectionForFile

drop database if exists testdb;
drop table if exists quotes;
CREATE database testdb owner postgres;
\connect testdb
-- Extend the database with TimescaleDB
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;
-- We start by creating a regular SQL table

CREATE TABLE quotes (
  time         TIMESTAMPTZ       NOT NULL,
  symbol       varchar(4)        NOT NULL,
  company_name TEXT              NOT NULL,
  close        DOUBLE PRECISION  NULL,
  open         DOUBLE PRECISION  NULL,
  high         DOUBLE PRECISION  NULL,
  low          DOUBLE PRECISION  NULL
);
-- This creates a hypertable that is partitioned by time
--   using the values in the `time` column.

SELECT create_hypertable('quotes', 'time');
INSERT INTO quotes(symbol, time, company_name, close, open, high, low)
  VALUES ('AAPL', NOW(), 'Apple computer', 700.0, 500.0, 1000.0, 200.0);
