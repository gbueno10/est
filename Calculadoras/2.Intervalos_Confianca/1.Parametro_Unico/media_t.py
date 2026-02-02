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

def intervalo_confianca_media_t(
    media_amostral = 10.5,        # média amostral (x̄)
    desvio_padrao_amostral = 2.0, # desvio padrão amostral (s)
    n = 15,                       # tamanho da amostra (n)
    nivel_confianca = 0.95        # nível de confiança (1-α)
):
    """
    Calcula o IC para a média de uma população com σ desconhecido e n pequeno.
    """
    df = n - 1
    alfa = 1 - nivel_confianca
    t_critico = stats.t.ppf(1 - alfa/2, df)
    erro_padrao = desvio_padrao_amostral / np.sqrt(n)
    margem_erro = t_critico * erro_padrao
    
    inferior = media_amostral - margem_erro
    superior = media_amostral + margem_erro
    
    print(f"📊 INTERVALO DE CONFIANÇA t PARA A MÉDIA")
    print(f"Graus de Liberdade: {df}")
    print(f"t crítico: {t_critico:.4f}")
    print(f"Margem de Erro: {margem_erro:.4f}")
    print(f"IC: [{inferior:.4f}, {superior:.4f}]")
    
    # Visualização (Escalando a dist t para os valores reais da média)
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(media_amostral - 4*erro_padrao, media_amostral + 4*erro_padrao, 1000)
    # scipy.stats.t(df, loc, scale)
    dist_t = stats.t(df, loc=media_amostral, scale=erro_padrao)
    y = dist_t.pdf(x)
    ax.plot(x, y, 'r-')
    
    x_fill = np.linspace(inferior, superior, 1000)
    ax.fill_between(x_fill, dist_t.pdf(x_fill), color='red', alpha=0.2, label=f'IC {nivel_confianca*100:.0f}%')
    
    ax.axvline(media_amostral, color='black', linestyle='--', label=f'Média = {media_amostral}')
    ax.set_title(f"Distribuição Amostral da Média (IC t)")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    intervalo_confianca_media_t(
        media_amostral = 10.5,         # média amostral (x̄)
        desvio_padrao_amostral = 2.0,  # desvio padrão amostral (s)
        n = 15,                        # tamanho da amostra (n)
        nivel_confianca = 0.95         # nível de confiança
    )
