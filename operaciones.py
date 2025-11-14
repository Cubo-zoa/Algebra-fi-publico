import ConversionesComplejas as CC #modulo de conversiones
import sympy as s

def multi(z,w):
    formasz = CC.complejo(z) #estas dos lineas transforman al numero ingresado a todas sus formas para versatilidad.
    formasw = CC.complejo(w)
    mod = formasz[1][0]*formasw[1][0] #modulo de la multiplicacion
    arg = int(s.deg(formasz[1][1]))+int(s.deg(formasw[1][1])) #argumento de la multiplicacion
    if arg > 360: #este bucle convierte los angulos fuera el intervalo de trabajo al intervalo trabajado
        while arg >360:
            arg -= 360
    elif arg < 0:
        while arg < 0:
            arg += 360
    polnum = str(int(mod)) + 'cis' + str(int(arg)) # hecho cadena para poder ser procesado por la funcion de conversiones
    num = CC.complejo(polnum) # los resultados en todas sus formas.
    return num

def div(z,w): #esta parte es igual a la multiplicacion, solo divide para el modulo y resta para el argumento
    formasz = CC.complejo(z) 
    formasw = CC.complejo(w)
    mod = formasz[1][0]/formasw[1][0]
    arg = int(s.deg(formasz[1][1]))-int(s.deg(formasw[1][1]))
    if arg > 360:
        while arg >360:
            arg -= 360
    elif arg < 0:
        while arg < 0:
            arg += 360
    polnum = str(int(mod)) + 'cis' + str(int(arg))
    num = CC.complejo(polnum)
    return num

def sub(z,w):
    formasz = CC.complejo(z)
    formasw = CC.complejo(w)
    a = s.sympify(formasz[0][0])-s.sympify(formasw[0][0]) # en este caso se utiliza la forma binómica y se  suma parte real con real y imaginario con imaginario
    b = s.sympify(formasz[0][1])-s.sympify(formasw[0][1])
    match b:
        case _ if b == 0:
            binomnum = str(a)
        case _ if b == 1:
            binomnum = str(a) + '+i'
        case _ if b > 1:
            binomnum = str(a) + '+' + str(b) + 'i'
        case _:
            binomnum = str(a) + str(b) + "i"
    if a == 0:
        binomnum = str(b) + 'i'
    num = CC.complejo(binomnum)
    return num



def add(z,w):
    formasz = CC.complejo(z)
    formasw = CC.complejo(w)
    a = s.sympify(formasz[0][0])+s.sympify(formasw[0][0])# en este caso se utiliza la forma binómica y se resta parte real con real y imaginario con imaginario
    b = s.sympify(formasz[0][1])+s.sympify(formasw[0][1])
    match b:
        case _ if b == 0:
            binomnum = str(a)
        case _ if b < 0:
            binomnum = str(a) + "+" + str(b) + "i"
        case _ if b == 1:
            binomnum = str(a) + "+i"
        case _:
            binomnum = str(a) + str(b) + "i"
    num = CC.complejo(binomnum)
    return num

def conj(z):
    formasz = CC.complejo(z)
    a = s.sympify(formasz[0][0]) #tambien se utiliza la binomica y solo se le cambia el signo a la parte imaginaria.
    b = s.sympify(formasz[0][1])
    match b:
        case _ if b == 0:
            binomnum = str(a)
        case _ if b < 0:
            binomnum = str(a) + "+" + str(-b) + "i"
        case _ if b == 1:
            binomnum = str(a) + "+i"
        case _:
            binomnum = str(a) + str(-b) + "i"
    if a == 0:
        binomnum = str(-b)+"i"

    num = CC.complejo (binomnum)
    return num

def sqrt(z):
    n = int(input("entra la potencia de la raiz")) # guarda la enesima raiz
    formasz = CC.complejo(z)
    argroots = [] #lista vacia para contener cuantas raices se quiera.
    k = 0 #constante para sumarle los angulos
    mod = s.sympify(formasz[1][0]) 
    arg = s.sympify(formasz[1][1])
    modroot = s.root(mod, n) #la raiz enesima del modulo
    for i in range (0,n): #bucle que añade a la lista las soluciones
        root = (s.deg(arg) + 360*k)/n #formula del argumento
        temp = (str(modroot),str(root)) #tupla para crear un tipo de matriz
        argroots.append(temp)
        k += 1
    return argroots

def pot(z):
    n = int(input("Entra el exponente"))
    formasz = CC.complejo(z)
    mod = s.sympify(formasz[1][0]) #Para pasar raiz de algo a decimal
    arg = s.sympify(formasz[1][1]) #Por si el argumento es raro, borrar si no funciona
    mod = mod**n 
    arg = arg*n
    if arg > 360: #este bucle convierte los angulos fuera el intervalo de trabajo al intervalo trabajado
        while arg >360:
            arg -= 360
    elif arg < 0:
        while arg < 0:
            arg += 360
    polnum = str(int(mod)) + 'cis' + str(int(arg)) # hecho cadena para poder ser procesado por la funcion de conversiones
    num = CC.complejo(polnum) # los resultados en todas sus formas.
    return num



