import numpy as np
import scipy.stats as st

print("Bibliotecas numpy e scipy.stats importadas com sucesso!")

# --- Funções para Testes Paramétricos (MANTIDAS ORIGINAIS) ---
def teste_qui_quadrado_variancia_uma_amostra_parametros(variancia_amostral, tamanho_amostra, variancia_populacional_hipotetica, tipo_teste='duas_caudas', alfa=0.05, variancia_populacional_alternativa=None):
    """Teste Qui-Quadrado para variância de uma amostra (parâmetros)."""
    n = tamanho_amostra
    s_quadrado = variancia_amostral
    sigma_quadrado_0 = variancia_populacional_hipotetica
    estatistica_teste = (n - 1) * s_quadrado / sigma_quadrado_0
    graus_de_liberdade = n - 1
    if tipo_teste == 'duas_caudas':
        p_valor_direita = st.chi2.sf(estatistica_teste, df=graus_de_liberdade)
        p_valor_esquerda = st.chi2.cdf(estatistica_teste, df=graus_de_liberdade)
        p_valor = 2 * min(p_valor_direita, p_valor_esquerda)
        valor_critico_superior = st.chi2.ppf(1 - alfa/2, df=graus_de_liberdade)
        valor_critico_inferior = st.chi2.ppf(alfa/2, df=graus_de_liberdade)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.chi2.cdf(estatistica_teste, df=graus_de_liberdade)
        valor_critico = st.chi2.ppf(alfa, df=graus_de_liberdade)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.chi2.sf(estatistica_teste, df=graus_de_liberdade)
        valor_critico = st.chi2.ppf(1 - alfa, df=graus_de_liberdade)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if variancia_populacional_alternativa is not None:
        non_centrality_parameter = (n - 1) * (variancia_populacional_alternativa / sigma_quadrado_0) 
        if tipo_teste == 'duas_caudas':
            valor_critico_inf, valor_critico_sup = valor_critico
            power_cauda_inferior = st.ncx2.cdf(valor_critico_inf, df=graus_de_liberdade, nc=non_centrality_parameter)
            power_cauda_superior = st.ncx2.sf(valor_critico_sup, df=graus_de_liberdade, nc=non_centrality_parameter)
            power = power_cauda_inferior + power_cauda_superior
        elif tipo_teste == 'cauda_esquerda':
            power = st.ncx2.cdf(valor_critico, df=graus_de_liberdade, nc=non_centrality_parameter)
        elif tipo_teste == 'cauda_direita':
            power = st.ncx2.sf(valor_critico, df=graus_de_liberdade, nc=non_centrality_parameter)

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'graus_de_liberdade': graus_de_liberdade, 'valor_critico': valor_critico, 'power': power}


def teste_f_variancia_duas_amostras_parametros(variancia_amostral1, tamanho_amostra1, variancia_amostral2, tamanho_amostra2, tipo_teste='duas_caudas', alfa=0.05, ratio_variancias_alternativo=None):
    """Teste F para variâncias de duas amostras (parâmetros)."""
    estatistica_teste = variancia_amostral1 / variancia_amostral2
    graus_de_liberdade_num = tamanho_amostra1 - 1
    graus_de_liberdade_den = tamanho_amostra2 - 1
    if tipo_teste == 'duas_caudas':
        p_valor_direita = st.f.sf(estatistica_teste, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den)
        p_valor_esquerda = st.f.cdf(estatistica_teste, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den)
        p_valor = 2 * min(p_valor_direita, p_valor_esquerda)
        valor_critico_superior = st.f.ppf(1 - alfa/2, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den)
        valor_critico_inferior = st.f.ppf(alfa/2, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.f.cdf(estatistica_teste, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den)
        valor_critico = st.f.ppf(alfa, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.f.sf(estatistica_teste, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den)
        valor_critico = st.f.ppf(1 - alfa, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if ratio_variancias_alternativo is not None:
        non_centrality_parameter = ratio_variancias_alternativo 
        if tipo_teste == 'duas_caudas':
            valor_critico_inf, valor_critico_sup = valor_critico
            power_cauda_inferior = st.ncf.cdf(valor_critico_inf, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den, nc=non_centrality_parameter)
            power_cauda_superior = st.ncf.sf(valor_critico_sup, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den, nc=non_centrality_parameter)
            power = power_cauda_inferior + power_cauda_superior
        elif tipo_teste == 'cauda_esquerda':
            power = st.ncf.cdf(valor_critico, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den, nc=non_centrality_parameter)
        elif tipo_teste == 'cauda_direita':
            power = st.ncf.sf(valor_critico, dfn=graus_de_liberdade_num, dfd=graus_de_liberdade_den, nc=non_centrality_parameter)

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'graus_de_liberdade_numerador': graus_de_liberdade_num, 'graus_de_liberdade_denominador': graus_de_liberdade_den, 'valor_critico': valor_critico, 'power': power}


def teste_z_media_uma_amostra_parametros(media_amostral, tamanho_amostra, media_populacional_hipotetica, desvio_padrao_populacional_conhecido, tipo_teste='duas_caudas', alfa=0.05, media_populacional_alternativa=None):
    """Teste Z para média de uma amostra (parâmetros)."""
    n = tamanho_amostra
    media_x_barra = media_amostral
    media_mu_0 = media_populacional_hipotetica
    sigma = desvio_padrao_populacional_conhecido
    estatistica_teste = (media_x_barra - media_mu_0) / (sigma / np.sqrt(n))
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * st.norm.sf(np.abs(estatistica_teste))
        valor_critico_superior = st.norm.ppf(1 - alfa/2)
        valor_critico_inferior = st.norm.ppf(alfa/2)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.norm.cdf(estatistica_teste)
        valor_critico = st.norm.ppf(alfa)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.norm.sf(estatistica_teste)
        valor_critico = st.norm.ppf(1 - alfa)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if media_populacional_alternativa is not None:
        efeito_tamanho_padronizado = (media_populacional_alternativa - media_populacional_hipotetica) / desvio_padrao_populacional_conhecido 
        if tipo_teste == 'duas_caudas':
            valor_critico_inf, valor_critico_sup = valor_critico
            power_cauda_inferior = st.norm.cdf(valor_critico_inf, loc=efeito_tamanho_padronizado * np.sqrt(tamanho_amostra)) 
            power_cauda_superior = st.norm.sf(valor_critico_sup, loc=efeito_tamanho_padronizado * np.sqrt(tamanho_amostra)) 
            power = power_cauda_inferior + power_cauda_superior
        elif tipo_teste == 'cauda_esquerda':
            power = st.norm.cdf(valor_critico, loc=efeito_tamanho_padronizado * np.sqrt(tamanho_amostra)) 
        elif tipo_teste == 'cauda_direita':
            power = st.norm.sf(valor_critico, loc=efeito_tamanho_padronizado * np.sqrt(tamanho_amostra)) 

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'valor_critico': valor_critico, 'power': power}


def teste_t_media_uma_amostra_parametros(media_amostral, tamanho_amostra, media_populacional_hipotetica, desvio_padrao_amostral, tipo_teste='duas_caudas', alfa=0.05, media_populacional_alternativa=None):
    """Teste t para média de uma amostra (parâmetros)."""
    n = tamanho_amostra
    media_x_barra = media_amostral
    media_mu_0 = media_populacional_hipotetica
    s = desvio_padrao_amostral
    estatistica_teste = (media_x_barra - media_mu_0) / (s / np.sqrt(n))
    graus_de_liberdade = n - 1
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * st.t.sf(np.abs(estatistica_teste), df=graus_de_liberdade)
        valor_critico_superior = st.t.ppf(1 - alfa/2, df=graus_de_liberdade)
        valor_critico_inferior = st.t.ppf(alfa/2, df=graus_de_liberdade)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.t.cdf(estatistica_teste, df=graus_de_liberdade)
        valor_critico = st.t.ppf(alfa, df=graus_de_liberdade)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.t.sf(estatistica_teste, df=graus_de_liberdade)
        valor_critico = st.t.ppf(1 - alfa, df=graus_de_liberdade)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if media_populacional_alternativa is not None:
        non_centrality_parameter = (media_populacional_alternativa - media_mu_0) / (s / np.sqrt(n)) 
        if tipo_teste == 'duas_caudas':
            t_crit_upper = st.t.ppf(1 - alfa/2, df=graus_de_liberdade)
            t_crit_lower = st.t.ppf(alfa/2, df=graus_de_liberdade)
            power_right_tail = st.nct.sf(t_crit_upper, df=graus_de_liberdade, nc=non_centrality_parameter)
            power_left_tail = st.nct.cdf(t_crit_lower, df=graus_de_liberdade, nc=non_centrality_parameter)
            power = power_right_tail + power_left_tail
        elif tipo_teste == 'cauda_esquerda':
            t_crit = valor_critico 
            power = st.nct.cdf(t_crit, df=graus_de_liberdade, nc=non_centrality_parameter)
        elif tipo_teste == 'cauda_direita':
            t_crit = valor_critico 
            power = st.nct.sf(t_crit, df=graus_de_liberdade, nc=non_centrality_parameter)

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'graus_de_liberdade': graus_de_liberdade, 'valor_critico': valor_critico, 'power': power}


