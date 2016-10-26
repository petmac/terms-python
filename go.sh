#!/usr/bin/env bash
set -ve
pushd output
git checkout master
git pull origin master
git ls-files -z | xargs -0 rm -f
popd

python main.py

pushd output
git add -A
if [ -n "$(git status --porcelain)" ]; then
    git commit --message="Updated `date -u`"
fi
popd
