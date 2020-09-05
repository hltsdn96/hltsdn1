
import time
from datetime import datetime
import webbrowser #default_browser
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import os

#halitsudan
r = sr.Recognizer()

def kayıt(ask = False): #kayıt fonksiyonu oluşturduk
    with sr.Microphone(0) as source:
        if ask:
           konus(ask)
        audio = r.listen(source)
        voice = '.'
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            konus('anlamadım')
        except sr.RequestError:
            konus("anlamadım")
        return voice
def cevap(voice): #cevap fn.u oluşturduk
    if 'nasılsın'  in voice:
        konus('Teşekkür ederim, sen nasılsın?' )
    elif 'iyiyim' in voice:
        konus('Bunu duyduğuma sevindim')
    elif 'hasta' in voice:
        konus('Geçmiş olsun! Senin için civardaki eczaneleri arıyorum')
        url1 = 'https://www.google.com/search?q=enyakineczane'
        webbrowser.get().open(url1)
    elif 'saat kaç' in voice:
        konus('saat tam olarak' + datetime.now().strftime('%H %M'))
        print(datetime.now().strftime('%H %M'))
    elif 'arama yap' in voice:
        search = kayıt('Ne aramak istiyorsun?')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        konus(search + ' için bulduklarım')
    elif 'müzik' in voice:
        konus('Elbette.Oynatma listenizi açıkıyorum')
        url2 = 'https://www.youtube.com/watch?v=UDVtMYqUAyw&list=PL0hLcSarbFFrRjuFdmq2gkQ0q_GWKL47S'
        webbrowser.get().open(url2)
    elif 'kapa' in voice:
        count = int(datetime.now().strftime('%H'))
        if count > 9 and count < 18:
            konus('sistem kapatılıyor. iyi günler' )
        else:
            konus('sistem kapatılıyor. iyi geceler')
        exit()


def konus(string):
    tts =  gTTS(string,lang='tr')
    rand = random.randint(1, 10000) #dosya isimlerinin çakışmaması için
    file = 'audio-'+str(rand)+'.mp3' #dosya ismini belirledik
    tts.save(file) # dosyayı kaydet
    playsound(file) #sesi çal
    os.remove(file) #dosya  okunduktan sonra silinsin

konus("Hoşgeldin halit")

time.sleep(0.5)
while 1:
    voice = kayıt()
    print(voice)
    cevap(voice)
























