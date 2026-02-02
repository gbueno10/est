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

def intervalo_confianca_diferenca_medias_t(
    media1 = 15.0,                # média da amostra 1 (x̄1)
    media2 = 12.0,                # média da amostra 2 (x̄2)
    s1 = 3.0,                     # desvio padrão amostral 1 (s1)
    s2 = 2.5,                     # desvio padrão amostral 2 (s2)
    n1 = 15,                      # tamanho da amostra 1 (n1)
    n2 = 12,                      # tamanho da amostra 2 (n2)
    nivel_confianca = 0.95,       # nível de confiança (1-α)
    variancias_iguais = True      # pressuposto de variâncias iguais (homocedasticidade)
):
    """
    IC para a diferença de médias com variâncias desconhecidas (t-Student).
    """
    diff = media1 - media2
    alfa = 1 - nivel_confianca
    
    if variancias_iguais:
        # Variância Agrupada (Sp²)
        sp2 = ((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2)
        erro_padrao = np.sqrt(sp2 * (1/n1 + 1/n2))
        df = n1 + n2 - 2
        tipo_teste = "Variâncias Iguais (Agrupada)"
    else:
        # Welch's Satterthwaite (Variâncias Desiguais)
        erro_padrao = np.sqrt((s1**2 / n1) + (s2**2 / n2))
        gl_num = ((s1**2 / n1) + (s2**2 / n2))**2
        gl_den = ((s1**2 / n1)**2 / (n1 - 1)) + ((s2**2 / n2)**2 / (n2 - 1))
        df = gl_num / gl_den
        tipo_teste = "Variâncias Desiguais (Welch)"

    t_critico = stats.t.ppf(1 - alfa/2, df)
    margem_erro = t_critico * erro_padrao
    
    inferior = diff - margem_erro
    superior = diff + margem_erro
    
    print(f"📊 IC t PARA DIFERENÇA DE MÉDIAS (μ1 - μ2)")
    print(f"Método: {tipo_teste}")
    print(f"Graus de Liberdade: {df:.2f}")
    print(f"t crítico: {t_critico:.4f}")
    print(f"IC: [{inferior:.4f}, {superior:.4f}]")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(diff - 4*erro_padrao, diff + 4*erro_padrao, 1000)
    dist_t = stats.t(df, loc=diff, scale=erro_padrao)
    y = dist_t.pdf(x)
    ax.plot(x, y, 'r-')
    ax.fill_between(x[ (x >= inferior) & (x <= superior) ], 
                    dist_t.pdf(x[ (x >= inferior) & (x <= superior) ]),
                    color='red', alpha=0.2, label=f'IC {nivel_confianca*100:.0f}%')
    
    ax.axvline(0, color='gray', linestyle='--')
    ax.set_title(f"Diferença de Médias (μ1 - μ2) - {tipo_teste}")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    intervalo_confianca_diferenca_medias_t(
        media1 = 15.0,             # média amostra 1
        media2 = 12.0,             # média amostra 2
        s1 = 3.0,                  # desvio padrão amostral 1 (s1)
        s2 = 2.5,                  # desvio padrão amostral 2 (s2)
        n1 = 15,                   # n1
        n2 = 12,                   # n2
        nivel_confianca = 0.95,    # nível de confiança
        variancias_iguais = True   # variâncias populacionais iguais?
    )
