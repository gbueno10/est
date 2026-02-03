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

def calcular_exponencial(
    lam = 0.5,          # taxa (λ)
    tipo = 'cdf',       # tipo de cálculo: 'cdf' (≤), 'sf' (≥), 'interval' (a≤X≤b), 'ppf', 'isf'
    x = 2.0,            # valor x para cdf e sf
    a = 1.0,            # limite inferior para interval
    b = 4.0,            # limite superior para interval
    p = 0.05            # probabilidade (α) para ppf e isf
):
    """
    Calculadora para Distribuição Exponencial com taxa λ (lambda).
    """
    if lam <= 0: 
        print("❌ λ > 0")
        return
    
    dist = stats.expon(scale=1/lam)
    print(f"📊 EXPONENCIAL (λ={lam})")
    
    x_max = max(5/lam, x+2, b+1)
    
    if tipo == 'cdf':
        res = dist.cdf(x)
        print(f"P(X ≤ {x}) = {res:.6f}")
        label, x_fill = f'P(X ≤ {x})', np.linspace(0, x, 1000)
    elif tipo == 'sf':
        res = dist.sf(x)
        print(f"P(X ≥ {x}) = {res:.6f}")
        label, x_fill = f'P(X ≥ {x})', np.linspace(x, x_max, 1000)
    elif tipo == 'interval':
        res = dist.cdf(b) - dist.cdf(a)
        print(f"P({a} ≤ X ≤ {b}) = {res:.6f}")
        label, x_fill = f'P({a} ≤ X ≤ {b})', np.linspace(a, b, 1000)
    elif tipo == 'ppf':
        res = dist.ppf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(X ≤ x) = {p}")
        label, x_fill = f'P(X ≤ {res:.2f}) = {p}', np.linspace(0, res, 1000)
    elif tipo == 'isf':
        res = dist.isf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(X ≥ x) = {p}")
        label, x_fill = f'P(X ≥ {res:.2f}) = {p}', np.linspace(res, x_max, 1000)

    fig, ax = plt.subplots(figsize=(10, 4))
    x_plot = np.linspace(0, x_max, 1000)
    y_plot = dist.pdf(x_plot)
    ax.plot(x_plot, y_plot, color='teal')
    ax.fill_between(x_fill, dist.pdf(x_fill), alpha=0.3, color='teal', label=label)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_exponencial(
        lam = 0.5,          # taxa (λ)
        tipo = 'cdf',       # tipo: 'cdf' (≤), 'sf' (≥), 'interval' (a≤X≤b), 'ppf', 'isf'
        x = 2.0,            # valor x para cdf e sf
        a = 1.0,            # limite inferior para interval
        b = 4.0,            # limite superior para interval
        p = 0.05            # probabilidade (α) para ppf e isf
    )