def teste_z_media_duas_amostras_indep_parametros_conhecido(media_amostral1, tamanho_amostra1, media_amostral2, tamanho_amostra2, diferenca_medias_hipotetica, desvio_padrao_populacional1_conhecido, desvio_padrao_populacional2_conhecido, tipo_teste='duas_caudas', alfa=0.05, diferenca_medias_alternativa=None):
    """Teste Z para médias de duas amostras independentes (desvios padrão conhecidos)."""
    n1 = tamanho_amostra1
    n2 = tamanho_amostra2
    media_x_barra1 = media_amostral1
    media_x_barra2 = media_amostral2
    diferenca_mu_0 = diferenca_medias_hipotetica
    sigma1 = desvio_padrao_populacional1_conhecido
    sigma2 = desvio_padrao_populacional2_conhecido
    estatistica_teste = ((media_x_barra1 - media_x_barra2) - diferenca_mu_0) / np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * st.norm.sf(np.abs(estatistica_teste))
        valor_critico_superior = st.norm.ppf(1 - alfa/2)
        valor_critico_inferior = st.norm.ppf(alfa/2)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.norm.cdf(estatistica_teste)
        valor_critico = st.norm.ppf(alfa)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.norm.sf(estatistica_teste)
        valor_critico = st.norm.ppf(1 - alfa)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if diferenca_medias_alternativa is not None:
        variancia_erro_padrao = (sigma1**2 / n1) + (sigma2**2 / n2)
        efeito_tamanho_padronizado = (diferenca_medias_alternativa - diferenca_mu_0) / np.sqrt(variancia_erro_padrao) 
        if tipo_teste == 'duas_caudas':
            valor_critico_inf, valor_critico_sup = valor_critico
            power_cauda_inferior = st.norm.cdf(valor_critico_inf, loc=efeito_tamanho_padronizado) 
            power_cauda_superior = st.norm.sf(valor_critico_sup, loc=efeito_tamanho_padronizado) 
            power = power_cauda_inferior + power_cauda_superior
        elif tipo_teste == 'cauda_esquerda':
            power = st.norm.cdf(valor_critico, loc=efeito_tamanho_padronizado) 
        elif tipo_teste == 'cauda_direita':
            power = st.norm.sf(valor_critico, loc=efeito_tamanho_padronizado) 

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'valor_critico': valor_critico, 'power': power}


def teste_t_media_duas_amostras_indep_parametros(media_amostral1, tamanho_amostra1, desvio_padrao_amostral1, media_amostral2, tamanho_amostra2, desvio_padrao_amostral2, diferenca_medias_hipotetica=0, variancias_iguais=False, tipo_teste='duas_caudas', alfa=0.05, diferenca_medias_alternativa=None):
    """Teste t para médias de duas amostras independentes (desvios padrão desconhecidos)."""
    n1 = tamanho_amostra1
    n2 = tamanho_amostra2
    media_x_barra1 = media_amostral1
    media_x_barra2 = media_amostral2
    s1 = desvio_padrao_amostral1
    s2 = desvio_padrao_amostral2
    diferenca_mu_0 = diferenca_medias_hipotetica

    if variancias_iguais:
        variancia_agrupada = ((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2)
        estatistica_teste = ((media_x_barra1 - media_x_barra2) - diferenca_mu_0) / np.sqrt(variancia_agrupada * (1/n1 + 1/n2))
        graus_de_liberdade = n1 + n2 - 2
        desvio_padrao_agrupado = np.sqrt(variancia_agrupada)
    else: # Welch's t-test
        estatistica_teste = ((media_x_barra1 - media_x_barra2) - diferenca_mu_0) / np.sqrt((s1**2 / n1) + (s2**2 / n2))
        gl_num = ((s1**2 / n1) + (s2**2 / n2))**2
        gl_den = ((s1**2 / n1)**2 / (n1 - 1)) + ((s2**2 / n2)**2 / (n2 - 1))
        graus_de_liberdade = gl_num / gl_den
        desvio_padrao_agrupado = np.sqrt(((s1**2 / n1) + (s2**2 / n2)) * (n1 * n2) / (n1 + n2)) 

    if tipo_teste == 'duas_caudas':
        p_valor = 2 * st.t.sf(np.abs(estatistica_teste), df=graus_de_liberdade)
        valor_critico_superior = st.t.ppf(1 - alfa/2, df=graus_de_liberdade)
        valor_critico_inferior = st.t.ppf(alfa/2, df=graus_de_liberdade)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.t.cdf(estatistica_teste, df=graus_de_liberdade)
        valor_critico = st.t.ppf(alfa, df=graus_de_liberdade)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.t.sf(estatistica_teste, df=graus_de_liberdade)
        valor_critico = st.t.ppf(1 - alfa, df=graus_de_liberdade)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if diferenca_medias_alternativa is not None:
        efeito_tamanho_padronizado = (diferenca_medias_alternativa - diferenca_mu_0) / desvio_padrao_agrupado
        non_centrality_parameter = efeito_tamanho_padronizado 
        if tipo_teste == 'duas_caudas':
            valor_critico_inf, valor_critico_sup = valor_critico
            power_cauda_inferior = st.nct.cdf(valor_critico_inf, df=graus_de_liberdade, nc=non_centrality_parameter)
            power_cauda_superior = st.nct.sf(valor_critico_sup, df=graus_de_liberdade, nc=non_centrality_parameter)
            power = power_cauda_inferior + power_cauda_superior
        elif tipo_teste == 'cauda_esquerda':
            power = st.nct.cdf(valor_critico, df=graus_de_liberdade, nc=non_centrality_parameter)
        elif tipo_teste == 'cauda_direita':
            power = st.nct.sf(valor_critico, df=graus_de_liberdade, nc=non_centrality_parameter)

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'graus_de_liberdade': graus_de_liberdade, 'variancias_iguais': variancias_iguais, 'valor_critico': valor_critico, 'power': power}


