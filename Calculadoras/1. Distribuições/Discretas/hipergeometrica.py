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

def calcular_hipergeometrica(
    M = 100,            # tamanho total da população (M)
    K = 30,             # número de sucessos na população (K)
    N = 20,             # tamanho da amostra (N)
    tipo = 'pmf',       # tipo de cálculo: 'pmf' (P(X=k)), 'cdf' (P(X≤k)), 'sf' (P(X≥k)), 'interval', 'ppf'
    k = 8,              # número de sucessos na amostra (k)
    a = 4,              # limite inferior para interval
    b = 12,             # limite superior para interval
    prob = 0.95         # probabilidade acumulada (α) para ppf
):
    """
    Calculadora para Distribuição Hipergeométrica.
    """
    if M < 0 or K < 0 or N < 0 or K > M or N > M: 
        print("❌ K≤M, N≤M")
        return
    
    dist = stats.hypergeom(M, K, N)
    print(f"📊 HIPERGEOMÉTRICA (M={M}, K={K}, N={N})")
    
    if M >= 10*N: 
        print(f"✅ Pode aproximar para BINOMIAL (M={M} ≥ 10N={10*N})")

    x_min, x_max = max(0, N-M+K), min(K, N)
    x_vals = np.arange(x_min, x_max + 1)
    
    if tipo == 'pmf':
        res = dist.pmf(k)
        print(f"P(X = {k}) = {res:.6f}")
        label, k_range = f'P(X = {k})', (k, k)
    elif tipo == 'cdf':
        res = dist.cdf(k)
        print(f"P(X ≤ {k}) = {res:.6f}")
        label, k_range = f'P(X ≤ {k})', (x_min, k)
    elif tipo == 'sf':
        res = dist.sf(k-1)
        print(f"P(X ≥ {k}) = {res:.6f}")
        label, k_range = f'P(X ≥ {k})', (k, x_max)
    elif tipo == 'interval':
        res = dist.cdf(b) - (dist.cdf(a-1) if a > x_min else 0)
        print(f"P({a} ≤ X ≤ {b}) = {res:.6f}")
        label, k_range = f'P({a} ≤ X ≤ {b})', (a, b)
    elif tipo == 'ppf':
        res = int(dist.ppf(prob))
        print(f"Menor k (dado α={prob}) tal que P(X ≤ k) ≥ {prob}: k = {res}")
        label, k_range = f'P(X ≤ {res}) ≥ {prob}', (x_min, res)
        
    fig, ax = plt.subplots(figsize=(10, 4))
    colors = ['mediumpurple'] * len(x_vals)
    for i in range(len(x_vals)):
        if k_range[0] <= x_vals[i] <= k_range[1]: 
            colors[i] = 'red'
    ax.bar(x_vals, dist.pmf(x_vals), color=colors, alpha=0.7, edgecolor='black', label=label)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_hipergeometrica(
        M = 100,            # tamanho total da população (M)
        K = 30,             # número de sucessos na população (K)
        N = 20,             # tamanho da amostra (N)
        tipo = 'pmf',       # tipo: 'pmf' (P(X=k)), 'cdf' (P(X≤k)), 'sf' (P(X≥k)), 'interval', 'ppf'
        k = 8,              # número de sucessos na amostra (k)
        a = 4,              # limite inferior para interval
        b = 12,             # limite superior para interval
        prob = 0.95         # probabilidade acumulada mínima (α) para ppf
    )
