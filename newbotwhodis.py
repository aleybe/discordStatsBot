token = "NDIwODMyOTE5ODQyNTg2NjI2.DYEfRg.GkeYt_imdmho4bZz9poNY1wRl3s"

import discord
import asyncio
import random

client = discord.Client()


@client.event
async def on_ready():
    print("Ready!")
    await client.send_message(client.get_channel('420840933580341250'), 'Ready!')


@client.event
async def on_message(message):
    if message.content.startswith("%rps"):
        await rockPaperScis(message.mentions[0], message.mentions[1], 3, message)


# await client.send_message(message.channel, 'what\'s up %s' % str(message.author.mention))

async def rockPaperScis(p1, p2, mr, message):
    p1score = 0
    p2score = 0
    scores = [p1score, p2score]

    for x in range(1, mr):

        gd = random.randint(1,9)
        # P1 Win Block
        if (gd == 3):
            p1score += 1
            # p1 wins
            print("%s Wins!\n" % p1)
            await client.send_message(message.channel, "%s Used :scissors:" % p1.mention)
            await client.send_message(message.channel, "%s Used :newspaper:" % p2.mention)
            await client.send_message(message.channel, "%s Wins!" % p1.mention)
        elif (gd == 4):
            p1score += 1
            # p1 wins
            print("%s Wins!\n" % p1)
            await client.send_message(message.channel, "%s Used :newspaper:" % p1.mention)
            await client.send_message(message.channel, "%s Used :full_moon:" % p2.mention)
            await client.send_message(message.channel, "%s Wins!" % p1.mention)
        elif (gd == 8):
            p1score += 1
            # p1 wins
            print("%s Wins!\n" % p1)
            await client.send_message(message.channel, "%s Used :full_moon:" % p1.mention)
            await client.send_message(message.channel, "%s Used :scissors:" % p2.mention)
            await client.send_message(message.channel, "%s Wins!" % p1.mention)
        ###
        # P2 Win Block
        elif (gd == 2):
            p2score += 1
            # p2 wins
            print("%s Wins!\n" % p2)
            await client.send_message(message.channel, "%s Used :scissors:" % p2.mention)
            await client.send_message(message.channel, "%s Used :newspaper:" % p1.mention)
            await client.send_message(message.channel, "%s Wins!" % p2.mention)
        elif (gd == 6):
            p2score += 1
            # p2 wins
            print("%s Wins!\n" % p2)
            await client.send_message(message.channel, "%s Used :newspaper:" % p2.mention)
            await client.send_message(message.channel, "%s Used :full_moon:" % p1.mention)
            await client.send_message(message.channel, "%s Wins!" % p2.mention)
        elif (gd == 7):
            p2score += 1
            # p2 wins
            print("%s Wins!\n" % p2)
            await client.send_message(message.channel, "%s Used :full_moon:" % p2.mention)
            await client.send_message(message.channel, "%s Used :scissors:" % p1.mention)
            await client.send_message(message.channel, "%s Wins!" % p2.mention)
        ###
        else:
            # draw
            if (gd == 1):
                await client.send_message(message.channel, "%s Used :full_moon:" % p2.mention)
                await client.send_message(message.channel, "%s Used :full_moon:" % p1.mention)
                await client.send_message(message.channel, "Draw!")
            elif (gd == 5):
                await client.send_message(message.channel, "%s Used :scissors:" % p2.mention)
                await client.send_message(message.channel, "%s Used :scissors:" % p1.mention)
                await client.send_message(message.channel, "Draw!")
            else:
                await client.send_message(message.channel, "%s Used :newspaper:" % p2.mention)
                await client.send_message(message.channel, "%s Used :newspaper:" % p1.mention)
                await client.send_message(message.channel, "Draw!")
                print("Draw")


   

    if (p1score > p2score):
        winner = p1
    elif (p2score > p1score):
        winner = p2
    else:
        winner = "No One"

    print("End Score:\n\t%s on %s\n\t%s on %s\n%s Wins!" % (p1, p1score, p2, p2score, winner))
    await client.send_message(message.channel,
                              "```End Score:\n\t%s on %s\n\t%s on %s\n%s Wins!```" % (p1, p1score, p2, p2score, winner))


client.run(token)
client.close()

#   r p s
# r  t 1 2
# p  2 t 1
# s  1 2 t
#
