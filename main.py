from edamino import *
from edamino.objects import *
from edamino.api import File
from asyncio import sleep
from gtts import gTTS
import time, random, json, requests
import pypokedex
import os
#impory aiofiles


###################################
e = "viktoraminobotsofia@gmail.com"
p = "sofia@bot"
d = "423ae9aef48008707155ba8ca2d258e5a90475821e2e59298731de68e29a4cf40aaaced538db3ee5fd"
Host = "4882e27f-c8dc-46de-a77f-8c0771bce8fa"
###################################
bot = Bot(email=e, password=p, prefix=".")

@bot.event()
async def on_ready(profile: UserProfile):
    logger.info(f'{profile.nickname} ready')
    
@bot.event()
async def on_mention(ctx: Context):
    await ctx.reply('interesante...')

@bot.event([api.MessageType.VIDEO_CHAT_START]) #api.MessageType.VOICE_CHAT_START
async def join_live(ctx: Context):
    await ctx.join_channel(channel_type = 1)

#@bot.event([api.MessageType.GROUP_MEMBER_JOIN])
#async def say_hello(ctx: Context):
#    x=ctx.msg.author.icon
#    response=requests.get(f"{x}")
#    file=open("sample.png","wb")
#    file.write(response.content)
#    file.close()
#    img = await File.async_load('sample.png')
#    embed = api.Embed(object_id= ctx.msg.author.uid, title=ctx.msg.author.nickname, link=f"ndc://x{ctx.msg.threadId}/user-profile/{ctx.msg.author.uid}", image= img,)
#    await ctx.send(f"""[C]━━━━━━━━━━━━━━━
#[c]Bienvenido <${ctx.msg.author.nickname}$>
#[C]━━━━━━━━━━━━━━━
#Sigue las reglas del Chat
#1.No hacer spam
#2.Respetar a Lideres, curadores, Anfitrión y Coanfitriones
#3.No propagues odio
#4.Ser educado en el Chat Grupal
#[C]━━━━━━━━━━━━━━━""", embed=embed, mentions= [ctx.msg.author.uid])


@bot.command('sofia')
async def info(ctx: Context):
    await ctx.send(message="""[bc]Mis datos
[c]
[i]Me llamo Sofía y soy un bot de Pokémon •Go•, fui creado por Alan para hacer mas entretenida a esta comunidad.
[i]
[i]• Mi función principal es dar
[i]  una mejor experiencia a los
[i]  miembros de la comunidad
[i]  al interactuar con otros
[i]  miembros
[i]
[i]• Puedes conocer mis comandos
[i]  enviando: .comandos
[i]
[i]• Úsarme con responsabilidad :,)""")

@bot.command('comandos')
async def info(ctx: Context):
    await ctx.send(message="""[buc]Tipos de comandos
[i]
▪︎.interaccion
▪︎.util
▪︎.juegos
▪︎.host
▪︎.staff
▪︎.chat
""")

@bot.command('interaccion')
async def info(ctx: Context):
    await ctx.send(message="""[ubc]Lista de Interacción
[i]
▪︎.abrazar
▪︎.golpear
▪︎.llorar
▪︎.8ball
▪︎.reir
▪︎.esquivar
▪︎.dar
▪︎.funar
▪︎.kill
▪︎.sonrrojar
▪︎.besito
▪︎.beso
▪︎.bailar
▪︎.pedir
▪︎.flcoin
▪︎.say
▪︎.info
▪︎*se
▪︎*le
▪︎*la
""")

@bot.command('se',prefix = '*')
async def se(ctx: Context, args: str):
    await ctx.send(message=f'*{ctx.msg.author.nickname} se {args}.')
    
@bot.command('le',prefix = '*')
async def le(ctx: Context, args: str):
    await ctx.send(message=f'*{ctx.msg.author.nickname} le {args}.')

@bot.command('la',prefix = '*')
async def le(ctx: Context, args: str):
    await ctx.send(message=f'*{ctx.msg.author.nickname} la {args}.')

@bot.command('abrazar')
async def abrazar(ctx: Context, args: str):
    await ctx.send(message=f'{ctx.msg.author.nickname} abraza apasionadamente a {args}.')

@bot.command('golpear')
async def golpear(ctx: Context, args: str):
    await ctx.send(message=f'{ctx.msg.author.nickname} golpea a {args}.')

@bot.command('llorar')
async def llorar(ctx: Context):
    await ctx.send(message=f'{ctx.msg.author.nickname} está llorando.')

@bot.command('8ball')
async def ball(ctx: Context, ball: str):
    lis = ["Es cierto","Es decididamente así","Sin duda","Puedes confiar en ello","Como yo lo veo, sí","Muy probable","Buena perspectiva","Si","Las señales apuntan a que sí","Pregunta confusa, intenta otra vez","Pregunta de nuevo más tarde","Mejor no decirte ahora","No se puede predecir ahora","Concéntrate y pregunta otra vez","No cuentes con eso","Mi respuesta es no","Mis fuentes dicen que no","Perspectiva no tan buena","Dudosamente si","Si","No","Probablemente","100%","No estoy segura"]
    m = random.choice(lis)
    await ctx.reply(message=m)

