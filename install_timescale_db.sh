#!/usr/bin/env bash
# set up the postgres/timescalDB on Mac OS X or Linux

# Mac (requires homebrew)
# Add the tap
brew tap timescale/tap

# Install
brew install timescaledb

# Post-install to move files to appropriate place
source /usr/local/bin/timescaledb_move.sh

# Modify postgresql.conf to uncomment this line and add required libraries.
shared_preload_libraries = 'timescaledb'

# Restart PostgreSQL instance
brew services restart postgresql

# Add a superuser postgres:
createuser postgres -s
# Connect to PostgreSQL, using a superuser named 'postgres' created above
#psql -U postgres -h localhost
