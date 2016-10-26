#!/usr/bin/env bash
set -ve

eval "$(ssh-agent -s)"
chmod 600 deploy_key.pem
ssh-add deploy_key.pem

pushd output
git push git@github.com:petmac/terms-python-output.git
popd
