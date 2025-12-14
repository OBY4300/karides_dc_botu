from config import *
import sqlite3
import ollama

conn = sqlite3.connect("data.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS kullanicilar (kullanici_adi, sifre TEXT, katilma_tarihi TEXT)") #Veri tablosunu oluştur.

def yeni_giris(kullanici_adi, sifre, katilma_tarihi):
	cur.execute("INSERT INTO kullanicilar (kullanici_adi, sifre, katilma_tarihi) VALUES (?, ?, ?)", (kullanici_adi, sifre, katilma_tarihi))
	conn.commit()
def isim_ver(sifre):
	deger = cur.executemany("SELECT * FROM kullanicilar WHERE sifre = (?)", (sifre,))
	return deger.fetchone()

def zaten_varmi(kullanici_adi):
	cur.execute("SELECT 1 FROM kullanicilar WHERE kullanici_adi = (?)", (kullanici_adi,))
	return cur.fetchone() is not None
	
async def yapay_zeka(giris: str, kullanici_ismi):
		cevap = ollama.generate(model="deepseek-r1:1.5b", prompt=f"{giris} You can refer to me as {kullanici_ismi} Please keep your answer below 500 chracters. You will help me determine my future career please answer specifically in this topic")
		return cevap["response"]
"""
		#Bir önceki cevapları hatırlayabilen bir yazışma arayüzü için:
		messages = [
		    {"role": "user", "content": f"{giris}. You can refer to me as {kullanici_ismi}."},
		]
		response = ollama.chat(model="deepseek-r1:1.5b", messages=messages)

		return response["message"]["content"]
"""