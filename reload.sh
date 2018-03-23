#!/usr/bin/env sh

source .env/bin/activate
git pull origin master
sh ./run.sh