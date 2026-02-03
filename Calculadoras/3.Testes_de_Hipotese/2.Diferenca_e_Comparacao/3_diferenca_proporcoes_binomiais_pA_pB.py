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

def teste_z_diferenca_proporcoes(
    p1 = 0.60,                    # proporção amostra A
    n1 = 100,                     # n de A
    p2 = 0.50,                    # proporção amostra B
    n2 = 120,                     # n de B
    diff0 = 0.0,                  # H0: pA - pB = diff0
    alfa = 0.05,
    tipo_teste = 'duas_caudas',
    diff_alternativa = None,      # Diferença real sob Ha para cálculo de poder
    show_plot = True              # se deve exibir o gráfico
):
    """
    Teste Z para a diferença entre proporções binomiais de duas populações independentes.
    """
    if diff0 == 0:
        # Se H0: pA = pB, usamos a proporção agrupada
        p_pooled = (p1 * n1 + p2 * n2) / (n1 + n2)
        erro_padrao = np.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
    else:
        # Se H0: pA - pB = d, usamos proporções individuais
        erro_padrao = np.sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))
        
    z_stat = ((p1 - p2) - diff0) / erro_padrao
    
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
        # Erro padrão sob Ha
        sigma_alt = np.sqrt((p1*(1-p1)/n1) + (p2*(1-p2)/n2))
        if tipo_teste == 'duas_caudas':
            p_diff_crit_inf = diff0 + z_crit_range[0] * erro_padrao
            p_diff_crit_sup = diff0 + z_crit_range[1] * erro_padrao
            power = stats.norm.cdf((p_diff_crit_inf - diff_alternativa)/sigma_alt) + \
                    (1 - stats.norm.cdf((p_diff_crit_sup - diff_alternativa)/sigma_alt))
        elif tipo_teste == 'cauda_esquerda':
            p_diff_crit = diff0 + z_crit_range * erro_padrao
            power = stats.norm.cdf((p_diff_crit - diff_alternativa)/sigma_alt)
        else:
            p_diff_crit = diff0 + z_crit_range * erro_padrao
            power = 1 - stats.norm.cdf((p_diff_crit - diff_alternativa)/sigma_alt)
    
    print(f"📊 TESTE Z PARA DIFERENÇA DE PROPORÇÕES (pA - pB)")
    print(f"H0: pA - pB = {diff0} | Ha: pA - pB {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {diff0}")
    print(f"Estatística Z: {z_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    if power is not None:
        print(f"Potência do Teste (1-β) para Δ={diff_alternativa}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x)
    ax.plot(x, y, color='purple', lw=2)
    
    if tipo_teste == 'duas_caudas':
        ax.fill_between(x[x < z_crit_range[0]], stats.norm.pdf(x[x < z_crit_range[0]]), color='red', alpha=0.5, label='Região de Rejeição')
        ax.fill_between(x[x > z_crit_range[1]], stats.norm.pdf(x[x > z_crit_range[1]]), color='red', alpha=0.5)
    elif tipo_teste == 'cauda_esquerda':
        ax.fill_between(x[x < z_crit_range], stats.norm.pdf(x[x < z_crit_range]), color='red', alpha=0.5, label='Região de Rejeição')
    else:
        ax.fill_between(x[x > z_crit_range], stats.norm.pdf(x[x > z_crit_range]), color='red', alpha=0.5, label='Região de Rejeição')
        
    ax.axvline(z_stat, color='black', linestyle='--', lw=2, label=f'Z observado = {z_stat:.2f}')
    ax.set_title("Diferença entre Proporções Binomiais (pA - pB)")
    ax.legend()
    if show_plot:
        plt.show()
    
    return {
        'estatistica_teste': z_stat,
        'p_valor': p_valor,
        'hipotese_rejeitada': rejeitar_h0,
        'alfa': alfa,
        'tipo_teste': tipo_teste,
        'valor_critico': z_crit_range,
        'power': power
    }

if __name__ == "__main__":
    teste_z_diferenca_proporcoes(
        p1 = 0.60, n1 = 100,
        p2 = 0.50, n2 = 120,
        # show_plot = True        # Descomente para ver o gráfico
    )
