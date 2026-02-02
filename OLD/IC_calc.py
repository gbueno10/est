import numpy as np
import scipy.stats as st

print("Bibliotecas numpy e scipy.stats importadas com sucesso!")

# --- Funções para Intervalos de Confiança ---

def intervalo_confianca_media_z(media_amostral, desvio_padrao_populacional, tamanho_amostra, nivel_confianca=0.95):
    z_critico = st.norm.ppf(1 - (1 - nivel_confianca) / 2)
    margem_erro = z_critico * (desvio_padrao_populacional / np.sqrt(tamanho_amostra))
    inferior = media_amostral - margem_erro
    superior = media_amostral + margem_erro
    return (inferior, superior)

def intervalo_confianca_media_t(media_amostral, desvio_padrao_amostral, tamanho_amostra, nivel_confianca=0.95):
    graus_liberdade = tamanho_amostra - 1
    t_critico = st.t.ppf(1 - (1 - nivel_confianca) / 2, graus_liberdade)
    margem_erro = t_critico * (desvio_padrao_amostral / np.sqrt(tamanho_amostra))
    inferior = media_amostral - margem_erro
    superior = media_amostral + margem_erro
    return (inferior, superior)

def intervalo_confianca_proporcao_binomial(proporcao_amostral, tamanho_amostra, nivel_confianca=0.95):
    z_critico = st.norm.ppf(1 - (1 - nivel_confianca) / 2)
    margem_erro = z_critico * np.sqrt((proporcao_amostral * (1 - proporcao_amostral)) / tamanho_amostra)
    inferior = proporcao_amostral - margem_erro
    superior = proporcao_amostral + margem_erro
    return (inferior, superior)

def intervalo_confianca_variancia_normal(variancia_amostral, tamanho_amostra, nivel_confianca=0.95):
    graus_liberdade = tamanho_amostra - 1
    chi2_inferior = st.chi2.ppf((1 - nivel_confianca) / 2, graus_liberdade)
    chi2_superior = st.chi2.ppf(1 - (1 - nivel_confianca) / 2, graus_liberdade)
    inferior = (graus_liberdade * variancia_amostral) / chi2_superior
    superior = (graus_liberdade * variancia_amostral) / chi2_inferior
    return (inferior, superior)

def intervalo_confianca_razao_variancias_normal(variancia_amostral1, tamanho_amostra1, variancia_amostral2, tamanho_amostra2, nivel_confianca=0.95):
    graus_liberdade_num = tamanho_amostra1 - 1
    graus_liberdade_den = tamanho_amostra2 - 1
    f_inferior = st.f.ppf((1 - nivel_confianca) / 2, graus_liberdade_num, graus_liberdade_den)
    # CORREÇÃO: Variável corrigida de 'graus_de_liberdade_den' para 'graus_liberdade_den'
    f_superior = st.f.ppf(1 - (1 - nivel_confianca) / 2, graus_liberdade_num, graus_liberdade_den)
    inferior = (variancia_amostral1 / variancia_amostral2) / f_superior
    superior = (variancia_amostral1 / variancia_amostral2) / f_inferior
    return (inferior, superior)

def intervalo_confianca_diferenca_medias_z(media_amostral1, media_amostral2, desvio_padrao_populacional1, desvio_padrao_populacional2, tamanho_amostra1, tamanho_amostra2, nivel_confianca=0.95):
    z_critico = st.norm.ppf(1 - (1 - nivel_confianca) / 2)
    erro_padrao = np.sqrt((desvio_padrao_populacional1**2 / tamanho_amostra1) + (desvio_padrao_populacional2**2 / tamanho_amostra2))
    margem_erro = z_critico * erro_padrao
    diferenca_medias = media_amostral1 - media_amostral2
    inferior = diferenca_medias - margem_erro
    superior = diferenca_medias + margem_erro
    return (inferior, superior)

