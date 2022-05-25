import discord
import random
from random import randint
from discord.ext import commands
import datetime
from discord.utils import get
from datetime import timedelta
import pyowm
import googletrans
from googletrans import Translator
import asyncio
import functools
import itertools
import math
import wikipedia
import requests
from bs4 import BeautifulSoup
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound
import os
import webbrowser
import sqlite3
import nekos
import time
import smtplib
import json
from io import BytesIO
from PIL import Image
from discord import Activity
from discord import ActivityType

PREFIX = '.'

client = commands.Bot(PREFIX, intents = discord.Intents.all())
client.remove_command( 'help' )


############################################################################################## Факты ####################################################################################################################################################################################
#@client.command(aliases = ['fact', 'факт'])
#async def __fact(ctx):
  #  await ctx.channel.purge( limit = 1 )
 #   facts = nekos.fact() # Случайный факт ( на английском языке )
 #   t = Translator() # Переводчик
#    result = t.translate(facts, dest = 'ru') # Выбираем текст, который будем редактировать ( в нашем случае facts и переводим на русский язык ( dest = 'ru'))
#    embed = discord.Embed(color = 0x650ef0) # Создаем эмбед
#    embed.set_author(icon_url = 'https://www.flaticon.com/premium-icon/icons/svg/1177/1177379.svg', name = 'Факт!')
 #   embed.description = result.text # Текст, который мы перевели ( переменная result )
    #embed.timestamp = datetime.datetime.utcnow() # Дата
#    await ctx.send(embed = embed) # Выводим текст
    
    
################################################################################# Слово задом на перёд ###########################################################################################################################################################################
@client.command()
async def слово (ctx, *, text: str):
    await ctx.channel.purge( limit = 1 )
    t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f"{t_rev}")

#################################################################################### Превратить свою картинку в 8 бит ################################################################################################################################################################
def pixel_img(image, pixel_size=8):
    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)  
    return image
    
@client.command()
async def бит8(ctx, member: discord.Member = None):
    await ctx.channel.purge( limit = 1 )
    image = pixel_img(Image.open(BytesIO(await member.avatar_url_as(format='png').read())).convert('RGBA'))
    output = BytesIO()
    image.save(output, 'png')
    image_pix=BytesIO(output.getvalue())
    await ctx.send(file=discord.File(fp=image_pix, filename='pix_ava.png'))

