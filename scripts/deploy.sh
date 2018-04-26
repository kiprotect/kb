#!/bin/bash
if [ ! -n "$SERVER_SSH_KEY" ]; then exit 0; fi
mkdir ~/.ssh
chmod 700 ~/.ssh
mv gdpr-ssh-key ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
pip3 install -r requirements.txt
make prod
echo "Deploying $TRAVIS_BRANCH..."
if [ "$TRAVIS_BRANCH" = "master" ]; then export DIRECTORY=gdpr-portal-master; fi;
if [ "$TRAVIS_BRANCH" = "staging" ]; then export DIRECTORY=gdpr-portal-staging; fi;
if [ -n "$DIRECTORY" ]; then rsync --progress -r -e "ssh -o StrictHostKeyChecking=no -o identityFile=~/.ssh/id_rsa" build/* ${SERVER_SSH_USER}@${SERVER_SSH_IP}:${SERVER_SSH_DIRECTORY}/$DIRECTORY --delete; fi;
