import matplotlib.pyplot as mat
import operaciones as op
import ConversionesComplejas as CC
import sympy as s

z = input("z")
w = input("w")
elec = input ("Que operacion deseas hacer?: ")

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

def plot1 (res):
        easy1 = float(s.N(s.sympify(res[0][0])))
        easy2 = float(s.N(s.sympify(res[0][1])))
        print(easy1,easy2)
        x = normalizer(res)
        y = str(x[0])
        fig, ax = mat.subplots()
        ax.plot()
        ax.axis((-(abs(easy1))-2,abs(easy1)+2,-(abs(easy2))-2,abs(easy2)+2))
        ax.grid()
        ax.axhline(y = 0, color = 'k')
        ax.axvline(x = 0, color = 'k')
        ax.annotate('',xy=(easy1,easy2),xytext=(0,0), arrowprops=dict(arrowstyle='->', color='red',lw=1.5))
        ax.annotate(y, xy=(easy1,easy2), xytext=(easy1,easy2))
        mat.show()

def plotsqrt (res):
        fig, ax = mat.subplots()
        ax.plot()
        ax.grid()
        ax.axhline(y = 0, color = 'k')
        ax.axvline(x = 0, color = 'k')
        ax.axis((-10,10,-10,10))
        for i in range(len(res)):
            easy1 = round(s.N(s.sympify(res[i][0])))
            easy2 = round(s.N(s.sympify(res[i][1])))
            easy3 = CC.complejo(str(easy1) + "cis" + str(easy2))
            a = s.sympify(easy3[0][0])
            b = s.sympify(easy3[0][1])
            ax.annotate('',xy=(a,b),xytext=(0,0), arrowprops=dict(arrowstyle='->', color='red',lw=1.5))
            match b:
                case _ if b == 0:
                    y= str(a)
                case _ if b < 0:
                    y= str(a) + str(b) + 'i'
                case _ if b > 1:
                    y= str(a) + '+' + str(b) + 'i'
                case _ if b == 1:
                    y= str(a) + '+ i'
            if a == 0:
                y = str(b) + 'i'
            ax.annotate(y, xy=(a,b), xytext=(a,b))  
        mat.show()          

match True: #este menu regresa la operacion deseada junto a la grafica respectiva.
    case _ if "mult" in elec:
        x = op.multi(z,w)
        plot1(x)
    case _ if "div" in elec:
        x = op.div(z,w)
        plot1(x)
    case _ if "suma" in elec:
        x = op.add(z,w)
        plot1(x)
    case _ if "resta" in elec:
        x = op.sub(z,w)
        plot1(x)
    case _ if "conj" in elec:
        x = op.conj(z)
        plot1(x)
    case _ if "raiz" in elec:
        x = op.sqrt(z)
        plotsqrt(x)
    case _ if "potencia" in elec:
        x = op.pot(z)
        plot1(x)



