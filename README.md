# 4DCleaner
This bot was made to fix misconfigured archive channels

## How to use
1. `git clone https://github.com/showierdata9978/4DCleaner.git`
2. `cd 4DCleaner`
3. `pip install -r requirements.txt`
4. `python main.py`

## How to configure
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the bot tab
4. Create a new bot
5. Copy the token
6. Go to the OAuth2 tab, and select the bot scope
7. Select the `manage_messages`, and `manage_channels` permissions
8. Add an env variable called `TOKEN` and paste the token as the value
9. copy the category id of the category you want to be cleaned, and paste that into the `ARCHIVED` env variable
10. copy your guild id, and paste that into the `GUILD` env variable

## Features

- [x] Delete messages in archived channels (only new messages, and does not effect people with the `manage_messages` permission)
- [x] info slash command
