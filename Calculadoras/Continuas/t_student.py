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

def calcular_t(
    df = 10,            # graus de liberdade (ν)
    tipo = 'cdf',       # tipo de cálculo: 'cdf' (≤), 'sf' (≥), 'two_tailed' (bilateral), 'interval' (a≤T≤b), 'ppf', 'isf'
    x = 2.0,            # valor t para cdf, sf e bilateral
    a = -2.0,           # limite inferior para interval
    b = 2.0,            # limite superior para interval
    p = 0.05            # probabilidade (α) para ppf e isf
):
    """
    Calculadora para Distribuição t de Student com df graus de liberdade.
    """
    if df < 1: 
        print("❌ df ≥ 1")
        return
    
    dist = stats.t(df)
    print(f"📊 t-STUDENT (df={df})")
    
    if df >= 30: 
        print(f"✅ Amostra Grande (GL={df} ≥ 30): Pode aproximar para NORMAL (Z)")
    
    if tipo == 'cdf':
        res = dist.cdf(x)
        print(f"P(T ≤ {x}) = {res:.6f}")
        label, x_fill = f'P(T ≤ {x})', np.linspace(-5, x, 1000)
    elif tipo == 'sf':
        res = dist.sf(x)
        print(f"P(T ≥ {x}) = {res:.6f}")
        label, x_fill = f'P(T ≥ {x})', np.linspace(x, 5, 1000)
    elif tipo == 'two_tailed':
        res = 2 * dist.sf(abs(x))
        print(f"P(|T| ≥ {abs(x)}) = {res:.6f}")
        label = f'P(|T| ≥ {abs(x)})'
        fig, ax = plt.subplots(figsize=(10, 4))
        x_plot = np.linspace(-5, 5, 1000)
        y_plot = dist.pdf(x_plot)
        ax.plot(x_plot, y_plot, 'r-')
        ax.fill_between(x_plot[x_plot <= -abs(x)], dist.pdf(x_plot[x_plot <= -abs(x)]), alpha=0.3, color='red')
        ax.fill_between(x_plot[x_plot >= abs(x)], dist.pdf(x_plot[x_plot >= abs(x)]), alpha=0.3, color='red', label=label)
        ax.legend()
        plt.show()
        return
    elif tipo == 'ppf':
        res = dist.ppf(p)
        print(f"t (dado α={p}): t = {res:.6f}  |  P(T ≤ t) = {p}")
        label, x_fill = f'P(T ≤ {res:.2f}) = {p}', np.linspace(-5, res, 1000)
    elif tipo == 'isf':
        res = dist.isf(p)
        print(f"t (dado α={p}): t = {res:.6f}  |  P(T ≥ t) = {p}")
        label, x_fill = f'P(T ≥ {res:.2f}) = {p}', np.linspace(res, 5, 1000)
    elif tipo == 'interval':
        res = dist.cdf(b) - dist.cdf(a)
        print(f"P({a} ≤ T ≤ {b}) = {res:.6f}")
        label, x_fill = f'P({a} ≤ T ≤ {b})', np.linspace(a, b, 1000)

    fig, ax = plt.subplots(figsize=(10, 4))
    x_plot = np.linspace(-5, 5, 1000)
    y_plot = dist.pdf(x_plot)
    ax.plot(x_plot, y_plot, 'r-')
    ax.fill_between(x_fill, dist.pdf(x_fill), alpha=0.3, color='red', label=label)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_t(
        df = 10,            # graus de liberdade (ν)
        tipo = 'cdf',       # tipo: 'cdf' (≤), 'sf' (≥), 'two_tailed' (bilateral), 'interval' (a≤T≤b), 'ppf', 'isf'
        x = 2.0,            # valor t para cdf, sf e bilateral
        a = -2.0,           # limite inferior para interval
        b = 2.0,            # limite superior para interval
        p = 0.05            # probabilidade (α) para ppf e isf
    )
