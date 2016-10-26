#!/usr/bin/env bash
set -ve
pushd output
git fetch
git checkout master
git reset origin/master --hard
git ls-files -z | xargs -0 rm -f
popd

python main.py

pushd output
git add -A
if [ -n "$(git status --porcelain)" ]; then
    git commit --message="Updated `date -u`"
fi
popd
