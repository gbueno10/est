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

def intervalo_confianca_proporcao(
    p_amostral = 0.6,             # proporção amostral (p̂)
    n = 100,                      # tamanho da amostra (n)
    nivel_confianca = 0.95,       # nível de confiança (1-α)
    M = None                      # tamanho da população (M) para correção finita
):
    """
    Calcula o IC para a proporção populacional usando aproximação Normal.
    """
    alfa = 1 - nivel_confianca
    z_critico = stats.norm.ppf(1 - alfa/2)
    erro_padrao = np.sqrt((p_amostral * (1 - p_amostral)) / n)

    # Fator de correção para população finita
    fpc = 1.0
    if M is not None:
        fpc = np.sqrt((M - n) / (M - 1))
        erro_padrao *= fpc

    margem_erro = z_critico * erro_padrao
    
    inferior = max(0, p_amostral - margem_erro)
    superior = min(1, p_amostral + margem_erro)
    
    print(f"📊 INTERVALO DE CONFIANÇA PARA PROPORÇÃO")
    print(f"Nível de Confiança: {nivel_confianca*100:.1f}%")
    print(f"Z crítico: {z_critico:.4f}")
    print(f"Erro Padrão: {erro_padrao:.4f}")
    print(f"IC: [{inferior:.4f}, {superior:.4f}]")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(max(0, p_amostral - 4*erro_padrao), min(1, p_amostral + 4*erro_padrao), 1000)
    y = stats.norm.pdf(x, p_amostral, erro_padrao)
    ax.plot(x, y, color='green')
    
    x_fill = np.linspace(inferior, superior, 1000)
    ax.fill_between(x_fill, stats.norm.pdf(x_fill, p_amostral, erro_padrao), color='green', alpha=0.2, label=f'IC {nivel_confianca*100:.0f}%')
    
    ax.axvline(p_amostral, color='darkgreen', linestyle='--', label=f'Prop. = {p_amostral}')
    ax.set_title(f"Distribuição da Proporção Amostral (Normal)")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    intervalo_confianca_proporcao(
        p_amostral = 0.6,        # proporção amostral (p̂)
        n = 100,                 # tamanho da amostra (n)
        nivel_confianca = 0.95   # nível de confiança
    )
