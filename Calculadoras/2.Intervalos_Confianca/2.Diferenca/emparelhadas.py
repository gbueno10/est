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

def intervalo_confianca_amostras_emparelhadas(
    diferencas = None,            # array ou lista com as diferenças (antes - depois)
    media_diff = 2.5,             # média das diferenças (se 'diferencas' for None)
    std_diff = 1.2,               # desvio padrão das diferenças (se 'diferencas' for None)
    n = 10,                       # tamanho da amostra
    nivel_confianca = 0.95        # nível de confiança (1-α)
):
    """
    IC para a média das diferenças (μΔ) em amostras emparelhadas (antes/depois).
    Calcula como um IC de uma única amostra (t-Student) sobre as diferenças.
    """
    if diferencas is not None:
        diferencas = np.array(diferencas)
        media_diff = np.mean(diferencas)
        std_diff = np.std(diferencas, ddof=1)
        n = len(diferencas)
    
    df = n - 1
    alfa = 1 - nivel_confianca
    t_critico = stats.t.ppf(1 - alfa/2, df)
    erro_padrao = std_diff / np.sqrt(n)
    margem_erro = t_critico * erro_padrao
    
    inferior = media_diff - margem_erro
    superior = media_diff + margem_erro
    
    print(f"📊 IC PARA AMOSTRAS EMPARELHADAS (Média das Diferenças)")
    print(f"n: {n} | Graus de Liberdade: {df}")
    print(f"Média das Diferenças (d̄): {media_diff:.4f}")
    print(f"Desvio Padrão das Diff (Sd): {std_diff:.4f}")
    print(f"t crítico: {t_critico:.4f}")
    print(f"IC (μΔ): [{inferior:.4f}, {superior:.4f}]")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(media_diff - 4*erro_padrao, media_diff + 4*erro_padrao, 1000)
    dist_t = stats.t(df, loc=media_diff, scale=erro_padrao)
    y = dist_t.pdf(x)
    
    ax.plot(x, y, 'm-')
    ax.fill_between(x[ (x >= inferior) & (x <= superior) ], 
                    dist_t.pdf(x[ (x >= inferior) & (x <= superior) ]),
                    color='magenta', alpha=0.2, label=f'IC {nivel_confianca*100:.0f}%')
    
    ax.axvline(0, color='black', linestyle='--', label='Zero (Sem efeito)')
    ax.axvline(media_diff, color='magenta', linestyle=':', label='Média das Diff')
    ax.set_title("Distribuição da Média das Diferenças (Amostras Emparelhadas)")
    ax.legend()
    plt.show()
    
    return inferior, superior

if __name__ == "__main__":
    # Exemplo: Notas antes e depois de um treinamento
    intervalo_confianca_amostras_emparelhadas(
        media_diff = 2.5,        # aumento médio de 2.5 pontos
        std_diff = 1.2,          # desvio padrão da melhora
        n = 10,                  # 10 alunos
        nivel_confianca = 0.95   # nível de confiança
    )
