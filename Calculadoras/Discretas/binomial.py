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

def calcular_binomial(
    n = 20,             # número de tentativas (n)
    p = 0.3,            # probabilidade de sucesso (p)
    tipo = 'pmf',       # tipo de cálculo: 'pmf' (P(X=k)), 'cdf' (P(X≤k)), 'sf' (P(X≥k)), 'interval', 'ppf'
    k = 6,              # número de sucessos (k) para pmf, cdf e sf
    a = 4,              # limite inferior para interval
    b = 10,             # limite superior para interval
    prob = 0.95         # probabilidade acumulada (α) para ppf
):
    """
    Calculadora para Distribuição Binomial B(n, p).
    """
    if n < 0 or p < 0 or p > 1: 
        print("❌ n ≥ 0, 0 ≤ p ≤ 1")
        return
    
    dist = stats.binom(n, p)
    print(f"📊 BINOMIAL (n={n}, p={p})")
    
    q = 1 - p
    if n >= 20:
        if (n*p <= 7 or n*q <= 7):
            print(f"✅ Pode aproximar para POISSON (n={n}≥20 e np={n*p:.2f}≤7 ou nq={n*q:.2f}≤7)")
        if (n*p > 7 and n*q > 7):
            print(f"✅ Pode aproximar para NORMAL (n={n}≥20 e np={n*p:.2f}>7 e nq={n*q:.2f}>7)")

    if tipo == 'pmf':
        res = dist.pmf(k)
        print(f"P(X = {k}) = {res:.6f}")
        label, k_range = f'P(X = {k})', (k, k)
    elif tipo == 'cdf':
        res = dist.cdf(k)
        print(f"P(X ≤ {k}) = {res:.6f}")
        label, k_range = f'P(X ≤ {k})', (0, k)
    elif tipo == 'sf':
        res = dist.sf(k-1)
        print(f"P(X ≥ {k}) = {res:.6f}")
        label, k_range = f'P(X ≥ {k})', (k, n)
    elif tipo == 'interval':
        res = dist.cdf(b) - (dist.cdf(a-1) if a > 0 else 0)
        print(f"P({a} ≤ X ≤ {b}) = {res:.6f}")
        label, k_range = f'P({a} ≤ X ≤ {b})', (a, b)
    elif tipo == 'ppf':
        res = int(dist.ppf(prob))
        print(f"Menor k (dado α={prob}) tal que P(X ≤ k) ≥ {prob}: k = {res}")
        label, k_range = f'P(X ≤ {res}) ≥ {prob}', (0, res)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    x_vals = np.arange(0, n+1)
    colors = ['steelblue'] * len(x_vals)
    for i in range(len(x_vals)):
        if k_range[0] <= x_vals[i] <= k_range[1]: 
            colors[i] = 'red'
    ax.bar(x_vals, dist.pmf(x_vals), color=colors, alpha=0.7, edgecolor='black', label=label)
    if n > 50: 
        ax.set_xlim(-1, 51) 
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_binomial(
        n = 20,             # número de tentativas (n)
        p = 0.3,            # probabilidade de sucesso (p)
        tipo = 'pmf',       # tipo: 'pmf' (P(X=k)), 'cdf' (P(X≤k)), 'sf' (P(X≥k)), 'interval', 'ppf'
        k = 6,              # número de sucessos (k) para pmf, cdf e sf
        a = 4,              # limite inferior para interval
        b = 10,             # limite superior para interval
        prob = 0.95         # probabilidade acumulada mínima (α) para ppf
    )
