import tkinter as tk
import matplotlib.pyplot as mat
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ConversionesComplejas as CC
import operaciones as op
import sympy as s

calc = tk.Tk()
calc.geometry("1300x630")

calc.title("Calculadora de numeros complejos")

#Declaramos frames para agrupar

grafic = tk.Frame(calc)
buttons = tk.Frame(calc)
ncomp = tk.Frame(calc)
result = tk.Frame(calc)
notas = tk.Frame(calc)

#Funciones para graficar

def normalizer(re):
    a = re[0][0]
    b = re[0][1]
    match b:
        case _ if b == 0:
            binom= str(a)
        case _ if b < 0:
            binom= str(a) + str(b) + 'i'
        case _ if b > 1:
            binom= str(a) + '+' + str(b) + 'i'
        case _ if b == 1:
            binom= str(a) + '+ i'
    if a == 0:
        binom= str(b) + 'i'
    
    if re[1][0] == 1:
        exp = 'e^' + str(s.rad(s.N(re[1][1]))) + 'i'
        pol = 'cis' + str(round(s.N(re[2][1])))
    else:
        exp= str(re[1][0]) + 'e^' + str(s.rad(s.N(re[1][1])))  + 'i'
        pol = str(re[2][0]) + 'cis' + str(round(s.N(re[2][1])))
    return binom, exp, pol

#Funcion para imprimir el complejo resultante
def resultante(binom,exp,pol): 
    comrb.config(state= "normal")
    comrp.config(state= "normal")
    comre.config(state= "normal")
    comrb.delete(0, tk.END)
    comrp.delete(0, tk.END)
    comre.delete(0, tk.END)
    comrb.insert(0, binom)
    comrp.insert(0, pol)
    comre.insert(0, exp)
    comrb.config(state= "readonly")
    comrp.config(state= "readonly")
    comre.config(state= "readonly")

def resultantesqrt(pol):
    comrp.config(state= "normal")
    comrp.delete(0, tk.END)
    comrp.insert(0, pol)
    comrp.config(state= "readonly")

def plot1 (res):
        global fig
        global canvas
        global ax
        easy1 = float(s.N(s.sympify(res[0][0])))
        easy2 = float(s.N(s.sympify(res[0][1])))
        print(easy1,easy2)
        x = normalizer(res)
        y = str(x[0])
        ax.clear()
        fig, ax = mat.subplots()
        ax.plot()
        ax.set_title("Plano de Argand")
        ax.set_xlabel("Eje \u211D")
        ax.set_ylabel("Eje i")
        ax.axis((-(abs(easy1))-2,abs(easy1)+2,-(abs(easy2))-2,abs(easy2)+2))
        ax.grid()
        ax.axhline(y = 0, color = 'k')
        ax.axvline(x = 0, color = 'k')
        ax.annotate('',xy=(easy1,easy2),xytext=(0,0), arrowprops=dict(arrowstyle='->', color='red',lw=1.5))
        ax.annotate(y, xy=(easy1,easy2), xytext=(easy1,easy2))
        canvas = FigureCanvasTkAgg(fig, master = grafic)
        canvas.draw()
        canvas.get_tk_widget().pack(side = "right", padx = 40)

        return easy1, easy2

def plotsqrt (res):
        global fig
        global canvas
        global ax
        ax.clear()
        fig, ax = mat.subplots()
        ax.plot()
        ax.grid()
        ax.axhline(y = 0, color = 'k')
        ax.axvline(x = 0, color = 'k')
        ax.axis((-10,10,-10,10))
        ax.set_title("Plano de Argand")
        ax.set_xlabel("Eje \u211D")
        ax.set_ylabel("Eje i")
        for i in range(len(res)):
            easy1 = round(s.N(s.sympify(res[i][0])))
            easy2 = round(s.N(s.sympify(res[i][1])))
            easy3 = CC.complejo(str(easy1) + "cis" + str(easy2))
            a = s.sympify(easy3[0][0])
            b = s.sympify(easy3[0][1])
            ax.annotate('',xy=(a,b),xytext=(0,0), arrowprops=dict(arrowstyle='->', color='red',lw=1.5))  
        canvas = FigureCanvasTkAgg(fig, master = grafic)
        canvas.draw()
        canvas.get_tk_widget().pack(side = "right", padx = 40)

