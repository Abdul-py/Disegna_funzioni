import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sympy as sp


sns.set_style("whitegrid")


# Setting the operators
sqrt = np.sqrt
log = np.log
abs = np.abs
sin = np.sin
cos = np.cos


# Setting the global variable
x = sp.Symbol('x')

# Creating the fnction to get the function type
def tipo_f():
    print("Che tipo di funzione vuoi disegnare?")
    print("1) Intera")
    print("2) Frazionaria")
    try:
        tipo = int(input("Inserisci il numero corrispondente: "))
        if tipo == 1:
            return "intera"
        if tipo == 2:
            return "frazionaria"
        print("Inserisci un numero valido")
        return tipo_f()
    except ValueError:
        print("Inserisci un numero valido")
        return tipo_f()
    
    
# Creating the function to get the function's expression as input
def input_eq(tipo):
    if tipo == "intera":
        try:
            equ = input("f(x)= ")
            return equ
        except ValueError:
            print("Inserisci una funzione valida!!")
            return input_eq(tipo)
    else:
        try:
            num = input("Inserisci il numeratore: ")
            den = input("Inserisci il denominatore: ")
            return num, den
        except ValueError:
            print("Inserisci una funzione valida!!")
            return input_eq(tipo)
        
        
# Creating the function to create the dataframe for the plot if the function is "Intera"
def df_intera(f):
    df = pd.DataFrame()
    df['x'] = np.linspace(-50, 50, 1001)
    df['y'] = df["x"].apply(lambda x: eval(f))
    return df


# Creating the function to create the dataframe for the plot if the function is "Frazionaria"
def df_fraz(num, den):
    valori_da_escludere = np.array(sp.solve(den))
    f = "(" + num + ")/(" + den + ")"
    df = pd.DataFrame()
    df['x'] = np.linspace(-50, 50, 201)
    cond = df['x'].isin(valori_da_escludere)
    df['x'] = df[~cond]
    df['y'] = df["x"].apply(lambda x: eval(f))
    return df
    
    
# Creating the function to plot the function
def plot(df):
    p = sns.scatterplot(x = "x", y = "y", data = df)
    p.set_title("Grafico della funzione")
    p.set_xlabel("x")
    p.set_ylabel("y")
    plt.show()
    
    
def main():
    tipo = tipo_f()

    if tipo == "intera":
        eq = input_eq(tipo)
        df = df_intera(eq)
    else:
        num, den = input_eq(tipo)
        df = df_fraz(num, den)

    plot(df)

if __name__ == "__main__":
    main()
