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

def teste_z_media_uma_amostra(
    media_amostral = 10.5,        # média observada na amostra (x̄)
    n = 30,                       # tamanho da amostra (n)
    mu0 = 10.0,                   # média hipotética (H0: μ = mu0)
    sigma = 2.0,                  # desvio padrão populacional (σ) conhecido
    alfa = 0.05,                  # nível de significância
    tipo_teste = 'duas_caudas',   # 'duas_caudas', 'cauda_esquerda' ou 'cauda_direita'
    mu_alternativo = None,        # μ sob Ha para cálculo de poder (ex: 11.0)
    show_plot = True              # se deve exibir o gráfico
):
    """
    Executa o Teste Z para a média de uma amostra com σ conhecido.
    """
    # Cálculo da estatística de teste
    erro_padrao = sigma / np.sqrt(n)
    z_stat = (media_amostral - mu0) / erro_padrao
    
    # P-valor e Valor Crítico
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
    
    # Cálculo da Potência (Power = 1 - Beta) se mu_alternativo for fornecido
    power = None
    if mu_alternativo is not None:
        # Distância em desvios padrão (Efeito)
        efeito = (mu_alternativo - mu0) / sigma
        # Para duas caudas, a potência é a soma das probabilidades nas caudas da nova distribuição
        if tipo_teste == 'duas_caudas':
            z_crit_inf = stats.norm.ppf(alfa/2)
            z_crit_sup = stats.norm.ppf(1 - alfa/2)
            ncp = (mu_alternativo - mu0) / (sigma / np.sqrt(n))
            power = stats.norm.cdf(z_crit_inf - ncp) + (1 - stats.norm.cdf(z_crit_sup - ncp))
        elif tipo_teste == 'cauda_esquerda':
            z_crit = stats.norm.ppf(alfa)
            ncp = (mu_alternativo - mu0) / (sigma / np.sqrt(n))
            power = stats.norm.cdf(z_crit - ncp)
        else:
            z_crit = stats.norm.ppf(1 - alfa)
            ncp = (mu_alternativo - mu0) / (sigma / np.sqrt(n))
            power = 1 - stats.norm.cdf(z_crit - ncp)

    print(f"📊 TESTE Z PARA A MÉDIA (μ)")
    print(f"H0: μ = {mu0} | Ha: μ {'≠' if tipo_teste=='duas_caudas' else '<' if tipo_teste=='cauda_esquerda' else '>'} {mu0}")
    print(f"Estatística Z: {z_stat:.4f}")
    print(f"P-valor: {p_valor:.4f}")
    print(f"Valor Crítico: {z_crit}")
    if power is not None:
        print(f"Potência do Teste (1-β) para μ={mu_alternativo}: {power:.4f}")
    print(f"Resultado: {'❌ REJEITAR H0' if rejeitar_h0 else '✅ NÃO REJEITAR H0'}")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x)
    ax.plot(x, y, 'b-', lw=2)
    
    # Regiões de Rejeição
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
    ax.set_title(f"Distribuição Normal Padrão - {teste_nome if 'teste_nome' in locals() else 'Teste Z'}")
    ax.legend()
    if show_plot:
        plt.show()
    
    return {'estatistica_teste': z_stat, 'p_valor': p_valor, 'hipotese_rejeitada': rejeitar_h0, 'alfa': alfa, 'tipo_teste': tipo_teste, 'valor_critico': z_crit, 'power': power}

if __name__ == "__main__":
    teste_z_media_uma_amostra(
        media_amostral = 10.5,    # média observada na amostra (x̄)
        n = 30,                   # tamanho da amostra (n)
        mu0 = 10.0,               # média hipotética (H0: μ = mu0)
        sigma = 2.0,              # desvio padrão populacional (σ) conhecido
        alfa = 0.05,              # nível de significância (α)
        tipo_teste = 'duas_caudas',# tipo: 'duas_caudas', 'cauda_esquerda', 'cauda_direita'
        mu_alternativo = 11.0,    # valor de μ sob Ha para cálculo de poder (opcional)
        show_plot = True          # exibir gráfico de regiões de rejeição
    )