#Contadores que se usan para escribir en los cuadros de texto
j = 0
k = 0
m = 0
cont = 0

n = 0

#Desabilitan los botones si no se van a usar
bnum = []
bonlyop = []
bgeneralop = []

#Grafica Inicial
fig = mat.figure(figsize=(5, 4))
ax = fig.add_subplot(111)
ax.set_title("Plano de Argand")
ax.set_xlabel("Eje \u211D")
ax.set_ylabel("Eje i")
ax.axhline(y = 0, color = 'k')
ax.axvline(x = 0, color = 'k')
#Fija los límites del plano
ax.set_xlim(-5, 5) 
ax.set_ylim(-5, 5)
ax.grid(True)
#Indica donde va a ir la grafica y la dibuja
canvas = FigureCanvasTkAgg(fig, master = grafic)
canvas.draw()

#Funciones predefinidas para operar

#Desabilita los numeros si se esta introduciendo algun operador
def actualizar():
    if cont == 0: 
        for boton in bnum:
            boton.config(state='disabled')
    if cont != 0:
        for boton in bnum:
            boton.config(state='normal')

#Desabilita todos los operadoes cuando se va a introducir potencia/raiz
def actallop():
    if cont == 1:
        for boton in bgeneralop:
            boton.config(state = 'disabled')
    if cont != 1:
        for boton in bgeneralop:
            boton.config(state = 'normal')

#Desabilita operadores que no se pueden usar dentro de un numero
def actop():
    if cont == 0:
        if cont == 0: 
            for boton in bonlyop:
                boton.config(state='normal')
    if cont != 0:
        for boton in bonlyop:
            boton.config(state='disabled')


#Funcion para moverse entre cuadros de texto
def enter():
    global cont
    if cont > 0: cont += 1
    if cont == 0:
        elec = comop.get()
        if elec == "z":
            com2.config(state = 'disabled')
            com1.grid(row = 1, column = 1, columnspan = 2)
            com2.grid(row = 2, column = 1, columnspan = 2)
        if elec == "√" or elec == "^":
            cont += 1
            com2.config(state = 'disabled')
            etiquetapr.grid(row =0, column = 5, columnspan=2)
            pr.grid(row = 1,column = 5, columnspan = 2, rowspan = 2)
        else: cont += 2
    actualizar()
    actop()
    actallop()
    if cont > 3 and c2 == 'normal' : cont = 3
    if cont > 2 and c2 == 'disabled' : cont = 2

#Funcion para introducir datos
def click_boton(valor):
    global j
    global k
    global m
    global cont
    if cont == 0:
        comop.insert(0, valor)
    if cont == 1:
        pr.insert(m, valor)
        m += 1
    if cont == 2:
        com1.insert(j, valor)
        j += 1
    if cont == 3:
        com2.insert(k, valor)
        k += 1

#Introducir e^
def click_boton2(valor):
    global j
    global k
    global cont
    if cont == 2:
        com1.insert(j, valor)
        j += 2
    if cont == 3:
        com2.insert(k, valor)
        k += 2

#Introducir cis
def click_boton3(valor):
    global j
    global k
    global cont
    if cont == 2:
        com1.insert(j, valor)
        j += 3
    if cont == 3:
        com2.insert(k, valor)
        k += 3

#Funcion para que el operador solo sea 1 caracter
def caracter(valor):
    if len(valor) <=1:
        return 1
    else: return 0

v1c = (calc.register(caracter), '%P')

