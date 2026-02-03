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

def intervalo_confianca_media_z(
    media_amostral = 10.5,        # média amostral (x̄)
    desvio_padrao_pop = 2.0,     # desvio padrão populacional (σ) conhecido
    n = 30,                       # tamanho da amostra (n)
    nivel_confianca = 0.95,       # nível de confiança (1-α)
    M = None                      # tamanho da população (M) para correção finita
):
    """
    Calcula o IC para a média de uma população com σ conhecido ou amostra grande.
    """
    alfa = 1 - nivel_confianca
    z_critico = stats.norm.ppf(1 - alfa/2)
    erro_padrao = desvio_padrao_pop / np.sqrt(n)

    # Fator de correção para população finita (se M fornecido e n > 5% de M)
    fpc = 1.0
    if M is not None:
        fpc = np.sqrt((M - n) / (M - 1))
        erro_padrao *= fpc

    margem_erro = z_critico * erro_padrao
    
    inferior = media_amostral - margem_erro
    superior = media_amostral + margem_erro
    
    print(f"📊 INTERVALO DE CONFIANÇA Z PARA A MÉDIA")
    print(f"Nível de Confiança: {nivel_confianca*100:.1f}%")
    print(f"Z crítico: {z_critico:.4f}")
    print(f"Margem de Erro: {margem_erro:.4f}")
    print(f"IC: [{inferior:.4f}, {superior:.4f}]")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(media_amostral - 4*erro_padrao, media_amostral + 4*erro_padrao, 1000)
    y = stats.norm.pdf(x, media_amostral, erro_padrao)
    ax.plot(x, y, 'b-')
    
    # Colorir área de confiança
    x_fill = np.linspace(inferior, superior, 1000)
    ax.fill_between(x_fill, stats.norm.pdf(x_fill, media_amostral, erro_padrao), color='blue', alpha=0.2, label=f'IC {nivel_confianca*100:.0f}%')
    
    ax.axvline(media_amostral, color='red', linestyle='--', label=f'Média = {media_amostral}')
    ax.set_title(f"Distribuição Amostral da Média (IC Z)")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    intervalo_confianca_media_z(
        media_amostral = 10.5,    # média amostral (x̄)
        desvio_padrao_pop = 2.0,  # desvio padrão populacional (σ) conhecido
        n = 30,                   # tamanho da amostra (n)
        nivel_confianca = 0.95,   # nível de confiança (1-α)
        M = 500                   # tamanho da população (M) para correção finita (opcional)
    )
