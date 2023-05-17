# VenusAnnouncementsBot

Announcements bot created for Venus Protocol Telegram groups.

# Telegram Forwarder

A simple Telegram Python bot running on Python3 to automatically forward messages from one chat to another.

## Starting The Bot

Once you've setup your your configuration (see below) is complete, simply run:

```shell
python -m forwarder
```

or with poetry (recommended)

```shell
poetry run forwarder
```

## Setting Up The Bot (Read the instruction bellow before starting the bot!):

Telegram Forwarder only supports Python 3.9 and higher.

### Configuration

There are two files mandatory for the bot to work `.env` and `chat_list.json`.

#### `.env`

Template env may be found in `sample.env`. Rename it to `.env` and fill in the values:

-   `BOT_TOKEN` - Telegram bot token. You can get it from [@BotFather](https://t.me/BotFather)

-   `OWNER_ID` - An integer of consisting of your owner ID.

-   `REMOVE_TAG` - set to `True` if you want to remove the tag ("Forwarded from xxxxx") from the forwarded message.

#### `chat_list.json`

Template chat_list may be found in `chat_list.sample.json`. Rename it to `chat_list.json`.

This file contains the list of chats to forward messages from and to. The bot expect it to be an Array of objects with the following structure:

```json
[
    {
        "source": -10012345678,
        "destination": [-10011111111, -10022222222]
    }
]
```

-   `source` - The chat ID of the chat to forward messages from. It can be a group or a channel.
-   `destination` - An array of chat IDs to forward messages to. It can be a group or a channel.

You may add as many objects as you want. The bot will forward messages from all the chats in the `source` field to all the chats in the `destination` field. Duplicates are allowed as it already handled by the bot.

### Python dependencies

Install the necessary python dependencies by moving to the project directory and running:

```shell
poetry install --only main
```

or with pip

```shell
pip3 install -r requirements.txt
```

This will install all necessary python packages.


