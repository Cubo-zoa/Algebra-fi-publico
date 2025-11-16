# Importamos la libreria sympy como 's'
import sympy as s

# ---
# Convierte la entrada de string a coordenadas polares.
# Devuelve: (modulo, argumento_en_grados)
# ---
def get_polar(z_str):
    # Prepara el string para sympy (requiere '*I' en lugar de 'i' o 'j')
    if 'j' in z_str:
        z_str = z_str.replace('j', '*I')
    # Este 'if' evita reemplazar 'i' en palabras como 'cis'
    if 'i' in z_str and 'cis' not in z_str:
        z_str = z_str.replace('i', '*I')
    
    # 1. Convertir el string a un objeto matematico de sympy
    num_obj = s.sympify(z_str)
    
    # 2. Sacar el modulo (r)
    # s.N() es para que nos de el numero decimal (ej. 5.0)
    mod = s.N(s.Abs(num_obj))
    
    # 3. Sacar el argumento (theta) en radianes
    arg_rad = s.arg(num_obj)
    
    # 4. Convertir a grados
    arg_grados = s.N(s.deg(arg_rad))
    
    # Devolvemos los dos valores listos para usar
    return (float(mod), float(arg_grados))


# ---
# Multiplicacion (z * w)
# ---
def multi(z, w):
    # 'formasz' y 'formasw' (modulo, argumento)
    formasz = get_polar(z)
    formasw = get_polar(w)
    
    # Regla: (r1 * r2)
    mod = formasz[0] * formasw[0]
    # Regla: (theta1 + theta2)
    arg = formasz[1] + formasw[1]
    
    # Bucle para normalizar el angulo
    while arg > 360:
        arg -= 360
    while arg < 0:
        arg += 360
    
    # Formateamos la respuesta como un STRING en forma exponencial
    resultado_str = f"{mod:.4f} * e^(i * {arg:.2f}°)"
    return resultado_str

# ---
# Division (z / w)
# ---
def div(z, w):
    # Sacamos los datos polares
    formasz = get_polar(z)
    formasw = get_polar(w)
    
    # Regla: (r1 / r2)
    mod = formasz[0] / formasw[0]
    # Regla: (theta1 - theta2)
    arg = formasz[1] - formasw[1]
    
    # Normalizamos el angulo
    while arg > 360:
        arg -= 360
    while arg < 0:
        arg += 360
    
    # Creamos el string de resultado
    resultado_str = f"{mod:.4f} * e^(i * {arg:.2f}°)"
    return resultado_str

# ---
# Potencia (z^n)
# ---
def pot(z, n_str):
    # Sacamos los datos polares
    formasz = get_polar(z)
    # Convertimos la potencia 'n' a un numero
    n = float(n_str) 
    
    # Regla: (r1^n)
    mod = formasz[0]**n
    # Regla: (theta1 * n)
    arg = formasz[1] * n
    
    # Normalizamos el angulo
    while arg > 360:
        arg -= 360
    while arg < 0:
        arg += 360
    
    # Creamos el string de resultado
    resultado_str = f"{mod:.4f} * e^(i * {arg:.2f}°)"
    return resultado_str

# ---
# Raiz n-esima (z^(1/n))
# ---
def raiz_n(z, n_str):
    formasz = get_polar(z)
    mod_z = formasz[0]
    arg_z = formasz[1] # Este ya esta en GRADOS
    n = int(n_str)     # La raiz debe ser un numero entero
    
    # 1. Calcular el nuevo modulo (es el mismo para todas las raices)
    mod_raiz = mod_z**(1/n) # r^(1/n)
    
    lista_raices = [] # Lista para guardar los strings
    
    # 2. Bucle 'k' de 0 a n-1 para encontrar todos los angulos
    for k in range(n):
        # Formula de Moivre para raices (version en grados)
        # (angulo_original + 360 * k) / n
        arg_nuevo = (arg_z + 360 * k) / n
        
        # Formateamos el string para esta raiz
        resultado_str = f"{mod_raiz:.4f} * e^(i * {arg_nuevo:.2f}°)"
        
        # Lo anadimos a la lista
        lista_raices.append(resultado_str)
        
    # Devolvemos la lista completa
    return lista_raices

# ---
# Parte principal para probar el codigo
# ---
if __name__ == "__main__":
    
    print("--- Calculadora Exponencial ---")
    
    # Pedimos los numeros al usuario
    z1 = input("Ingresa el primer numero (ej. 3+4i o 2-5j): ")
    z2 = input("Ingresa el segundo numero (ej. 1+1i): ")
    n = input("Ingresa la potencia/raiz (ej. 3): ") 

    print("\n--- Resultados ---")
    
    # Probamos la multiplicacion
    res_multi = multi(z1, z2)
    print(f"Multiplicacion (z1 * z2): {res_multi}")
    
    # Probamos la division
    res_div = div(z1, z2)
    print(f"Division (z1 / z2):     {res_div}")
    
    # Probamos la potencia
    res_pot = pot(z1, n)
    print(f"Potencia (z1^{n}):       {res_pot}")

    # Probar la raiz n-esima
    print(f"\nRaices {n} de z1:")
    lista_de_raices = raiz_n(z1, n)
    
    # Imprimimos cada raiz de la lista
    for raiz_individual in lista_de_raices:
        print(f"  {raiz_individual}")