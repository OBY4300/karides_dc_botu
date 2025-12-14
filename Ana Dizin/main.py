from config import *
from logic import *

from discord.ext import commands
import discord
import asyncio
import time
from datetime import date
from translate import Translator

cevirici_en_tr = Translator(from_lang="en", to_lang="tr")
cevirici_tr_en = Translator(from_lang="tr", to_lang="en")

translation = cevirici_tr_en.translate("Merhaba, nasılsınız?")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
suanki_tarih = str(date.today())

#Kullanılabilir komutların bir listesi
komutlar = ["!about", "!merhaba", "!help", "!kayit_ol", "!kariyer_onerisi"]

mesaj_isleme = True
mesaj_kanali = "guild"

@bot.event
async def on_ready():
	print(f"{bot.user} olarak giriş yaptık.")

@bot.event
async def on_message(message):
	global mesaj_kanali
	#if mesaj_isleme == True:
	if message.author == bot.user:
		return
	if isinstance(message.channel, discord.DMChannel):
		mesaj_kanali = "ozel"
	else:
		mesaj_kanali = "guild"
	await bot.process_commands(message)
#	elif mesaj_isleme == False:
#		await message.send("An itibariyle başka bir kullanıcıya refakat ediyorum, lütfen daha sonra tekrar dene.")

@bot.command()
async def about(ctx):
	await ctx.send(f"Bu kod, kariyer önerileri yapan bir Discord botu için bir şablon. An itibariyle {bot.user} olarak tanımlanıyor olabilir.")


@bot.command()
async def merhaba(ctx):
	await ctx.send("Merhaba! Dilerseniz potansiyel gelecek kariyeriniz için hazırlık yapmaya başlayalım.")
	await ctx.send('"!kayit_ol" yazarak kayıt olduktan sonra, "!kariyer_onerisi" yazarak Deepseek model r1:1.5b' + "'den yardım alabilirsin.")
"""
@bot.command()
async def help(ctx):
	global mesaj_kanali
	if mesaj_kanali == "ozel":
		await ctx.author.send("İşte kullanılabilir komutların bir listesi:", komutlar)
		await ctx.author.send('"!kayit_ol" yazarak kayıt olduktan sonra, "!kariyer_onerisi" yazarak Deepseek model r1:1.5b' + "'den yardım alabilirsin.")
	if mesaj_kanali == "guild":
		await ctx.send("İşte kullanılabilir komutların bir listesi:", komutlar)
		await ctx.send('"!kayit_ol" yazarak kayıt olduktan sonra, "!kariyer_onerisi" yazarak Deepseek model r1:1.5b' + "'den yardım alabilirsin.")
"""
@bot.command()
async def kayit_ol(ctx):
	global suanki_tarih
	global mesaj_isleme
	def check(message):
		return message.author == ctx.author and isinstance(message.channel, discord.DMChannel)

	kullanici_adi = ctx.author.name
	bulunurluk = zaten_varmi(ctx.author.name)
	if bulunurluk == True:
		await ctx.author.send(f'{kullanici_adi}, kayıt olmayı denediniz fakat veri tabanında bulunmaktasınız.')#\nEğer kullanıcı adınızı kaybettiyseniz "!sifre_yardim" komuduna danışın.')
	elif bulunurluk == False:	
		mesaj_isleme = False
		while True:
			await ctx.author.send(f"{kullanici_adi} özel mesajlarına (DM) bakarak, kaydolmak için gerekli talimatları izleyebilir.")
			await ctx.author.send(f"@here! {kullanici_adi} ile kaydolma işlemine giriş yapıldı. Lütfen kaydolmak için başka zaman yeniden deneyin.")
			try:
				await ctx.author.send("Kariyer botu veri tabanına bir hesap kaydetmek için lütfen...")
				await ctx.author.send("Otuz saniye içinde şifrenizi girin. Şifrenizi kimseye göstermemeye dikkat edin!")
				try:
					cevap = await bot.wait_for("message", check=check, timeout=30)
					sifre = cevap.content
					await ctx.author.send(f'Şifreniz "{sifre}". Eğer bu işlemi onaylıyorsanız lütfen "e" ile cevap verin.')
					cevap = await bot.wait_for("message", check=check, timeout=30)
					await ctx.author.send("İşlemi onayladınız.")
				except asyncio.TimeoutError:
					await ctx.author.send("Otuz saniye içinde cevap vermediğiniz için işlem otomatik olarak duraklatıldı.")
					break
				if str(cevap.content).lower() == "e":
					await asyncio.sleep(1.5)
					yeni_giris(str(ctx.author.name), str(sifre), str(suanki_tarih))
					await ctx.author.send("Hesabınız başarıyla oluşturuldu! Şimdi bu sohebti açık bırakıp, diğer komutları tek başınıza deneyebilirsiniz.")
					await ctx.author.send('Kullanılabilir komutların bir listesi için "!help" komutu yeterli olur.')
					break
				elif str(cevap.content).lower() != "e":
					await asyncio.sleep(1.5)
					await ctx.author.send("Şifrenizi onaylamadınız. Lütfen baştan başlayın.")
					await asyncio.sleep(2)
			except discord.Forbidden:
				await ctx.send(f"{kullanici_adi}, kaydolmak için lütfen geçici olarak özel mesajlarınızı açın.")
				mesaj_isleme = True

@bot.command()
async def kariyer_onerisi(ctx):
	def check(message):
		return message.author == ctx.author and isinstance(message.channel, discord.DMChannel)
	
	cevap = ""
	bulunurluk = zaten_varmi(ctx.author.name)
	if bulunurluk == True:
		await ctx.author.send("Kısa süre sonra yapay zeka modu ile size bir kariyer önerisi vereceğim.")
		await ctx.author.send("Lütfen en iyi sonuçlar için uzun bir yazı yazmayı deneyin.")
		while True:
			if cevap == "BREAK":
				await ctx.author.send("Yapay zeka sohbeti durduruluyor...")
				await asyncio.sleep(1.5)
				await ctx.author.send("Durduruldu.")
				break
			elif cevap != "BREAK":
				await ctx.send('Yapay zeka ile yazışmayı durdurmak için "BREAK" yazabilirsiniz.')
				await ctx.author.send("Hazırım. lütfen yapay zekaya demek istediklerinizi eksiksiz şekilde yazın.")
				cevap = await bot.wait_for("message", check=check)
				cevap = cevap.content
				cevap = cevirici_tr_en.translate(str(cevap))
				await ctx.author.send(f"DEBUG: {cevap}")
				await ctx.author.send("Yapay zekanın cevap vermesi uzun bir süre alabilir.")
				yapay_zeka_cevap = await yapay_zeka(cevap, ctx.author)
				yapay_zeka_cevap = cevirici_en_tr.translate(str(yapay_zeka_cevap))
				await ctx.author.send("İşte yapay zekanın verdiği çıktının Türkçe'ye çevirilmiş hali:")
				if "QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS" in yapay_zeka_cevap:
					await ctx.author.send("Yapay zekanın yanıtı beş yüz karakteri aşmış gibi görünüyor.\nVerilen yazı kesik veya direkten boş olabilir.")
				await ctx.author.send(yapay_zeka_cevap)
				await ctx.send("Yapay zeka cevabı sonu.")
	elif bulunurluk == False:
		await ctx.author.send('Lütfen kariyer önerisi almadan "!kayit_ol" komuduyla veri tabanına kayıt olun.')

bot.run(token)

