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

def intervalo_confianca_variancia(
    variancia_amostral = 4.0,     # variância amostral (s²)
    n = 20,                       # tamanho da amostra (n)
    nivel_confianca = 0.95        # nível de confiança (1-α)
):
    """
    Calcula o IC para a variância de uma população normal (Qui-Quadrado).
    """
    df = n - 1
    alfa = 1 - nivel_confianca
    
    # Valores críticos da Qui-Quadrado
    chi2_inf = stats.chi2.ppf(alfa/2, df)
    chi2_sup = stats.chi2.ppf(1 - alfa/2, df)
    
    inferior = (df * variancia_amostral) / chi2_sup
    superior = (df * variancia_amostral) / chi2_inf
    
    print(f"📊 INTERVALO DE CONFIANÇA PARA A VARIANÇA")
    print(f"Graus de Liberdade: {df}")
    print(f"Qui-Quadrado Críticos: {chi2_inf:.4f} e {chi2_sup:.4f}")
    print(f"IC Variância (σ²): [{inferior:.4f}, {superior:.4f}]")
    print(f"IC Desvio Padrão (σ): [{np.sqrt(inferior):.4f}, {np.sqrt(superior):.4f}]")
    
    # Visualização (distribuição Qui-Quadrado)
    fig, ax = plt.subplots(figsize=(10, 4))
    x_max = chi2_sup * 1.5
    x = np.linspace(0, x_max, 1000)
    y = stats.chi2.pdf(x, df)
    ax.plot(x, y, color='darkorange')
    
    x_fill = np.linspace(chi2_inf, chi2_sup, 1000)
    ax.fill_between(x_fill, stats.chi2.pdf(x_fill, df), color='orange', alpha=0.3, label='Área de Aceitação')
    
    ax.set_title(f"Distribuição Qui-Quadrado (df={df})")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    intervalo_confianca_variancia(
        variancia_amostral = 4.0,   # variância amostral (s²)
        n = 20,                     # tamanho da amostra (n)
        nivel_confianca = 0.95      # nível de confiança
    )
