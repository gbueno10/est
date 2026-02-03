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

def teste_t_diferenca_medias(
    media1 = 12.5,                # média amostra A
    n1 = 15,                      # n de A
    s1 = 1.8,                     # s de A (desconhecido)
    media2 = 11.0,                # média amostra B
    n2 = 12,                      # n de B
    s2 = 2.2,                     # s de B (desconhecido)
    diff0 = 0.0,                  # H0: μA - μB = diff0
    variancias_iguais = True,     # True: pooled variance, False: Welch
    alfa = 0.05,
    tipo_teste = 'duas_caudas',
    diff_alternativa = None,      # Diferença real sob Ha para cálculo de poder
    show_plot = True              # se deve exibir o gráfico
):
    """
    Teste t para a diferença entre médias de duas populações independentes (σ desconhecidos).
    """
    if variancias_iguais:
        # Variância Agrupada (Pooled)
        sp2 = ((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2)
        erro_padrao = np.sqrt(sp2 * (1/n1 + 1/n2))
        df = n1 + n2 - 2
        metodo = "Variâncias Iguais (Agrupada)"
    else:
        # Welch-Satterthwaite
        erro_padrao = np.sqrt((s1**2 / n1) + (s2**2 / n2))
        gl_num = ((s1**2 / n1) + (s2**2 / n2))**2
        gl_den = ((s1**2 / n1)**2 / (n1 - 1)) + ((s2**2 / n2)**2 / (n2 - 1))
        df = gl_num / gl_den
        metodo = "Variâncias Desiguais (Welch)"
        
    t_stat = ((media1 - media2) - diff0) / erro_padrao
    
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
    if diff_alternativa is not None:
        ncp = (diff_alternativa - diff0) / erro_padrao
        if tipo_teste == 'duas_caudas':
            power = stats.nct.cdf(t_crit[0], df, ncp) + stats.nct.sf(t_crit[1], df, ncp)
        elif tipo_teste == 'cauda_esquerda':
            power = stats.nct.cdf(t_crit, df, ncp)
        else:
            power = stats.nct.sf(t_crit, df, ncp)
    
    print(f"📊 TESTE t PARA DIFERENÇA DE MÉDIAS (μA - μB)")
    print(f"Método: {metodo}")
    print(f"Graus de Liberdade: {df:.2f}")
    print(f"H0: μA - μB = {diff0} | Ha: μA - μB {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {diff0}")
    print(f"Estatística t: {t_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    if power is not None:
        print(f"Potência do Teste (1-β) para Δ={diff_alternativa}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-4, 4, 1000)
    y = stats.t.pdf(x, df)
    ax.plot(x, y, 'r-', lw=2)
    
    if tipo_teste == 'duas_caudas':
        ax.fill_between(x[x < t_crit[0]], stats.t.pdf(x[x < t_crit[0]], df), color='red', alpha=0.5, label='Região de Rejeição')
        ax.fill_between(x[x > t_crit[1]], stats.t.pdf(x[x > t_crit[1]], df), color='red', alpha=0.5)
    elif tipo_teste == 'cauda_esquerda':
        ax.fill_between(x[x < t_crit], stats.t.pdf(x[x < t_crit], df), color='red', alpha=0.5, label='Região de Rejeição')
    else:
        ax.fill_between(x[x > t_crit], stats.t.pdf(x[x > t_crit], df), color='red', alpha=0.5, label='Região de Rejeição')
        
    ax.axvline(t_stat, color='black', linestyle='--', lw=2, label=f't observado = {t_stat:.2f}')
    ax.set_title(f"Diferença de Valores Esperados (μA - μB) - Distribuição t (df={df:.1f})")
    ax.legend()
    if show_plot:
        plt.show()
    
    return {'t_stat': t_stat, 'p_valor': p_valor, 'rejeitar_h0': rejeitar_h0}

if __name__ == "__main__":
    teste_t_diferenca_medias(
        media1 = 12.5,            # média amostra A
        n1 = 15,                  # n de A
        s1 = 1.8,                 # desvio padrão amostral de A (s1)
        media2 = 11.0,            # média amostra B
        n2 = 12,                  # n de B
        s2 = 2.2,                 # desvio padrão amostral de B (s2)
        diff0 = 0.0,              # diferença hipotética (H0: μA - μB = diff0)
        variancias_iguais = True, # True: variâncias iguais (agrupada), False: Welch
        alfa = 0.05,              # nível de significância (α)
        tipo_teste = 'duas_caudas',# tipo: 'duas_caudas', 'cauda_esquerda', 'cauda_direita'
        diff_alternativa = 1.0,   # diferença real sob Ha para cálculo de poder (opcional)
        show_plot = True          # exibir gráfico da distribuição t
    )
