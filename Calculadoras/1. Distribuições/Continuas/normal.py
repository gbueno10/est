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

def calcular_normal(
    mu = 0,             # média (μ)
    sigma = 1,          # desvio padrão (σ)
    tipo = 'cdf',       # tipo de cálculo: 'cdf' (P(X≤x)), 'sf' (P(X≥x)), 'interval' (P(a≤X≤b)), 'ppf' (quantil), 'isf' (quantil inverso)
    x = 1.96,           # valor x para cdf e sf
    a = -1.96,          # limite inferior para interval
    b = 1.96,           # limite superior para interval
    p = 0.95            # probabilidade (α) para ppf e isf
):
    """
    Calculadora para Distribuição Normal N(mu, sigma).
    """
    if sigma <= 0: 
        print("❌ σ > 0")
        return
    
    dist = stats.norm(mu, sigma)
    print(f"📊 NORMAL (μ={mu}, σ={sigma})")
    
    if tipo == 'cdf':
        res = dist.cdf(x)
        print(f"P(X ≤ {x}) = {res:.6f}")
        label, x_fill = f'P(X ≤ {x})', np.linspace(mu - 4*sigma, x, 1000)
    elif tipo == 'sf':
        res = dist.sf(x)
        print(f"P(X ≥ {x}) = {res:.6f}")
        label, x_fill = f'P(X ≥ {x})', np.linspace(x, mu + 4*sigma, 1000)
    elif tipo == 'interval':
        res = dist.cdf(b) - dist.cdf(a)
        print(f"P({a} ≤ X ≤ {b}) = {res:.6f}")
        label, x_fill = f'P({a} ≤ X ≤ {b})', np.linspace(a, b, 1000)
    elif tipo == 'ppf':
        res = dist.ppf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(X ≤ x) = {p}")
        label, x_fill = f'P(X ≤ {res:.2f}) = {p}', np.linspace(mu - 4*sigma, res, 1000)
    elif tipo == 'isf':
        res = dist.isf(p)
        print(f"x (dado α={p}): x = {res:.6f}  |  P(X ≥ x) = {p}")
        label, x_fill = f'P(X ≥ {res:.2f}) = {p}', np.linspace(res, mu + 4*sigma, 1000)

    fig, ax = plt.subplots(figsize=(10, 4))
    x_plot = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y_plot = dist.pdf(x_plot)
    ax.plot(x_plot, y_plot, 'b-')
    ax.fill_between(x_fill, dist.pdf(x_fill), alpha=0.3, color='blue', label=label)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    calcular_normal(
        mu = 0,             # média (μ)
        sigma = 1,          # desvio padrão (σ)
        tipo = 'cdf',       # tipo de cálculo: 'cdf' (P(X≤x)), 'sf' (P(X≥x)), 'interval' (P(a≤X≤b)), 'ppf' (quantil), 'isf' (quantil inverso)
        x = 1.96,           # valor x para cdf e sf
        a = -1.96,          # limite inferior para interval
        b = 1.96,           # limite superior para interval
        p = 0.95            # probabilidade (α) para ppf e isf
    )
    
