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

def eq():
    print("Inserisci il tipo di equazione:")
    print(r"1. Intera")
    print(r"2. Frazionaria")
    tipo = str(int(input("Inserisci il numero corrispondente: ")))
    if tipo == "1":
        try:
            eqaz = str(input("Inserisci l'equazione: ")) 
            return eqaz
        except ValueError:
            print("Inserisci una equazione valida")
            eq()
            
    elif tipo == "2":
        try:
            num = str(input("Inserisci il numeratore dell'equazione: "))
            den = str(input("Inserisci il denominatore dell'equazione: "))
            equz = "(" + num + ")" + "/" + "(" + den + ")"
            return equz
        except ValueError:
            print("Inserisci una equazione valida")
            eq()
            
def main():
    print(eq())
    
if __name__ == "__main__":
    main()