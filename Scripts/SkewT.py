import pandas as pd
import numpy as np
import metpy.calc as mpcalc
from datetime import datetime
from siphon.simplewebservice.wyoming import WyomingUpperAir
from metpy.units import units
import metpy.plots as plots 
import matplotlib.pyplot as plt

#Selecionando o arquivo
#Ajustando data 
date = datetime(2020,1,10,0)
station = '83378'
#Chamando a base de dados para uma estação em brasília 
df = WyomingUpperAir.request_data(date,station)


#Pegando os dados
p = df['pressure'].values * units(df.units['pressure'])
t = df['temperature'].values * units(df.units['temperature'])
td = df['dewpoint'].values * units(df.units['dewpoint'])
u = df['u_wind'].values * units(df.units['u_wind'])
v = df['v_wind'].values * units(df.units['v_wind'])

#Defininindo a figura e como objeto do metodo Skew
fig = plt.figure(figsize=(9,9))
skew = plots.SkewT(fig)

skew.plot(p,t,'red')
skew.plot(p,td,'green')
skew.ax.set_ylim(1000,50)
skew.ax.set_xlim(-60,40)

#Criando uma maskara para filtrar dados
mask = p >= 100 * units.hPa

#####skew.plot_barbs(p[mask][::2],u[mask][::2],v[mask][::2])

#Criando uma assimilação para cada indíce em relação as barbelas

interval = np.arange(100,1000,50) * units.hPa
index = mpcalc.resample_nn_1d(p,interval)

####skew.plot_barbs(p[index],u[index],v[index])

#Como o skew-t é baseado em escala logarítma o espaço faltante pode ser preenchido relacionando as barbelas para cada nível de pressão

interval_log = np.logspace(2,3) * units.hPa
index_log  = mpcalc.resample_nn_1d(p,interval_log)

skew.plot_barbs(p[index_log],u[index_log],v[index_log])


plt.show()
plt.savefig("./Output/Skew_t_maiscompleto_Brasilia.jpg", dpi = 500)