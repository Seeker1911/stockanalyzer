#!/usr/bin/env bash

psql -U postgres -h localhost -f sql_files/create_db.sql
psql -U postgres -h localhost -d testdb
