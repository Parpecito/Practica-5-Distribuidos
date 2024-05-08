import Pyro4  # Importamos la libreria Pyro4 que nos permitira trabajar con RMI


@Pyro4.expose  # Con esto le decimos a Pyro4 que exponga la clase para que pueda ser utilizada por el servidor
class Servidor(object):

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b

    def potencia(self, a, b):
        return a ** b

    def raizCuadrada(self, a):
        return a ** 0.5

    def sumaNnumerosSeguidos(self,a):
        if(a<=0):
            return "El valor de n debe ser mayor que 0"
        resultado=0
        for i in range(a):
            resultado+=i
        return resultado

    def sucesionFibonnaci(self, n):
        if n<=0:
            return "El valor de n debe ser mayor que 0"
        elif n==1:
            return 0
        elif n==2:
            return 1
        a=0
        b=1
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        return c

    def operacionCombinada(self,a,b,c):
        return (a+b)*c

daemon = Pyro4.Daemon()  # Le pasa el puerto al demonio
ns = Pyro4.locateNS()  # Localizamos el NameServer
uri = daemon.register(Servidor)  # Registramos la funcion suma
ns.register("CalculadoraRMI", uri)
print("Servidor corriendo")

daemon.requestLoop()  # Iniciamos el demonio
