# ---
# Multiplicacion (z * w)
# ---
def multi(mod_z, arg_z, mod_w, arg_w):
    mod = mod_z * mod_w # Regla: (r1 * r2)
    arg = arg_z + arg_w # Regla: (theta1 + theta2)
    
    # Normalizar el angulo
    while arg > 360:
        arg -= 360
    while arg < 0:
        arg += 360
    
    resultado_str = f"{mod:.4f} * e^(i * {arg:.2f}°)"
    return resultado_str

# ---
# Division (z / w)
# ---
def div(mod_z, arg_z, mod_w, arg_w):
    mod = mod_z / mod_w # Regla: (r1 / r2)
    arg = arg_z - arg_w # Regla: (theta1 - theta2)
    
    # Normalizar el angulo
    while arg > 360:
        arg -= 360
    while arg < 0:
        arg += 360
    
    resultado_str = f"{mod:.4f} * e^(i * {arg:.2f}°)"
    return resultado_str

# ---
# Potencia (z^n)
# ---
def pot(mod_z, arg_z, n_str):
    n = float(n_str) 
    
    mod = mod_z**n # Regla: (r1^n)
    arg = arg_z * n  # Regla: (theta1 * n)
    
    # Normalizar el angulo
    while arg > 360:
        arg -= 360
    while arg < 0:
        arg += 360
    
    resultado_str = f"{mod:.4f} * e^(i * {arg:.2f}°)"
    return resultado_str

# ---
# Raiz n-esima (z^(1/n))
# ---
def raiz_n(mod_z, arg_z, n_str):
    n = int(n_str)     
    
    mod_raiz = mod_z**(1/n) # r^(1/n)
    
    lista_raices = [] 
    
    # Bucle de 0 a n-1
    for k in range(n):
        # Formula de Moivre (en grados)
        arg_nuevo = (arg_z + 360 * k) / n
        
        resultado_str = f"{mod_raiz:.4f} * e^(i * {arg_nuevo:.2f}°)"
        
        lista_raices.append(resultado_str)
        
    return lista_raices

# ---
# Parte principal para probar
# ---
if __name__ == "__main__":
    
    print("--- Calculadora Exponencial (Sin Librerias) ---")
    
    # Pedimos los datos polares de z1
    print("\n--- Datos del Primer Numero (z1) ---")
    # float() es una funcion predefinida basica para convertir texto a numero
    r1 = float(input("Ingresa el modulo (r) de z1: "))
    t1 = float(input("Ingresa el argumento (angulo en grados) de z1: "))
    
    # Pedimos los datos polares de z2
    print("\n--- Datos del Segundo Numero (z2) ---")
    r2 = float(input("Ingresa el modulo (r) de z2: "))
    t2 = float(input("Ingresa el argumento (angulo en grados) de z2: "))
    
    print("\n--- Potencia/Raiz ---")
    n = input("Ingresa la potencia/raiz (ej. 3): ") 

    print("\n--- Resultados ---")
    
    # Probamos la multiplicacion
    res_multi = multi(r1, t1, r2, t2)
    print(f"Multiplicacion (z1 * z2): {res_multi}")
    
    # Probamos la division
    res_div = div(r1, t1, r2, t2)
    print(f"Division (z1 / z2):     {res_div}")
    
    # Probamos la potencia
    res_pot = pot(r1, t1, n)
    print(f"Potencia (z1^{n}):       {res_pot}")

    # Probamos la raiz
    print(f"\nRaices {n} de z1:")
    lista_de_raices = raiz_n(r1, t1, n)
    
    # Imprimimos cada raiz
    for raiz_individual in lista_de_raices:
        print(f"  {raiz_individual}")