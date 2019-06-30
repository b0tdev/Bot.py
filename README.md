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
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    client = MyClient()
    client.run('token')
    
    ***
    
    ### Functions and Specifications
    
    *Ping finder
    
    *Moderation
    
    *Welcomer
    
    *Fun
    
    ***
    
   
   
   
   
   
   
   
   
   
   
   
   
   
