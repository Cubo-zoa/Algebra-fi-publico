import re #para leer las formas exponenciales y polares
import sympy as s #biblioteca para matematicas simbolicas (principalmente para el input y output pero tambien funciona en vez de cmath o math)

def complejo(x):

    r = 0
    ang = 0

    match True:
        case _ if re.fullmatch(r'[^\diI * ]+', x): #checa si el numero es válido. ejemplo si entra "1-2avs" no será un numero valido. OJO un numero "valido" con espacios ("1 - 2i") tampoco será válido.
            return("Numero no valido")

        case _ if "cis" in x: #case _ por que _ compara con cualquier cosa
            spl = list(re.split('cis', x)) #separa el string de la forma polar, y la convierte en una lista para evitar problemas con el tipo de dato

            if spl[0]=='': # si el primer elem-2ento de la lista de antes esta vacía, significa que el radio es 1 (cis180 por ejemplo tiene r de 1) 
                r = 1
            else:
                r = int(spl[0]) #sin el if de antes te da error, no puedes convertir "nada" a un entero.
        
            ang = s.rad(int(spl[1]))    
            a = s.cos(ang)*r # round para que no te de un valor muy chico, a pesar de que sea 0 el resultado
            b = s.sin(ang)*r

            binom = [a,b] #no lo guardo como complex(a,b) por que está en floating point, y se me hinchan que se vea bonito

            if r == 1:
                exp = [1, ang] # redundante pero mejor para organizacion
                pol = [1, s.deg(ang)]
            else:
                exp = [r, ang] #modulo y angulo en radianes
                pol = [r,s.deg(ang)] #modulo y angulo en grados. No hay "cis" o mas cosas para facilitar las operaciones. 

        case _ if "e^" in x:
            x = re.sub('[*I|*i|I|i]$','',x) #[] conjunto de caracteres | "o" $ termina con (para que no tome a la i de "pi" sino la imaginaria.)
            spl = list(re.split(r'e\^', x)) #hace lo mismo que el re.split de antes, solo que la doble barra invertida escapa al ^

            if spl[0]=='': 
                r = 1
            else:
                r = int(spl[0]) 

            ang = spl[1]  #no necesita en radianes por que el exponente de e ya esta en radianes
            a = s.cos(ang)*r
            b = s.sin(ang)*r

            binom = [a,b]
            if r == 1:
                pol = [1, s.deg(s.sympify(ang))]
                exp = [1, s.sympify(ang)]
            else:
                pol = [r,s.deg(s.sympify(ang))] #sympify para que lo convierta al s y no piense que solo es un string
                exp = [r, ang]

        case _:
            x = re.sub(r'\*I|\*i|i|I','i',x) #para que acepte cualquier forma rara, quita el i, solo quiero almacenar los valores.
 
            spl = list(re.split(r'(?<!^)(?=[+-])', x)) #(?=[+-]) para que no se coma el -

            if len(spl) == 1: #infierno de ifs
                if "i" in spl[0]:
                    spl[0] = re.sub(r'i','',spl[0])
                    if spl[0] == '':
                        b = 1
                    elif spl[0] == '-':
                        b = -1
                    else:
                        b = int(spl[0])
                    a = 0
                    r = b
                    if b < 0:
                        ang = s.sympify('3*pi/2')
                    else:
                        ang = s.sympify('pi/2')
                else:
                    a = int(spl[0])
                    b = 0
                    r = a
                    if a < 0:
                        ang = s.sympify('pi')
                    else:
                        ang = s.sympify('0')
            else:
                a = s.sympify(spl[0])
                if spl[1] == "+i": 
                    b = 1
                    ang = s.sympify("pi")
                elif spl[1] == "-i": 
                    b = -1
                    ang = s.sympify("3*pi/2")                    
                else:
                    spl[1] = re.sub(r'i', '', spl[1])
                    b = s.sympify(spl[1])
                r = s.sqrt(a**2+b**2)
                ang = s.N(s.atan2(b, a)) # s.atan2 maneja los cuadrantes bien, el s.atan normal no le sabe

            binom = [a,b]

            if r == 1:
                exp = [1, ang]
                pol = [1, s.deg(ang)]
            else:
                exp = [r, ang] 
                pol = [r, s.deg(ang)]
    return ([binom,exp,pol])