def teste_t_media_amostras_pareadas_parametros(media_diferencas_amostral, tamanho_amostra, media_diferencas_hipotetica, desvio_padrao_diferencas_amostral, tipo_teste='duas_caudas', alfa=0.05, media_diferencas_alternativa=None):
    """Teste t para médias de amostras pareadas (parâmetros)."""
    n = tamanho_amostra
    media_d_barra = media_diferencas_amostral
    media_d_0 = media_diferencas_hipotetica
    sd = desvio_padrao_diferencas_amostral
    estatistica_teste = (media_d_barra - media_d_0) / (sd / np.sqrt(n))
    graus_de_liberdade = n - 1
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * st.t.sf(np.abs(estatistica_teste), df=graus_de_liberdade)
        valor_critico_superior = st.t.ppf(1 - alfa/2, df=graus_de_liberdade)
        valor_critico_inferior = st.t.ppf(alfa/2, df=graus_de_liberdade)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.t.cdf(estatistica_teste, df=graus_de_liberdade)
        valor_critico = st.t.ppf(alfa, df=graus_de_liberdade)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.t.sf(estatistica_teste, df=graus_de_liberdade)
        valor_critico = st.t.ppf(1 - alfa, df=graus_de_liberdade)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if media_diferencas_alternativa is not None:
        efeito_tamanho_padronizado = (media_diferencas_alternativa - media_d_0) / sd 
        non_centrality_parameter = efeito_tamanho_padronizado * np.sqrt(n) 
        if tipo_teste == 'duas_caudas':
            valor_critico_inf, valor_critico_sup = valor_critico
            power_cauda_inferior = st.nct.cdf(valor_critico_inf, df=graus_de_liberdade, nc=non_centrality_parameter)
            power_cauda_superior = st.nct.sf(valor_critico_sup, df=graus_de_liberdade, nc=non_centrality_parameter)
            power = power_cauda_inferior + power_cauda_superior
        elif tipo_teste == 'cauda_esquerda':
            power = st.nct.cdf(valor_critico, df=graus_de_liberdade, nc=non_centrality_parameter)
        elif tipo_teste == 'cauda_direita':
            power = st.nct.sf(valor_critico, df=graus_de_liberdade, nc=non_centrality_parameter)

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'graus_de_liberdade': graus_de_liberdade, 'valor_critico': valor_critico, 'power': power}


def teste_z_proporcao_uma_amostra_parametros(proporcao_amostral, tamanho_amostra, proporcao_populacional_hipotetica, tipo_teste='duas_caudas', alfa=0.05, proporcao_populacional_alternativa=None):
    """Teste Z para proporção de uma amostra (parâmetros)."""
    n = tamanho_amostra
    p_barra = proporcao_amostral
    p_0 = proporcao_populacional_hipotetica
    estatistica_teste = (p_barra - p_0) / np.sqrt((p_0 * (1 - p_0)) / n)
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * st.norm.sf(np.abs(estatistica_teste))
        valor_critico_superior = st.norm.ppf(1 - alfa/2)
        valor_critico_inferior = st.norm.ppf(alfa/2)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.norm.cdf(estatistica_teste)
        valor_critico = st.norm.ppf(alfa)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.norm.sf(estatistica_teste)
        valor_critico = st.norm.ppf(1 - alfa)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if proporcao_populacional_alternativa is not None:
        efeito_tamanho_padronizado = (proporcao_populacional_alternativa - proporcao_populacional_hipotetica) / np.sqrt(p_0 * (1 - p_0)) 
        if tipo_teste == 'duas_caudas':
            valor_critico_inf, valor_critico_sup = valor_critico
            power_cauda_inferior = st.norm.cdf(valor_critico_inf, loc=efeito_tamanho_padronizado * np.sqrt(tamanho_amostra)) 
            power_cauda_superior = st.norm.sf(valor_critico_sup, loc=efeito_tamanho_padronizado * np.sqrt(tamanho_amostra)) 
            power = power_cauda_inferior + power_cauda_superior
        elif tipo_teste == 'cauda_esquerda':
            power = st.norm.cdf(valor_critico, loc=efeito_tamanho_padronizado * np.sqrt(tamanho_amostra)) 
        elif tipo_teste == 'cauda_direita':
            power = st.norm.sf(valor_critico, loc=efeito_tamanho_padronizado * np.sqrt(tamanho_amostra)) 

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'valor_critico': valor_critico, 'power': power}


