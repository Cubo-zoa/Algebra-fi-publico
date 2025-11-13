import ConversionesComplejas as CC #inporto concerciones complejas
import sympy as s # #importo sympy para las operaciones con simbolos

def multi_binomica(z, w): # Defino la funcion para la multiplicación
    formasz = CC.complejo(z) #ingreso los numeros complejos que se va a usar a un formato mas eficas
    formasw = CC.complejo(w)              
          
    #desgloso los numeros complejos en partes, para tener un mejor manejo e las operaciones 
    a = s.sympify(formasz[0][0]) #Tomo la variable a de los numeros complejos
    b = s.sympify(formasz[0][1]) #Tomo la variable b
    c = s.sympify(formasw[0][0]) #Tomo la variable c
    d = s.sympify(formasw[0][1]) #Tomo la variable d
    
    #hago la multiplicación
    parte_real = a*c - b*d # hago la operacion para la parte a
    parte_imag = a*d + b*c # hago la operacion para la parte b
    
    #muesto el numero complejo en las 3 formas
    binom_resultado = str(parte_real) + "+" + str(parte_imag) + "i" #Muestro el vinomio
    num_final = CC.complejo(binom_resultado)
    return num_final


#defino la funcion para la división
def div_binomica(z, w):
    formasz = CC.complejo(z) #ingreso los numeros complejos que se va a usar a un formato mas eficas
    formasw = CC.complejo(w)
    
    #desgloso los numeros complejos en partes, para tener un mejor manejo e las operaciones 
    a = s.sympify(formasz[0][0]) #variable a
    b = s.sympify(formasz[0][1]) #variable b 
    c = s.sympify(formasw[0][0]) #variable c
    d = s.sympify(formasw[0][1]) #variable d

    #hago que el denominador sea mas facil de utilizar
    denominador = c**2 + d**2 

    #hago las operaciones
    parte_real = (a*c + b*d) / denominador #hago la operacion para la parte real
    parte_imag = (b*c - a*d) / denominador #hago la operacion para la parte imaginaria

    #muetro el numero complejo en los 3 formatos 
    binom_resultado = str(parte_real) + "+" + str(parte_imag) + "i"
    num_final = CC.complejo(binom_resultado)
    return num_final

#hago que el usuario elija entre multiplicación o division
if __name__ == "__main__": #hago que el archivo se ejecute desde la termina
    z = input("Ingresa el primer número complejo z: ") #le pido al usuario que ingrese z
    w = input("Ingresa el segundo número complejo w: ") #le pido al usuario que ingrese w
    operacion = input("¿Multiplicación (m) o División (d)?: ") #hago que el usuario decida la operacion
    
    #hago que deendiendo la desición haga una u otra operación 
    if operacion == "m":  
        resultado = multi_binomica(z, w) #el resultado sera el de la multiplicacion
    else:
        resultado = div_binomica(z, w) #el resultado sera el de la division
        
    print("Resultado:", resultado) #muestra el resultado
