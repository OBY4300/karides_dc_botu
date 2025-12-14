# Karides Discord, Kariyer Öneri Botu:
Bu repositoryde açık kaynak koduna sahip bir Discord botunu bulabilirsiniz.

## Bu botun yararlandığı dış kaynaklar:

- Ollama, yapay zekâ modeli aracı:
<br>https://github.com/ollama/ollama

- discord.py modülü:
<br>https://github.com/Rapptz/discord.py

- sqlite3 modülü:
<br>(url mevcut değil)

## Bu bot ne işe yarar?
Bu Discord botu, çeşitli kariyer önerileri verir. Gemma 3 LLM'sini Ollama'nın yerel entegrasyonu ile kişiselleştirilmiş sorulara cevaplar verebilir.
<br>
Yapay zekânın sahip olduğu kendinden-emin-yalan-söyleme handikapının varlığını da gözden geçirmeyi unutmayın.

## Bu bot nasıl kullanılır?
İlk önce, bu botu çalıştırabilecek dosyaları edinmek için bu depoyu HTTP veya SSH yöntemiyle kopyalayın.
<br>"git clone https://github.com/OBY4300/karides_dc_botu.git" (HTTP yöntemi, bulunduğunuz dizine dosyaları kopyalar)

<br>İkinci olarak Discord botunuzun gizli tokenini config.py'deki "token" değişkeni içine koyun.

<br>Üçüncü olarak https://ollama.com/download/windows adresinden uygun işletim sisteminiz için Ollama uygulamasını indirin.

<br>Dördüncü olarak komut satırınıza (Mac ve Windows) "ollama pull deepseek-r1:1.5b" yazarak Deepseek r1:1.5b yapay zeka modelini bilgisayarınıza inidirin.
<br>(1.1 GB alan gerektirir)

<br>Son olarak logic.py'yi ve sonradan da main.py'yi çalıştırarak (terminalden "python" komuduyla, veya bir İDE ile) bu şablonu kullanarak çalışan bir
<br>Discord botu elde edersiniz.

<br>Fazladan: config.py'deki "model_ismi" değişkenini uygun bir şekilde değiştirerek ve uygun modeli komutlarla indirerek farklı bir yapay zeka modelini kullanabilirsiniz.
<br>Lütfen Ollama aracının Python modülü dokümantasyonuna danışın: https://github.com/ollama/ollama-python

<br>Ayrıca logic.py'nin oluşturduğu "data.db" belgesi "Ana Dizin" klasörünün dışında olmalıdır.
<br>Bu davranışın normal olduğunu bildirmeliyim.



<br><br><br>Bu bottaki yapay zeka özelliklerinin gösterebileceği davranışlardan ben sorumlu değilim.