def intervalo_confianca_diferenca_medias_t(media_amostral1, media_amostral2, desvio_padrao_amostral1, desvio_padrao_amostral2, tamanho_amostra1, tamanho_amostra2, nivel_confianca=0.95, variancias_iguais=True):
    if variancias_iguais:
        variancia_agrupada = ((tamanho_amostra1 - 1) * desvio_padrao_amostral1**2 + (tamanho_amostra2 - 1) * desvio_padrao_amostral2**2) / (tamanho_amostra1 + tamanho_amostra2 - 2)
        erro_padrao = np.sqrt(variancia_agrupada * (1/tamanho_amostra1 + 1/tamanho_amostra2))
        graus_liberdade = tamanho_amostra1 + tamanho_amostra2 - 2
    else: # Welch's t-test
        erro_padrao = np.sqrt((desvio_padrao_amostral1**2 / tamanho_amostra1) + (desvio_padrao_amostral2**2 / tamanho_amostra2))
        gl_num = ((desvio_padrao_amostral1**2 / tamanho_amostra1) + (desvio_padrao_amostral2**2 / tamanho_amostra2))**2
        gl_den = ((desvio_padrao_amostral1**2 / tamanho_amostra1)**2 / (tamanho_amostra1 - 1)) + ((desvio_padrao_amostral2**2 / tamanho_amostra2)**2 / (tamanho_amostra2 - 1))
        graus_liberdade = gl_num / gl_den

    t_critico = st.t.ppf(1 - (1 - nivel_confianca) / 2, graus_liberdade)
    margem_erro = t_critico * erro_padrao
    diferenca_medias = media_amostral1 - media_amostral2
    inferior = diferenca_medias - margem_erro
    superior = diferenca_medias + margem_erro
    return (inferior, superior)

def intervalo_confianca_diferenca_proporcoes_binomial(proporcao_amostral1, proporcao_amostral2, tamanho_amostra1, tamanho_amostra2, nivel_confianca=0.95):
    z_critico = st.norm.ppf(1 - (1 - nivel_confianca) / 2)
    erro_padrao = np.sqrt((proporcao_amostral1 * (1 - proporcao_amostral1) / tamanho_amostra1) + (proporcao_amostral2 * (1 - proporcao_amostral2) / tamanho_amostra2))
    margem_erro = z_critico * erro_padrao
    diferenca_proporcoes = proporcao_amostral1 - proporcao_amostral2
    inferior = diferenca_proporcoes - margem_erro
    superior = diferenca_proporcoes + margem_erro
    return (inferior, superior)

# --- Interface Interativa ---

print("\n--- Menu Principal de Intervalos de Confiança Paramétricos ---")

parametros_anteriores_ic = {}

