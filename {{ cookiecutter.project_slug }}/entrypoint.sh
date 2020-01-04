#!/bin/bash
# Create configuration files (see: https://github.com/sQu4rks/config_templater)
python -m config_templater 

# Create webhooks (see: https://github.com/CiscoSE/webhooksimple)
python -m webhookSimple setup

# Run gunicorn
gunicorn --bind 0.0.0.0:5000 --worker 4 bot:app
