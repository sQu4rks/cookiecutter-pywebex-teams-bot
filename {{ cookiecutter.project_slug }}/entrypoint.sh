#!/bin/bash
# Create configuration files (see: https://github.com/sQu4rks/config_templater)
python -m config_templater 

# Create webhooks (see: https://github.com/CiscoSE/webhooksimple)
python -m webhooksimple setup

# Run gunicorn
gunicorn --bind 0.0.0.0:5000 --workers 4 bot:app
