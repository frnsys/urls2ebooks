#!/bin/bash

rm -rf out
mkdir out

echo "fetching articles..."
python get_articles.py

echo "making epubs..."
for file in out/*.md; do
    pandoc -S -o "${file/%.md/.epub}" "${file/%.md/_title.txt}" "${file}"
done

echo "making mobis..."
for file in out/*.epub; do
    ebook-convert "${file}" "${file/%.epub/.mobi}"
done

echo "done"