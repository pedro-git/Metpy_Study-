from metpy.units import units

#Para adicionar unidades basta multiplicar pelo objeto de units 
a = 25 * units.km
b = 5 * units('miles')

c = 25 * units.degC
d = 6 * units.degC

#Convertendo unidadades usando to.("Unidade")

print(c.to('kelvin') - d.to('kelvin'))

#Usando delta das unidades 

print(c + 20 * units.delta_degF)