while True:
    print("\nQual tipo de análise você quer realizar?")
    print("1. Intervalo de Confiança para um Parâmetro Populacional")
    print("2. Intervalo de Confiança para a Diferença de Parâmetros Populacionais")
    print("3. Intervalo de Confiança para a Razão de Variâncias Populacionais")
    print("4. Sair")

    escolha_ic_tipo_principal = input("Digite o número da sua escolha (1-4): ")

    resultados_ic = None
    intervalo_nome = ""
    nivel_confianca_para_print_ic = 0.95
    parametros_input_ic = {}

    if escolha_ic_tipo_principal == '1':
        print("\n--- Escolha do Parâmetro Populacional ---")
        print("a. Valor Esperado (Média)")
        print("b. Proporção Binomial")
        print("c. Variância (População Normal)")
        print("d. Voltar ao Menu Principal")

        escolha_parametro_populacional = input("Digite a letra (a, b, c ou d): ").lower()

        if escolha_parametro_populacional == 'a':
            print("\na. Amostra Grande (Z) ou σ Conhecido")
            print("b. Amostra Pequena (t) e σ Desconhecido")
            escolha_media_ic_subtipo = input("Digite a letra (a ou b): ").lower()

            if escolha_media_ic_subtipo == 'a':
                intervalo_nome = "IC Z para a Média"
                conf = float(input("Nível de confiança [0.95]: ") or 0.95)
                media = float(input("Média amostral: "))
                sigma = float(input("Desvio padrão populacional (σ): "))
                n = int(input("Tamanho da amostra: "))
                resultados_ic = intervalo_confianca_media_z(media, sigma, n, conf)
                nivel_confianca_para_print_ic = conf

            elif escolha_media_ic_subtipo == 'b':
                intervalo_nome = "IC t para a Média"
                conf = float(input("Nível de confiança [0.95]: ") or 0.95)
                media = float(input("Média amostral: "))
                s = float(input("Desvio padrão amostral (s): "))
                n = int(input("Tamanho da amostra: "))
                resultados_ic = intervalo_confianca_media_t(media, s, n, conf)
                nivel_confianca_para_print_ic = conf

        elif escolha_parametro_populacional == 'b':
            intervalo_nome = "IC para Proporção Binomial"
            conf = float(input("Nível de confiança [0.95]: ") or 0.95)
            p_hat = float(input("Proporção amostral (p̂): "))
            n = int(input("Tamanho da amostra: "))
            resultados_ic = intervalo_confianca_proporcao_binomial(p_hat, n, conf)
            nivel_confianca_para_print_ic = conf

        elif escolha_parametro_populacional == 'c':
            intervalo_nome = "IC para Variância"
            conf = float(input("Nível de confiança [0.95]: ") or 0.95)
            s2 = float(input("Variância amostral (s²): "))
            n = int(input("Tamanho da amostra: "))
            resultados_ic = intervalo_confianca_variancia_normal(s2, n, conf)
            nivel_confianca_para_print_ic = conf

    elif escolha_ic_tipo_principal == '2':
        print("\na. Diferença de Médias")
        print("b. Diferença de Proporções")
        escolha_diff = input("Digite a letra: ").lower()

        if escolha_diff == 'a':
            print("a. Z (σ conhecidos) | b. t (σ desconhecidos)")
            sub_diff = input("Digite a letra: ").lower()
            conf = float(input("Nível de confiança [0.95]: ") or 0.95)
            m1 = float(input("Média 1: "))
            m2 = float(input("Média 2: "))
            n1 = int(input("n1: "))
            n2 = int(input("n2: "))

            if sub_diff == 'a':
                s1 = float(input("σ1: "))
                s2 = float(input("σ2: "))
                resultados_ic = intervalo_confianca_diferenca_medias_z(m1, m2, s1, s2, n1, n2, conf)
                intervalo_nome = "IC Z Diferença de Médias"
            else:
                s1 = float(input("s1: "))
                s2 = float(input("s2: "))
                var_iguais = input("Variâncias iguais? (s/n): ").lower() == 's'
                resultados_ic = intervalo_confianca_diferenca_medias_t(m1, m2, s1, s2, n1, n2, conf, var_iguais)
                intervalo_nome = "IC t Diferença de Médias"
            nivel_confianca_para_print_ic = conf

        elif escolha_diff == 'b':
            intervalo_nome = "IC Diferença de Proporções"
            conf = float(input("Nível de confiança [0.95]: ") or 0.95)
            p1 = float(input("p̂1: "))
            p2 = float(input("p̂2: "))
            n1 = int(input("n1: "))
            n2 = int(input("n2: "))
            resultados_ic = intervalo_confianca_diferenca_proporcoes_binomial(p1, p2, n1, n2, conf)
            nivel_confianca_para_print_ic = conf

    elif escolha_ic_tipo_principal == '3':
        intervalo_nome = "IC Razão de Variâncias"
        conf = float(input("Nível de confiança [0.95]: ") or 0.95)
        v1 = float(input("Variância amostral 1 (s1²): "))
        v2 = float(input("Variância amostral 2 (s2²): "))
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
        resultados_ic = intervalo_confianca_razao_variancias_normal(v1, n1, v2, n2, conf)
        nivel_confianca_para_print_ic = conf

    elif escolha_ic_tipo_principal == '4':
        break

    if resultados_ic:
        inf, sup = resultados_ic
        print(f"\n--- Resultados do {intervalo_nome} ---")
        print(f"Intervalo ({nivel_confianca_para_print_ic*100}%): ({inf:.4f}, {sup:.4f})")

print("\nScript finalizado!")