def teste_z_proporcao_duas_amostras_parametros(proporcao_amostral1, tamanho_amostra1, proporcao_amostral2, tamanho_amostra2, diferenca_proporcoes_hipotetica=0, tipo_teste='duas_caudas', alfa=0.05, diferenca_proporcoes_alternativa=None):
    """Teste Z para proporções de duas amostras (parâmetros)."""
    n1 = tamanho_amostra1
    n2 = tamanho_amostra2
    p_barra1 = proporcao_amostral1
    p_barra2 = proporcao_amostral2
    diferenca_p_0 = diferenca_proporcoes_hipotetica
    p_agrupado = (proporcao_amostral1 * n1 + proporcao_amostral2 * n2) / (n1 + n2) 
    estatistica_teste = ((p_barra1 - p_barra2) - diferenca_p_0) / np.sqrt(p_agrupado * (1 - p_agrupado) * (1/n1 + 1/n2))
    if tipo_teste == 'duas_caudas':
        p_valor = 2 * st.norm.sf(np.abs(estatistica_teste))
        valor_critico_superior = st.norm.ppf(1 - alfa/2)
        valor_critico_inferior = st.norm.ppf(alfa/2)
        valor_critico = (valor_critico_inferior, valor_critico_superior) 
    elif tipo_teste == 'cauda_esquerda':
        p_valor = st.norm.cdf(estatistica_teste)
        valor_critico = st.norm.ppf(alfa)
    elif tipo_teste == 'cauda_direita':
        p_valor = st.norm.sf(estatistica_teste)
        valor_critico = st.norm.ppf(1 - alfa)
    else:
        raise ValueError("Tipo de teste inválido.")
    hipotese_rejeitada = p_valor < alfa

    power = None
    if diferenca_proporcoes_alternativa is not None:
        p1_0 = p_agrupado 
        p2_0 = p_agrupado 
        variancia_erro_padrao_H1 = (p1_0 * (1 - p1_0) / n1) + (p2_0 * (1 - p2_0) / n2) 
        efeito_tamanho_padronizado = (diferenca_proporcoes_alternativa - diferenca_p_0) / np.sqrt(variancia_erro_padrao_H1) 
        if tipo_teste == 'duas_caudas':
            valor_critico_inf, valor_critico_sup = valor_critico
            power_cauda_inferior = st.norm.cdf(valor_critico_inf, loc=efeito_tamanho_padronizado) 
            power_cauda_superior = st.norm.sf(valor_critico_sup, loc=efeito_tamanho_padronizado) 
            power = power_cauda_inferior + power_cauda_superior
        elif tipo_teste == 'cauda_esquerda':
            power = st.norm.cdf(valor_critico, loc=efeito_tamanho_padronizado) 
        elif tipo_teste == 'cauda_direita':
            power = st.norm.sf(valor_critico, loc=efeito_tamanho_padronizado) 

    return {'estatistica_teste': estatistica_teste, 'p_valor': p_valor, 'hipotese_rejeitada': hipotese_rejeitada, 'alfa': alfa, 'tipo_teste': tipo_teste, 'valor_critico': valor_critico, 'power': power}


# --- Interface Interativa Principal (REESTRUTURADA) ---
print("\n--- Menu Principal de Testes Paramétricos ---")

parametros_anteriores = {} 

