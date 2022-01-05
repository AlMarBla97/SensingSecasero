from SI7006A20 import SI7006A20
from pycoproc_2 import Pycoproc

class sense:
    #py = Pycoproc()
    def getTemp():
        py = Pycoproc()
        si = SI7006A20(py)                      #Lllamar al sensor de humedad y temp (SI7006-A20) con 'si'
        Temperature = str(si.temperature())
        print('Temperatura igual a:  ' , Temperature, ' ºC')
        return Temperature

    def getHum():
        py = Pycoproc()
        si = SI7006A20(py)                      #Lllamar al sensor de humedad y temp (SI7006-A20) con 'si'
        HumRelativa = str(si.humidity())
        print('Humedad relativa del: ' , HumRelativa, ' %')
        return HumRelativa
