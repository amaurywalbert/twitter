#!/bin/bash

for line in `data01.json`; do
	python -m json.tool line
done
