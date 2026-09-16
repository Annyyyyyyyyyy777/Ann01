from paciente import Paciente

def main():
    #Crear paciente con el constructor __init__
    p1= Paciente("11.111.111-1","Luis arriagada",40,"Isapre")
    #Mostrar informacion del Paciente
    #__str__ es llamado automaticamente al imprimir el objeto
    print(p1)

if __name__ == "__main__":
    main()  
    