######################################################################################### Монетка ##################################################################################################################################################################################
@client.command()
async def монетка(ctx):
    await ctx.channel.purge( limit = 1 )
    a = random.randint(1, 2)
    if a == 1:
        emb = discord.Embed(title = '__**Орёл и решка**__', colour = 0x7b18fc)
        emb.add_field(name = 'Что выпало:', value = '*Вам выпал* __**орёл**__')       
        emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/726433613088030782/760248953341739109/0f62e15b07768eea.gif')
        emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/755370081390690344/dd3cf605c01e680c.png' )
        emb.set_footer(text='Запросил: {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title = '__**Орёл и решка**__', colour = 0x7b18fc)
        emb.add_field(name = 'Что выпало:', value = '*Вам выпала* __**решка**__')       
        emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/726433613088030782/760248953341739109/0f62e15b07768eea.gif')
        emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/755370263436198008/031f426d35a42d78.png' )
        emb.set_footer(text='Запросил: {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = emb)

####################################################################### Проверка на гейство ########################
@client.command()
async def гей(ctx, member: discord.Member = None):
    await ctx.channel.purge( limit = 1 )
    clr = (random.randint(0,100))
    emb = discord.Embed( description= f':rainbow_flag: Поздравляю! {member.mention} гей на: {(clr)}% :rainbow_flag:', colour = 0x7b18fc )
    await ctx.send(embed=emb)
  
######################################################################## Тик-Ток Данила ############################################
@client.command()
async def тикток(ctx):
    await ctx.channel.purge( limit = 1 )
    a = random.randint(1, 3)
    if a == 1:
        emb = discord.Embed(title = '__**Тик-Ток**__', colour = 0x7b18fc)
        emb.add_field(name = 'Нажмите на ссылку, чтобы увидеть профиль:', value = '__**https://vm.tiktok.com/ZSed1WorC/**__')       
        emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/726433613088030782/757203595710955540/7777777777777777777.jpg')
        emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/757240092522971137/image_6_1.gif' )
        await ctx.send(embed = emb)
    if a == 2:
        emb = discord.Embed(title = '__**Тик-Ток**__', colour = 0x7b18fc)
        emb.add_field(name = 'Нажмите на ссылку, чтобы увидеть профиль:', value = '__**https://vm.tiktok.com/ZSed1WorC/**__') 
        emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/726433613088030782/757203595710955540/7777777777777777777.jpg')
        emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/757237336193892443/image_2_1.gif' )
        await ctx.send(embed = emb)
    if a == 3:
        emb = discord.Embed(title = '__**Тик-Ток**__', colour = 0x7b18fc)
        emb.add_field(name = 'Нажмите на ссылку, чтобы увидеть профиль:', value = '__**https://vm.tiktok.com/ZSed1WorC/**__') 
        emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/726433613088030782/757203595710955540/7777777777777777777.jpg')
        emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/757235225414598706/image_1_1.gif' )
        await ctx.send(embed = emb)
        
########################################################################################## Игра Кс ######################################################################################################################################################################################
@client.command(pass_context=True)  
async def кс(ctx):
    await ctx.channel.purge( limit = 1 )
    await ctx.send (embed = discord.Embed( description = f'**{ctx.message.author}** зовёт играть в **Counter-Strike:**', colour = 0x7b18fc) )
    await ctx.send ('<@503477692365012992> <@292731077007507458> <@932586400501616640> <@496315126492823552> <@885069462007599144> <@921660582929764382> <@324790794068295691> <@863688020893237248> <@747396573889167400> <@533565589839413263> <@264285061602476032> <@468116515108028447>' )
    await ctx.send(embed = emb)
    
########################################################################################## Игра Гта ######################################################################################################################################################################################
@client.command(pass_context=True)  
async def гта(ctx):
    await ctx.channel.purge( limit = 1 )
    await ctx.send (embed = discord.Embed( description = f'**{ctx.message.author}** зовёт играть в **GTA V:**', colour = 0x7b18fc) )
    await ctx.send ('▒█▀▀█ ▒▀█▀ ▒█▀▀█ ══════════ஜ۩۞۩ஜ══════════ ▒█▀▀█ ▒▀█▀ ▒█▀▀█')
    await ctx.send ('▒█░▄▄ ▒▒█ ░▒█▀▀█ ۞<@591999335546486790> <@324790794068295691> <@327814559777947678> <@496315126492823552>۞▒█░▄▄ ▒▒█ ░▒█▀▀█')
    await ctx.send ('▒█▄▄█ ▒▒█ ░▒█▒▒█ ══════════ஜ۩۞۩ஜ══════════ ▒█▄▄█ ▒▒█ ░▒█▒▒█')
    await ctx.send(embed = emb)
    
##################################################################### Пргласить бота на сервер ######################################################################################################################################################################################
@client.command()
async def бот(ctx):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = 'Ссылка для приглашения бота на свой севрер!', description = 'https://discord.com/oauth2/authorize?client_id=724600680672919584&scope=bot&permissions=2147483647', colour = 0x7b18fc )
    emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/760252254849728542/CLAY.png' )
    await ctx.send( embed = emb )
######################################################################################### Статус бота ##############################################################################################################################################################################
@client.event
async def on_ready():
    print("CLAY-BOT")
    await client.change_presence(status = discord.Status.online,activity =Activity(name='за сервером',type=ActivityType.watching) )
####################################################################### Вопросы участника к боту (общение, вопросы) ################################################################################################################################################################
привет_words = [ 'hello', 'hi', 'привет', 'ky', 'ку', 'хай', 'здарова' ]
ответ_words = [ 'инфу', 'инфо', 'узнать инфу', 'узнать информацию', 'что здесь делать?', 'узнать команды',
                'команды', 'комманды', 'что здесь делать?', 'узнать комманды', 'как начать?', 'что дальше?', 'что делать?' ]
пока_words = [ 'пока', 'бб', 'poka', 'бай', 'пака', 'bb', 'покеда', 'пакеда' ]


######################################################################## Выдача роли при входе на сервер ###########################################################################################################################################################################
@client.event
async def on_member_join( member ):
    channel = client.get_channel( 715966574309146624 )
    role = discord.utils.get( member.guild.roles, id = 725776359745650718 )
    await member.add_roles( role )
    await channel.send( embed = discord.Embed( description = f'Пользователь ``{ member.name }``, присоеденился к нам!', color = 0x7b18fc ) )
    
    
####################################################################### Ответы бота на сообщения участника (общение, ответы) ####################################################################################################################################################
@client.event

async def on_message( message ):
    await client.process_commands( message )
    msg = message.content.lower()

    if msg in привет_words:
        await message.channel.send( embed = discord.Embed( description = f'Привет! Чего хотел?', color = 0x7b18fc ) )
    if msg in ответ_words:
        await message.channel.send( embed = discord.Embed( description = f'Напиши в чат ``.команды``, и все узнаешь!', color = 0x7b18fc ) )
    if msg in пока_words:
        await message.channel.send( embed = discord.Embed( description = f'Давай пиздуй уже, заебал...', color = 0x7b18fc ) )


################################################################################# Очистить чат ##################################################################################################################################################################################
@client.command( pass_context = True )

async def очистить( ctx, amount : int ):
    await ctx.channel.purge( limit = amount )

    await ctx.send( embed = discord.Embed( description = f'::::: :put_litter_in_its_place: Удалено {amount} сообщений(-ия) :put_litter_in_its_place: :::::', color = 0x03ff00 ) )


################################################################################## Кикнуть ######################################################################################################################################################################################
@client.command( pass_context = True )
@commands.has_permissions(kick_members = True)
async def кик( ctx, member: discord.Member, *, reason = None ):
    emb = discord.Embed( title = 'Кикнул участника!', colour = discord.Color.orange() )
    await ctx.channel.purge( limit = 1 )
    await member.send( embed = discord.Embed( description = f'Привет { member.name }, тебя кикнули с сервера "Viking", по причине: Плохое поведение или оскорбления! Надеюсь, ты никогда не вернешься :)', color = 0x650ef0 ) )
    await member.kick( reason = reason )
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    emb.add_field( name = 'Причина: плохое поведение или оскорбления!', value = 'Кто кикнул: {}'.format( ctx.author.name ) )
    emb.set_footer( text = 'Кого кикнули: {}'.format( member.name ), icon_url = member.avatar_url )
    emb.set_thumbnail( url = 'https://free-png.ru/wp-content/uploads/2019/07/pow-t-1.png' )
    emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/751014552958795876/kick.png' )
    await ctx.send( embed = emb )
    
    
############################################################################################## Фейк команды ###################################################################################################################################################################
@client.command(pass_comtext=True)
async def фейки(ctx):
    emb=discord.Embed(title = 'Фейк команды', colour = discord.Color.dark_gold())
    emb.add_field(name = 'фейк_кик', value='Фейковый кик участника')
    emb.add_field(name = 'фейк_бан', value='Фейковый бан участника')
    emb.add_field(name = 'фейк_мут', value='Фейковый мут участника')
    await ctx.send(embed=emb)
@client.command()
async def фейк_кик( ctx, member: discord.Member ):
        emb = discord.Embed( title = 'Кикнул участника!', colour = discord.Color.orange() )
        await ctx.channel.purge( limit = 1 )
        await member.send( embed = discord.Embed( description = f'Привет { member.name }, тебя кикнули с сервера "Viking", по причине: Плохое поведение или оскорбления! Надеюсь, ты никогда не вернешься :)', color = 0x650ef0 ) )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name = 'Причина: плохое поведение или оскорбления!', value = 'Кто кикнул: {}'.format( ctx.author.name ) )
        emb.set_footer( text = 'Кого кикнули: {}'.format( member.name ), icon_url = member.avatar_url )
        emb.set_thumbnail( url = 'https://free-png.ru/wp-content/uploads/2019/07/pow-t-1.png' )
        emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/751014552958795876/kick.png' )
        await ctx.send( embed = emb )
