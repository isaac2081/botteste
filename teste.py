import discord

client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Making a    bot"))
@client.event
async def on_message(message):
    print(message.author.id+" - "+message.content)
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")
client.run("NTY1ODk2NDQyOTcyMjA5MTUy.XK9RTA.ZjYXljm-XxLxEYxbkBuGAncmk7Q")