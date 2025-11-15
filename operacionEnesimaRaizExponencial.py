import ConversionesComplejas as CC #inporto concerciones complejas
import sympy as s # #importo sympy para las operaciones con simbolos

def sqrt_exponencial(z, n):
    formasz = CC.complejo(z)
    raices = []  # Lista para las raíces en formato exponencial
    
    mod = s.sympify(formasz[1][0]) 
    arg = s.sympify(formasz[1][1])  # Ya está en radianes
    n = int(n)
    
    modroot = s.root(mod, n)  # Raíz n-ésima del módulo
    
    for k in range(0, n):
        # Fórmula en RADIANES (no grados)
        ang_raiz = (arg + 2*s.pi*k) / n
        
        # Crear formato exponencial (sin convertir a int)
        exp_resultado = f"{modroot}e^({ang_raiz}i)"
        
        # Convertir a número complejo completo
        num_completo = CC.complejo(exp_resultado)
        raices.append(num_completo)
        
    return raices
