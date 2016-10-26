#!/usr/bin/env bash
set -ve
pushd output
git pull origin master
git ls-files -z | xargs -0 rm -f
popd

python main.py

pushd output
git add -A
git commit --message="Updated `date -u`"
popd
