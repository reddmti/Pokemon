import math
import random
from moves import get_move
from class_pokemon import Pokemon


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def HP(Base):
    level = 50
    IV = 31
    EV = 250
    HP = ((((Base + IV) * 2 + (math.sqrt(EV) / 4)) * level) / 100) + level + 10
    return HP


def stats(Puntos):
    level = 50
    IV = 31
    EV = 250
    Stat = ((((Puntos + IV) * 2 + (math.sqrt(EV) / 4)) * level) / 100) + 5
    return Stat


def cargarDatos(archivo):
    fd = open(archivo, "r")
    listaDatos = []
    for filafd in fd:
        filafd = filafd.strip()
        lisFila = filafd.split(",")
        listaDatos.append(lisFila)
    fd.close()
    return listaDatos


def datos_del_pokemon(pokemon_datos):
    for i in range(len(lista_datos)):
        if pokemon_datos in lista_datos[i]:
            datos_pokemon = lista_datos[i]
    return datos_pokemon


def num_pokemon(dato):
    i = 0
    for i in range(len(tabla_efectividad)):
        if dato == tabla_efectividad[i][0]:
            break
            i = i + 1
    num = i
    return num


def verificador_pokemon(pokemon_seleccionado):
    num = 0
    for i in range(len(lista_datos)):
        if pokemon_seleccionado == lista_datos[i][0]:
            num = i
    while pokemon_seleccionado != lista_datos[num][0]:
        pokemon_seleccionado = input('Pokémon no registrado en la pokédex, ingrese otro: ')
        for i in range(len(lista_datos)):
            if pokemon_seleccionado == lista_datos[i][0]:
                num = i
    return pokemon_seleccionado


