import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
 
sns.set_style("whitegrid") 
 
sqrt = np.sqrt 
cos = np.cos 
sin = np.sin 
abs = np.abs 
 
n_f = int(input("Inserisci il numero delle funzioni: ")) 
# formule = {"formula_1": "1/2*x", 
#            "formula_2": '-3*x', 
#             "formula_3": '1/2*x**2', 
#             "formula_4": '-4*x**2', 
#             "formula_5": '3/x', 
#             "formula_6": '-3/x', 
#             "formula_7": 'x**3', 
#             "formula_8": '-x**3', 
#             "formula_9": 'sqrt(x)', 
#             "formula_10": 'abs(x)', 
#                    } 
 
formule = {} 
for i in range(1, n_f + 1): 
    nome_f = f"funzione_{i}" 
    print(f"Inserisci la formula della funzione {i}: ") 
    formule[nome_f] = input("f(x) = ") 
 
df = pd.DataFrame(np.arange(-50, 51), columns=["x"]) 
df_positivo = df[df["x"] >= 0] 
 
for formula in formule.keys(): 
    if formule[formula].__contains__('sqrt') or formule[formula] == '3/x' or formule[formula] == '-3/x': 
        df[formula] = df_positivo.apply(lambda x: eval(formule[formula])) 
    else: 
        df[formula] = df['x'].apply(lambda x: eval(formule[formula])) 
     
for formula in formule.keys(): 
    f = sns.lineplot(x="x", y=formula, data=df) 
    f.set_title(formule[formula]) 
    f.set(xlabel="x", ylabel="y") 
    plt.show()