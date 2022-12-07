import sympy as sp


def ask_func():
    funcs = {}
    
    n_f = int(input("Inserisci in numero di funzioni: "))
    if n_f < 1:
        exit()
    for i in range(1, n_f + 1):
        try:
            f = input("Inserisci la funzione: ")
            nome = f'func_{i}'
            funcs[nome] = f
        except:
            print("Funzione non valida")
            ret = str(input("Vuoi riprovare? (y/n): "))
            if ret == 'y':
                ask_func()
            else:
                exit()
        return funcs
        

        
        
def main():
    functions = ask_func()
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    if functions:
        print(functions)
        p = sp.plot(functions['func_1'], show=False)
        print(p)
        p.show()
        
    
if __name__ == "__main__":
    main()
    