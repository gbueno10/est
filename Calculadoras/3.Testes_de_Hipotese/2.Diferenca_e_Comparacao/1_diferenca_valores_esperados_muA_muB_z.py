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

def teste_z_diferenca_medias(
    media1 = 15.0,                # média da amostra A (x̄A)
    n1 = 40,                      # n da amostra A
    sigma1 = 2.5,                 # σ de A (conhecido)
    media2 = 13.5,                # média da amostra B (x̄B)
    n2 = 35,                      # n da amostra B
    sigma2 = 3.0,                 # σ de B (conhecido)
    diff0 = 0.0,                  # diferença hipotética (H0: μA - μB = diff0)
    alfa = 0.05,                  # significância
    tipo_teste = 'duas_caudas',   # tipo
    diff_alternativa = None       # diferença real sob Ha para cálculo de poder
):
    """
    Teste Z para a diferença entre médias de duas populações independentes (σ conhecidos).
    """
    erro_padrao = np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    z_stat = ((media1 - media2) - diff0) / erro_padrao
    
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        z_crit_inf = stats.norm.ppf(alfa/2)
        z_crit_sup = stats.norm.ppf(1 - alfa/2)
        z_crit = (z_crit_inf, z_crit_sup)
    elif tipo_teste == 'cauda_esquerda':
        p_valor = stats.norm.cdf(z_stat)
        z_crit = stats.norm.ppf(alfa)
    else: # cauda_direita
        p_valor = 1 - stats.norm.cdf(z_stat)
        z_crit = stats.norm.ppf(1 - alfa)
        
    rejeitar_h0 = p_valor < alfa

    # Cálculo da Potência
    power = None
    if diff_alternativa is not None:
        ncp = (diff_alternativa - diff0) / erro_padrao
        if tipo_teste == 'duas_caudas':
            power = stats.norm.cdf(z_crit[0] - ncp) + (1 - stats.norm.cdf(z_crit[1] - ncp))
        elif tipo_teste == 'cauda_esquerda':
            power = stats.norm.cdf(z_crit - ncp)
        else:
            power = 1 - stats.norm.cdf(z_crit - ncp)
    
    print(f"📊 TESTE Z PARA DIFERENÇA DE MÉDIAS (μA - μB)")
    print(f"H0: μA - μB = {diff0} | Ha: μA - μB {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {diff0}")
    print(f"Estatística Z: {z_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    if power is not None:
        print(f"Potência do Teste (1-β) para Δ={diff_alternativa}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x)
    ax.plot(x, y, 'b-', lw=2)
    
    if tipo_teste == 'duas_caudas':
        ax.fill_between(x[x < z_crit[0]], stats.norm.pdf(x[x < z_crit[0]]), color='red', alpha=0.5, label='Região de Rejeição')
        ax.fill_between(x[x > z_crit[1]], stats.norm.pdf(x[x > z_crit[1]]), color='red', alpha=0.5)
    elif tipo_teste == 'cauda_esquerda':
        ax.fill_between(x[x < z_crit], stats.norm.pdf(x[x < z_crit]), color='red', alpha=0.5, label='Região de Rejeição')
    else:
        ax.fill_between(x[x > z_crit], stats.norm.pdf(x[x > z_crit]), color='red', alpha=0.5, label='Região de Rejeição')
        
    ax.axvline(z_stat, color='black', linestyle='--', lw=2, label=f'Z observado = {z_stat:.2f}')
    ax.set_title("Diferença de Valores Esperados (μA - μB) - Distribuição Normal Padrão")
    ax.legend()
    plt.show()
    
    return {'z_stat': z_stat, 'p_valor': p_valor, 'rejeitar_h0': rejeitar_h0}

if __name__ == "__main__":
    teste_z_diferenca_medias(
        media1 = 15.0, n1 = 40, sigma1 = 2.5,
        media2 = 13.5, n2 = 35, sigma2 = 3.0,
        diff0 = 0.0, alfa = 0.05, tipo_teste = 'duas_caudas'
    )
