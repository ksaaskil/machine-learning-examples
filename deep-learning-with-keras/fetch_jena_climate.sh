#!/usr/bin/env bash
set -eux

mkdir -p datasets/jena_climate
cd datasets/jena_climate
wget https://s3.amazonaws.com/keras-datasets/jena_climate_2009_2016.csv.zip
unzip jena_climate_2009_2016.csv.zip
rm jena_climate_2009_2016.csv.zip
