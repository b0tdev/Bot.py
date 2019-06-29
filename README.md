# Bot.py

**A Discord Bot Made Using Python**

## Bot Info and Some Examples

### Example Codes

**Install libraries via**

_Module(text)_

`pip install discord.py`

_Module(voice)_

`pip install discord.py[voice]`

### Bot Example

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
                     
client = MyClient()
client.run('token'
