import sounddevice as sd
import soundfile as sf
import numpy
def record(time,file_name):
    frekans = 44100
    print("kaydediliyor")
    ses = sd.rec(int(time * frekans), samplerate=frekans, channels=2)
    sd.wait()
    print("kaydedildi")
    sf.write(file_name,ses,frekans)

sure = float(input("Kaydedilcek süreyi saniye cinsinden girin: "))
dosya_adi = input("Kaydedilecek dosyanın ismini yazın: ") + ".wav"
record(sure,dosya_adi)