while True: # Loop Principal do Menu (seleção de teste)
    print("\nO que você quer determinar?")
    print("1. Testar um parâmetro populacional")
    print("2. Testar a diferença entre parâmetros de duas populações")
    print("3. Sair")
    escolha_objetivo = input("Digite o número da sua escolha (1, 2 ou 3): ")

    resultados_teste = {}
    teste_nome = ""
    alfa_para_print = 0.05
    tipo_teste_para_print = 'duas_caudas'
    parametros_input = {}

    if escolha_objetivo == '1': # Teste de um parâmetro
        print("\nQual parâmetro populacional você quer testar?")
        print("a. Variância (Teste Qui-Quadrado)")
        print("b. Valor Esperado (Média) - Teste t (σ desconhecido)")
        print("c. Valor Esperado (Média) - Teste Z (σ conhecido)")
        print("d. Proporção Binomial (Teste Z)")
        escolha_teste_parametro = input("Digite a letra da sua escolha (a, b, c ou d): ").lower()

        if escolha_teste_parametro not in ['a', 'b', 'c', 'd']:
            print("Escolha inválida de parâmetro.")
            continue

        # --- LOOP DE PARÂMETROS PARA OBJETIVO 1 ---
        while True:
            if escolha_teste_parametro == 'a': 
                print("\n--- Teste Qui-Quadrado para Variância de Uma Amostra ---")
                print("\n**Quando usar:** Testar a variância de uma população Normal.")

                tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_chi2_var_1a', 0.05)))
                variancia_amostral_input = float(input(f"   Variância amostral (s²) [padrão: {parametros_anteriores.get('variancia_amostral_chi2_var_1a', '')}]: ") or str(parametros_anteriores.get('variancia_amostral_chi2_var_1a', '')))
                tamanho_amostra_input = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores.get('tamanho_amostra_chi2_var_1a', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_chi2_var_1a', '')))
                variancia_pop_hipotetica_input = float(input(f"   Variância populacional hipotética (σ₀²) sob H0 [padrão: {parametros_anteriores.get('variancia_populacional_hipotetica_chi2_var_1a', '')}]: ") or str(parametros_anteriores.get('variancia_populacional_hipotetica_chi2_var_1a', '')))

                calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                variancia_pop_alternativa = None
                if calcular_potencia == 's':
                    try:
                        variancia_pop_alternativa = float(input(f"   Digite a Variância populacional sob H1 (σ₁²): "))
                    except ValueError:
                        print("   **Aviso:** Valor inválido. Cálculo da potência ignorado.")

                parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'variancia_amostral': variancia_amostral_input, 'tamanho_amostra': tamanho_amostra_input, 'variancia_populacional_hipotetica': variancia_pop_hipotetica_input, 'variancia_populacional_alternativa': variancia_pop_alternativa}
                teste_nome = "Teste Qui-Quadrado para Variância de Uma Amostra"
                alfa_para_print = alfa_input
                tipo_teste_para_print = tipo_teste_str
                # Persistência simplificada para o próximo loop
                parametros_anteriores.update({'alfa_chi2_var_1a': alfa_input, 'variancia_amostral_chi2_var_1a': variancia_amostral_input, 'tamanho_amostra_chi2_var_1a': tamanho_amostra_input, 'variancia_populacional_hipotetica_chi2_var_1a': variancia_pop_hipotetica_input})

            elif escolha_teste_parametro == 'b': 
                print("\n--- Teste t para Média de Uma Amostra (σ desconhecido) ---")
                tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_t_1a', 0.05)))
                media_amostral_input = float(input(f"   Média amostral (x̄) [padrão: {parametros_anteriores.get('media_amostral_t_1a', '')}]: ") or str(parametros_anteriores.get('media_amostral_t_1a', '')))
                tamanho_amostra_input = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores.get('tamanho_amostra_t_1a', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_t_1a', '')))
                media_pop_hipotetica_input = float(input(f"   Média populacional hipotética (μ₀) sob H0 [padrão: {parametros_anteriores.get('media_populacional_hipotetica_t_1a', 0)}]: ") or str(parametros_anteriores.get('media_populacional_hipotetica_t_1a', 0)))
                desvio_amostral_input = float(input(f"   Desvio padrão amostral (s) [padrão: {parametros_anteriores.get('desvio_padrao_amostral_t_1a', '')}]: ") or str(parametros_anteriores.get('desvio_padrao_amostral_t_1a', '')))

                calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                media_pop_alternativa = None
                if calcular_potencia == 's':
                    try:
                        media_pop_alternativa = float(input(f"   Digite a Média populacional sob H1 (μ₁): "))
                    except ValueError:
                         print("   **Aviso:** Valor inválido. Cálculo da potência ignorado.")

                parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'media_amostral': media_amostral_input, 'tamanho_amostra': tamanho_amostra_input, 'media_populacional_hipotetica': media_pop_hipotetica_input, 'desvio_padrao_amostral': desvio_amostral_input, 'media_populacional_alternativa': media_pop_alternativa}
                teste_nome = "Teste t para Média de Uma Amostra"
                alfa_para_print = alfa_input
                tipo_teste_para_print = tipo_teste_str
                parametros_anteriores.update({'alfa_t_1a': alfa_input, 'media_amostral_t_1a': media_amostral_input, 'tamanho_amostra_t_1a': tamanho_amostra_input, 'media_populacional_hipotetica_t_1a': media_pop_hipotetica_input, 'desvio_padrao_amostral_t_1a': desvio_amostral_input})

            elif escolha_teste_parametro == 'c': 
                print("\n--- Teste Z para Média de Uma Amostra (σ conhecido) ---")
                tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_z_1a', 0.05)))
                media_amostral_input = float(input(f"   Média amostral (x̄) [padrão: {parametros_anteriores.get('media_amostral_z_1a', '')}]: ") or str(parametros_anteriores.get('media_amostral_z_1a', '')))
                tamanho_amostra_input = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores.get('tamanho_amostra_z_1a', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_z_1a', '')))
                media_pop_hipotetica_input = float(input(f"   Média populacional hipotética (μ₀) sob H0 [padrão: {parametros_anteriores.get('media_populacional_hipotetica_z_1a', 0)}]: ") or str(parametros_anteriores.get('media_populacional_hipotetica_z_1a', 0)))
                desvio_pop_input = float(input(f"   Desvio padrão populacional conhecido (σ) [padrão: {parametros_anteriores.get('desvio_padrao_populacional_conhecido_z_1a', '')}]: ") or str(parametros_anteriores.get('desvio_padrao_populacional_conhecido_z_1a', '')))

                calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                media_pop_alternativa = None
                if calcular_potencia == 's':
                    try:
                        media_pop_alternativa = float(input(f"   Digite a Média populacional sob H1 (μ₁): "))
                    except ValueError:
                         print("   **Aviso:** Valor inválido. Cálculo da potência ignorado.")

                parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'media_amostral': media_amostral_input, 'tamanho_amostra': tamanho_amostra_input, 'media_populacional_hipotetica': media_pop_hipotetica_input, 'desvio_padrao_populacional_conhecido': desvio_pop_input, 'media_populacional_alternativa': media_pop_alternativa}
                teste_nome = "Teste Z para Média de Uma Amostra"
                alfa_para_print = alfa_input
                tipo_teste_para_print = tipo_teste_str
                parametros_anteriores.update({'alfa_z_1a': alfa_input, 'media_amostral_z_1a': media_amostral_input, 'tamanho_amostra_z_1a': tamanho_amostra_input, 'media_populacional_hipotetica_z_1a': media_pop_hipotetica_input, 'desvio_padrao_populacional_conhecido_z_1a': desvio_pop_input})

            elif escolha_teste_parametro == 'd': 
                print("\n--- Teste Z para Proporção de Uma Amostra ---")
                tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_z_prop_1a', 0.05)))
                prop_amostral_input = float(input(f"   Proporção amostral (p̂) [padrão: {parametros_anteriores.get('proporcao_amostral_z_prop_1a', '')}]: ") or str(parametros_anteriores.get('proporcao_amostral_z_prop_1a', '')))
                tamanho_amostra_input = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores.get('tamanho_amostra_z_prop_1a', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_z_prop_1a', '')))
                prop_pop_hipotetica_input = float(input(f"   Proporção populacional hipotética (p₀) sob H0 [padrão: {parametros_anteriores.get('proporcao_populacional_hipotetica_z_prop_1a', 0.5)}]: ") or str(parametros_anteriores.get('proporcao_populacional_hipotetica_z_prop_1a', 0.5)))

                calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                prop_pop_alternativa = None
                if calcular_potencia == 's':
                    try:
                        prop_pop_alternativa = float(input(f"   Digite a Proporção populacional sob H1 (p₁): "))
                    except ValueError:
                         print("   **Aviso:** Valor inválido. Cálculo da potência ignorado.")

                parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'proporcao_amostral': prop_amostral_input, 'tamanho_amostra': tamanho_amostra_input, 'proporcao_populacional_hipotetica': prop_pop_hipotetica_input, 'proporcao_populacional_alternativa': prop_pop_alternativa}
                teste_nome = "Teste Z para Proporção de Uma Amostra"
                alfa_para_print = alfa_input
                tipo_teste_para_print = tipo_teste_str
                parametros_anteriores.update({'alfa_z_prop_1a': alfa_input, 'proporcao_amostral_z_prop_1a': prop_amostral_input, 'tamanho_amostra_z_prop_1a': tamanho_amostra_input, 'proporcao_populacional_hipotetica_z_prop_1a': prop_pop_hipotetica_input})

            # --- CONFIRMAÇÃO (Dentro do loop de parâmetros) ---
            print("\n--- Confirme os parâmetros inseridos: ---")
            for chave, valor in parametros_input.items():
                print(f"   {chave}: {valor}")
            confirmacao = input("\nOs parâmetros estão corretos? (s/n): ").lower()
            if confirmacao == 's':
                break # Sai do loop de parâmetros e vai para execução
            else:
                print("Edição cancelada. Por favor, insira os parâmetros novamente.\n")
                continue # Volta para o início do loop de inputs

    elif escolha_objetivo == '2': # Teste de diferença entre parâmetros
        print("\nAs amostras são independentes ou pareadas?")
        print("i. Amostras Independentes")
        print("ii. Amostras Pareadas")
        escolha_tipo_amostra = input("Digite 'i' para independentes ou 'ii' para pareadas: ").lower()

        if escolha_tipo_amostra == 'i': # Amostras Independentes
            print("\nQual parâmetro você quer comparar?")
            print("a. Variâncias (Teste F)")
            print("b. Valores Esperados (Médias) - Teste t (σ desconhecidos)")
            print("c. Valores Esperados (Médias) - Teste Z (σ conhecidos)")
            print("d. Proporções Binomiais (Teste Z)")
            escolha_parametro_duas_amostras_indep = input("Digite a letra da sua escolha (a, b, c ou d): ").lower()
            
            if escolha_parametro_duas_amostras_indep not in ['a', 'b', 'c', 'd']:
                print("Escolha inválida.")
                continue

            # --- LOOP DE PARÂMETROS PARA OBJETIVO 2 (INDEPENDENTES) ---
            while True:
                if escolha_parametro_duas_amostras_indep == 'a':
                    print("\n--- Teste F para Variâncias de Duas Amostras Independentes ---")
                    tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                    tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                    alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_f_var_2a', 0.05)))
                    var1_input = float(input(f"   Variância amostral 1 (s1²) [padrão: {parametros_anteriores.get('variancia_amostral_f_2a_1', '')}]: ") or str(parametros_anteriores.get('variancia_amostral_f_2a_1', '')))
                    n1_input = int(input(f"   Tamanho amostra 1 (n1) [padrão: {parametros_anteriores.get('tamanho_amostra_f_2a_1', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_f_2a_1', '')))
                    var2_input = float(input(f"   Variância amostral 2 (s2²) [padrão: {parametros_anteriores.get('variancia_amostral_f_2a_2', '')}]: ") or str(parametros_anteriores.get('variancia_amostral_f_2a_2', '')))
                    n2_input = int(input(f"   Tamanho amostra 2 (n2) [padrão: {parametros_anteriores.get('tamanho_amostra_f_2a_2', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_f_2a_2', '')))

                    calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                    ratio_var_alternativo = None
                    if calcular_potencia == 's':
                        try:
                            ratio_var_alternativo = float(input(f"   Digite o Ratio das variâncias sob H1 (σ₁²/σ₂²): "))
                        except ValueError:
                             print("   **Aviso:** Valor inválido. Cálculo da potência ignorado.")

                    parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'variancia_amostral1': var1_input, 'tamanho_amostra1': n1_input, 'variancia_amostral2': var2_input, 'tamanho_amostra2': n2_input, 'ratio_variancias_alternativo': ratio_var_alternativo}
                    teste_nome = "Teste F para Variâncias de Duas Amostras Independentes"
                    alfa_para_print = alfa_input
                    tipo_teste_para_print = tipo_teste_str
                    parametros_anteriores.update({'alfa_f_var_2a': alfa_input, 'variancia_amostral_f_2a_1': var1_input, 'tamanho_amostra_f_2a_1': n1_input, 'variancia_amostral_f_2a_2': var2_input, 'tamanho_amostra_f_2a_2': n2_input})

                elif escolha_parametro_duas_amostras_indep == 'b': 
                    print("\n--- Teste t para Médias de Duas Amostras Independentes ---")
                    tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                    tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                    alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_t_media_2a_indep', 0.05)))
                    media1_input = float(input(f"   Média amostral 1 (x̄1) [padrão: {parametros_anteriores.get('media_amostral_t_2a_1', '')}]: ") or str(parametros_anteriores.get('media_amostral_t_2a_1', '')))
                    n1_input = int(input(f"   Tamanho amostra 1 (n1) [padrão: {parametros_anteriores.get('tamanho_amostra_t_2a_1', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_t_2a_1', '')))
                    s1_input = float(input(f"   Desvio padrão amostral 1 (s1) [padrão: {parametros_anteriores.get('desvio_padrao_amostral1_t_2a', '')}]: ") or str(parametros_anteriores.get('desvio_padrao_amostral1_t_2a', '')))
                    media2_input = float(input(f"   Média amostral 2 (x̄2) [padrão: {parametros_anteriores.get('media_amostral_t_2a_2', '')}]: ") or str(parametros_anteriores.get('media_amostral_t_2a_2', '')))
                    n2_input = int(input(f"   Tamanho amostra 2 (n2) [padrão: {parametros_anteriores.get('tamanho_amostra_t_2a_2', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_t_2a_2', '')))
                    s2_input = float(input(f"   Desvio padrão amostral 2 (s2) [padrão: {parametros_anteriores.get('desvio_padrao_amostral2_t_2a', '')}]: ") or str(parametros_anteriores.get('desvio_padrao_amostral2_t_2a', '')))
                    var_iguais_input = input(f"   Variâncias populacionais consideradas iguais? (s/n) [padrão: {'n' if not parametros_anteriores.get('variancias_iguais_t_2a', False) else 's'}]: ").lower() or ('n' if not parametros_anteriores.get('variancias_iguais_t_2a', False) else 's')
                    var_iguais_bool = var_iguais_input == 's'
                    dif_hip_input = float(input(f"   Diferença de médias hipotética (μ1 - μ2) sob H0 [padrão: {parametros_anteriores.get('diferenca_medias_hipotetica_t_2a', 0)}]: ") or str(parametros_anteriores.get('diferenca_medias_hipotetica_t_2a', 0)))

                    calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                    dif_medias_alternativa = None
                    if calcular_potencia == 's':
                        try:
                            dif_medias_alternativa = float(input(f"   Digite a Diferença de médias sob H1 (μ1 - μ2): "))
                        except ValueError:
                             print("   **AVISO:** Valor inválido. Cálculo da potência ignorado.")

                    parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'media_amostral1': media1_input, 'tamanho_amostra1': n1_input, 'desvio_padrao_amostral1': s1_input, 'media_amostral2': media2_input, 'tamanho_amostra2': n2_input, 'desvio_padrao_amostral2': s2_input, 'diferenca_medias_hipotetica': dif_hip_input, 'variancias_iguais': var_iguais_bool, 'diferenca_medias_alternativa': dif_medias_alternativa}
                    teste_nome = "Teste t para Médias de Duas Amostras Independentes"
                    alfa_para_print = alfa_input
                    tipo_teste_para_print = tipo_teste_str
                    parametros_anteriores.update({'alfa_t_media_2a_indep': alfa_input, 'media_amostral_t_2a_1': media1_input, 'tamanho_amostra_t_2a_1': n1_input, 'desvio_padrao_amostral1_t_2a': s1_input, 'media_amostral_t_2a_2': media2_input, 'tamanho_amostra_t_2a_2': n2_input, 'desvio_padrao_amostral2_t_2a': s2_input, 'variancias_iguais_t_2a': var_iguais_bool, 'diferenca_medias_hipotetica_t_2a': dif_hip_input})

                elif escolha_parametro_duas_amostras_indep == 'c': 
                    print("\n--- Teste Z para Médias de Duas Amostras Independentes ---")
                    tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                    tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                    alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_z_media_2a_indep', 0.05)))
                    media1_input = float(input(f"   Média amostral 1 (x̄1) [padrão: {parametros_anteriores.get('media_amostral_z_2a_1', '')}]: ") or str(parametros_anteriores.get('media_amostral_z_2a_1', '')))
                    n1_input = int(input(f"   Tamanho amostra 1 (n1) [padrão: {parametros_anteriores.get('tamanho_amostra_z_2a_1', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_z_2a_1', '')))
                    media2_input = float(input(f"   Média amostral 2 (x̄2) [padrão: {parametros_anteriores.get('media_amostral_z_2a_2', '')}]: ") or str(parametros_anteriores.get('media_amostral_z_2a_2', '')))
                    n2_input = int(input(f"   Tamanho amostra 2 (n2) [padrão: {parametros_anteriores.get('tamanho_amostra_z_2a_2', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_z_2a_2', '')))
                    sigma1_input = float(input(f"   Desvio padrão populacional 1 (σ1) [padrão: {parametros_anteriores.get('desvio_padrao_populacional1_conhecido_z_2a', '')}]: ") or str(parametros_anteriores.get('desvio_padrao_populacional1_conhecido_z_2a', '')))
                    sigma2_input = float(input(f"   Desvio padrão populacional 2 (σ2) [padrão: {parametros_anteriores.get('desvio_padrao_populacional2_conhecido_z_2a', '')}]: ") or str(parametros_anteriores.get('desvio_padrao_populacional2_conhecido_z_2a', '')))
                    dif_hip_input = float(input(f"   Diferença de médias hipotética (μ1 - μ2) sob H0 [padrão: {parametros_anteriores.get('diferenca_medias_hipotetica_z_2a', 0)}]: ") or str(parametros_anteriores.get('diferenca_medias_hipotetica_z_2a', 0)))

                    calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                    dif_medias_alternativa = None
                    if calcular_potencia == 's':
                        try:
                            dif_medias_alternativa = float(input(f"   Digite a Diferença de médias sob H1 (μ1 - μ2): "))
                        except ValueError:
                             print("   **AVISO:** Valor inválido. Cálculo da potência ignorado.")

                    parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'media_amostral1': media1_input, 'tamanho_amostra1': n1_input, 'media_amostral2': media2_input, 'tamanho_amostra2': n2_input, 'diferenca_medias_hipotetica': dif_hip_input, 'desvio_padrao_populacional1_conhecido': sigma1_input, 'desvio_padrao_populacional2_conhecido': sigma2_input, 'diferenca_medias_alternativa': dif_medias_alternativa}
                    teste_nome = "Teste Z para Médias de Duas Amostras Independentes"
                    alfa_para_print = alfa_input
                    tipo_teste_para_print = tipo_teste_str
                    parametros_anteriores.update({'alfa_z_media_2a_indep': alfa_input, 'media_amostral_z_2a_1': media1_input, 'tamanho_amostra_z_2a_1': n1_input, 'media_amostral_z_2a_2': media2_input, 'tamanho_amostra_z_2a_2': n2_input, 'desvio_padrao_populacional1_conhecido_z_2a': sigma1_input, 'desvio_padrao_populacional2_conhecido_z_2a': sigma2_input, 'diferenca_medias_hipotetica_z_2a': dif_hip_input})

                elif escolha_parametro_duas_amostras_indep == 'd': 
                    print("\n--- Teste Z para Proporções de Duas Amostras Independentes ---")
                    tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                    tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                    alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_z_prop_2a_indep', 0.05)))
                    p1_input = float(input(f"   Proporção amostral 1 (p̂1) [padrão: {parametros_anteriores.get('proporcao_amostral1_z_prop_2a', '')}]: ") or str(parametros_anteriores.get('proporcao_amostral1_z_prop_2a', '')))
                    n1_input = int(input(f"   Tamanho amostra 1 (n1) [padrão: {parametros_anteriores.get('tamanho_amostra1_z_prop_2a', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra1_z_prop_2a', '')))
                    p2_input = float(input(f"   Proporção amostral 2 (p̂2) [padrão: {parametros_anteriores.get('proporcao_amostral2_z_prop_2a', '')}]: ") or str(parametros_anteriores.get('proporcao_amostral2_z_prop_2a', '')))
                    n2_input = int(input(f"   Tamanho amostra 2 (n2) [padrão: {parametros_anteriores.get('tamanho_amostra2_z_prop_2a', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra2_z_prop_2a', '')))
                    dif_p_hip_input = float(input(f"   Diferença de proporções hipotética (p1 - p2) sob H0 [padrão: {parametros_anteriores.get('diferenca_proporcoes_hipotetica_z_prop_2a', 0)}]: ") or str(parametros_anteriores.get('diferenca_proporcoes_hipotetica_z_prop_2a', 0)))

                    calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                    dif_prop_alternativa = None
                    if calcular_potencia == 's':
                        try:
                            dif_prop_alternativa = float(input(f"   Digite a Diferença de proporções sob H1 (p1 - p2): "))
                        except ValueError:
                             print("   **AVISO:** Valor inválido. Cálculo da potência ignorado.")

                    parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'proporcao_amostral1': p1_input, 'tamanho_amostra1': n1_input, 'proporcao_amostral2': p2_input, 'tamanho_amostra2': n2_input, 'diferenca_proporcoes_hipotetica': dif_p_hip_input, 'diferenca_proporcoes_alternativa': dif_prop_alternativa}
                    teste_nome = "Teste Z para Proporções de Duas Amostras Independentes"
                    alfa_para_print = alfa_input
                    tipo_teste_para_print = tipo_teste_str
                    parametros_anteriores.update({'alfa_z_prop_2a_indep': alfa_input, 'proporcao_amostral1_z_prop_2a': p1_input, 'tamanho_amostra1_z_prop_2a': n1_input, 'proporcao_amostral2_z_prop_2a': p2_input, 'tamanho_amostra2_z_prop_2a': n2_input, 'diferenca_proporcoes_hipotetica_z_prop_2a': dif_p_hip_input})

                # --- CONFIRMAÇÃO (Dentro do loop de parâmetros 2.i) ---
                print("\n--- Confirme os parâmetros inseridos: ---")
                for chave, valor in parametros_input.items():
                    print(f"   {chave}: {valor}")
                confirmacao = input("\nOs parâmetros estão corretos? (s/n): ").lower()
                if confirmacao == 's':
                    break # Sai do loop
                else:
                    print("Edição cancelada. Reiniciando inputs...\n")
                    continue

        elif escolha_tipo_amostra == 'ii': # Amostras Pareadas
            print("\nQual parâmetro você quer comparar?")
            print("a. Valores Esperados (Médias) - Teste t")
            escolha_parametro_duas_amostras_pareadas = input("Digite a letra da sua escolha (a): ").lower()
            
            if escolha_parametro_duas_amostras_pareadas != 'a':
                print("Escolha inválida.")
                continue

            # --- LOOP DE PARÂMETROS PARA OBJETIVO 2 (PAREADAS) ---
            while True:
                if escolha_parametro_duas_amostras_pareadas == 'a':
                    print("\n--- Teste t para Médias de Amostras Pareadas ---")
                    tipo_teste_input = input(f"   Tipo de teste (1-Duas Caudas, 2-Cauda Esquerda, 3-Cauda Direita) [padrão: 1]: ") or '1'
                    tipo_teste_str = ['duas_caudas', 'cauda_esquerda', 'cauda_direita'][int(tipo_teste_input)-1] if tipo_teste_input in ['1', '2', '3'] else 'duas_caudas'
                    alfa_input = float(input(f"   Nível de significância alfa (ex: 0.05) [padrão: 0.05]: ") or str(parametros_anteriores.get('alfa_t_media_pareada', 0.05)))
                    media_d_input = float(input(f"   Média das diferenças amostrais (x̄d) [padrão: {parametros_anteriores.get('media_diferencas_amostral_t_pareada', '')}]: ") or str(parametros_anteriores.get('media_diferencas_amostral_t_pareada', '')))
                    n_input = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores.get('tamanho_amostra_t_pareada', '')}]: ") or str(parametros_anteriores.get('tamanho_amostra_t_pareada', '')))
                    sd_input = float(input(f"   Desvio padrão das diferenças amostrais (sd) [padrão: {parametros_anteriores.get('desvio_padrao_diferencas_amostral_t_pareada', '')}]: ") or str(parametros_anteriores.get('desvio_padrao_diferencas_amostral_t_pareada', '')))
                    media_d0_input = float(input(f"   Média das diferenças hipotética (μd) sob H0 [padrão: {parametros_anteriores.get('media_diferencas_hipotetica_t_pareada', 0)}]: ") or str(parametros_anteriores.get('media_diferencas_hipotetica_t_pareada', 0)))

                    calcular_potencia = input("   Deseja calcular a potência do teste? (s/n) [padrão: n]: ").lower() or 'n'
                    media_d_alternativa = None
                    if calcular_potencia == 's':
                        try:
                            media_d_alternativa = float(input(f"   Digite a Média das diferenças sob H1 (μd): "))
                        except ValueError:
                             print("   **AVISO:** Valor inválido. Cálculo da potência ignorado.")

                    parametros_input = {'tipo_teste': tipo_teste_str, 'alfa': alfa_input, 'media_diferencas_amostral': media_d_input, 'tamanho_amostra': n_input, 'media_diferencas_hipotetica': media_d0_input, 'desvio_padrao_diferencas_amostral': sd_input, 'media_diferencas_alternativa': media_d_alternativa}
                    teste_nome = "Teste t para Médias de Amostras Pareadas"
                    alfa_para_print = alfa_input
                    tipo_teste_para_print = tipo_teste_str
                    parametros_anteriores.update({'alfa_t_media_pareada': alfa_input, 'media_diferencas_amostral_t_pareada': media_d_input, 'tamanho_amostra_t_pareada': n_input, 'desvio_padrao_diferencas_amostral_t_pareada': sd_input, 'media_diferencas_hipotetica_t_pareada': media_d0_input})

                # --- CONFIRMAÇÃO (Dentro do loop de parâmetros 2.ii) ---
                print("\n--- Confirme os parâmetros inseridos: ---")
                for chave, valor in parametros_input.items():
                    print(f"   {chave}: {valor}")
                confirmacao = input("\nOs parâmetros estão corretos? (s/n): ").lower()
                if confirmacao == 's':
                    break # Sai do loop
                else:
                    print("Edição cancelada. Reiniciando inputs...\n")
                    continue
        else:
            print("Escolha inválida de tipo de amostra.")
            continue

    elif escolha_objetivo == '3': # Sair
        print("Saindo do script de testes paramétricos.")
        break

    else:
        print("Escolha inválida. Digite 1, 2 ou 3.")
        continue


    # --- EXECUÇÃO DOS TESTES (Fora dos loops de input) ---
    if teste_nome == "Teste Qui-Quadrado para Variância de Uma Amostra":
        resultados_teste = teste_qui_quadrado_variancia_uma_amostra_parametros(**parametros_input)
    elif teste_nome == "Teste F para Variâncias de Duas Amostras Independentes":
        resultados_teste = teste_f_variancia_duas_amostras_parametros(**parametros_input)
    elif teste_nome == "Teste Z para Média de Uma Amostra":
        resultados_teste = teste_z_media_uma_amostra_parametros(**parametros_input)
    elif teste_nome == "Teste t para Média de Uma Amostra":
        resultados_teste = teste_t_media_uma_amostra_parametros(**parametros_input)
    elif teste_nome == "Teste Z para Proporção de Uma Amostra":
        resultados_teste = teste_z_proporcao_uma_amostra_parametros(**parametros_input)
    elif teste_nome == "Teste Z para Médias de Duas Amostras Independentes":
        resultados_teste = teste_z_media_duas_amostras_indep_parametros_conhecido(**parametros_input)
    elif teste_nome == "Teste t para Médias de Duas Amostras Independentes":
        resultados_teste = teste_t_media_duas_amostras_indep_parametros(**parametros_input)
    elif teste_nome == "Teste t para Médias de Amostras Pareadas":
            resultados_teste = teste_t_media_amostras_pareadas_parametros(**parametros_input)
    elif teste_nome == "Teste Z para Proporções de Duas Amostras Independentes":
        resultados_teste = teste_z_proporcao_duas_amostras_parametros(**parametros_input)

    # --- IMPRESSÃO DOS RESULTADOS ---
    print(f"\n--- Resultados do {teste_nome} ---")
    print(f"Estatística de Teste: {resultados_teste.get('estatistica_teste'):.4f}")
    print(f"P-valor: {resultados_teste.get('p_valor'):.4f}")

    valor_critico_result = resultados_teste.get('valor_critico')
    if isinstance(valor_critico_result, tuple):
        print(f"Valor Crítico (para alfa={alfa_para_print}, teste {tipo_teste_para_print}): Inferior = {valor_critico_result[0]:.4f}, Superior = {valor_critico_result[1]:.4f}")
    else:
        print(f"Valor Crítico (para alfa={alfa_para_print}, teste {tipo_teste_para_print}): {valor_critico_result:.4f}")

    if 'graus_de_liberdade' in resultados_teste:
        print(f"Graus de Liberdade: {resultados_teste['graus_de_liberdade']:.2f}")
    elif 'graus_de_liberdade_numerador' in resultados_teste:
            print(f"Graus de Liberdade (Numerador): {resultados_teste['graus_de_liberdade_numerador']}")
            print(f"Graus de Liberdade (Denominador): {resultados_teste['graus_de_liberdade_denominador']}")

    print(f"Hipótese Nula Rejeitada? {resultados_teste.get('hipotese_rejeitada')}")
    print(f"Nível de Significância (alfa): {alfa_para_print}")
    print(f"Tipo de Teste: {tipo_teste_para_print}")
    if resultados_teste.get('power') is not None:
        print(f"Potência do Teste: {resultados_teste.get('power'):.4f}")

    if resultados_teste.get('hipotese_rejeitada'):
        print("\nConclusão: Rejeitamos a hipótese nula (H₀).")
    else:
        print("\nConclusão: Não rejeitamos a hipótese nula (H₀).")