#Borrar todo lo escrito en un cuadro de texto
def borrar():
    global j
    global k
    global m
    global cont
    if cont == 0:
        comop.delete(0, tk.END)
    if cont == 1:
        pr.delete(0, tk.END)
        m = 0
    if cont == 2:
        com1.delete(0, tk.END)
        j = 0
    if cont == 3:
        com2.delete(0, tk.END)
        k = 0

#Borrar el ultimo valor escrito
def mfinal():
    global j
    global k
    global m
    global cont
    if cont == 0:
        comop.delete(0)
    if cont == 1:
        pr.delete(m-1)
        m -= 1
        if m < 0:
            m = 0
    if cont == 2:
        com1.delete(j-1)
        j -= 1
        if j < 0:
            j = 0
    if cont == 3:
        com2.delete(k-1)
        k -=1
        if k < 0:
            k = 0

#Operar nuestros numeros
def operar():
    global j
    global k
    global m
    global cont
    global n
    z = com1.get()
    w = com2.get()
    elec = comop.get()
    if pr.winfo_ismapped():
        n = pr.get()
    j = 0
    k = 0
    m = 0
    cont = 0
    canvas.get_tk_widget().pack_forget()
    match True: #este menu regresa la operacion deseada junto a la grafica respectiva.
        case _ if "*" in elec:
            x = op.multi(z,w)
            plot1(x)
            binom, exp, pol = normalizer(x)
            resultante(binom, exp, pol)
        case _ if "/" in elec:
            x = op.div(z,w)
            plot1(x)
            binom, exp, pol = normalizer(x)
            resultante(binom, exp, pol)
        case _ if "+" in elec:
            x = op.add(z,w)
            plot1(x)
            binom, exp, pol = normalizer(x)
            resultante(binom, exp, pol)
        case _ if "-" in elec:
            x = op.sub(z,w)
            plot1(x)
            binom, exp, pol = normalizer(x)
            resultante(binom, exp, pol)
        case _ if "z" in elec:
            x = op.conj(z)
            plot1(x)
            binom, exp, pol = normalizer(x)
            resultante(binom, exp, pol)
        case _ if "√" in elec:
            x = op.sqrt(z,n)
            plotsqrt(x)
            pol = normalizer(x)
            resultantesqrt(pol)
        case _ if "^" in elec:
            x = op.pot(z,n)
            plot1(x)
            binom, exp, pol = normalizer(x)
            resultante(binom, exp, pol)

#Pasar el resultado como primer numero complejo a operar
def ans():
    global j
    global k
    global m
    if comrp != "":
        z = comrp.get()
        com1.delete(0, tk.END)
        com1.insert(0, z)
        com2.delete(0, tk.END)
        j = len(com1)
        k = 0
        m = 0

#Borrar de todos los cuadros de texto
def reset():
    global j
    global k
    global m
    global cont
    com1.delete(0, tk.END)
    com2.delete(0, tk.END)
    comop.delete(0, tk.END)
    pr.delete(0, tk.END)
    j = 0
    k = 0
    cont = 0
    pr.grid_forget()
    etiquetapr.grid_forget()
    com2.config(state = "normal")
    comrb.config(state = "normal")
    comrb.delete(0, tk.END)
    comrb.config(state = "readonly")
    comrp.config(state = "normal")
    comrp.delete(0, tk.END)
    comrp.config(state = "readonly")
    comre.config(state = "normal")
    comre.delete(0, tk.END)
    comre.config(state = "readonly")
    actualizar()
    actop()
    actallop()

def _on_closing():
    global plot1
    """
    Función personalizada para el cierre.
    """
    print("Cerrando la aplicación...")
    
    # 1. Cierra todas las figuras de Matplotlib (¡Importante!)
    mat.close('all')
    
    # 2. Destruye tu ventana principal 'calc'
    calc.destroy()

#Aqui empieza la interfaz

