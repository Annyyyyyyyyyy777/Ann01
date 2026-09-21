from paciente import Paciente
pacientes: list [Paciente] = []

def agregar_paciente()->None:
    rut= input ("Ingrese el Rut del paciente: ")
    nombre= input ("Ingrese Nombre del paciente: ")
    edad= int(input ("Ingrese Edad del Paciente: "))
    print("Previsiones disponibles: ")
    print ("1.- Fonasa")
    print ("2.- Isapre")
    prevision= input ("Seleccione la prevision del paciente: ")
    if prevision == "1":
            prevision == "Fonasa"
    else: 
            prevision = "Isapre"
    paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.append(paciente)
    print ("Paciente agregado exitosamente.")

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese  un numero valido.")

def menu()->int:
    opcion=-1
    while opcion<0 or opcion>5:
        print("Menu de clinica")
        print("1.- Agregar paciente")
        print("2.- Editar paciente")
        print("3.- Eliminar Paciente")
        print("4.- Imprimir paciente")
        print("5.- Imprimir todos los pacientes")
        print("0.- Salir")
        opcion= leer_numero("Seleccione una opcion: ")
    return opcion

def main():
    op=-1
    while op!=0:
        op=menu()
        if op==1:
            print("Agregando al paciente")
        elif op==2:
            print("Editando paciente")
        elif op==3:
            print("Eliminando paciente")
        elif op==4:
            print("Imprimiento Paciente")
        elif op==5:
            print("Imprimiendo todos los pacientes")
        elif op==0:
            print("Saliendo del programa")

  


if __name__ == "__main__":
    main()  

