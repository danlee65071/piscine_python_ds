#!/bin/sh

< ../ex01/hh.csv head -n 1 > hh_sorted.csv
< ../ex01/hh.csv tail -n20 | sort -t , -k2 -k1n >> hh_sorted.csv
rm -rf hh.csv
