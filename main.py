import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from playsound import playsound 
import time
import pyautogui
from gtts import gTTS, tts
import random
import webbrowser
import pyttsx3
import os


def descansar():
    time.sleep(2)

class virtual_assit():
    def __init__(self, assistente, pessoa):
        self.person = pessoa
        self.assit_name = assistente

        self.engine = pyttsx3.init()
        self.microfone = sr.Recognizer()
        
        self.voice_data = ''
    def assistente_fala(self, text):
        """
        fala da assitente virtual
        """
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def assistente_fala(self, audio_strig):
        audio_strig = str(audio_strig)
        tts = gTTS(text=audio_strig, lang='pt-BR')
        r = random.randint(1, 20000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(f"C:\eubrunodev\Assistente\Audios\{audio_file}")
        time.sleep(1)
        playsound(f"C:\eubrunodev\Assistente\Audios\{audio_file}")
        #f"C:\eubrunodev\Assistente\{audio_file}"
        #C:\eubrunodev\audio13475.mp3
        time.sleep(1)
        print(self.assit_name + ':', audio_strig)
        #time.sleep(10)
        #os.remove(f"Audios\{audio_file}")

    def record_audio(self, ask=""):
        with sr.Microphone() as source:
            if ask:
                self.assistente_fala(ask)
            #Chama um algoritmo de reducao de ruidos no som
            self.microfone.adjust_for_ambient_noise(source)
            
            #Frase para o usuario dizer algo
            print("Diga alguma coisa: ")
            
            #Armazena o que foi dito numa variavel
            audio = self.microfone.listen(source)
            print('Aguarde...')
            try:
                self.voice_data = self.microfone.recognize_google(audio,language='pt-BR')

            except sr.UnknownValueError:
                self.assistente_fala(f'Desculpe {self.person}, eu não entendi o que você falou')

            except sr.RequestError:
                self.assistente_fala('Deu error no meu sistema')

            print(">>",self.voice_data.lower()) #imprime o que vc disse
            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def there_exist(self, terms):
        """
        função para identificar se o termo existe
        """
        for term in terms:
            if term in self.voice_data:
                return True

    def respond(self, voice_data):

        if self.there_exist(['oi', 'ola', 'olá', 'eae', 'hello', 'e aí']):
            greetigns = [f'Olá {self.person}, eu sou a {self.assit_name}, em que posso ajudar?']

            greet = greetigns[random.randint(0,len(greetigns)-1)]
            self.assistente_fala(greet)

        #youtube
        if self.there_exist(['toque']):
            search_term = voice_data.split("toque")[-1]
            url =  "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            time.sleep(1)
            self.assistente_fala("achei esse vídeo sobre " + search_term + 'no youtube')
            time.sleep(2)
            pyautogui.click(x=780, y=234)

        #discord
        if self.there_exist(["abrir discord"]):
            #descansar()
            pyautogui.press('winleft')
            descansar()
            pyautogui.write('discord')
            descansar()
            pyautogui.press('enter')
            descansar()
            pyautogui.press('esc')
            self.assistente_fala(f'{self.person}, estou abrindo o Discord par você!')

        if self.there_exist(["tocar"]):
            item_pesquisa = voice_data.split("tocar")[-1]
            link_youtube = 'https://www.youtube.com'
            navegador = webdriver.Chrome()

            # navegador.get('https://www.google.com.br')
            navegador.get(link_youtube)

            time.sleep(2)
            # clica aonde digita
            elemento_busca = navegador.find_element(By.NAME, "search_query")
            # digita o que voce procura
            time.sleep(2)
            elemento_busca.send_keys(f"{item_pesquisa}")
            time.sleep(2)
            # clica no botao de pesquisa
            navegador.find_element(By.ID, 'search-icon-legacy').click()
            descansar()
            navegador.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()
            self.assistente_fala(f'{self.person}, encontrei isso sobre {item_pesquisa} no youtube!')
        if self.there_exist(["abrir spotify"]):
            pyautogui.press('winleft')
            descansar()
            pyautogui.write('spotify')
            descansar()
            pyautogui.press('enter')
            descansar()
            self.assistente_fala(f'{self.person}, estou abrindo o Spotify par você!')
        if self.there_exist(["buscar"]):
            # lembre-se de estar em tela cheia
            search_term = voice_data.split("buscar")[-1]
            pyautogui.click(367, 752)
            descansar()
            pyautogui.click(107, 103)
            descansar()
            pyautogui.write(search_term)
            descansar()
            pyautogui.click(710, 150)
        if self.there_exist(["nitro"]):
            pyautogui.press('winleft')
            descansar()
            pyautogui.write('steel')
            descansar()
            pyautogui.press('enter')
            descansar()
            pyautogui.press('esc')
            self.assistente_fala(f'{self.person}, irei pegar o Link, não use o Computador durante o processo!')

assistente = virtual_assit('synzada', 'GlockHS')

while True:
    voice_data = assistente.record_audio('Mais alguma coisa?')
    assistente.respond(voice_data)

    if assistente.there_exist(['bye', 'stop', 'parar', 'sair', 'fechar', 'tchau', 'até mais', 'não']):
        assistente.assistente_fala(f"Tchau {assistente.person}.. Tenha um ótimo dia!")
        break