#Declaracionde botones, etiquetas y cuadros de texto
#En grafic va la grafica, buttons para operadores, ncomp para los numeros complejos y result para resultados

grafic.grid(row = 0, column= 1, rowspan = 3)
buttons.grid(row = 1, column = 0)
ncomp.grid(row = 0, column = 0)
result.grid(row = 2, column= 0)
notas.grid(row = 3 ,column = 1)

#Etiquetas para los numeros complejos a operar
etiquetan1=tk.Label(ncomp, text = "Complejo1")
etiquetan2=tk.Label(ncomp, text = "Complejo2")

#Etiqueta y cuadro para el operador asi como la potencia o raiz
etiquetaopc = tk.Label(ncomp, text = "Operador")
comop = tk.Entry(ncomp, width = 2, validate = 'key', validatecommand = v1c, font = "Helvetica 15")
etiquetapr = tk.Label(ncomp, text = "Potencia o Raiz" )
pr = tk.Entry(ncomp, width = 2, font = "Helvetica 15")

#Cuadros de texto para intoducir numeros complejos
com1 = tk.Entry(ncomp, font = "Helvetica 15")
com2 = tk.Entry(ncomp, font = "Helvetica 15")
c2 = com2.cget('state')

#Etiquetas para operar con los botones
etiquetanum=tk.Label(buttons, text = "Numeros")
etiquetasimb = tk.Label(buttons, text = "Simbolos")
etiquetaop=tk.Label(buttons, text = "Operadores")

#Botones para numeros (0 al 9, i, π)
b1 = tk.Button(buttons, text = "1", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(1))
b2 = tk.Button(buttons, text = "2", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(2))
b3 = tk.Button(buttons, text = "3", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(3))
b4 = tk.Button(buttons, text = "4", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(4))
b5 = tk.Button(buttons, text = "5", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(5))
b6 = tk.Button(buttons, text = "6", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(6))
b7 = tk.Button(buttons, text = "7", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(7))
b8 = tk.Button(buttons, text = "8", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(8))
b9 = tk.Button(buttons, text = "9", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(9))
b0 = tk.Button(buttons, text = "0", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton(0))
bi = tk.Button(buttons, text = "i", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton("i"))
bπ = tk.Button(buttons, text = "π", width = 10, heigh = 4, bg = "light blue", activebackground= "dark blue", command = lambda: click_boton("π"))

#Agregamos todos los botones de numeros una lista

bnum.append(b1)
bnum.append(b2)
bnum.append(b3)
bnum.append(b4)
bnum.append(b5)
bnum.append(b6)
bnum.append(b7)
bnum.append(b8)
bnum.append(b9)
bnum.append(b0)
bnum.append(bi)
bnum.append(bπ)

#Botones para operaciones (Todos los operadores)
bmulti = tk.Button(buttons, text = "x", width = 10, height = 4, bg = '#CCCCCC', activebackground = '#696969', command = lambda: click_boton("*"))
bdiv = tk.Button(buttons, text = "÷", width = 10, height = 4, bg = '#CCCCCC', activebackground = '#696969', command = lambda: click_boton("/"))
badd = tk.Button(buttons, text = "+", width = 10, height = 4, bg = '#CCCCCC', activebackground = '#696969', command = lambda: click_boton("+"))
bsub = tk.Button(buttons, text = "-", width = 10, height = 4, bg = '#CCCCCC', activebackground = '#696969', command = lambda: click_boton("-"))
bexp = tk.Button(buttons, text = "a\u207F", width = 10, height = 4, bg = '#CCCCCC', activebackground = '#696969',command = lambda: click_boton("^"))
bsqrt = tk.Button(buttons, text = "√", width = 10, height = 4, bg = '#CCCCCC', activebackground = '#696969', command = lambda: click_boton("√"))
bconj = tk.Button(buttons, text = "z\u0305", width = 10, height = 4, bg = '#CCCCCC', activebackground = '#696969', command = lambda: click_boton("z"))

