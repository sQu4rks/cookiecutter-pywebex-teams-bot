#!/bin/bash
echo "Installing dependencies"
pip3 install -r requirements.txt
echo "What is your WEBEX Teams access token?"
read access_token
export WEBEX_TEAMS_ACCESS_TOKEN=$access_token
echo "Webex Teams token set to $access_token"
echo "What is your development webhook endpoint(i.e. ngrok)"
read remote
echo "Remote prefix set to $remote"
export REMOTE_PREFIX="$remote"
echo "Generating vars.yml file"
python3 -m config_templater

