class Pokemon:
    # metodo inicial es el que se ejecuta al ingresar los datos de un pokémon
    def __init__(self):
        self.nombre = ""
        self.elemento = ""
        self.hp = 0
        self.ataque = 0
        self.defensa = 0
        self.ataque_especial = 0
        self.defensa_especial = 0
        self.velocidad = 0
        self.movimientos = []

    # metodos setters que acualizan los datos del pokémon
    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def setHp(self, nuevo_hp):
        self.hp = nuevo_hp

    def setElemento(self, nuevo_elemento):
        self.elemento = nuevo_elemento

    def setAtaque(self, nuevo_ataque):
        self.ataque = nuevo_ataque

    def setDefensa(self, nuevo_rut):
        self.defensa = nuevo_rut

    def setAtaque_especial(self, nuevo_ataque_especial):
        self.ataque_especial = nuevo_ataque_especial

    def setDefensa_especial(self, nuevo_defensa_especial):
        self.defensa_especial = nuevo_defensa_especial

    def setVelocidad(self, nuevo_velocidad):
        self.velocidad = nuevo_velocidad

    def setMovimientos(self, nuevo_movimientos):
        self.movimientos = nuevo_movimientos

    # metodos getters que recuperan los datos del pokémon
    def getNombre(self):
        # la funcion .capitalize() se usa para que la primera letra del nombre del pokemon sea mayuscula, solo es estetico
        return self.nombre.capitalize()

    def getHp(self):
        return self.hp

    def getElemento(self):
        return self.elemento

    def getAtaque(self):
        return self.ataque

    def getDefensa(self):
        return self.defensa

    def getAtaque_especial(self):
        return self.ataque_especial

    def getDefensa_especial(self):
        return self.defensa_especial

    def getVelocidad(self):
        return self.velocidad

    def getMovimientos(self):
        return self.movimientos
