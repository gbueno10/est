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

def teste_f_comparacao_variancias(
    var1 = 5.0,                   # variância amostra A (sA²)
    n1 = 20,                      # n de A
    var2 = 2.0,                   # variância amostra B (sB²)
    n2 = 15,                      # n de B
    alfa = 0.05,
    tipo_teste = 'duas_caudas',   # 'duas_caudas', 'cauda_esquerda' ou 'cauda_direita'
    razao_alternativa = None      # Razão real (σA²/σB²) sob Ha para cálculo de poder
):
    """
    Teste F para a comparação (razão) das variâncias de duas populações Normais.
    H0: σA² = σB²  (ou σA²/σB² = 1)
    """
    dfn = n1 - 1
    dfd = n2 - 1
    f_stat = var1 / var2
    
    if tipo_teste == 'duas_caudas':
        p_inf = stats.f.cdf(f_stat, dfn, dfd)
        p_sup = 1 - stats.f.cdf(f_stat, dfn, dfd)
        p_valor = 2 * min(p_inf, p_sup)
        f_crit_inf = stats.f.ppf(alfa/2, dfn, dfd)
        f_crit_sup = stats.f.ppf(1 - alfa/2, dfn, dfd)
        f_crit = (f_crit_inf, f_crit_sup)
    elif tipo_teste == 'cauda_esquerda':
        p_valor = stats.f.cdf(f_stat, dfn, dfd)
        f_crit = stats.f.ppf(alfa, dfn, dfd)
    else: # cauda_direita
        p_valor = 1 - stats.f.cdf(f_stat, dfn, dfd)
        f_crit = stats.f.ppf(1 - alfa, dfn, dfd)
        
    rejeitar_h0 = p_valor < alfa

    # Cálculo da Potência
    power = None
    if razao_alternativa is not None:
        if tipo_teste == 'duas_caudas':
            power = stats.f.cdf(f_crit[0] / razao_alternativa, dfn, dfd) + \
                    (1 - stats.f.cdf(f_crit[1] / razao_alternativa, dfn, dfd))
        elif tipo_teste == 'cauda_esquerda':
            power = stats.f.cdf(f_crit / razao_alternativa, dfn, dfd)
        else:
            power = 1 - stats.f.cdf(f_crit / razao_alternativa, dfn, dfd)
    
    print(f"📊 TESTE F PARA RAZÃO DE VARIÂNCIAS (σA² / σB²)")
    print(f"H0: σA² = σB² | Ha: σA² {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} σB²")
    print(f"Graus de Liberdade: Num={dfn}, Den={dfd}")
    print(f"Estatística F: {f_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    if power is not None:
        print(f"Potência do Teste (1-β) para razão={razao_alternativa}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x_max = max(f_stat * 1.5, stats.f.ppf(0.99, dfn, dfd))
    x = np.linspace(0.01, x_max, 1000)
    y = stats.f.pdf(x, dfn, dfd)
    ax.plot(x, y, color='teal', lw=2)
    
    if tipo_teste == 'duas_caudas':
        ax.fill_between(x[x < f_crit[0]], stats.f.pdf(x[x < f_crit[0]], dfn, dfd), color='red', alpha=0.5, label='Região de Rejeição')
        ax.fill_between(x[x > f_crit[1]], stats.f.pdf(x[x > f_crit[1]], dfn, dfd), color='red', alpha=0.5)
    elif tipo_teste == 'cauda_esquerda':
        ax.fill_between(x[x < f_crit], stats.f.pdf(x[x < f_crit], dfn, dfd), color='red', alpha=0.5, label='Região de Rejeição')
    else:
        ax.fill_between(x[x > f_crit], stats.f.pdf(x[x > f_crit], dfn, dfd), color='red', alpha=0.5, label='Região de Rejeição')
        
    ax.axvline(f_stat, color='black', linestyle='--', lw=2, label=f'F observado = {f_stat:.2f}')
    ax.set_title(f"Razão entre Variâncias (σA² / σB²) - Distribuição F (df1={dfn}, df2={dfd})")
    ax.legend()
    plt.show()
    
    return {'f_stat': f_stat, 'p_valor': p_valor, 'rejeitar_h0': rejeitar_h0}

if __name__ == "__main__":
    teste_f_comparacao_variancias(
        var1 = 5.0, n1 = 20,
        var2 = 2.0, n2 = 15
    )
