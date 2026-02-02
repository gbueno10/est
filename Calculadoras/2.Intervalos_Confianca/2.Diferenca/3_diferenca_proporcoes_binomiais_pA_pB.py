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

def intervalo_confianca_diferenca_proporcoes(
    p_amostral1 = 0.6,             # proporção amostra 1 (p̂1)
    p_amostral2 = 0.45,            # proporção amostra 2 (p̂2)
    n1 = 100,                      # tamanho da amostra 1 (n1)
    n2 = 120,                      # tamanho da amostra 2 (n2)
    nivel_confianca = 0.95         # nível de confiança (1-α)
):
    """
    IC para a diferença de proporções populacionais (aproximação Normal).
    """
    diff = p_amostral1 - p_amostral2
    alfa = 1 - nivel_confianca
    z_critico = stats.norm.ppf(1 - alfa/2)
    
    erro_padrao = np.sqrt((p_amostral1 * (1 - p_amostral1) / n1) + (p_amostral2 * (1 - p_amostral2) / n2))
    margem_erro = z_critico * erro_padrao
    
    inferior = diff - margem_erro
    superior = diff + margem_erro
    
    print(f"📊 IC PARA DIFERENÇA DE PROPORÇÕES (p1 - p2)")
    print(f"Diferença Amostral: {diff:.4f}")
    print(f"Z crítico: {z_critico:.4f}")
    print(f"IC: [{inferior:.4f}, {superior:.4f}]")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(diff - 4*erro_padrao, diff + 4*erro_padrao, 1000)
    y = stats.norm.pdf(x, diff, erro_padrao)
    ax.plot(x, y, color='purple')
    ax.fill_between(x[ (x >= inferior) & (x <= superior) ], 
                    stats.norm.pdf(x[ (x >= inferior) & (x <= superior) ], diff, erro_padrao),
                    color='purple', alpha=0.2, label=f'IC {nivel_confianca*100:.0f}%')
    
    ax.axvline(0, color='gray', linestyle='--')
    ax.set_title("Diferença de Proporções Amostrais (Normal)")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    intervalo_confianca_diferenca_proporcoes(
        p_amostral1 = 0.6,        # proporção p1
        p_amostral2 = 0.45,       # proporção p2
        n1 = 100,                 # n1
        n2 = 120,                 # n2
        nivel_confianca = 0.95    # nível de confiança
    )
