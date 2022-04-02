#!/bin/sh

curl https://api.hh.ru/vacancies/\?text\=data+scientist\&search_field\=name\&per_page\=20 | jq > hh.json
< hh.json jq -r '.items | map({id: .id, created_at: .created_at, name: .name, has_test: .has_test, alternate_url: .alternate_url})' > filter.jq
< filter.jq jq -r '(map(keys_unsorted) | add | .[0:5]) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv' > hh.csv
rm -rf hh.json
rm -rf filter.jq
rm -rf hh_sorted.csv
< hh.csv head -n 1 > hh_sorted.csv
< hh.csv tail -n20 | sort -t , -k2 -k1 >> hh_sorted.csv
rm -rf hh.csv