def stab(elemento, naturaleza_ataque):
    stab = 1.2
    if elemento != naturaleza_ataque:
        stab = 1
    return stab


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
iniciar=input('¿iniciar juego? si o no: ')
print('   ______     ____')
print('  /\/\/\/\   | "0 \ ')
print('<|\/\/\/\/|_/ /___/')
print(' |___________/ ')
print(' |_|_|  /_/_/')
print('\n-->')
while iniciar==('si'):
    print('Bienvenido al simulador')
    lista_datos = cargarDatos('pokemon_data.csv')
    pokemon_seleccionado = input('Ingrese el nombre del primer Pokémon: ')

    pokemon_seleccionado = verificador_pokemon(pokemon_seleccionado)

    datos_pokemon = datos_del_pokemon(pokemon_seleccionado)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print(f'\nNombre del Pokémon seleccionado: {pokemon1.getNombre()}')
    print('\nEstadísticas base del Pokémon: ')
    print(f'\t- HP = {pokemon1.getHp()}')
    print(f'\t- Ataque = {pokemon1.getAtaque()}')
    print(f'\t- Defensa = {pokemon1.getDefensa()}')
    print(f'\t- Ataque especial = {pokemon1.getAtaque_especial()}')
    print(f'\t- Defensa especial = {pokemon1.getDefensa_especial()}')
    print(f'\t- Velocidad = {pokemon1.getVelocidad()}')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print('\nMovimientos que puede aprender el pokémon:')
    #
    i = 0
    for i in range(len(pokemon1.getMovimientos())):
        print(f'{i} - {pokemon1.getMovimientos()[i]}')
        i = +1
    #
    def mov0():
        ataque = int(input("Seleccione un ataque a ejecutar: "))

        ataque = pokemon1.getMovimientos()[ataque]

        movimiento_ataque = get_move(ataque)[1]

        while int(movimiento_ataque) == 0:
            ataque = int(input("Este ataque tiene 0 de daño, seleccione otro ataque: "))
            ataque = pokemon1.getMovimientos()[ataque]
            movimiento_ataque = get_move(ataque)[1]

        return (movimiento_ataque,ataque)

    movimientoyataque=mov0()
    movimiento_ataque=movimientoyataque[0]
    ataque=movimientoyataque[1]
    print(f"El ataque seleccionado es: {ataque}")

    print('Poder de ataque es: ', movimiento_ataque)

    print(f'El hp al nivel 50 de {pokemon1.getNombre()} es', HP(pokemon1.getHp()))

    ataque_fisico = stats(pokemon1.getAtaque())
    print(f'El atk al nivel 50 de {pokemon1.getNombre()} es', ataque_fisico)

    print(f'El def al nivel 50 de {pokemon1.getNombre()} es', stats(pokemon1.getDefensa()))

    ataque_especial = stats(pokemon1.getAtaque_especial())
    print(f'El spa al nivel 50 de {pokemon1.getNombre()} es', ataque_especial)

    defensa_especial = stats(pokemon1.getDefensa_especial())
    print(f'El spd al nivel 50 de {pokemon1.getNombre()} es', defensa_especial)

    print(f'El spe al nivel 50 de {pokemon1.getNombre()} es', stats(pokemon1.getVelocidad()))
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    pokemon_atacante = input('Ingrese el nombre a atacar Pokémon: ')
    datos_pokemon_atacante = datos_del_pokemon(pokemon_atacante)
    naturaleza_ataque = get_move(ataque)[2]
    tipo_ataque = get_move(ataque)[3]

    pokemon2 = Pokemon()
    pokemon2.setNombre(datos_pokemon_atacante[0])
    pokemon2.setElemento(datos_pokemon_atacante[1])
    pokemon2.setHp(int(datos_pokemon_atacante[2]))
    pokemon2.setDefensa(int(datos_pokemon_atacante[4]))
    pokemon2.setDefensa_especial(int(datos_pokemon_atacante[6]))

    naturaleza_pokemon_enemigo = pokemon2.getElemento()
    print('\nNombre del Pokémon seleccionado:', pokemon2.getNombre())

    HP_enemigo = ((((((pokemon2.getHp() + 31) * 2) + ((250 ** 0.5) / 4)) * 50) / 100) + (50 + 10))

    defensa_fisica_enemiga = stats(pokemon2.getDefensa())
    defensa_especial_enemiga = stats(pokemon2.getDefensa_especial())

    print(f'\nEl hp al nivel 50 de {pokemon2.getNombre()} es', HP_enemigo)
    tipo_defensa_enemigo = pokemon2.getElemento()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    tabla_efectividad = cargarDatos('tabla_efectividad.csv')
    numero_atk = num_pokemon(naturaleza_ataque)
    numero_def = num_pokemon(tipo_defensa_enemigo)
    tipo = tabla_efectividad[numero_atk][numero_def]

    stab = stab(pokemon1.getElemento(), naturaleza_ataque)

    num_random = round((random.uniform(0.85, 1)), 2)
    modifier = float(tipo) * stab * num_random * 1

    def dmg_realizar(tipo_ataque, movimiento_ataque, ataque_especial, ataque_fisico, defensa_especial_enemiga,
                     defensa_fisica_enemiga, modifier):
        if tipo_ataque == 'special':
            dmg_realizar = ((((((2 * 50) / 5) + 2) * int(movimiento_ataque) * (
                        ataque_especial / defensa_especial_enemiga)) / 50) + 2) * modifier

        elif tipo_ataque == 'physical':
            dmg_realizar = ((((((2 * 50) / 5) + 2) * int(movimiento_ataque) * (
                        ataque_fisico / defensa_fisica_enemiga)) / 50) + 2) * modifier
        return dmg_realizar


    dmg_realizar = dmg_realizar(tipo_ataque, movimiento_ataque, ataque_especial, ataque_fisico, defensa_especial_enemiga,
                                defensa_fisica_enemiga, modifier)

    print(f'El daño que realizó {pokemon1.getNombre()} a {pokemon2.getNombre()} fue de:', dmg_realizar)
    print(f'\n{pokemon2.getNombre()} quedó con un HP de:', HP_enemigo - dmg_realizar)
