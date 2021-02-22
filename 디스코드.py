import discord
import asyncio

client = discord.Client()

token = "ODEzMzk4NzE0MjUyMDAxMjgx.YDOulQ.7iHHSNWJVFnfRsqR7EiVkHvsdcQ"

@client.event
async def on_ready():

    print(client.user.name)
    print('sucess')
    game = discord.Game('poppoppop')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "!팝":
        await message.channel.send("팝팝팝팝")

    if message.content == "!뽷":
        await message.channel.send("뽷뽷뽷뽷")

    if message.content == "!임베드":
        embed = discord.Embed(title="팝팝부르기", descript="뽷뽷도 부르기", color=0x00ff00)
        embed.set_footer(text="팝팝팝팝,뽷뽷뽷뽷원합니다")
        await message.channel.send(embed=embed)

    if message.content == "!이미지":
        embed = discord.Embed(title="팝팝이", descript="pop", color=0x00ff00)
        embed.set_footer(text="이름:뽭뽭이,나이:불명")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_fM2Co9n5Nb6VWtVHKib1hZxO0UXKcVtMww&usqp=CAU")
        await message.channel.send(embed=embed)

    
client.run(token)
