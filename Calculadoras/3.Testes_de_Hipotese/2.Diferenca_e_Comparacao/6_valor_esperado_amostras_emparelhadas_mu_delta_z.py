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

def teste_z_amostras_emparelhadas(
    media_diff = 2.5,             # média das diferenças observadas (d̄)
    n = 40,                       # n > 30 (grande dimensão)
    sigma_d = 1.5,                # desvio padrão das diferenças (conhecido ou aproximado por s)
    diff0 = 0.0,                  # H0: μΔ = diff0
    alfa = 0.05,
    tipo_teste = 'duas_caudas',
    diff_alternativa = None       # Diferença real sob Ha para cálculo de poder
):
    """
    Executa o Teste Z para a média das diferenças de amostras emparelhadas.
    Utilizado para amostras de grande dimensão (N >= 30) conforme o quadro resumo.
    """
    erro_padrao = sigma_d / np.sqrt(n)
    z_stat = (media_diff - diff0) / erro_padrao
    
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        z_crit = stats.norm.ppf(1 - alfa/2)
        z_crit_range = (-z_crit, z_crit)
    elif tipo_teste == 'cauda_esquerda':
        p_valor = stats.norm.cdf(z_stat)
        z_crit_range = stats.norm.ppf(alfa)
    else: # cauda_direita
        p_valor = 1 - stats.norm.cdf(z_stat)
        z_crit_range = stats.norm.ppf(1 - alfa)
        
    rejeitar_h0 = p_valor < alfa

    # Cálculo da Potência
    power = None
    if diff_alternativa is not None:
        ncp = (diff_alternativa - diff0) / erro_padrao
        if tipo_teste == 'duas_caudas':
            power = stats.norm.cdf(z_crit_range[0] - ncp) + (1 - stats.norm.cdf(z_crit_range[1] - ncp))
        elif tipo_teste == 'cauda_esquerda':
            power = stats.norm.cdf(z_crit_range - ncp)
        else:
            power = 1 - stats.norm.cdf(z_crit_range - ncp)
    
    print(f"📊 TESTE Z PARA AMOSTRAS EMPARELHADAS (μΔ - Amostra Grande)")
    print(f"H0: μΔ = {diff0} | Ha: μΔ {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {diff0}")
    print(f"Estatística Z: {z_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    if power is not None:
        print(f"Potência do Teste (1-β) para Δ={diff_alternativa}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x)
    ax.plot(x, y, color='darkred', lw=2)
    
    if tipo_teste == 'duas_caudas':
        ax.fill_between(x[x < z_crit_range[0]], stats.norm.pdf(x[x < z_crit_range[0]]), color='red', alpha=0.5, label='Região de Rejeição')
        ax.fill_between(x[x > z_crit_range[1]], stats.norm.pdf(x[x > z_crit_range[1]]), color='red', alpha=0.5)
    elif tipo_teste == 'cauda_esquerda':
        ax.fill_between(x[x < z_crit_range], stats.norm.pdf(x[x < z_crit_range]), color='red', alpha=0.5, label='Região de Rejeição')
    else:
        ax.fill_between(x[x > z_crit_range], stats.norm.pdf(x[x > z_crit_range]), color='red', alpha=0.5, label='Região de Rejeição')
        
    ax.axvline(z_stat, color='black', linestyle='--', lw=2, label=f'Z observado = {z_stat:.2f}')
    ax.set_title("Amostras Emparelhadas (Amostra Grande) - Distribuição Normal Z")
    ax.legend()
    plt.show()
    
    return {'z_stat': z_stat, 'p_valor': p_valor, 'rejeitar_h0': rejeitar_h0}

if __name__ == "__main__":
    teste_z_amostras_emparelhadas(
        media_diff = 2.5, n = 40, sigma_d = 1.5
    )
