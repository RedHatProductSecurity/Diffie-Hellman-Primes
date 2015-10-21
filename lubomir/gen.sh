#! /bin/bash

BITS=$1
FILE="$BITS/$2"
if [ -s "$FILE" ]; then
    exit 0
fi

mkdir -p "$BITS"
echo "Generating $FILE"
exec nice -n15 openssl dhparam "$BITS" -text >>"$FILE" 2>/dev/null