@client.command()
async def фейк_бан( ctx, member: discord.Member ):
    emb = discord.Embed( title = 'Вам БАН!', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )
    await member.send( embed = discord.Embed( description = f'{ member.name }, Привет, тебя забанили на сервере "Viking", по причине: Плохое поведение, читы, обман или оскорбления! Надеюсь, тебя никогда не разбанят :)', color = 0x650ef0 ) )
    emb.set_author( name = member.name, icon_url = member.avatar_url )
    emb.add_field( name = 'За что?:', value = 'Участник {} был забанен за: Плохое поведение, читы, обман или оскорбления'.format( member.mention ) )
    emb.set_footer( text = 'Кто забанил: {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
    emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/745613570968125481/b-81_1.png' )
    emb.set_thumbnail( url = 'https://i.gifer.com/8G8J.gif' )
    await ctx.send( embed = emb )
@client.command()
async def фейк_мут( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = 'Мут!', description = f'Администратор: ``{ ctx.author.name }``, выдал мут: { member.mention }!', colour = discord.Color.red())
    await ctx.send( embed = emb )

    
################################################################################## Бот отправляет в ЛС ссылку на оф.сервер ##########################################################################################################################################################
@client.command()
async def лс( ctx ):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = '**Официальный сервер бота!**', description = '**Ссылка на официальный сервер бота отправлена тебе в** ``Личные сообщения!``', color = 0x650ef0 )
    await ctx.send( embed = emb )
    embb = discord.Embed( title = '**Вот ссылка:**', description = 'https://discord.gg/c6jd2sqayz', color = 0x650ef0 )
    embb.set_thumbnail (url = 'https://cdn.discordapp.com/attachments/726433613088030782/760250942419107870/viking.gif')
    await ctx.author.send( embed = embb )

####################################################################################### Поцеловать участника ##########################################################################################################################################################################
@client.command()
async def поцелуй(ctx, member: discord.Member):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed(title = '💋Поцелуй💋', description = f'**💋Пользователь: ``{ctx.author.name}``, поцеловал { member.mention }!💋**', color = 0x650ef0 )
    emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/726433613088030782/755098852293476352/333333333333333333.gif')
    await ctx.send( embed = emb )