#Agregamos a esta lista operadores que solo sirven en la casilla operador
bonlyop.append(bexp)
bonlyop.append(bconj)

#Agregamos a otra lista los demas operadores
bgeneralop.append(bmulti)
bgeneralop.append(bdiv)
bgeneralop.append(badd)
bgeneralop.append(bsub)
bgeneralop.append(bsqrt)

#Botones para borrar
bnull = tk.Button(buttons, text = "AC", width= 10, height = 4 , bg = '#FFDAB9', activebackground = "#FFA500", command = lambda: borrar())
bdel = tk.Button(buttons,text = "DEL", width= 10, height = 4 , bg = '#FFDAB9', activebackground = "#FFA500", command = lambda: mfinal())
breset = tk.Button(buttons,text = "RESET", width= 10, height = 4 , bg = '#FFA07A', activebackground = "red", command = lambda: reset())

#Botones de otros simboloes
bdot = tk.Button(buttons, text = "•", width= 10, height = 4, bg = '#F8C8DC', activebackground = "pink", command = lambda: click_boton(".") )
bresult = tk.Button(buttons, text = "=", width=10, height = 4 , bg = '#C1FFC1', activebackground = "green", command = lambda: operar())
bans = tk.Button(buttons, text = "ANS", width = 10, height = 4, bg = '#C1FFC1', activebackground = "green", command = lambda: ans())
benter = tk.Button(buttons, text = '\u21B5', width = 10, height = 4, bg = '#CCCCCC', activebackground = '#696969', command = lambda: enter())
bnum.append(bdot)

#Boton para cis y e^
bcis = tk.Button(buttons, text = "cis",width = 10, height=4, bg = '#EEE8AA', activebackground = "gold", command = lambda: click_boton3("cis"))
be = tk.Button(buttons, text = "e^", width = 10, height=4, bg = '#EEE8AA', activebackground = "gold", command = lambda: click_boton2("e^"))
bnum.append(bcis)
bnum.append(be)


#Resultado
etiquetan3 = tk.Label(result, text = "Complejo Resultante")
etiquetafb = tk.Label(result, text = "Forma Binomica")
etiquetafp = tk.Label(result, text = "Forma Polar")
etiquetafe = tk.Label(result, text = "Forma Polar")
comrb = tk.Entry(result, state = "readonly", font = "Helvetica 15", bg = "white")
comrp = tk.Entry(result, state = "readonly", font = "Helvetica 15", bg = "white")
comre = tk.Entry(result, state = "readonly", font = "Helvetica 15", bg = "white")

#Notas para operar en la calculadora
etiquetanotas = tk.Label(notas, text = "Consejos de uso")
etiqueta1 = tk.Label(notas, text = "•Debes colocar los numeros sin separaciones")
etiqueta2 = tk.Label(notas, text = "•Despues de cis y de e no introducir parentesis")
etiqueta3 = tk.Label(notas, text = "•Para colocar en forma exponencial 3π/2i colocar 3*π/2i")
etiquetares = tk.Label(notas, text = "•Para operar oprima el boton de =")

#Desde aqui empiezan posiciones para todos los widgets

actualizar()

#Posicion para boton cis y e
bcis.grid(row = 2, column = 3,)
be.grid(row = 3, column = 3,)

#Posicion para numeros complejos (Cajas de texto para los numeros)
etiquetan1.grid(row = 1, column = 0)
etiquetan2.grid(row = 2, column = 0)
com1.grid(row = 1, column = 1, columnspan = 2)
com2.grid(row = 2, column = 1, columnspan = 2)

#Posicion para el operador (Operacion a realizar y potencia o raiz)
etiquetaopc.grid(row = 0, column = 3)
comop.grid(row = 1, column = 3, rowspan = 2)
etiquetapr.grid(row =0, column = 5, columnspan=2)
pr.grid(row = 1,column = 5, columnspan = 2, rowspan = 2)
pr.grid_forget()
etiquetapr.grid_forget()

