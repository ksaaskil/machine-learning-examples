#!/usr/bin/env bash
set -eux

DIR=datasets/jena_climate
mkdir -p $DIR
DEST_FILE=$DIR/jena_climate_2009_2016.csv

if [ ! -f "${DEST_FILE}" ]; then
    echo "File ${DEST_FILE} does not exist, fetching."
    cd $DIR
    wget https://s3.amazonaws.com/keras-datasets/jena_climate_2009_2016.csv.zip
    # Answer yes in case dataset exists already
    yes | unzip jena_climate_2009_2016.csv.zip
    rm jena_climate_2009_2016.csv.zip
else
    echo "File ${DEST_FILE} exists, skipping fetching."
fi