################################################################################ Забанить ########################################################################################################################################################################################
@client.command( pass_context = True )
@commands.has_permissions(kick_members = True)
async def бан( ctx, member: discord.Member, *, reason = 'bad boy' ):
    emb = discord.Embed( title = 'Вам БАН!', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )
    await member.send( embed = discord.Embed( description = f'Привет { member.name }, тебя забанили на сервере "Viking", по причине: Плохое поведение, читы, обман или оскорбления! Надеюсь, тебя никогда не разбанят :)', color = 0x650ef0 ) )
    await member.ban( reason = reason )
    emb.set_author( name = member.name, icon_url = member.avatar_url )
    emb.add_field( name = 'За что?', value = 'Участник {} был забанен за: Плохое поведение, читы, обман или оскорбления'.format( member.mention ) )
    emb.set_footer( text = 'Кто забанил: {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
    emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/745613570968125481/b-81_1.png' )
    emb.set_thumbnail( url = 'https://i.gifer.com/8G8J.gif' )
    await ctx.send( embed = emb )
################################################################################## Разбанить ######################################################################################################################################################################################
@client.command( pass_context = True )
@commands.has_permissions(kick_members = True)
async def разбан( ctx, *, member ):
    await ctx.channel.purge( limit = 1 )
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban( user )
        await ctx.send( f'Разбанил  { user.mention }' )
        return
################################################################################# Команды #######################################################################################################################################################################################
@client.command( pass_context = True )
async def команды( ctx ):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = '**Навигация по командам**', color = 0xdab611 )
    emb.add_field( name = '``{}очистить``'.format( PREFIX ), value = '**Очистить чат**' )
    emb.add_field( name = '``{}бан``'.format( PREFIX ), value = '**Забанить участника**' )
    emb.add_field( name = '``{}кик``'.format( PREFIX ), value = '**Кикнуть участника**' )
    emb.add_field( name = '``{}разбан``'.format( PREFIX ), value = '**Разбанить участника**' )
    emb.add_field( name = '``{}привет``'.format( PREFIX ), value = '**Передать боту привет)**' )
    emb.add_field( name = '``{}мут``'.format( PREFIX ), value = '**Запретить писать в чат**' )
    emb.add_field( name = '``{}лс``'.format( PREFIX ), value = '**Бот пришлёт ссылку на сервер в лс**' )
    emb.add_field( name = '``{}сообщений``'.format( PREFIX ), value = '**Узнать, сколько сообщений вы отправили**' )
    emb.add_field( name = '``{}курс``'.format( PREFIX ), value = '**Узнать курс валю**' )
    emb.add_field( name = '``{}погода``'.format( PREFIX ), value = '**Узнать погоду в своем городе**' )
    emb.add_field( name = '``{}перевод``'.format( PREFIX ), value = '**Перевести слово на другой язык**' )
    emb.add_field( name = '``{}повышение``'.format( PREFIX ), value = '**Повысить роль участника на одну ступень выше**' )
    emb.add_field( name = '``{}вики``'.format( PREFIX ), value = '**Обычная Википедия**' )
    emb.add_field( name = '``{}гонка``'.format( PREFIX ), value = '**Игра гонка**' )
    emb.add_field( name = '``{}монетка``'.format( PREFIX ), value = '**Орёл и Решка**' )
    emb.add_field( name = '``{}ллс``'.format( PREFIX ), value = '**Бот попросит человека (которого вы указали) зайти на сервер**' )
    emb.add_field( name = '``{}инфо``'.format( PREFIX ), value = '**Узнать информацию об участнике**' )
    emb.add_field( name = '``{}поцелуй``'.format( PREFIX ), value = '**Поцеловать участника**' )
    #emb.add_field( name = '``{}факт``'.format( PREFIX ), value = '**Узнать какой-нибудь интересный факт**' )
    emb.add_field( name = '``{}фейки``'.format( PREFIX ), value = '**Список фейковых команд**' )
    emb.add_field( name = '``{}кс``'.format( PREFIX ), value = '**Позвать играть в кс**' )
    emb.add_field( name = '``{}гта``'.format( PREFIX ), value = '**Позвать играть в гта**' )
    emb.add_field( name = '``{}гей``'.format( PREFIX ), value = '**Проверить друга на гейство**' )
    emb.add_field( name = '``{}бит8``'.format( PREFIX ), value = '**Превратить свою(или чью-то) аватарку в 8bit(ную)**' )
    emb.add_field( name = '``{}слово``'.format( PREFIX ), value = '**Пишет ваше предложение задом наперёд**' )
    #emb.add_field( name = '{}'.format( PREFIX ), value = ' ' )
    await ctx.send( embed = emb )


