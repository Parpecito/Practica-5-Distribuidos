import Pyro4


class Cliente:
    def __init__(self):
        ns = Pyro4.locateNS()  # Localizamos el NameServer
        uri=ns.lookup("CalculadoraRMI")  # Buscamos el servidor
        self.Servidor=Pyro4.Proxy(uri)  # Con esto le decimos a Pyro4 que se conecte al servidor
    def menu(self):
        while True:
            print("Elige una opcion que deseas realizar")
            print("1.-Sumar")
            print("2.-Restar")
            print("3.-Multiplicar")
            print("4.-Dividir")
            print("5-`Potencia")
            print("6.-Raiz Cuadrada")
            print("7.-Suma de N numeros")
            print("8.-Sucesion de Fibonnaci")
            print("9. Operacion Combinada")
            print("10.-Salir")
            opcion=int(input("Introduce la opcion que vas a realizar: "))
            if opcion==1:
                a=int(input("Introduce el primer numero: "))
                b=int(input("Introduce el segundo numero: "))
                resultado= self.Servidor.sumar(a,b)
                print("El resultado de la suma va a ser ",resultado)
                print("------------------------------------------------")
            elif opcion==2:
                print("Introduce el primer numero")
                a=int(input())
                print("Introduce el segundo numero")
                b=int(input())
                print("El resultado de la resta va a ser ",self.Servidor.restar(a,b))
                print("------------------------------------------------")
            elif opcion==3:
                print("Introduce el primer numero")
                a=int(input())
                print("Introduce el segundo numero")
                b=int(input())
                print("El resultado de la multiplicacion va a ser ",self.Servidor.multiplicar(a,b))
                print("------------------------------------------------")
            elif opcion==4:
                print("Introduce el primer numero")
                a=int(input())
                print("Introduce el segundo numero")
                b=int(input())
                print("El resultado de la division va a ser ",self.Servidor.dividir(a,b))
                print("------------------------------------------------")
            elif opcion==5:
                print("Introduce el primer numero")
                a=int(input())
                print("Introduce el segundo numero")
                b=int(input())
                print("El resultado de la potencia va a ser ",self.Servidor.potencia(a,b))
                print("------------------------------------------------")
            elif opcion==6:
                print("Introduce el numero al que le vas a sacar la raiz cuadrada")
                a=int(input())
                print("El resultado de la raiz cuadrada va a ser ",self.Servidor.raizCuadrada(a))
                print("------------------------------------------------")
            elif opcion==7:
                print("Introduce los numeros que deseas sumar seguidimamente")
                a=int(input())
                print("El resultaod es ", self.Servidor.sumaNnumeros(a))
                print("------------------------------------------------")
            elif opcion==8:
                print("Introduce el numero hasta el que deseas la sucesion de Fibonnaci")
                a=int(input())
                print("El resultado de la sucesion de Fibonnaci es ",self.Servidor.sucesionFibonnaci(a))
                print("------------------------------------------------")
            elif opcion==9:
                print("Introduce el primer numero")
                a=int(input())
                print("Introduce el segundo numero")
                b=int(input())
                print("Introduce el tercer numero que va a ser el que multiplique la suma de los dos primeros")
                c=int(input())
                print("El resultado de la operacion combinada es ",self.Servidor.operacionCombinada(a,b,c))
                print("------------------------------------------------")
            elif opcion==10:
                print("Saliendo del programa...")
                exit()
            else:
                print("Opcion invalida")
                self.menu()


cliente=Cliente()

cliente.menu()









