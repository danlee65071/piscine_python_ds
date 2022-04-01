#!/bin/sh

curl https://api.hh.ru/vacancies/\?text\=data+scientist\&search_field\=name\&per_page\=20 | jq > hh.json
