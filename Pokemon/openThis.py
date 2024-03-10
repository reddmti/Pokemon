import math
import random
from moves import get_move
from class_pokemon import Pokemon
import funciones

#iniciar=input('¿iniciar juego? si o no: ')
print('   ______     ____')
print('  /\/\/\/\   | "0 \ ')
print('<|\/\/\/\/|_/ /___/')
print(' |___________/ ')
print(' |_|_|  /_/_/')
print('\n-->')
#while iniciar==('si'):
print('Bienvenido al simulador')
lista_datos = funciones.cargarDatos('pokemon_data.csv')
pokemon_seleccionado = input('Ingrese el nombre del primer Pokémon: ')
pokemon_seleccionado = funciones.verificador_pokemon(pokemon_seleccionado,lista_datos)
datos_pokemon = funciones.datos_del_pokemon(pokemon_seleccionado,lista_datos)

#
print('watafak')
pokemon1 = Pokemon()
pokemon1.setNombre(datos_pokemon[0])
pokemon1.setElemento(datos_pokemon[1])
pokemon1.setHp(int(datos_pokemon[2]))
pokemon1.setAtaque(int(datos_pokemon[3]))
pokemon1.setDefensa(int(datos_pokemon[4]))
pokemon1.setAtaque_especial(int(datos_pokemon[5]))
pokemon1.setDefensa_especial(int(datos_pokemon[6]))
pokemon1.setVelocidad(int(datos_pokemon[7]))
pokemon1.setMovimientos(datos_pokemon[8].split(';'))
print('watafak')
#
print(f'\nNombre del Pokémon seleccionado: {pokemon1.getNombre()}')
print('\nEstadísticas base del Pokémon: ')
print(f'\t- HP = {pokemon1.getHp()}')
print(f'\t- Ataque = {pokemon1.getAtaque()}')
print(f'\t- Defensa = {pokemon1.getDefensa()}')
print(f'\t- Ataque especial = {pokemon1.getAtaque_especial()}')
print(f'\t- Defensa especial = {pokemon1.getDefensa_especial()}')
print(f'\t- Velocidad = {pokemon1.getVelocidad()}')

#
print('\nMovimientos que puede aprender el pokémon:')
print(funciones.Movimientos(pokemon1.getMovimientos()))
ataque = int(input("Seleccione un ataque a ejecutar: "))

ataque = pokemon1.getMovimientos()[ataque]

movimiento_ataque = get_move(ataque)[1]

while int(movimiento_ataque) == 0:
	ataque = int(input("Este ataque tiene 0 de daño, seleccione otro ataque: "))
	ataque = pokemon1.getMovimientos()[ataque]
	movimiento_ataque = get_move(ataque)[1]

