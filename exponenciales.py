# Importamos la libreria sympy como 's'
import sympy as s

# ---
# Esta es nuestra funcion "ayudante".
# Reemplaza a tu "ConversionesComplejas" (CC).
# Toma un string (ej. "3+4i") y devuelve (modulo, argumento_en_grados)
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
    
    # 4. Convertir a grados, como en tu ejemplo
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
    
    # Bucle para normalizar el angulo (igual al tuyo)
    while arg > 360:
        arg -= 360
    while arg < 0:
        arg += 360
    
    # Formateamos la respuesta como un STRING en forma exponencial
    # r * e^(i * theta°)
    # El :.4f significa "formatear con 4 decimales"
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
    
    # Normalizamos el angulo (este bucle es mas eficiente)
    while arg > 360:
        arg -= 360
    while arg < 0:
        arg += 360
    
    # Creamos el string de resultado
    resultado_str = f"{mod:.4f} * e^(i * {arg:.2f}°)"
    return resultado_str

# ---
# Parte principal para probar el codigo
# El if __name__ == "__main__": es estandar en Python 
# para que el codigo solo se ejecute si corres este archivo
# ---
if __name__ == "__main__":
    
    print("--- Calculadora Exponencial (Estilo Humano) ---")
    
    # Pedimos los numeros al usuario
    z1 = input("Ingresa el primer numero (ej. 3+4i o 2-5j): ")
    z2 = input("Ingresa el segundo numero (ej. 1+1i): ")
    n = input("Ingresa la potencia (ej. 3): ")

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