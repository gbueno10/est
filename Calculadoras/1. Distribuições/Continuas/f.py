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

def calcular_f(
    dfn = 5,            # graus de liberdade do numerador (ν1)
    dfd = 10,           # graus de liberdade do denominador (ν2)
    tipo = 'cdf',       # tipo de cálculo: 'cdf' (≤), 'sf' (≥), 'interval' (a≤F≤b), 'ppf', 'isf'
    x = 2.5,            # valor F para cdf e sf
    a = 1.0,            # limite inferior para interval
    b = 4.0,            # limite superior para interval
    p = 0.05            # probabilidade (α) para ppf e isf
):
    """
    Calculadora para Distribuição F (Fisher-Snedecor).
    """
    dist = stats.f(dfn, dfd)
    print(f"📊 F (dfn={dfn}, dfd={dfd})")
    
    x_max = max(6, x+2, b+1)
    
    if tipo == 'cdf':
        res = dist.cdf(x)
        print(f"P(F ≤ {x}) = {res:.6f}")
        label, x_fill = f'P(F ≤ {x})', np.linspace(0, x, 1000)
    elif tipo == 'sf':
        res = dist.sf(x)
        print(f"P(F ≥ {x}) = {res:.6f}")
        label, x_fill = f'P(F ≥ {x})', np.linspace(x, x_max, 1000)
    elif tipo == 'interval':
        res = dist.cdf(b) - dist.cdf(a)
        print(f"P({a} ≤ F ≤ {b}) = {res:.6f}")
        label, x_fill = f'P({a} ≤ F ≤ {b})', np.linspace(a, b, 1000)
    elif tipo == 'ppf':
        res = dist.ppf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(F ≤ x) = {p}")
        label, x_fill = f'P(F ≤ {res:.2f}) = {p}', np.linspace(0, res, 1000)
    elif tipo == 'isf':
        res = dist.isf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(F ≥ x) = {p}")
        label, x_fill = f'P(F ≥ {res:.2f}) = {p}', np.linspace(res, x_max, 1000)

    fig, ax = plt.subplots(figsize=(10, 4))
    x_plot = np.linspace(0.01, x_max, 1000)
    y_plot = dist.pdf(x_plot)
    ax.plot(x_plot, y_plot, color='purple')
    ax.fill_between(x_fill, dist.pdf(x_fill), alpha=0.3, color='purple', label=label)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_f(
        dfn = 5,            # graus de liberdade do numerador (ν1)
        dfd = 10,           # graus de liberdade do denominador (ν2)
        tipo = 'sf',        # tipo: 'cdf' (≤), 'sf' (≥), 'interval' (a≤F≤b), 'ppf', 'isf'
        x = 2.5,            # valor F para cdf e sf
        a = 1.0,            # limite inferior para interval
        b = 4.0,            # limite superior para interval
        p = 0.05            # probabilidade (α) para ppf e isf
    )
