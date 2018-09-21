#!/bin/bash

shopt -s nullglob
for f in *.png
do
    cp -- "$f" "${f/%.png/_2.png}"
done

for f in *_2.png
do
    convert -alpha off "$f" "$f"
done
