import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "#", description =  "Bot d'aide aux Helpeurs")

urlconfig = "https://fr.pcpartpicker.com/user/Fayte31/saved/"
urlsitecg = "||https://videocardz.com||"
urlbenchcg1 = "\nhttps://prnt.sc/10myi78\nhttps://prnt.sc/10myjhp\nhttps://prnt.sc/10myk5e"
urlbenchcpu1 = "\nhttps://prnt.sc/10mz3m0\nhttps://prnt.sc/10mz4hj\n"
urlconsocpu1 = "\nhttps://prnt.sc/10mz728"
urlconsogpu1 = "\nhttps://prnt.sc/10mzay9"



@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def who(ctx) :
    await ctx.send("Bonjour à toi, je suis Zodius, un bot pour aider les Helpeurs de serveurs Hardware")

#C:\Bot_discord\zodius.py
@bot.command()
async def config1(ctx):
    await ctx.send("Voici une liste de configurations pc à divers prix !" + " " + urlconfig)

@bot.command()
async def sitecg(ctx):
    await ctx.send("Voici un très bon site qui parle uniquement de cartes graphiques" + " " + urlsitecg)

@bot.command()
async def perfcg(ctx):
    await ctx.send("Voici plusieurs benchmarks indiquant le niveau de puissance de cartes graphiques" + urlbenchcg1)

@bot.command()
async def salesite(ctx):
    await ctx.send("Voici les bon sites sur lesquels tu peux acheter :" + recobon + recomoyen)

@bot.command()
async def badsite(ctx):
    await ctx.send("Voici les mauvais sites sur lesquels tu ne dois pas acheter :" + recoevite + "\n" + raison_evite)

@bot.command()
async def motherboard(ctx):
    embed = discord.Embed(title = "C'est quoi une carte mère ?", colour = discord.Colour.blue())
    embed.add_field(name = "La carte mère", value = topo_motherboard1)
    await ctx.send(embed=embed)

@bot.command()
async def motherboard2(ctx):
    embed = discord.Embed(title =  "C'est quoi une carte mère ?", colour = discord.Colour.blue())
    embed.add_field(name = "Les sockets et Chipsets", value = topo_motherboard2 + topo_motherboard3)
    await ctx.send(embed = embed)

@bot.command()
async def mbintel(ctx):
    embed = discord.Embed(title = "Précisions carte mères Intel", colour = discord.Colour.blue())
    embed.add_field(name = "Sockets Intel", value = topo_motherboardintel + topo_motherboardintel2)
    await ctx.send(embed = embed)

@bot.command()
async def perfcpu(ctx):
    await ctx.send("Voici plusieurs benchmarks indiquant le niveau de puissance des derniers processeurs" + urlbenchcpu1)

@bot.command()
async def consocpu(ctx):
    await ctx.send("Voici un benchmark indiquant le niveau de consommation des derniers processeurs" + urlconsocpu1)

@bot.command()
async def consogpu(ctx):
    await ctx.send("Voici un benchmark indiquant le niveau de consommation des cartes graphiques" + urlconsogpu1)

@bot.command()
async def aide(ctx):
    await ctx.send("Voici la liste de commandes")

@bot.command()
async def mission(ctx):
    await ctx.send("Ma mission est d'aider les Helpeurs Hardware de serveurs hardware.")




        
recobon = "\n \nRECOMANDATION DE VENDEURS\n \nFiable avec bonne couverture client :\n \n- Amazon (Toujours vérifier les vendeurs)\n- Caseking (Allemagne)\n- Cdiscout (Toujours vérifier les vendeurs)\n- Computeruniverse (Allemagne)\n- LDLC\n- Materiel.net\n- Top Achat "
recomoyen = "\n \nMoyen / Pile ou Face (soit pour des soucis de langue, ou de vendeur pas fiable, ou de SAV pas toujours compétent):\n \n- Aliexpress\n- Alternate (Allemagne, Belgique, France)\n- Alza (Allemagne)\n- Arlt (Allemagne)\n- Boulanger.com\n- Cybertek\n- Darty\n- Ebay\n- Fnac\n- Mindfactory (Allemagne)\n- Rakuten (Toujours vérifier les vendeurs)\n- Rue du Commerce "
recoevite = "\n \nA vraiment éviter :\n \n- Grosbill\n- Wish"
raison_evite = "Site à absolument éviter. Pour découvrir les raisons, nous vous invitons à lire les commentaires de leur page Facebook !\nhttps://www.facebook.com/Grosbill"
topo_motherboard1 = "La carte mère est une des pièces essentielles d'un pc. En effet, celle ci a pour but de relier tous les composants de celui-ci : la carte graphique, le processeur, le stockage (hdd ou ssd etc).\nElle est notamment composée d'un PCB (alias le composant en époxy sur lequel on retrouve la majorité des soudures), de VRM (les étages d'alimentations, donnant l'électricité au processeur) d'un socket (par exemple AM4, 115x etc), de slot PCI-Express (où l'on branche des cartes d'acquisition ou la carte graphique par exemple).\n \n"
topo_motherboard2 = "Plusieurs constructeurs de cartes mères se disputent le marché, comme MSI, Gigabyte, ASUS, AsRock etc.\nDeux grands constructeurs de processeurs se disputent également le marché des sockets: les plus récents de AMD sont les socket AM3+ et AM4 (passage au AM5 en fin d'année 2021), tandis que ceux chez Intel sont les sockets LGA 1151 pour les processeurs de 6th à la 9ème génération, et LGA1200 pour ceux de 10ème génération.\nParlons maintenant des chipsets. Les derniers chipsets de chez AMD sont les B450, B550 et x570. Les derniers (corrects) de chez Intel sont les Z390 et Z490 (les Z590 arriveront dans quelques semaines).\n \n"
topo_motherboard3 = "Les chipsets B450 sont compatibles avec tous les Ryzen (attention : mise à jour bios nécessaire et incompabilité avec les anciennes générations), tandis que les B550 et X570 sont compatibles avec les Ryzen de 3e génération (exception faite sur les X570 qui supportent les Ryzen de 2de gen).\n \n"
topo_motherboardintel = "Pour plus d'informations sur les socket LGA 1151 et 1200 d'Intel :\n \nLe socket LGA 1151 est divisé en deux parties, l'une pour accueillir les 6 et 7th gen, et une deuxième pour les 8 et 9th gen.\n \n-Intel 6th Skylake et 6th Kaby Lake (Exemple=i7 6700K et i7 7700K)=B150, H110, H170 et Z170 (màj bios nécessaire pour supporter les 7th) et B250, H270 et Z270 (compatibles avec ces deux générations)\n-Intel 8th Coffee Lake et 9th Coffee Lake Refresh (Exemple=i7 8700K et i9 9900KS)=B360, H310, H370 et Z370 (màj bios nécessaire pour supporter les 9th) et B365 et Z390 (compatibles avec ces deux générations).\n"
topo_motherboardintel2 = "-Intel 10th Comet Lake-S et 11th Rocket Lake (Exemple=i7 10700K et i9 11900K)=H410, H470, B460 et Z490 (màj bios pour supporter les 11th) et B560, H570, H510 et Z590 (compatibles avec ces deux générations)."







bot.run()
