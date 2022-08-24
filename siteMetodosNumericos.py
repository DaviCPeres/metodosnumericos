import streamlit as st
import pandas as pd
import math

def bissecao(a,b,erro,funcao,iteracoes = 0):
    continuar = True
    iteracao = 0
    
    if funcao(a)*funcao(b) >= 0:
        return "Sem raizes no intervalo"
        
    
    else:
        x = (a+b)/2
        
        As = [a]
        Bs = [b]
        Xs = [x]
        Varx = [0]
        
        while continuar:
            iteracao += 1
            
            if funcao(a)*funcao(x) < 0:
                b = x
            else:
                a = x
                
            x = (a+b)/2
            
            As.append(a)
            Bs.append(b)
            Xs.append(x)
            Varx.append(abs((Xs[-1]-Xs[-2])/Xs[-1]))
            
            if iteracoes == 0 and Varx[-1] <= erro:
                continuar = False
                
            elif iteracoes != 0 and iteracao >= iteracoes:
                continuar = False
    
        Data = {"A":As, "B":Bs, "X": Xs, "VARIAÇÃO DE X":Varx}
        df = pd.DataFrame(Data)
        return df

def falsaposicao(a, b, erro, funcao, iteracoes=0):
    continuar = True
    iteracao = 0

    if funcao(a) * funcao(b) >= 0:
        print("Sem raizes no intervalo")
        return

    else:
        x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))

        As = [a]
        Bs = [b]
        Xs = [x]
        Varx = [0]

        while continuar:
            iteracao += 1

            if funcao(a) * funcao(x) < 0:
                b = x
            else:
                a = x

            x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))

            As.append(a)
            Bs.append(b)
            Xs.append(x)
            Varx.append(abs((Xs[-1] - Xs[-2]) / Xs[-1]))

            if iteracoes == 0 and Varx[-1] <= erro:
                continuar = False

            elif iteracoes > 0 and iteracao >= iteracoes:
                continuar = False

        Data = {"A": As, "B": Bs, "X": Xs, "VARIAÇÃO DE X": Varx}
        df = pd.DataFrame(Data)
        return df

def pontofixo(x, erro, f, iteracoes=0):
    iteracao = 0
    Xs = [x]
    Varx = [0]

    continuar = True

    while continuar:
        iteracao += 1
        x = f(x)
        Xs.append(x)
        variacao = (Xs[-1] - Xs[-2]) / Xs[-1]
        Varx.append(variacao)

        if iteracoes == 0 and Varx[-1] <= erro:
            continuar = False

        elif iteracoes > 0 and iteracao >= iteracoes:
            continuar = False

    dados = {'X': Xs, 'Variação': Varx}
    df = pd.DataFrame(dados)
    return df

def newtonraphson(x, erro, f, df, iteracoes=0):
    iteracao = 0
    Xs = [x]
    Varx = [0]

    continuar = True

    for i in range(1,5):
        iteracao += 1
        x = x - f(x) / df(x)
        Xs.append(x)
        variacao = (Xs[-1] - Xs[-2]) / Xs[-1]
        Varx.append(variacao)

        if iteracoes == 0 and abs(Varx[-1]) <= erro:
            continuar = False

        elif iteracoes > 0 and iteracao >= iteracoes:
            continuar = False

    dados = {'X': Xs, 'Variação': Varx}
    df = pd.DataFrame(dados)
    return df

def secante(x0, x1, erro, f, iteracoes=0):
    iteracao = 0
    Xs = [x0, x1]
    Varx = [0,0]

    continuar = True

    while continuar:
        iteracao += 1
        x = Xs[-1] - f(Xs[-1]) * (Xs[-2] - Xs[-1]) / (f(Xs[-2]) - f(Xs[-1]))
        Xs.append(x)
        variacao = (Xs[-1] - Xs[-2]) / Xs[-1]
        Varx.append(variacao)

        if iteracoes == 0 and abs(Varx[-1]) <= erro:
            continuar = False

        elif iteracoes > 0 and iteracao >= iteracoes:
            continuar = False

    dados = {'X': Xs, 'Variação': Varx}
    df = pd.DataFrame(dados)
    return df

metodo = st.selectbox("Escolha o método",["Bisseção","Falsa Posição","Ponto Fixo","Newton Raphson", "Secante"])

st.title("Métodos Numéricos")

if metodo == "Bisseção":

    st.header("Bisseção")
    a = st.number_input("Digite o valor de A")
    st.write(a)

    b = st.number_input("Digite o valor de B")
    st.write(b)

    var = st.number_input("Digite o valor da Variação mínima de X")
    st.write(var)

    funcao = st.text_input("Escreva a função")
    st.write(funcao)
    st.write("A função deve ser escrita como uma linha de python utilizando x como variável")

    def f(x):
        return eval(funcao)

    if funcao != "":
        st.table(bissecao(a,b,var,f))

if metodo == "Falsa Posição":

    st.header("Falsa Posição")
    a = st.number_input("Digite o valor de A")
    st.write(a)

    b = st.number_input("Digite o valor de B")
    st.write(b)

    var = st.number_input("Digite o valor da Variação mínima de X")
    st.write(var)

    funcao = st.text_input("Escreva a função")
    st.write(funcao)
    st.write("A função deve ser escrita como uma linha de python utilizando x como variável")


    def f(x):
        return eval(funcao)


    if funcao != "":
        st.table(falsaposicao(a, b, var, f))

if metodo == "Ponto Fixo":

    st.header("Ponto Fixo")
    x = st.number_input("Digite o valor de X")
    st.write(x)

    var = st.number_input("Digite o valor da Variação mínima de X")
    st.write(var)

    funcao = st.text_input("Escreva a função")
    st.write(funcao)
    st.write("A função deve ser escrita como uma linha de python utilizando x como variável")


    def f(x):
        return eval(funcao)


    if funcao != "":
        st.table(pontofixo(x,var,f))

if metodo == "Newton Raphson":
    st.header("Newton Raphson")
    x = st.number_input("Digite o valor de X")
    st.write(x)

    var = st.number_input("Digite o valor da Variação mínima de X")
    st.write(var)

    funcao = st.text_input("Escreva a função")
    st.write(funcao)
    st.write("A função deve ser escrita como uma linha de python utilizando x como variável")

    dfuncao = st.text_input("Escreva a função derivada")
    st.write(dfuncao)
    st.write("A função deve ser escrita como uma linha de python utilizando x como variável")


    def f(x):
        return eval(funcao)

    def df(x):
        return eval(dfuncao)


    if funcao != "":
        st.table(newtonraphson(x, var, f,df))

if metodo == "Secante":
    st.header("Secante")
    x0 = st.number_input("Digite o valor de X0")
    st.write(x0)

    x1 = st.number_input("Digite o valor de X1")
    st.write(x1)

    var = st.number_input("Digite o valor da Variação mínima de X")
    st.write(var)

    funcao = st.text_input("Escreva a função")
    st.write(funcao)
    st.write("A função deve ser escrita como uma linha de python utilizando x como variável")

    def f(x):
        return eval(funcao)

    if funcao != "":
        st.table(secante(x0,x1, var, f))


