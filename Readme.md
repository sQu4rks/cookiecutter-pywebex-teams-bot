# cookiecutter-pywebex-teams-bot

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/sQu4rks/cookiecutter-pywebex-teams-bot)

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to easily create deployable Webex Teams bots in python. 

## Features 
Features include

* Fully customizable setup of webhooks from a configuration file using [webhooksimple](https://github.com/CiscoSE/webhooksimple)
* Comes with support for [adaptive cards](https://adaptivecards.io/) in native python (using [pyadaptivecards](https://github.com/CiscoSE/pyadaptivecards))
* Comes with `Dockerfile` and `docker-compose.yml` for container deployment
* [flask](https://github.com/pallets/flask)-based bot served by [gunicorn](https://gunicorn.org/)

## How to use

Create a new project based on this cookiecutter by issuing the following command

```bash
$ cookiecutter https://github.com/sQu4rks/cookiecutter-pywebex-teams-bot
```

### For development
In order to develop your bot you will want to make it able to receive [webhooks](https://developer.webex.com/docs/api/guides/webhooks). To do so you need a way of receiving http requests i.e. [ngrok](https://ngrok.com/) or [serveo](http://serveo.net/). You will also need a bot access token that you can obtain from [developer.webex.com](https://developer.webex.com). 

To setup your local machine for development just run 

```bash
$ source developer_setup.sh
```

This script will ask you for your bot access token and your remote prefix i.e. `https://d342d393.ngrok.io` (no trailing slash). 

The template code comes prepared with functions to handle all webhooks available within the Webex Teams API and you can automate the setup of the webhooks using [webhooksimple](https://github.com/CiscoSE/webhooksimple). To setup all webhooks simply run

```bash
$ python3 -m webhooksimple sync
```
inside of your project directory. 

Your bot code is ready to be modified in `bot.py`. Happy coding!

### For deployment
Once you have finished your bot you can create a docker image using the `deployment_setup.sh` script. 

This script will 

1. Log you into docker hub
2. Create a new build of your bot image
3. Push the newly created image to docker hub. 

When deploying the container make sure to set the `WEBEX_TEAMS_ACCESS_TOKEN` and `REMOTE_PREFIX` environment variables. The `entrypoint.sh` script used by the container upon start will setup the webhooks according to these environment variables. 

## Additional options

### Customizing which webhooks are setup
You can customize the webhooks you want to use. In order to keep your deployment and development environment the same you should not edit the `vars.yml` file that is created during the developer setup but rather edit the `vars.yml.conftpl` file that will be used during deployment on your remote host. 

1. Delete the `vars.yml` file (i.e. `rm vars.yml`)
2. Edit the `vars.yml.conftpl` file. In the *webhooks* section at the bottom of the file you can find the list of resources (i.e. *messages, rooms, memberships*) and events (i.e. *created, deleted*). Delete (or comment out) all events and or resources you don't need.
3. Run config templater to create a new `vars.yml` file by issuing the `python3 -m config_templater` command. 
4. Run `python3 -m webhooksimple setup` to delete all webhooks currently registered for your bot and overwrite them with the newly specified webhooks.

### Customize the function skeletons provided by the bot

In the bot directory is a file called `template.py` that can be used to create new function stubs for each of the webhooks specified in `vars.yml`. Simply run the script and copy&paste the resulting code into the `bot.py` file. 