######################################################################################## Информация о человеке ##################################################################################################################################################################################
@client.command(aliases=['юзер', 'юзеринфо', 'user'])
async def инфо(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    roles = member.roles
    role_list = ""
    for role in roles:
        role_list += f"<@&{role.id}> "
    emb = discord.Embed(title=f'Информация о пользователе {member}', colour = 0x650ef0)
    emb.set_thumbnail(url=member.avatar_url)
    emb.add_field(name='ID:', value=member.id)
    emb.add_field(name='Никнэйм:', value=member.mention)
    emb.add_field(name='Высшая роль:', value=member.top_role)
    emb.add_field(name='Дискриминатор:', value=member.discriminator)
    emb.add_field(name='Присоеденился к серверу:', value=member.joined_at.strftime('%Y.%m.%d \n %H:%M:%S'))
    emb.add_field(name='Присоеденился к Discord:', value=member.created_at.strftime("%Y.%m.%d %H:%M:%S"))
    emb.add_field(name="Статус:", value=member.status)
    emb.add_field(name='Роли:', value=role_list)
    if 'online' in member.desktop_status:
        emb.add_field(name="Устройство:", value=":computer:Компьютер:computer:")
    elif 'online' in member.mobile_status:
        emb.add_field(name="Устройство:", value=":iphone:Телефон:iphone:")
    elif 'online' in member.web_status:
        emb.add_field(name="Устройство:", value=":globe_with_meridians:Браузер:globe_with_meridians:")
    emb.set_footer(text='Вызвал команду: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed = emb)
    
####################################################################################### Погода #######################################################################################################################################################################################
@client.command()
async def погода(ctx, *, arg):
    await ctx.channel.purge( limit = 1 )
    embed = discord.Embed(title = 'Погода в вашем городе', colour = 0x650ef0 )

    owm = pyowm.OWM( '9aac2f7b194e8a88add910928e6646ab' )
    city = arg

    observation = owm.weather_at_place( city )
    w = observation.get_weather()
    temperature = w.get_temperature( 'celsius' )[ 'temp' ]

    embed.add_field( name = '**Температура**', value = f'Температура в городе { city }: ``{ temperature }°C``', inline = False )

    await ctx.send( embed = embed )


########################################################################### Бот отправляет сообщение в лс кому-либо ##################################################################################################################################################################
@client.command()
async def ллс( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )
    await member.send( embed = discord.Embed( description = f'{ member.name } привет, {ctx.author.mention} просит тебя зайти на сервер "Viking"!', color = 0x650ef0 ) )
################################################################################## Выдача новой роли #################################################################################################################################################################################
@client.command()
async def повышение(ctx, member: discord.Member):
    await ctx.channel.purge( limit = 1 )
    new_top_role_position = member.top_role.position + 1 #узнаём позицию более высшей роли, чем высшая роль участника
    new_top_role = discord.utils.get(ctx.guild.roles, position = new_top_role_position) #вычисляем саму роль которая выше роли участника
    if new_top_role == None: #проверка, срабатывающая если роли выше нет
        e = discord.Embed(title = "Ошибка!")
        e.add_field(name = "Ошибка:", value = "Участник обладает самой высокой ролью, и выдать роль выше невозможно!", inline = False)
        e.add_field(name = "Решение:", value = "Создайте более высшую роль в списке ролей")
    else: #в остальных случаях прекрасно работает, пишет само сообщение о повышении и выдаёт роль участнику
        e = discord.Embed(title = "Участник был повышен!")
        e.add_field(name = "Повысил:", value = f"{ctx.author.mention}")
        e.add_field(name = "Повышен:", value = f"{member.mention}")
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
        e.add_field(name = "Новая роль:", value = f"{new_top_role.mention}")
        e.add_field(name = "Старая роль:", value = f"{member.top_role.mention}")
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
        await member.remove_roles(member.top_role) #сначала изымает старую высшую роль участника, обязательно здесь надо разместить эту строчку чтобы не возникло никаких проблем, потому что если поменяете со следующей, получится так что выдаётся новая высшая роль и снимается сразу же
        await member.add_roles(new_top_role) #выдаёт новую высшую роль
        await ctx.send(embed = e) #отправляет сообщение в виде эмбеда


####################################################################################### Переводчик слов ##############################################################################################################################################################################
translator = Translator()

@client.command()
async def перевод(ctx, dest, *txt):
    
 try:
    txt = str(txt)
    result = translator.translate(txt, dest = dest)
    await ctx.message.delete()
    embed = discord.Embed(title = f'**Перевод вашего сообщения**', description = f'''**Ваше сообщение:** {result.origin}\n**Перевод вашего сообщения:** {result.text}\n**Язык с которого переводим:**{result.src}\n**Язык на которой переводим:** {result.dest}\n**Произношение:** {result.pronunciation}''', color=0x35c6be)
    embed.set_footer(text = f'{client.user.name} © 2020 | Все права под защитой', icon_url = client.user.avatar_url)
    embed.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/1/14/Google_Translate_logo_%28old%29.png')

    await ctx.send(embed = embed)
 except ValueError:

    await  ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, данного языка не существует!\n Вот список всех языков \n {googletrans.LANGUAGES} \n ``Пример:`` **.переводчик kazakh привет**', colour=discord.Color.red()))




############################################################################################## Мут ################################################################################################################################################################################### 
@client.command(aliases=['мьют'])
@commands.has_permissions(kick_members=True)
async def мут(ctx, member: discord.Member = None, amount = None, type = None, reason=None):
    if member == None:
        emb2 = discord.Embed(title='Укажи пользователя, которого хочешь замьютить!',description=f'{ ctx.author.mention } вот пример .мут @CLAY-BOT 60 сек (или мин, или час, или дней) плохое поведение',color = 0x650ef0)
        emb2.set_footer( text = 'Вызвал команду: {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

        await ctx.send(embed=emb2)
    else:
        if amount == None:
            emb3 = discord.Embed(title='Укажи время!',description=f'{ ctx.author.mention } вот пример .мут @CLAY-BOT 60 сек (или мин, или час, или дней) плохое поведение',color = 0x650ef0)
            emb3.set_footer( text = 'Вызвал команду: {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

            await ctx.send(embed=emb3)
        else:
            if amount == None:
                emb4 = discord.Embed(title='Укажи формат времяни!',description=f'{ ctx.author.mention } вот пример .мут @CLAY-BOT 60 сек (или мин, или час, или дней) плохое поведение',color = 0x650ef0)
                emb4.set_footer( text = 'Вызвал команду: {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

                await ctx.send(embed=emb4)
            else:
                for i in ctx.guild.text_channels:
                    channel = client.get_channel(i.id)
                    await channel.set_permissions(member, send_messages=False, add_reactions=False)
                await ctx.channel.purge(limit=1)
                emb = discord.Embed(title='Участник замьючен!',description=f'Пользователь { member.mention }  был замьючен по причине { reason } на { amount } { type }!',color = 0x650ef0)
                emb.set_footer( text = 'Кто замьютил: {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )

                await ctx.send(embed=emb)
                if type == "с" or type == "сек" or type == "секунды" or type == "секунд":
                    await asyncio.sleep(amount)
                elif type == "м" or type == "мин" or type == "минуты" or type == "минут":
                    await asyncio.sleep(int(amount) * 60)
                elif type == "ч" or type == "час" or type == "часа" or type == "часов":
                    await asyncio.sleep(int(amount) * 60 * 60)
                elif type == "д" or type == "день" or type == "дня" or type == "дней":
                    await asyncio.sleep(int(amount) * 60 * 60 * 24)
                for i in ctx.guild.text_channels:
                    channel = client.get_channel(i.id)
                    await channel.set_permissions(member, send_messages=None, add_reactions=None)

@client.command(aliases=['размьют'])
@commands.has_permissions(kick_members = True)
async def размут(ctx, member: discord.Member):
    await ctx.channel.purge( limit = 1 )
    for i in ctx.guild.text_channels:
        channel = client.get_channel(i.id)
        await channel.set_permissions(member, send_messages = None, add_reactions = None)
    await ctx.send("Участник размьючен!")
###########################################################################№№№############# Википедия ###########№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№##########№№№№№№№№№№№№№№№№№№№№№№№№№№########################################################
@client.command()
async def вики(ctx, *, text):
    await ctx.channel.purge( limit = 1 )
    wikipedia.set_lang("ru")
    new_page = wikipedia.page(text)
    summ = wikipedia.summary(text)
    emb = discord.Embed(description= summ)
    emb.set_author(name= new_page.title, url= new_page.url, icon_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
    emb.set_footer(text='Вызвал команду: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)

####################################################################### Игра гонка ###################################################################################################################
@client.command()
async def гонка(ctx, member: discord.Member = None, amount: int = 1000):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed(title = '**Гонка!**', description = f'Пользователь: ``{ctx.author.name}``, бросил вызов в гонке пользователю: {member.mention}! Гонка началась! Ожидайте 10 секунд', colour = 0x650ef0)
    await ctx.send(embed = emb)
    await asyncio.sleep(10)
    a = random.randint(1, 2)
    embb = discord.Embed(title =  'Итоги!', description = f'**В соревнование:** {ctx.author.mention} и {member.mention}!\n **Побеждает:** {ctx.author.mention}!!\n **Поздравим!**', colour = 0x0354f5)
    embbb = discord.Embed(title =  'Итоги!', description = f'**В соревнование:** {ctx.author.mention} и {member.mention}!\n **Побеждает:** {member.mention}!!\n **Поздравим!**', colour = 0x0354f5)
    if a == 1:
        await ctx.send(embed = embb)
    if a == 2:
        await ctx.send(embed = embbb)
############################################################################ Сказать человеку об ошибке в написании команды ##########################################################################################################################################################
@client.event
async def on_command_error( ctx, error ):
    pass
## Если неправильно написал команду "очистить"
@очистить.error
async def очистить_error( ctx, error ):
    await ctx.channel.purge( limit = 1 )
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send(  embed = discord.Embed( description = f' { ctx.author.mention }, обязательно укажи колличествово!', color = 0xff5900 ) )
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( embed = discord.Embed( description = f' { ctx.author.mention }, ваша роль не имеет таких прав!', color = 0xff5900 ) )
## Переводчик
@перевод.error
async def перевод_error( ctx, error ):
    await ctx.channel.purge( limit = 1 )
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send(  embed = discord.Embed( description = f' { ctx.author.mention }, Неправильно! Надо так: ``.перевод (нужный язык) (слово, которое нужно перевести)``', color = 0xff5900 ) )

## Разбанить
@разбан.error
async def разбан_error( ctx, error ):
    await ctx.channel.purge( limit = 1 )
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( embed = discord.Embed( description = f' { ctx.author.mention }, обязательно укажи участника!', color = 0xff5900 ) )
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( embed = discord.Embed(description = f' { ctx.author.mention }, ваша роль не имеет таких прав!', color = 0xff5900 ) )
## Забанить
@бан.error
async def бан_error( ctx, error ):
    await ctx.channel.purge( limit = 1 )
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( embed = discord.Embed( description = f' { ctx.author.mention }, обязательно укажи участника!', color = 0xff5900 ) )
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( embed = discord.Embed( description = f' { ctx.author.mention }, ваша роль не имеет таких прав!', color = 0xff5900 ) )
## Кикнуть
@кик.error
async def кик_error( ctx, error ):
    await ctx.channel.purge( limit = 1 )
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( embed = discord.Embed( description = f' { ctx.author.mention }, обязательно укажи участника!', color = 0xff5900 ) )
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( embed = discord.Embed( description = f' { ctx.author.mention }, ваша роль не имеет таких прав!', color = 0xff5900 ) )
## Погода
@погода.error
async def погода_error( ctx, error ):
    await ctx.channel.purge( limit = 1 )
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( embed = discord.Embed( description = f' { ctx.author.mention }, обязательно укажи город!', color = 0xff5900 ) )


############################################################################ Сколько сообщений отправил #############################################################################################################################################################################
@client.command(pass_context = True)
async def сообщений(ctx):
    await ctx.channel.purge( limit = 1 )
    counter = 0
    yesterday = datetime.datetime.today() - timedelta(days = 1)
    async for message in ctx.channel.history(limit=None, after=yesterday):
        counter += 1
    counter2 = 0
    weekago = datetime.datetime.today() - timedelta(weeks = 1)
    async for message in ctx.channel.history(limit=None, after=weekago):
        counter2 += 1
    counter3 = 0
    monthago = datetime.datetime.today() - timedelta(weeks = 4)
    async for message in ctx.channel.history(limit=None, after=monthago):
        counter3 += 1
    await ctx.send( embed = discord.Embed( description = f' { ctx.author.mention } \nЗа сегодня: ``{counter}`` сообщений\nЗа неделю: ``{counter2}`` сообщений\nЗа месяц: ``{counter3}`` сообщений', color = 0x650ef0 ) )


#################################################################################### Курс валют #####################################################################################################################################################################################
@client.command()
async def курс(ctx):
    await ctx.channel.purge( limit = 1 )
    cgrn =Currensy_rub()
    cgrn.get_currency_price()
    cgrnn =Currensy_grn()
    cgrnn.get_currency_price()
    cgrnz =Currensy_kzt()
    cgrnz.get_currency_price()
    cgrn =Currensy_kzzt()
    cgrn.get_currency_price()
    emb = discord.Embed(colour = 0x650ef0)
    emb.set_author(name = "Курс валют", url = emb.Empty, icon_url = "https://t4.ftcdn.net/jpg/01/34/67/51/240_F_134675192_TC1KncAkC6EAEBDxXj5Uy1900F1ZbJ6v.jpg")
    emb.add_field(name = 'Доллар к рублю', value = f'1$ = {odin}₽')
    emb.add_field(name = "Доллар к гривне", value = f"1$ = {odnag}₴")
    emb.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
    emb.add_field(name = "Доллар к тенге", value = f"1$ = {odnakz}₸")
    emb.add_field(name = 'Рубль к тенге', value = f'1₽ = {odan}₸')
    emb.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
    await ctx.send(embed = emb)
    
class Currensy_rub:
    #Ссылка на сам ссайт
    DOLAR_RU = 'https://www.google.com/search?sxsrf=ALeKk01jZWoCi7DPRT-l4VJfCTYqs4DhtA%3A1584913719655&ei=N913XuzLJ4nurgSg27rgCA&q=доллара+к+рублю&oq=долара+к+ру&gs_l=psy-ab.3.0.0i10l4j0i22i10i30l6.9772.12721..13473...1.1..0.101.1022.11j1......0....1..gws-wiz.......0i71j35i39j0i131j0j0i131i67j0i10i67j0i67j0i203j35i305i39.mwJK-h5dzto'
    #Для таго чтоб сайт понял что вы не бот
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    def get_currency_price(self):
        #делаем запрос на самом сайте
        full_page = requests.get(self.DOLAR_RU, headers=self.headers)
        
        #Делаю так чтоб мы парсели через библиотеку бютифулл суп
        soup = BeautifulSoup(full_page.content, 'html.parser')
        
        #Нахожу все нужные елементы 
        convert = soup.findAll('span', {'class': 'DFlfde', 
                                        'class': 'SwHCTb',
                                        'data-precision': 2})
        global odin 
        odin = convert[0].text
class Currensy_grn:
    #Ссылка на сам ссайт
    DOLAR_UA = 'https://www.google.com/search?sxsrf=ALeKk03fHfLO2ZLgvH2aCYHyylK169bp7Q%3A1584807405441&ei=7T12Xt69Gsyf6ASQjpvADw&q=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_l=psy-ab.3..0i7i30j0i7i10i30l9.96278.96485..97742...0.2..0.99.195.2......0....1..gws-wiz.......0i71.ruuxORUhmxA&ved=0ahUKEwie6MDT-6voAhXMD5oKHRDHBvgQ4dUDCAs&uact=5'
    #Для таго чтоб сайт понял что вы не бот
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    def get_currency_price(self):
        #делаем запрос на самом сайте
        full_page = requests.get(self.DOLAR_UA, headers=self.headers)
        
        #Делаю так чтоб мы парсели через библиотеку бютифулл суп
        soup = BeautifulSoup(full_page.content, 'html.parser')
        
        #Нахожу все нужные елементы 
        convert = soup.findAll('span', {'class': 'DFlfde', 
                                        'class': 'SwHCTb',
                                        'data-precision': 2})
        global odnag
        odnag = convert[0].text
class Currensy_kzt:
    #Ссылка на сам ссайт
    DOLAR_KZT = 'https://www.google.com/search?sxsrf=ALeKk01Lm4ZMdoc_4oc6JqpIdXGPXAlJyQ%3A1590743968555&ei=oNPQXtqeIcSQrgSrkZKgDA&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=CgZwc3ktYWIQAzIECAAQQzICCAAyBQgAEMsBMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECAAQRzoFCAAQgwE6BwgAEBQQhwI6CQgAEEMQRhCCAjoECAAQCjoHCCMQ6gIQJ1DpUVj_mwFgx50BaBZwEHgAgAGzAogBuh-SAQg0LjEzLjYuMZgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab&ved=0ahUKEwja7rGJ39jpAhVEiIsKHauIBMQQ4dUDCAs&uact=5'
    #Для таго чтоб сайт понял что вы не бот
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    def get_currency_price(self):
        #делаем запрос на самом сайте
        full_page = requests.get(self.DOLAR_KZT, headers=self.headers)
        
        #Делаю так чтоб мы парсели через библиотеку бютифулл суп
        soup = BeautifulSoup(full_page.content, 'html.parser')
        
        #Нахожу все нужные елементы 
        convert = soup.findAll('span', {'class': 'DFlfde', 
                                        'class': 'SwHCTb',
                                        'data-precision': 2})
        global odnakz
        odnakz = convert[0].text
class Currensy_kzzt:
    #Ссылка на сам ссайт
    RU_KZT = 'https://www.google.com/search?sxsrf=ALeKk01LL49C5oTQyH99XrTX4e4vwguqgQ%3A1601060125419&ei=HT1uX4-PGc2SrgTZwLigDQ&q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&oq=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=CgZwc3ktYWIQAzIICAAQsQMQgwEyBwgAEBQQhwIyBggAEAcQHjIHCAAQFBCHAjIGCAAQBxAeMgIIADICCAAyAggAMgIIADICCAA6BwgAEEcQsANQzghYzRNguBZoAnABeACAAY0BiAGAApIBAzAuMpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwjPkajg_YTsAhVNiYsKHVkgDtQQ4dUDCA0&uact=5'
    #Для таго чтоб сайт понял что вы не бот
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    def get_currency_price(self):
        #делаем запрос на самом сайте
        full_page = requests.get(self.RU_KZT, headers=self.headers)
        
        #Делаю так чтоб мы парсели через библиотеку бютифулл суп
        soup = BeautifulSoup(full_page.content, 'html.parser')
        
        #Нахожу все нужные елементы 
        convert = soup.findAll('span', {'class': 'DFlfde', 
                                        'class': 'SwHCTb',
                                        'data-precision': 2})
        global odan 
        odan = convert[0].text

        
################################################################################ Игра сапёр #########################################################################################################################################################################################
@client.command()
async def сапер(ctx):
    await ctx.channel.purge( limit = 1 )
    embed = discord.Embed(description = '''
                     Держи :smile:
||0️⃣||||0️⃣||||0️⃣||||1️⃣||||1️⃣||||2️⃣||||1️⃣||||2️⃣||||1️⃣||||1️⃣||||
2️⃣||||2️⃣||||1️⃣||||1️⃣||||💥||||2️⃣||||💥||||3️⃣||||💥||||1️⃣||||
💥||||💥||||1️⃣||||1️⃣||||2️⃣||||3️⃣||||3️⃣||||💥||||2️⃣||||1️⃣||||
2️⃣||||2️⃣||||1️⃣||||0️⃣||||1️⃣||||💥||||2️⃣||||1️⃣||||1️⃣||||0️⃣||||
0️⃣||||0️⃣||||0️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||0️⃣||||0️⃣||||0️⃣||||
1️⃣||||1️⃣||||0️⃣||||1️⃣||||💥||||1️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||
💥||||1️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||1️⃣||||💥||||💥||||1️⃣||||
1️⃣||||1️⃣||||1️⃣||||💥||||1️⃣||||1️⃣||||2️⃣||||3️⃣||||2️⃣||||1️⃣||||
1️⃣||||2️⃣||||2️⃣||||2️⃣||||2️⃣||||2️⃣||||💥||||1️⃣||||0️⃣||||0️⃣||||
💥||||2️⃣||||💥||||1️⃣||||1️⃣||||💥||||2️⃣||||2️⃣||||1️⃣||||1️⃣||||
1️⃣||||2️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||💥||||1️⃣||         
    ''', color = 0x7b18fc )
    await ctx.send(embed=embed)

    
    
    
@client.command()
async def iso(ctx):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = 'Ссылка', description = 'https://mega.nz/file/LmBgnDgA#WOYrVz_EG7ZaMVfF_5UG0JAFyFjqSzuUuy7CG2k_zHk', colour = 0x7b18fc )
    emb.set_image( url = 'https://cdn.discordapp.com/attachments/726433613088030782/760252254849728542/CLAY.png' )
    await ctx.send( embed = emb )
####################################################################### Подключение ######################################################################################################################################################################################################
token = os.environ.get( 'token' )
client.run(str(token))
