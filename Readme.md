# Saveget Zulip Bot

Simple Zulip bot that will save a given link with a given tag, and if you ask him for the tag he'll return you the url related to it

## Table of Contents
1. Implementation

## Implemetation

## Downloads
1. Clone the repository of saveget bot `git clone https://github.com/rcascante/zulip_saveget_bot.git`
2. Clone the respository of zulip bot api `git clone https://github.com/zulip/python-zulip-api.git`
3. Move the saveget folder in the python-zulip-api/zulip-bots/zulip_bots/bots


### Installation
1. Register a new bot user on the Zulip server's web interface.
   - Log in to the Zulip server
   - Navigate to Settings -> Your bots -> Add a new bot. Select Generic bot for bot type, fill out the form and click on Create bot
   - Your created bot will apper in "Active bots"
   - On your active bot Click on the little green download icon to download its configuration file zuliprc : zuliprc
   - Save zuliprc in  python-zulip-api/zulip-bots/
   
1. `cd python-zulip-api`
2. `python3 ./tools/provision` it'll install all the dependencies
3. `source zulip-api-py3-venv/activate` it'll start the virtualenvironment
4. `pip install peewee` an ORM for connecting model to database

## Usage
1. `cd python-zulip-api/zulip-bots/`
2.  `zulip-run-bot saveget --config-file zuliprc`
3. Go to your zulip chat and write @name_bot (the name that you gave to your active bot in the settings, it does not have to be the same as saveget)
4. Save url tag command: @name_bot save https://someurl.com sometag 
5. Get url from tag: @name_bot get sometag 



