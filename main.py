class Persona:
    def __init__(self,nombre,apellido,dni,idioma,adina):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = " "
        self.dni = dni
        self.adina = adina
        self.idioma = idioma

    def hitz_egin(self):
        if self.idioma == "euskera":
            return "Kaixo!!"
        if self.idioma == "castellano":
            return "Hola!!"
        if self.idioma == "ingles":
            return"Hellow!!"

    def botoa_eman(self):
        if self.adina < 18:
            if self.idioma == "euskera":
                print("Ezin duzu bozkatu!!")
            if self.idioma == "castellano":
                print("No puedes botar!!")
            if self.idioma == "ingles":
                print("You can't bote!!")
        else:
            if self.idioma == "euskera":
                print("Bozkatzeko aukera duzu!!")
            if self.idioma == "castellano":
                print("Tienes permiso para votar!!")
            if self.idioma == "ingles":
                print("You can bote!!")

    def nan_balidazioa(self):
        palabra = "TRWAGMYFPDXBNJZSQVHLCKE"
        dni_sin = self.dni[:-1]

        if palabra[int(dni_sin)%23] == self.dni[8]:
            if self.idioma == "euskera":
                print("NAN-a zuzen dago!!")
            if self.idioma == "castellano":
                print("El DNI es correcto!!")
            if self.idioma == "ingles":
                print("DNI was incorrect!!")
        else:
            if self.idioma == "euskera":
                print("NAN-a ez dago zuzen!!")
            if self.idioma == "castellano":
                print("El DNI es incorrecto!!")
            if self.idioma == "ingles":
                print("Is the incorrect DNI!!")

p1 = Persona("Iñigo","Perez","72605276A","euskera",24)
p2 = Persona("Ander","Erandio","72602276A","castellano",12)

p1.botoa_eman()
print(p1.hitz_egin())
p1.nan_balidazioa()
print("---------------------")
p2.botoa_eman()
print(p2.hitz_egin())
p2.nan_balidazioa()