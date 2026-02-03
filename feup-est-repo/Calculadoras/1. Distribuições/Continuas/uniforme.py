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

def calcular_uniforme(
    a_min = 0,          # limite inferior (a)
    b_max = 10,         # limite superior (b)
    tipo = 'cdf',       # tipo de cálculo: 'cdf' (≤), 'sf' (≥), 'interval' (a≤X≤b), 'ppf', 'isf'
    x = 5.0,            # valor x para cdf e sf
    a = 2.0,            # limite inferior para interval
    b = 8.0,            # limite superior para interval
    p = 0.5             # probabilidade (α) para ppf e isf
):
    """
    Calculadora para Distribuição Uniforme Contínua [a_min, b_max].
    """
    if b_max <= a_min: 
        print("❌ b > a")
        return
    
    dist = stats.uniform(loc=a_min, scale=b_max-a_min)
    print(f"📊 UNIFORME [ {a_min}, {b_max} ]")
    
    if tipo == 'cdf':
        res = dist.cdf(x)
        print(f"P(X ≤ {x}) = {res:.6f}")
        label, x_fill = f'P(X ≤ {x})', np.linspace(a_min, x, 1000)
    elif tipo == 'sf':
        res = dist.sf(x)
        print(f"P(X ≥ {x}) = {res:.6f}")
        label, x_fill = f'P(X ≥ {x})', np.linspace(x, b_max, 1000)
    elif tipo == 'interval':
        res = dist.cdf(b) - dist.cdf(a)
        print(f"P({a} ≤ X ≤ {b}) = {res:.6f}")
        label, x_fill = f'P({a} ≤ X ≤ {b})', np.linspace(a, b, 1000)
    elif tipo == 'ppf':
        res = dist.ppf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(X ≤ x) = {p}")
        label, x_fill = f'P(X ≤ {res:.2f}) = {p}', np.linspace(a_min, res, 1000)
    elif tipo == 'isf':
        res = dist.isf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(X ≥ x) = {p}")
        label, x_fill = f'P(X ≥ {res:.2f}) = {p}', np.linspace(res, b_max, 1000)

    fig, ax = plt.subplots(figsize=(10, 4))
    x_plot = np.linspace(a_min-1, b_max+1, 1000)
    y_plot = dist.pdf(x_plot)
    ax.plot(x_plot, y_plot, color='darkgreen')
    ax.fill_between(x_fill, dist.pdf(x_fill), alpha=0.3, color='green', label=label)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_uniforme(
        a_min = 0,          # limite inferior (a)
        b_max = 10,         # limite superior (b)
        tipo = 'cdf',       # tipo: 'cdf' (≤), 'sf' (≥), 'interval' (a≤X≤b), 'ppf', 'isf'
        x = 5.0,            # valor x para cdf e sf
        a = 2.0,            # limite inferior para interval
        b = 8.0,            # limite superior para interval
        p = 0.5             # probabilidade (α) para ppf e isf
    )
