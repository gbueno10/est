import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Configurar estilo dos gráficos
warnings.filterwarnings('ignore')
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    plt.style.use('default')

def calcular_geometrica(
    p = 0.3,            # probabilidade de sucesso (p)
    tipo = 'pmf',       # tipo de cálculo: 'pmf' (P(X=k)), 'cdf' (P(X≤k)), 'sf' (P(X≥k)), 'interval', 'ppf'
    k = 5,              # número da tentativa em que ocorre o primeiro sucesso (k)
    a = 2,              # limite inferior para interval
    b = 8,              # limite superior para interval
    prob = 0.95         # probabilidade acumulada (α) para ppf
):
    """
    Calculadora para Distribuição Geométrica com probabilidade p.
    """
    if p <= 0 or p > 1: 
        print("❌ 0 < p ≤ 1")
        return
    
    dist = stats.geom(p)
    print(f"📊 GEOMÉTRICA (p={p})")
    
    x_max = min(50, int(dist.mean() + 5*dist.std()))
    x_vals = np.arange(1, x_max + 1)
    
    if tipo == 'pmf':
        res = dist.pmf(k)
        print(f"P(X = {k}) = {res:.6f}")
        label, k_range = f'P(X = {k})', (k, k)
    elif tipo == 'cdf':
        res = dist.cdf(k)
        print(f"P(X ≤ {k}) = {res:.6f}")
        label, k_range = f'P(X ≤ {k})', (1, k)
    elif tipo == 'sf':
        res = dist.sf(k-1)
        print(f"P(X ≥ {k}) = {res:.6f}")
        label, k_range = f'P(X ≥ {k})', (k, x_max)
    elif tipo == 'interval':
        res = dist.cdf(b) - (dist.cdf(a-1) if a > 1 else 0)
        print(f"P({a} ≤ X ≤ {b}) = {res:.6f}")
        label, k_range = f'P({a} ≤ X ≤ {b})', (a, b)
    elif tipo == 'ppf':
        res = int(dist.ppf(prob))
        print(f"Menor k (dado α={prob}) tal que P(X ≤ k) ≥ {prob}: k = {res}")
        label, k_range = f'P(X ≤ {res}) ≥ {prob}', (1, res)
        
    fig, ax = plt.subplots(figsize=(10, 4))
    colors = ['mediumseagreen'] * len(x_vals)
    for i in range(len(x_vals)):
        if k_range[0] <= x_vals[i] <= k_range[1]: 
            colors[i] = 'red'
    ax.bar(x_vals, dist.pmf(x_vals), color=colors, alpha=0.7, edgecolor='black', label=label)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_geometrica(
        p = 0.3,            # probabilidade de sucesso (p)
        tipo = 'pmf',       # tipo: 'pmf' (P(X=k)), 'cdf' (P(X≤k)), 'sf' (P(X≥k)), 'interval', 'ppf'
        k = 5,              # tentativa do primeiro sucesso (k)
        a = 2,              # limite inferior para interval
        b = 8,              # limite superior para interval
        prob = 0.95         # probabilidade acumulada mínima (α) para ppf
    )
