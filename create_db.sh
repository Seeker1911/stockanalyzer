#!/usr/bin/env bash

psql -U postgres -h localhost -f sql_files/create_db.sql
#source sql_files/create_db.sql
##-- Connect to the database
#\c tutorial
#
psql -U postgres -h localhost -d tutorial
