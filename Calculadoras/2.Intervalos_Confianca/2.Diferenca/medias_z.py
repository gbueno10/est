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

def intervalo_confianca_diferenca_medias_z(
    media1 = 15.0,                # média da amostra 1 (x̄1)
    media2 = 12.0,                # média da amostra 2 (x̄2)
    sigma1 = 3.0,                 # desvio padrão da amostra 1 (σ1)
    sigma2 = 2.5,                 # desvio padrão da amostra 2 (σ2)
    n1 = 40,                      # tamanho da amostra 1 (n1)
    n2 = 35,                      # tamanho da amostra 2 (n2)
    nivel_confianca = 0.95        # nível de confiança (1-α)
):
    """
    IC para a diferença de médias com variâncias conhecidas ou amostras grandes (Z).
    """
    diff = media1 - media2
    alfa = 1 - nivel_confianca
    z_critico = stats.norm.ppf(1 - alfa/2)
    
    erro_padrao = np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    margem_erro = z_critico * erro_padrao
    
    inferior = diff - margem_erro
    superior = diff + margem_erro
    
    print(f"📊 IC Z PARA DIFERENÇA DE MÉDIAS (μ1 - μ2)")
    print(f"Diferença Amostral: {diff:.4f}")
    print(f"Z crítico: {z_critico:.4f}")
    print(f"IC: [{inferior:.4f}, {superior:.4f}]")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(diff - 4*erro_padrao, diff + 4*erro_padrao, 1000)
    y = stats.norm.pdf(x, diff, erro_padrao)
    ax.plot(x, y, 'b-')
    ax.fill_between(x[ (x >= inferior) & (x <= superior) ], 
                    stats.norm.pdf(x[ (x >= inferior) & (x <= superior) ], diff, erro_padrao),
                    color='blue', alpha=0.2, label=f'IC {nivel_confianca*100:.0f}%')
    
    ax.axvline(0, color='gray', linestyle='--') # Linha do zero (independência)
    ax.set_title("Distribuição da Diferença de Médias (μ1 - μ2)")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    intervalo_confianca_diferenca_medias_z(
        media1 = 15.0,             # média amostra 1
        media2 = 12.0,             # média amostra 2
        sigma1 = 3.0,              # desvio padrão populacional 1
        sigma2 = 2.5,              # desvio padrão populacional 2
        n1 = 40,                   # n1
        n2 = 35,                   # n2
        nivel_confianca = 0.95     # nível de confiança
    )
