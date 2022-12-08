from datetime import datetime
import pandas as pd
from siphon.simplewebservice.wyoming import WyomingUpperAir


#Ajustando data 
date = datetime(2020,1,10,0)
station = '83378'
#Chamando a base de dados para uma estação em brasília 
df = WyomingUpperAir.request_data(date,station)

#Salvando o dado baixado

df.to_csv('./Input/UpperAir_Brasilia_20200110.csv')
