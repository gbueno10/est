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

def teste_qui_quadrado_variancia(
    var_amostral = 4.5,            # variância observada na amostra (s²)
    n = 20,                        # tamanho da amostra (n)
    sigma2_0 = 4.0,                # variância hipotética (H0: σ² = sigma2_0)
    alfa = 0.05,                   # nível de significância
    tipo_teste = 'duas_caudas',    # 'duas_caudas', 'cauda_esquerda' ou 'cauda_direita'
    sigma2_alternativo = None      # σ² sob Ha para cálculo de poder
):
    """
    Executa o Teste Qui-Quadrado para a variância populacional (população Normal).
    """
    df = n - 1
    chi_stat = (df * var_amostral) / sigma2_0
    
    if tipo_teste == 'duas_caudas':
        p_inf = stats.chi2.cdf(chi_stat, df)
        p_sup = 1 - stats.chi2.cdf(chi_stat, df)
        p_valor = 2 * min(p_inf, p_sup)
        chi_crit_inf = stats.chi2.ppf(alfa/2, df)
        chi_crit_sup = stats.chi2.ppf(1 - alfa/2, df)
        chi_crit = (chi_crit_inf, chi_crit_sup)
    elif tipo_teste == 'cauda_esquerda':
        p_valor = stats.chi2.cdf(chi_stat, df)
        chi_crit = stats.chi2.ppf(alfa, df)
    else: # cauda_direita
        p_valor = 1 - stats.chi2.cdf(chi_stat, df)
        chi_crit = stats.chi2.ppf(1 - alfa, df)
        
    rejeitar_h0 = p_valor < alfa

    # Cálculo da Potência (usando Qui-Quadrado Não Central)
    power = None
    if sigma2_alternativo is not None:
        lambda_val = (sigma2_alternativo / sigma2_0)
        # O poder é a prob de chi_stat estar na região crítica sob sigma2_alt
        # Ajustamos os pontos críticos pela razão das variâncias
        if tipo_teste == 'duas_caudas':
            power = stats.chi2.cdf(chi_crit[0] / lambda_val, df) + (1 - stats.chi2.cdf(chi_crit[1] / lambda_val, df))
        elif tipo_teste == 'cauda_esquerda':
            power = stats.chi2.cdf(chi_crit / lambda_val, df)
        else:
            power = 1 - stats.chi2.cdf(chi_crit / lambda_val, df)
    
    print(f"📊 TESTE QUI-QUADRADO PARA VARIANÇA (σ²)")
    print(f"H0: σ² = {sigma2_0} | Ha: σ² {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {sigma2_0}")
    print(f"Graus de Liberdade: {df}")
    print(f"Estatística χ²: {chi_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    if power is not None:
        print(f"Potência do Teste (1-β) para σ²={sigma2_alternativo}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x_max = max(chi_stat * 1.5, stats.chi2.ppf(0.99, df))
    x = np.linspace(0, x_max, 1000)
    y = stats.chi2.pdf(x, df)
    ax.plot(x, y, color='orange', lw=2)
    
    if tipo_teste == 'duas_caudas':
        x_inf = np.linspace(0, chi_crit[0], 100)
        x_sup = np.linspace(chi_crit[1], x_max, 100)
        ax.fill_between(x_inf, stats.chi2.pdf(x_inf, df), color='red', alpha=0.5, label='Região de Rejeição')
        ax.fill_between(x_sup, stats.chi2.pdf(x_sup, df), color='red', alpha=0.5)
    elif tipo_teste == 'cauda_esquerda':
        x_fill = np.linspace(0, chi_crit, 100)
        ax.fill_between(x_fill, stats.chi2.pdf(x_fill, df), color='red', alpha=0.5, label='Região de Rejeição')
    else:
        x_fill = np.linspace(chi_crit, x_max, 100)
        ax.fill_between(x_fill, stats.chi2.pdf(x_fill, df), color='red', alpha=0.5, label='Região de Rejeição')
        
    ax.axvline(chi_stat, color='black', linestyle='--', lw=2, label=f'χ² observado = {chi_stat:.2f}')
    ax.set_title(f"Distribuição Qui-Quadrado (df={df})")
    ax.legend()
    plt.show()
    
    return {'chi_stat': chi_stat, 'p_valor': p_valor, 'rejeitar_h0': rejeitar_h0}

if __name__ == "__main__":
    teste_qui_quadrado_variancia(
        var_amostral = 4.5,       # s²
        n = 20,                   # n
        sigma2_0 = 4.0,           # H0: sigma² = 4.0
        alfa = 0.05,              # significância
        tipo_teste = 'duas_caudas'# tipo
    )
