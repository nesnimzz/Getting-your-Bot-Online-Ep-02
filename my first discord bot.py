#import packages
import discord

#our bot
client = discord.Client()

#content
@client.event
async def on_ready():
    general =  client.get_channel(838423158033874984)
    await general.send("mn online awa yaluwane")

@client.event
async def on_disconnect():
    general =  client.get_channel(838423158033874984)
    await general.send("good bye kastiya")





#run the bot
client.run("ODQzOTcxMDYyMjY1NDEzNjcz.YKLnTQ.mxXnXznOAUpvHRCqmHwMPPN2THQ")

