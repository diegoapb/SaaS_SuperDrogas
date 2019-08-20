#!/bin/bash
echo "Cleanning Migrations"
cd apps
for i in $(ls -1); do
	rm -rf ${i}/migrations
	rm -rf ${i}/__pycache__
	mkdir -p ${i}/migrations
	touch ${i}/migrations/__init__.py
done
echo "Migrations cleaned"
cd ..