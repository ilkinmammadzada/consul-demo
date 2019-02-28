#!/bin/bash

mongo_secondary=$(mongo --quiet --eval 'JSON.stringify(db.isMaster())' | jq -r .secondary 2> /dev/null)
if [[ $mongo_secondary == false ]]; then
    exit 123
fi
