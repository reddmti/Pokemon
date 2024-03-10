def HP(Base):
    level = 50
    IV = 31
    EV = 250
    HP = ((((Base + IV) * 2 + (math.sqrt(EV) / 4)) * level) / 100) + level + 10
    return HP


def HP_enemigo(Base):
    ((((((Base + 31) * 2) + ((250 ** 0.5) / 4)) * 50) / 100) + (50 + 10))
    return HP_enemigo


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


def datos_del_pokemon(pokemon_datos,lista_datos):
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


def verificador_pokemon(pokemon_seleccionado,lista_datos):
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

def Movimientos(movimientos):
    i=0
    for i in range(len(movimientos)):
        print(f"{i}-{movimientos[i]}")
        i=+1
    return ""