token = "NDIwODMyOTE5ODQyNTg2NjI2.DYEfRg.GkeYt_imdmho4bZz9poNY1wRl3s"

import discord
import asyncio
import math
import random

client = discord.Client()


@client.event
async def on_ready():
    print("Ready!")
    await client.send_message(client.get_channel('420840933580341250'), 'Ready!')


@client.event
async def on_message(message):
    if message.content.startswith("%rps"):

        await client.send_message(message.channel, 'what\'s up @%s' % str(message.author.id))


client.run(token)
client.close()

# 1 is rock
# 2 is paper
# 3 is scissors

@client.event
async def rockPaperScis(p1, p2, mr):
    p1score = 0
    p2score = 0
    scores = [p1score, p2score]

    for x in range(1, mr):
        # print("Current Score:\n\t%s on %s\n\t%s on %s\n" % (p1, p1score, p2, p2score))

        gd = random.randint(1, 9)

        if (gd == 3 or gd == 4 or gd == 8):
            p1score += 1
            # p1 wins
            print("%s Wins!\n" % p1)
            await client.send_message(message.channel, "%s Wins!" %p1)

        elif (gd == 2 or gd == 6 or gd == 7):
            # p2 wins
            print("%s Wins!\n" % p2)
            await client.send_message(message.channel, "%s Wins!" % p2)
            p2score += 1

        else:
            # draw
            print("Draw")
            mr += 1

            pass

    if (p1score > p2score):
        winner = p1
    elif (p2score > p1score):
        winner = p2
    else:
        winner = "No One"

    print("End Score:\n\t%s on %s\n\t%s on %s\n%s Wins!" % (p1, p1score, p2, p2score, winner))

    #   r p s p2
    # r  1 2 3
    # p  4 5 6
    # s  7 8 9
    # p1

    # check to see who won the round