@bot.command('reir')
async def reir(ctx: Context, args: str = None):
    if args: await ctx.send(message=f'{ctx.msg.author.nickname} se ríe de {args}.')
    else: await ctx.send(message=f'*{ctx.msg.author.nickname} se está riendo.')

@bot.command('esquivar')
async def esquivar(ctx: Context, args: str = None):
    await ctx.send(message=f'{ctx.msg.author.nickname} lo esquiva épicamente.')

@bot.command('dar')
async def dar(ctx: Context, args: str = None):
    if args:
        await ctx.send(message=f'{ctx.msg.author.nickname} está llorando.')
    else:
        await ctx.reply(message=f'{ctx.msg.author.nickname} está llorando.')

@bot.command('funar')
async def esquivar(ctx: Context, args: str = None):
    if args:
        await ctx.send(message=f'{ctx.msg.author.nickname} ha abandonado la conversación.', message_type=109) 

@bot.command('kill')
async def esquivar(ctx: Context, args: str = None):
    await ctx.send(message=f'{ctx.msg.author.nickname} lo esquiva épicamente.')

@bot.command('flcoin', description="Cara o cruz!")
async def on_send(ctx: Context, coins: int, link: str):
    moneda = {"cara","cruz","cara","cruz"}
    moneda = random.choice(moneda)
    await ctx.reply(f'Ha salido: {moneda}')

@bot.command('say')
async def _(ctx: Context, args: str):
    await ctx.reply(args)



@bot.command('bailar')
async def bailar(ctx: Context):
    mx = random.choice(os.listdir('_dance_'))
    f = await File.async_load(f"_dance_/{mx}")
    await ctx.send_gif(f)


@bot.command('util')
async def info(ctx: Context):
    await ctx.send(message="""[ubc]Lista de util
[i]
▪︎.sigueme
▪︎.decir
▪︎.sey
▪︎.global
▪︎.horoscopo
▪︎.loteria
▪︎.claim
▪︎.pokedex
▪︎.dia
▪︎.playlist
▪︎.playURL
▪︎.play
▪︎.ping
▪︎.pong
▪︎.speed
▪︎.count
""")


@bot.command('sigueme')
async def sigueme(ctx: Context):
    await ctx.follow()
    await ctx.reply(message=f"Vale, te sigo {ctx.msg.author.nickname}!!")


@bot.command('decir')
async def decir(ctx: Context, args: str):
  t=''
  for i in args: t= t+i
  out = gTTS(text=t,lang="es",tld='co.in',slow=False); out.save("soundfx.mp3")
  audio = await File.async_load('soundfx.mp3')
  await ctx.send_audio(audio)


@bot.command('ping', description="Pong!")
async def echo(ctx: Context):
  async with ctx.typing():
      await sleep(0.5)
      await ctx.reply('Pong!')


@bot.command('pong', description="Ping!")
async def pong(ctx: Context):
    async with ctx.typing():
        await sleep(0.5)
        await ctx.reply('Ping!')


@bot.command('speed', description="Tiempo que tarda el bot en realizar los comandos")
async def on_speed(ctx: Context):
    timestamp = time.time()
    await ctx.reply('.')
    await ctx.reply(f'Tiempo de procesamiento: {time.time() - timestamp:.2f}s.')


@bot.command('count')
async def on_count(ctx: Context):
    response = await ctx.client.request("GET",f"live-layer?topic=ndtopic%3A{ctx.client.ndc_id}%3Aonline-members&start=0&size=1")
    await ctx.reply(str(response["userProfileCount"]))


@bot.command('chat')
async def info(ctx: Context):
    await ctx.send(message="""[ubc]Lista de comandos de chat
[i]
▪︎.miembros
▪︎.invitar
▪︎.unirse
▪︎.salir
▪︎.ban
▪︎.permaban
▪︎.strike
""")

@bot.command('live')
async def info(ctx: Context):
    await ctx.send(message="""[ubc]Lista de comandos de live
[i]
▪︎.vc
▪︎.videochat
▪︎.playlist
▪︎.endvc
▪︎.end
""")


@bot.command('playlist')
async def playlist(ctx: Context, action: str = None, link: str = None):
    if not action and not link:
      files= os.listdir("_music_")
      o=""
      for f in files: o=o+f+"\n"
      await ctx.send(message=f"""
[c]Music Playlist
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
    elif action == 'add' and link:
        data = await ctx.download_from_link(link)
        dir = os.path.join("_music_/", ".mp3")
        file = open(dir, "w")
        file.save(data)
        
@bot.command('host')
async def info(ctx: Context):
    await ctx.send(message="""[ubc]Lista de comandos de live
[i]
▪︎.get
▪︎.ndc
▪︎.change
▪︎.sleep
""")

@bot.command('get')
async def on_get(ctx: Context, link: str):
    info = await ctx.get_info_link(link)
    await ctx.reply(str(info.community.ndcId))


@bot.command('ndc')
async def on_get(ctx: Context, link: str):
    ndc = await ctx.get_info_link(link)
    await ctx.start_chat(content=ndc)

if __name__ == '__main__':
    bot.start(device_id = d)
