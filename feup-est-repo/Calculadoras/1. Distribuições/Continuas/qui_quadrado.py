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

def calcular_chi2(
    df = 5,             # graus de liberdade (ν)
    tipo = 'cdf',       # tipo de cálculo: 'cdf' (≤), 'sf' (≥), 'interval' (a≤X≤b), 'ppf', 'isf'
    x = 7.0,            # valor χ² para cdf e sf
    a = 2.0,            # limite inferior para interval
    b = 10.0,           # limite superior para interval
    p = 0.05            # probabilidade (α) para ppf e isf
):
    """
    Calculadora para Distribuição Qui-Quadrado (X²) com df graus de liberdade.
    """
    if df < 1: 
        print("❌ df ≥ 1")
        return
    
    dist = stats.chi2(df)
    print(f"📊 QUI-QUADRADO (df={df})")
    
    x_max = df + 4*np.sqrt(2*df)
    
    if tipo == 'cdf':
        res = dist.cdf(x)
        print(f"P(χ² ≤ {x}) = {res:.6f}")
        label, x_fill = f'P(χ² ≤ {x})', np.linspace(0, x, 1000)
    elif tipo == 'sf':
        res = dist.sf(x)
        print(f"P(χ² ≥ {x}) = {res:.6f}")
        label, x_fill = f'P(χ² ≥ {x})', np.linspace(x, x_max, 1000)
    elif tipo == 'interval':
        res = dist.cdf(b) - dist.cdf(a)
        print(f"P({a} ≤ χ² ≤ {b}) = {res:.6f}")
        label, x_fill = f'P({a} ≤ χ² ≤ {b})', np.linspace(a, b, 1000)
    elif tipo == 'ppf':
        res = dist.ppf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(χ² ≤ x) = {p}")
        label, x_fill = f'P(χ² ≤ {res:.2f}) = {p}', np.linspace(0, res, 1000)
    elif tipo == 'isf':
        res = dist.isf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(χ² ≥ x) = {p}")
        label, x_fill = f'P(χ² ≥ {res:.2f}) = {p}', np.linspace(res, x_max, 1000)

    fig, ax = plt.subplots(figsize=(10, 4))
    x_plot = np.linspace(0, x_max, 1000)
    y_plot = dist.pdf(x_plot)
    ax.plot(x_plot, y_plot, color='darkorange')
    ax.fill_between(x_fill, dist.pdf(x_fill), alpha=0.3, color='orange', label=label)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_chi2(
        df = 5,             # graus de liberdade (ν)
        tipo = 'sf',        # tipo: 'cdf' (≤), 'sf' (≥), 'interval' (a≤X≤b), 'ppf', 'isf'
        x = 7.0,            # valor χ² para cdf e sf
        a = 2.0,            # limite inferior para interval
        b = 10.0,           # limite superior para interval
        p = 0.05            # probabilidade (α) para ppf e isf
    )
