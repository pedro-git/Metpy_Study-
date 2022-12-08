import matplotlib.pyplot as plt 
import pandas as pd
import xarray as xr
import metpy.calc as  mpcalc
from metpy.units import units
#Sliders interativos 
from ipywidgets import interact,FloatSlider,IntSlider 

#Função da calculadora 
def calculate_dewpoint(temperature,rh):
    #Arrumando as unidades 
    temperature = temperature*units.degC
    rh = rh*units.percent
    #Utilizando a função vinda do metpy com 1 casa decimal  e organizando as unidads 
    return (mpcalc.dewpoint_from_relative_humidity(temperature,rh).to('degC'),1)

#Criando os objetos passiveis de se usar no slider 
temperature_slider = FloatSlider(min=32,max=90,step=0.5,value=65)
rh_slider = IntSlider(min=1,max=100,value=50)

#Hud interativo calculando o ponto de orvalho
interact(calculate_dewpoint, temperature = temperature_slider,rh=rh_slider)

#Teste 
print(calculate_dewpoint(10,40)) 
