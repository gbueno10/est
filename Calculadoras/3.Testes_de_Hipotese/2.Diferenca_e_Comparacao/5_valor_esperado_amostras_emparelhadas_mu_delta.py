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

def teste_t_amostras_emparelhadas(
    media_diff = 2.5,             # média das diferenças observadas (d̄)
    n = 10,                       # número de pares
    sd = 1.2,                     # desvio padrão das diferenças (sd)
    diff0 = 0.0,                  # H0: μΔ = diff0
    alfa = 0.05,
    tipo_teste = 'duas_caudas',
    diff_alternativa = None       # Diferença real sob Ha para cálculo de poder
):
    """
    Teste t para a média das diferenças de amostras emparelhadas (dependentes).
    Equivale a um teste t de uma amostra sobre as diferenças.
    """
    df = n - 1
    erro_padrao = sd / np.sqrt(n)
    t_stat = (media_diff - diff0) / erro_padrao
    
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        t_crit = stats.t.ppf(1 - alfa/2, df)
        t_crit_range = (-t_crit, t_crit)
    elif tipo_teste == 'cauda_esquerda':
        p_valor = stats.t.cdf(t_stat, df)
        t_crit_range = stats.t.ppf(alfa, df)
    else: # cauda_direita
        p_valor = 1 - stats.t.cdf(t_stat, df)
        t_crit_range = stats.t.ppf(1 - alfa, df)
        
    rejeitar_h0 = p_valor < alfa

    # Cálculo da Potência
    power = None
    if diff_alternativa is not None:
        ncp = (diff_alternativa - diff0) / erro_padrao
        if tipo_teste == 'duas_caudas':
            power = stats.nct.cdf(t_crit_range[0], df, ncp) + stats.nct.sf(t_crit_range[1], df, ncp)
        elif tipo_teste == 'cauda_esquerda':
            power = stats.nct.cdf(t_crit_range, df, ncp)
        else:
            power = stats.nct.sf(t_crit_range, df, ncp)
    
    print(f"📊 TESTE t PARA AMOSTRAS EMPARELHADAS (μΔ)")
    print(f"H0: μΔ = {diff0} | Ha: μΔ {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {diff0}")
    print(f"Graus de Liberdade: {df}")
    print(f"Estatística t: {t_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    if power is not None:
        print(f"Potência do Teste (1-β) para Δ={diff_alternativa}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-4, 4, 1000)
    y = stats.t.pdf(x, df)
    ax.plot(x, y, color='magenta', lw=2)
    
    if tipo_teste == 'duas_caudas':
        ax.fill_between(x[x < t_crit_range[0]], stats.t.pdf(x[x < t_crit_range[0]], df), color='red', alpha=0.4, label='Região de Rejeição')
        ax.fill_between(x[x > t_crit_range[1]], stats.t.pdf(x[x > t_crit_range[1]], df), color='red', alpha=0.4)
    elif tipo_teste == 'cauda_esquerda':
        ax.fill_between(x[x < t_crit_range], stats.t.pdf(x[x < t_crit_range], df), color='red', alpha=0.4, label='Região de Rejeição')
    else:
        ax.fill_between(x[x > t_crit_range], stats.t.pdf(x[x > t_crit_range], df), color='red', alpha=0.4, label='Região de Rejeição')
        
    ax.axvline(t_stat, color='black', linestyle='--', lw=2, label=f't observado = {t_stat:.2f}')
    ax.set_title(f"Amostras Emparelhadas (Média das Diferenças μΔ) - Distribuição t (df={df})")
    ax.legend()
    plt.show()
    
    return {'t_stat': t_stat, 'p_valor': p_valor, 'rejeitar_h0': rejeitar_h0}

if __name__ == "__main__":
    teste_t_amostras_emparelhadas(
        media_diff = 2.5, n = 10, sd = 1.2
    )
