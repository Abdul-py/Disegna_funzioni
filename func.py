import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
 
sns.set_style("whitegrid") 
 
sqrt = np.sqrt 
cos = np.cos 
sin = np.sin 
abs = np.abs 
 
 
def chiedi_equaz():
    n_f = int(input("Inserisci il numero delle funzioni: ")) 
 
    formule = {} 
    for i in range(1, n_f + 1): 
        nome_f = f"funzione_{i}" 
        print(f"Inserisci la formula della funzione {i}: ") 
        formule[nome_f] = input("f(x) = ") 
    return formule
 
 
def crea_df(formule):
    df = pd.DataFrame(np.arange(-50, 51), columns=["x"]) 
    df_positivo = df[df["x"] >= 0] 
    
    for formula in formule.keys(): 
        if formule[formula].__contains__('sqrt') or formule[formula] == '3/x' or formule[formula] == '-3/x': 
            df[formula] = df_positivo.apply(lambda x: eval(formule[formula])) 
        else: 
            df[formula] = df['x'].apply(lambda x: eval(formule[formula])) 
   
   
def plots(df, formule):  
    for formula in formule.keys(): 
        f = sns.lineplot(x="x", y=formula, data=df) 
        f.set_title(formule[formula]) 
        f.set(xlabel="x", ylabel="y") 
        plt.show()