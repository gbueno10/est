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

def intervalo_confianca_razao_variancias(
    var_amostral1 = 5.0,           # variância da amostra 1 (s1²)
    var_amostral2 = 2.0,           # variância da amostra 2 (s2²)
    n1 = 20,                       # tamanho da amostra 1 (n1)
    n2 = 15,                       # tamanho da amostra 2 (n2)
    nivel_confianca = 0.95         # nível de confiança (1-α)
):
    """
    IC para a razão das variâncias de duas populações normais (Distribuição F).
    """
    df1 = n1 - 1
    df2 = n2 - 1
    razao = var_amostral1 / var_amostral2
    alfa = 1 - nivel_confianca
    
    # Valores críticos da F
    f_inf = stats.f.ppf(alfa/2, df1, df2)
    f_sup = stats.f.ppf(1 - alfa/2, df1, df2)
    
    # O IC para σ1²/σ2² é [ (s1²/s2²) / f_sup, (s1²/s2²) / f_inf ] 
    # Dependendo da definição da tabela, mas scipy retorna o quantil direto
    inferior = razao / f_sup
    superior = razao / f_inf
    
    print(f"📊 IC PARA RAZÃO DE VARIÂNCIAS (σ1² / σ2²)")
    print(f"Razão Amostral (s1²/s2²): {razao:.4f}")
    print(f"Graus de Liberdade: gl1={df1}, gl2={df2}")
    print(f"F críticos: {f_inf:.4f} e {f_sup:.4f}")
    print(f"IC Razão Variâncias: [{inferior:.4f}, {superior:.4f}]")
    
    # Visualização (Distribuição F)
    fig, ax = plt.subplots(figsize=(10, 4))
    x_max = f_sup * 1.5
    x = np.linspace(0.01, x_max, 1000)
    y = stats.f.pdf(x, df1, df2)
    ax.plot(x, y, color='teal')
    
    x_fill = np.linspace(f_inf, f_sup, 1000)
    ax.fill_between(x_fill, stats.f.pdf(x_fill, df1, df2), color='teal', alpha=0.3, label='Área IC Central')
    
    ax.set_title(f"Distribuição F (gl1={df1}, gl2={df2})")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    intervalo_confianca_razao_variancias(
        var_amostral1 = 5.0,       # variância amostra 1
        var_amostral2 = 2.0,       # variância amostra 2
        n1 = 20,                   # n1
        n2 = 15,                   # n2
        nivel_confianca = 0.95     # nível de confiança
    )
