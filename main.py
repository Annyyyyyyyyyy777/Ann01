from paciente import Paciente
pacientes: list[Paciente] = []

def agregar_paciente()->None:
    rut= input("Ingrese el RUT del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    print("Previsiones disponibles: ")
    print("1.- Fonasa")
    print("2.- Isapre")
    prevision = input("Seleccione la previsión del paciente: ")
    if prevision == "1":
        prevision = "Fonasa"
    else:
        prevision = "Isapre"
    try:
        paciente = Paciente(rut, nombre, edad, prevision)
    except (ValueError, TypeError) as e:
        print(f"Error al crear el paciente: {e}")
        return
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

def menu()->int:
    opcion=-1
    while opcion<0 or opcion>5:
        print("Menú de clinica")
        print("1.- Agregar paciente")
        print("2.- Editar paciente")
        print("3.- Eliminar paciente")
        print("4.- Imprimir un paciente")
        print("5.- Imprimir todos los pacientes")
        print("0-. Salir")
        opcion = leer_numero("Seleccione una opción: ")
    return opcion

def buscar_paciente()->Paciente:
    rut = input("Ingrese el R.U.T. del paciente a buscar: ")
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
    return None

def imprimir_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("Paciente no encontrado.")

def imprimir_pacientes()->None:
    if pacientes:
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados.")

def editar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
        print("Menu de edición de paciente")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar previsión")
        opcion = leer_numero("Seleccione una opción: ")
        if opcion == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            try:
                paciente.nombre = nuevo_nombre
            except ValueError as e:
                print(f"Error al actualizar el nombre: {e}")
                return
        elif opcion == 2:
            nueva_edad = leer_numero("Ingrese la nueva edad: ")
            try:
                paciente.edad = nueva_edad
            except (ValueError, TypeError) as e:
                print(f"Error al actualizar la edad: {e}")
                return
        elif opcion == 3:
            print("Previsiones disponibles: ")
            print("1.- Fonasa")
            print("2.- Isapre")
            print("0.- No hacer cambios")
            nueva_prevision = input("Seleccione la nueva previsión: ")
            try:
                if nueva_prevision == "1":
                    paciente.prevision = "Fonasa"
                elif nueva_prevision == "2":
                    paciente.prevision = "Isapre"
                elif nueva_prevision == "0":
                    print("No se realizaron cambios en la previsión.")
                else:
                    print("Opción no válida. No se realizaron cambios en la previsión.")
            except (ValueError, TypeError) as e:
                print(f"Error al actualizar la previsión: {e}")
                return
    else:
        print("Paciente no encontrado.")

def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        pacientes.remove(paciente)
        print("Paciente eliminado exitosamente.")
    else:
        print("Paciente no encontrado.")

def main():
    op=-1
    while op!=0:
        op=menu()
        if op==1:
            print("Agregando paciente")
            agregar_paciente()
        elif op==2:
            print("Editando paciente")
            editar_paciente()
        elif op==3:
            print("Eliminando paciente")
            eliminar_paciente()
        elif op==4:
            print("Imprimiendo un paciente")
            imprimir_paciente()
        elif op==5:
            print("Imprimiendo todos los pacientes")
            imprimir_pacientes()
        elif op==0:
            print("Saliendo del programa")
    
    
if __name__ == "__main__":
    main()  