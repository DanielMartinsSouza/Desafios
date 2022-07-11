from gtts import gTTS
from playsound import playsound

def cria_audio(audio): #função para criar audio
    tts = gTTS(audio, lang='pt-br') #Cria um audio de acordo com o parametro passado
    tts.save('audios/comandoinvalido.mp3') #Insere o diretorio e o nome desejado para salvar



cria_audio("Não compreendo!!")
playsound('audios/comandoinvalido.mp3')