#!/bin/sh

echo '"name","count"' > hh_uniq_positions.csv
tail -n +2 "../ex03/hh_positions.csv" | cut -f 3 -d ',' | sort | uniq -ci | while read -r line ; do words=($line); echo "${words[1]}","${words[0]}" >> hh_uniq_positions.csv ; done
