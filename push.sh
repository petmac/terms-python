#!/usr/bin/env bash
set -ve

pushd output
git push git@github.com:petmac/terms-python-output.git
popd
