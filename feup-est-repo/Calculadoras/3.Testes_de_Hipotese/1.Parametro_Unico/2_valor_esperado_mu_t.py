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

def teste_t_media_uma_amostra(
    media_amostral = 10.5,        # média amostral observada (x̄)
    n = 15,                       # tamanho da amostra (n)
    mu0 = 10.0,                   # média hipotética (H0: μ = mu0)
    s = 2.0,                      # desvio padrão amostral (s)
    alfa = 0.05,                  # nível de significância
    tipo_teste = 'duas_caudas',   # 'duas_caudas', 'cauda_esquerda' ou 'cauda_direita'
    mu_alternativo = None,        # μ sob Ha para cálculo de poder
    show_plot = True              # se deve exibir o gráfico
):
    """
    Executa o Teste t para a média de uma amostra com σ desconhecido.
    """
    df = n - 1
    erro_padrao = s / np.sqrt(n)
    t_stat = (media_amostral - mu0) / erro_padrao
    
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        t_crit_inf = stats.t.ppf(alfa/2, df)
        t_crit_sup = stats.t.ppf(1 - alfa/2, df)
        t_crit = (t_crit_inf, t_crit_sup)
    elif tipo_teste == 'cauda_esquerda':
        p_valor = stats.t.cdf(t_stat, df)
        t_crit = stats.t.ppf(alfa, df)
    else: # cauda_direita
        p_valor = 1 - stats.t.cdf(t_stat, df)
        t_crit = stats.t.ppf(1 - alfa, df)
        
    rejeitar_h0 = p_valor < alfa

    # Cálculo da Potência
    power = None
    if mu_alternativo is not None:
        ncp = (mu_alternativo - mu0) / erro_padrao
        if tipo_teste == 'duas_caudas':
            power = stats.nct.cdf(t_crit[0], df, ncp) + stats.nct.sf(t_crit[1], df, ncp)
        elif tipo_teste == 'cauda_esquerda':
            power = stats.nct.cdf(t_crit, df, ncp)
        else:
            power = stats.nct.sf(t_crit, df, ncp)
    
    print(f"📊 TESTE t PARA A MÉDIA (μ)")
    print(f"H0: μ = {mu0} | Ha: μ {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {mu0}")
    print(f"Graus de Liberdade: {df}")
    print(f"Estatística t: {t_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    print(f"Valor Crítico: {t_crit}")
    if power is not None:
        print(f"Potência do Teste (1-β) para μ={mu_alternativo}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-4, 4, 1000)
    y = stats.t.pdf(x, df)
    ax.plot(x, y, 'r-', lw=2)
    
    if tipo_teste == 'duas_caudas':
        x_inf = np.linspace(-4, t_crit[0], 100)
        x_sup = np.linspace(t_crit[1], 4, 100)
        ax.fill_between(x_inf, stats.t.pdf(x_inf, df), color='red', alpha=0.5, label='Região de Rejeição')
        ax.fill_between(x_sup, stats.t.pdf(x_sup, df), color='red', alpha=0.5)
    elif tipo_teste == 'cauda_esquerda':
        x_fill = np.linspace(-4, t_crit, 100)
        ax.fill_between(x_fill, stats.t.pdf(x_fill, df), color='red', alpha=0.5, label='Região de Rejeição')
    else:
        x_fill = np.linspace(t_crit, 4, 100)
        ax.fill_between(x_fill, stats.t.pdf(x_fill, df), color='red', alpha=0.5, label='Região de Rejeição')
        
    ax.axvline(t_stat, color='black', linestyle='--', lw=2, label=f't observado = {t_stat:.2f}')
    ax.set_title(f"Distribuição t-Student (df={df})")
    ax.legend()
    if show_plot:
        plt.show()
    
    return {'estatistica_teste': t_stat, 'p_valor': p_valor, 'hipotese_rejeitada': rejeitar_h0, 'alfa': alfa, 'tipo_teste': tipo_teste, 'valor_critico': t_crit, 'power': power, 'graus_de_liberdade': df}

if __name__ == "__main__":
    teste_t_media_uma_amostra(
        media_amostral = 10.5,    # média amostral observada (x̄)
        n = 15,                   # tamanho da amostra (n)
        mu0 = 10.0,               # média hipotética (H0: μ = mu0)
        s = 2.0,                  # desvio padrão amostral (s)
        alfa = 0.05,              # nível de significância (α)
        tipo_teste = 'duas_caudas',# tipo: 'duas_caudas', 'cauda_esquerda' ou 'cauda_direita'
        mu_alternativo = 11.5,    # valor de μ sob Ha para cálculo de poder (opcional)
        show_plot = True          # exibir gráfico da distribuição t
    )
