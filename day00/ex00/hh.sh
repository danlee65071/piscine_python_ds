#!/bin/sh

if [ $# -eq 1 ]; then
    curl https://api.hh.ru/vacancies/\?text\=${1// /%20}\&search_field\=name\&per_page\=20 | jq > hh.json
else
	echo "Usage: ./hh.sh 'data scientist'"
fi