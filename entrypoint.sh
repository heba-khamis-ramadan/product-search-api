#!/bin/sh

# Wait for DB
./wait_for_db.sh

# Seed products
./seed.sh
