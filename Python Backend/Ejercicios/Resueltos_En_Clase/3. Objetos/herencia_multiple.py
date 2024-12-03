class Volador:
    def volar(self):
        print('Estoy Volando')

class Nadador:
    def nadar(self):
        print('Estoy Nadando')

class SuperHeroe(Volador, Nadador):
    def saludar(self):
        pass

heroe = SuperHeroe()
