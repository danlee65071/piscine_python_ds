#!/bin/sh

< ../ex00/hh.json jq -r '.items | map({id: .id, created_at: .created_at, name: .name, has_test: .has_test, alternate_url: .alternate_url})' > filter.jq
< filter.jq jq -r '(map(keys_unsorted) | add | .[0:5]) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv' > hh.csv
rm -rf hh.json
