import discord

TOKEN = "MTA1NzUwNjE3MzAyMjEyNjE1Mg.GJgRg9.HJsD81-SEIrwatnGafCMsPdess7gH0uMKZ3EHA"

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("{0.user} is online!".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("!hello") or message.content.startswith("/hello"):
        await message.channel.send("Hello from the other side!")


client.run(TOKEN)