#Posiciones etiquetas para operar (Palabras arriba de los botones)
etiquetanum.grid(row = 0, column = 0, columnspan = 3)
etiquetasimb.grid(row = 0, column = 3, columnspan = 2)
etiquetaop.grid(row =  0, column = 5, columnspan = 2)

#Posicion para botones de numeros del 0 al 9, tambien i, π
b7.grid(row = 1, column = 0, sticky = 'we', padx=2, pady=2)
b8.grid(row = 1, column = 1, sticky = 'we', padx=2, pady=2)
b9.grid(row = 1, column = 2, sticky = 'we', padx=2, pady=2)
b4.grid(row = 2, column = 0, sticky = 'we', padx=2, pady=2)
b5.grid(row = 2, column = 1, sticky = 'we', padx=2, pady=2)
b6.grid(row = 2, column = 2, sticky = 'we', padx=2, pady=2)
b1.grid(row = 3, column = 0, sticky = 'we', padx=2, pady=2)
b2.grid(row = 3, column = 1, sticky = 'we', padx=2, pady=2)
b3.grid(row = 3, column = 2, sticky = 'we', padx=2, pady=2)
b0.grid(row = 4, column = 0, sticky = 'we', padx=2, pady=2)
bi.grid(row = 4, column = 2, sticky = 'we', padx=2, pady=2)
bπ.grid(row = 4, column = 1, sticky = 'we', padx=2, pady=2)

#Posicion para botones de eliminar
bnull.grid(row = 1, column = 3, sticky = 'we', padx=2, pady=2)
bdel.grid(row = 1, column = 4, sticky = 'we', padx=2, pady=2)
breset.grid(row = 2, column = 4, sticky = 'we', padx=2, pady=2)

#Posicion para operadores (Botones de operador)
bmulti.grid(row = 1, column = 6, padx=2, pady=2) 
bdiv.grid(row = 2, column = 6, padx=2, pady=2)
badd.grid(row = 1, column = 5, padx=2, pady=2)
bsub.grid(row = 2, column = 5, padx=2, pady=2)
bexp.grid(row = 3, column = 5, padx=2, pady=2)
bsqrt.grid(row = 3, column = 6, padx=2, pady=2)
bconj.grid(row = 4, column = 5, padx=2, pady=2)

#Posicion otros simbolos
bdot.grid(row = 4, column = 3, sticky = 'we', padx=2, pady=2)
bresult.grid(row = 3, column = 4, sticky = 'we', padx=2, pady=2)
bans.grid(row = 4, column = 4, sticky= 'we', padx=2, pady=2)
benter.grid(row = 4, column = 6, sticky= 'we', padx=2, pady=2)

#Posicion para el complejo resultante
canvas.get_tk_widget().pack(side = "right", padx = 40)
etiquetan3.grid(row = 0, column = 1, columnspan = 2, pady = 10, sticky = 'w')
etiquetafb.grid(row = 1, column = 0, columnspan = 2)
etiquetafp.grid(row = 2, column = 0, columnspan = 2)
etiquetafe.grid(row = 3, column = 0, columnspan = 2)
comrb.grid(row = 1, column = 2, padx = 20, columnspan = 4, sticky= 'w')
comrp.grid(row = 2, column = 2, padx = 20, columnspan = 4, sticky = 'w')
comre.grid(row = 3, column = 2, padx = 20, columnspan = 4, sticky = 'w')

#Posicion para notas de operacion

etiquetanotas.grid(row = 0, column = 0)
etiqueta1.grid(row = 1, column = 0)
etiqueta2.grid(row = 2, column = 0)
etiqueta3.grid(row = 3, column = 0)
etiquetares.grid(row = 4, column = 0)

#Cierra la grafica para que no quede en segundo plano

calc.protocol("WM_DELETE_WINDOW", _on_closing)

calc.mainloop()