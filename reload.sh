#!/usr/bin/env sh

cd casting/
source .env/bin/activate
git pull origin master
sh ./run.sh