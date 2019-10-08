#!/usr/bin/env bash

curl http://elasticsearch:9200
while [ "$?" = "7" ]
do
    sleep 4;
    echo '---';
    curl http://elasticsearch:9200;
done

elasticdump \
    --output=http://elasticsearch:9200/search_000 \
    --input=/search_dump.json\
    --type=data
