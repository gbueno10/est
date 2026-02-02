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

def teste_z_proporcao_uma_amostra(
    p_amostral = 0.65,             # proporção observada na amostra (p̂)
    n = 100,                       # tamanho da amostra (n)
    p0 = 0.50,                     # proporção hipotética (H0: p = p0)
    alfa = 0.05,                   # nível de significância
    tipo_teste = 'duas_caudas'     # 'duas_caudas', 'cauda_esquerda' ou 'cauda_direita'
):
    """
    Executa o Teste Z para a proporção de uma amostra.
    """
    # Cálculo da estatística de teste (usando p0 sob H0)
    erro_padrao = np.sqrt((p0 * (1 - p0)) / n)
    z_stat = (p_amostral - p0) / erro_padrao
    
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
    
    print(f"📊 TESTE Z PARA PROPORÇÃO (p)")
    print(f"H0: p = {p0} | Ha: p {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {p0}")
    print(f"Estatística Z: {z_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    print(f"Valor Crítico: {z_crit}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x)
    ax.plot(x, y, color='green', lw=2)
    
    if tipo_teste == 'duas_caudas':
        x_inf = np.linspace(-4, z_crit[0], 100)
        x_sup = np.linspace(z_crit[1], 4, 100)
        ax.fill_between(x_inf, stats.norm.pdf(x_inf), color='red', alpha=0.5, label='Região de Rejeição')
        ax.fill_between(x_sup, stats.norm.pdf(x_sup), color='red', alpha=0.5)
    elif tipo_teste == 'cauda_esquerda':
        x_fill = np.linspace(-4, z_crit, 100)
        ax.fill_between(x_fill, stats.norm.pdf(x_fill), color='red', alpha=0.5, label='Região de Rejeição')
    else:
        x_fill = np.linspace(z_crit, 4, 100)
        ax.fill_between(x_fill, stats.norm.pdf(x_fill), color='red', alpha=0.5, label='Região de Rejeição')
        
    ax.axvline(z_stat, color='black', linestyle='--', lw=2, label=f'Z observado = {z_stat:.2f}')
    ax.set_title("Distribuição Normal Padrão (Teste de Proporção)")
    ax.legend()
    plt.show()
    
    return {'z_stat': z_stat, 'p_valor': p_valor, 'rejeitar_h0': rejeitar_h0}

if __name__ == "__main__":
    teste_z_proporcao_uma_amostra(
        p_amostral = 0.65,        # proporção p̂
        n = 100,                  # n
        p0 = 0.50,                # H0: p = 0.5
        alfa = 0.05,              # significância
        tipo_teste = 'duas_caudas'# tipo
    )
