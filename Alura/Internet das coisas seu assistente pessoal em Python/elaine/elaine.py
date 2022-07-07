import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from paho.mqtt import publish

assistente = 'elaine'

# FUNÇÔES PRINCIPAIS
def cria_audio(mensagem, local): #função para criar audio
    tts = gTTS(mensagem, lang='pt-br') #Cria um audio de acordo com o parametro passado
    tts.save('audios/'+local+'.mp3') #Insere o diretorio e o nome desejado para salvar
    playsound('audios/'+local+'.mp3')

def AssistenteResponde(arquivo):
    playsound('audios/'+arquivo+'.mp3')

def executa_comando(trigger):
    if 'apresente' in trigger:
        AssistenteResponde('apresentacao')

    elif 'luz' in trigger:
        if 'ligar' in trigger:
            publica_mqtt('/luz', '1')
        elif 'apaga' in trigger:
            publica_mqtt('/luz', '0')

    elif 'tv' in trigger:
        if 'ligar' in trigger:
            publica_mqtt('/tv', '1')
        elif 'desliga' and 'tv' in trigger:
            publica_mqtt('/tv', '0')

    elif 'ar' in trigger:
        if 'ligar' in trigger:
            publica_mqtt('/ar', '1')
        elif 'desliga' in trigger:
            publica_mqtt('/ar', '0')

    else:
        AssistenteResponde('comandoinvalido')

def CapturaImprimeMicrofone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True: #Deixando em loop
            print("Aguardando o Comando")
            audio = microfone.listen(source) #Captura o audio do microfone

            try:
                trigger = microfone.recognize_google(audio, language='pt-BR') #atribui o texto do audio capturado para o trigger
                trigger = trigger.lower() #Transformando tudo em minusculo para evitar problemas de comparação

                if assistente in trigger: # se 'elaine' estiver dentro da frase ele executa
                    print('Comando: ', trigger) #Imprime o trigger
                    AssistenteResponde('feedback')
                    executa_comando(trigger)
                    break

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio") #Tratamento de erro - Documentação do python
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e)) #Tratamento de erro - Documentação python
    return trigger

#FUNÇÔES DO COMANDO DE VOZ

def publica_mqtt(topic, payload):
    publish.single(topic, payload=payload, qos=1, retain=True, hostname="broker.hivemq.com", port=1883, client_id="TrabalhoAPS", auth={'username': 'trabalhoaps', 'password':'123'})


def main():
    while True:
        CapturaImprimeMicrofone()

main()