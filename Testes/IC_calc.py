import numpy as np
import scipy.stats as st

print("Bibliotecas numpy e scipy.stats importadas com sucesso!")

# --- Funções para Intervalos de Confiança (já definidas anteriormente - MANTIDAS) ---
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
    f_superior = st.f.ppf(1 - (1 - nivel_confianca) / 2, graus_liberdade_num, graus_de_liberdade_den)
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


# --- Interface Interativa Principal para Intervalos de Confiança (MENU OTIMIZADO) ---
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

    if escolha_ic_tipo_principal == '1': # Intervalo de Confiança para um Parâmetro Populacional
        print("\n--- Escolha do Parâmetro Populacional ---")
        print("a. Valor Esperado (Média)")
        print("b. Proporção Binomial")
        print("c. Variância (População Normal)")
        print("d. Voltar ao Menu Principal")

        escolha_parametro_populacional = input("Digite a letra da sua escolha (a, b, c ou d): ").lower()

        if escolha_parametro_populacional == 'a': # Valor Esperado (Média)
            print("\n--- Intervalo de Confiança para o Valor Esperado (Média) ---")
            print("a. Amostra Grande (Z) ou σ Conhecido")
            print("b. Amostra Pequena (t) e σ Desconhecido")
            escolha_media_ic_subtipo = input("Digite a letra da sua escolha (a ou b): ").lower()

            if escolha_media_ic_subtipo == 'a': # IC para Média - Z
                print("\n--- Intervalo de Confiança Z para a Média ---")
                intervalo_nome = "Intervalo de Confiança Z para a Média"
                nivel_confianca_input_media_z_ic = float(input(f"   Nível de confiança [padrão: 0.95]: ") or str(parametros_anteriores_ic.get('nivel_confianca_media_z_ic', 0.95)))
                media_amostral_input_media_z_ic = float(input(f"   Média amostral (x̄) [padrão: {parametros_anteriores_ic.get('media_amostral_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('media_amostral_media_z_ic', '')))
                desvio_padrao_populacional_input_media_z_ic = float(input(f"   Desvio padrão populacional (σ) [padrão: {parametros_anteriores_ic.get('desvio_padrao_populacional_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('desvio_padrao_populacional_media_z_ic', '')))
                tamanho_amostra_input_media_z_ic = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores_ic.get('tamanho_amostra_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra_media_z_ic', '')))

                parametros_input_ic = {
                    'nivel_confianca': nivel_confianca_input_media_z_ic,
                    'media_amostral': media_amostral_input_media_z_ic,
                    'desvio_padrao_populacional': desvio_padrao_populacional_input_media_z_ic,
                    'tamanho_amostra': tamanho_amostra_input_media_z_ic,
                }
                nivel_confianca_para_print_ic = nivel_confianca_input_media_z_ic
                resultados_ic = intervalo_confianca_media_z(**parametros_input_ic)
                # ... (persistência dos parâmetros) ...
                parametros_anteriores_ic['nivel_confianca_media_z_ic'] = nivel_confianca_input_media_z_ic
                parametros_anteriores_ic['media_amostral_media_z_ic'] = media_amostral_input_media_z_ic
                parametros_anteriores_ic['desvio_padrao_populacional_media_z_ic'] = desvio_padrao_populacional_input_media_z_ic
                parametros_anteriores_ic['tamanho_amostra_media_z_ic'] = tamanho_amostra_input_media_z_ic


            elif escolha_media_ic_subtipo == 'b': # IC para Média - t
                print("\n--- Intervalo de Confiança t para a Média ---")
                intervalo_nome = "Intervalo de Confiança t para a Média"
                nivel_confianca_input_media_t_ic = float(input(f"   Nível de confiança [padrão: 0.95]: ") or str(parametros_anteriores_ic.get('nivel_confianca_media_t_ic', 0.95)))
                media_amostral_input_media_t_ic = float(input(f"   Média amostral (x̄) [padrão: {parametros_anteriores_ic.get('media_amostral_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('media_amostral_media_t_ic', '')))
                desvio_padrao_amostral_input_media_t_ic = float(input(f"   Desvio padrão amostral (s) [padrão: {parametros_anteriores_ic.get('desvio_padrao_amostral_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('desvio_padrao_amostral_media_t_ic', '')))
                tamanho_amostra_input_media_t_ic = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores_ic.get('tamanho_amostra_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra_media_t_ic', '')))

                parametros_input_ic = {
                    'nivel_confianca': nivel_confianca_input_media_t_ic,
                    'media_amostral': media_amostral_input_media_t_ic,
                    'desvio_padrao_amostral': desvio_padrao_amostral_input_media_t_ic,
                    'tamanho_amostra': tamanho_amostra_input_media_t_ic,
                }
                nivel_confianca_para_print_ic = nivel_confianca_input_media_t_ic
                resultados_ic = intervalo_confianca_media_t(**parametros_input_ic)
                # ... (persistência dos parâmetros) ...
                parametros_anteriores_ic['nivel_confianca_media_t_ic'] = nivel_confianca_input_media_t_ic
                parametros_anteriores_ic['media_amostral_media_t_ic'] = media_amostral_input_media_t_ic
                parametros_anteriores_ic['desvio_padrao_amostral_media_t_ic'] = desvio_padrao_amostral_input_media_t_ic
                parametros_anteriores_ic['tamanho_amostra_media_t_ic'] = tamanho_amostra_input_media_t_ic

            elif escolha_media_ic_subtipo == 'c':
                continue # Voltar ao menu anterior
            else:
                print("Escolha inválida para o tipo de Intervalo de Confiança para a Média.")
                continue

        elif escolha_parametro_populacional == 'b': # Proporção Binomial
            print("\n--- Intervalo de Confiança para a Proporção Binomial ---")
            intervalo_nome = "Intervalo de Confiança para a Proporção Binomial"
            nivel_confianca_input_prop_ic = float(input(f"   Nível de confiança [padrão: 0.95]: ") or str(parametros_anteriores_ic.get('nivel_confianca_prop_ic', 0.95)))
            proporcao_amostral_input_prop_ic = float(input(f"   Proporção amostral (p̂) [padrão: {parametros_anteriores_ic.get('proporcao_amostral_prop_ic', '')}]: ") or str(parametros_anteriores_ic.get('proporcao_amostral_prop_ic', '')))
            tamanho_amostra_input_prop_ic = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores_ic.get('tamanho_amostra_prop_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra_prop_ic', '')))

            parametros_input_ic = {
                'nivel_confianca': nivel_confianca_input_prop_ic,
                'proporcao_amostral': proporcao_amostral_input_prop_ic,
                'tamanho_amostra': tamanho_amostra_input_prop_ic,
            }
            nivel_confianca_para_print_ic = nivel_confianca_input_prop_ic
            resultados_ic = intervalo_confianca_proporcao_binomial(**parametros_input_ic)
            # ... (persistência dos parâmetros) ...
            parametros_anteriores_ic['nivel_confianca_prop_ic'] = nivel_confianca_input_prop_ic
            parametros_anteriores_ic['proporcao_amostral_prop_ic'] = proporcao_amostral_input_prop_ic
            parametros_anteriores_ic['tamanho_amostra_prop_ic'] = tamanho_amostra_input_prop_ic

        elif escolha_parametro_populacional == 'c': # Variância (População Normal)
            print("\n--- Intervalo de Confiança para a Variância ---")
            intervalo_nome = "Intervalo de Confiança para a Variância"
            nivel_confianca_input_var_ic = float(input(f"   Nível de confiança [padrão: 0.95]: ") or str(parametros_anteriores_ic.get('nivel_confianca_var_ic', 0.95)))
            variancia_amostral_input_var_ic = float(input(f"   Variância amostral (s²) [padrão: {parametros_anteriores_ic.get('variancia_amostral_var_ic', '')}]: ") or str(parametros_anteriores_ic.get('variancia_amostral_var_ic', '')))
            tamanho_amostra_input_var_ic = int(input(f"   Tamanho da amostra (n) [padrão: {parametros_anteriores_ic.get('tamanho_amostra_var_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra_var_ic', '')))

            parametros_input_ic = {
                'nivel_confianca': nivel_confianca_input_var_ic,
                'variancia_amostral': variancia_amostral_input_var_ic,
                'tamanho_amostra': tamanho_amostra_input_var_ic,
            }
            nivel_confianca_para_print_ic = nivel_confianca_input_var_ic
            resultados_ic = intervalo_confianca_variancia_normal(**parametros_input_ic)
            # ... (persistência dos parâmetros) ...
            parametros_anteriores_ic['nivel_confianca_var_ic'] = nivel_confianca_input_var_ic
            parametros_anteriores_ic['variancia_amostral_var_ic'] = variancia_amostral_input_var_ic
            parametros_anteriores_ic['tamanho_amostra_var_ic'] = tamanho_amostra_input_var_ic

        elif escolha_parametro_populacional == 'd':
            continue # Voltar ao menu principal
        else:
            print("Escolha inválida para o tipo de Parâmetro Populacional.")
            continue


    elif escolha_ic_tipo_principal == '2': # Intervalo de Confiança para a Diferença de Parâmetros Populacionais
        print("\n--- Escolha da Diferença de Parâmetros Populacionais ---")
        print("a. Diferença de Valores Esperados (Médias)")
        print("b. Diferença de Proporções Binomiais")
        print("c. Voltar ao Menu Principal")

        escolha_diff_parametro_populacional = input("Digite a letra da sua escolha (a, b ou c): ").lower()

        if escolha_diff_parametro_populacional == 'a': # Diferença de Valores Esperados (Médias)
            print("\n--- Intervalo de Confiança para a Diferença de Médias ---")
            print("a. Amostras Grandes (Z) ou σ Conhecidos")
            print("b. Amostras Pequenas (t) e σ Desconhecidos")
            escolha_diff_medias_ic_subtipo_principal = input("Digite a letra da sua escolha (a ou b): ").lower()

            if escolha_diff_medias_ic_subtipo_principal == 'a': # IC para Diferença de Médias - Z
                print("\n--- Intervalo de Confiança Z para a Diferença de Médias ---")
                intervalo_nome = "Intervalo de Confiança Z para a Diferença de Médias"
                nivel_confianca_input_diff_media_z_ic = float(input(f"   Nível de confiança [padrão: 0.95]: ") or str(parametros_anteriores_ic.get('nivel_confianca_diff_media_z_ic', 0.95)))
                media_amostral1_input_diff_media_z_ic = float(input(f"   Média amostral 1 (x̄1) [padrão: {parametros_anteriores_ic.get('media_amostral1_diff_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('media_amostral1_diff_media_z_ic', '')))
                media_amostral2_input_diff_media_z_ic = float(input(f"   Média amostral 2 (x̄2) [padrão: {parametros_anteriores_ic.get('media_amostral2_diff_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('media_amostral2_diff_media_z_ic', '')))
                desvio_padrao_populacional1_input_diff_media_z_ic = float(input(f"   Desvio padrão populacional 1 (σ1) [padrão: {parametros_anteriores_ic.get('desvio_padrao_populacional1_diff_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('desvio_padrao_populacional1_diff_media_z_ic', '')))
                desvio_padrao_populacional2_input_diff_media_z_ic = float(input(f"   Desvio padrão populacional 2 (σ2) [padrão: {parametros_anteriores_ic.get('desvio_padrao_populacional2_diff_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('desvio_padrao_populacional2_diff_media_z_ic', '')))
                tamanho_amostra1_input_diff_media_z_ic = int(input(f"   Tamanho da amostra 1 (n1) [padrão: {parametros_anteriores_ic.get('tamanho_amostra1_diff_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra1_diff_media_z_ic', '')))
                tamanho_amostra2_input_diff_media_z_ic = int(input(f"   Tamanho da amostra 2 (n2) [padrão: {parametros_anteriores_ic.get('tamanho_amostra2_diff_media_z_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra2_diff_media_z_ic', '')))

                parametros_input_ic = {
                    'nivel_confianca': nivel_confianca_input_diff_media_z_ic,
                    'media_amostral1': media_amostral1_input_diff_media_z_ic,
                    'media_amostral2': media_amostral2_input_diff_media_z_ic,
                    'desvio_padrao_populacional1': desvio_padrao_populacional1_input_diff_media_z_ic,
                    'desvio_padrao_populacional2': desvio_padrao_populacional2_input_diff_media_z_ic,
                    'tamanho_amostra1': tamanho_amostra1_input_diff_media_z_ic,
                    'tamanho_amostra2': tamanho_amostra2_input_diff_media_z_ic,
                }
                nivel_confianca_para_print_ic = nivel_confianca_input_diff_media_z_ic
                resultados_ic = intervalo_confianca_diferenca_medias_z(**parametros_input_ic)
                # ... (persistência dos parâmetros) ...
                parametros_anteriores_ic['nivel_confianca_diff_media_z_ic'] = nivel_confianca_input_diff_media_z_ic
                parametros_anteriores_ic['media_amostral1_diff_media_z_ic'] = media_amostral1_input_diff_media_z_ic
                parametros_anteriores_ic['media_amostral2_diff_media_z_ic'] = media_amostral2_input_diff_media_z_ic
                parametros_anteriores_ic['desvio_padrao_populacional1_diff_media_z_ic'] = desvio_padrao_populacional1_input_diff_media_z_ic
                parametros_anteriores_ic['desvio_padrao_populacional2_diff_media_z_ic'] = desvio_padrao_populacional2_input_diff_media_z_ic
                parametros_anteriores_ic['tamanho_amostra1_diff_media_z_ic'] = tamanho_amostra1_input_diff_media_z_ic
                parametros_anteriores_ic['tamanho_amostra2_diff_media_z_ic'] = tamanho_amostra2_input_diff_media_z_ic

            elif escolha_diff_medias_ic_subtipo_principal == 'b': # IC para Diferença de Médias - t
                print("\n--- Intervalo de Confiança t para a Diferença de Médias ---")
                print("i. Variâncias Populacionais Iguais")
                print("ii. Variâncias Populacionais Desiguais")
                escolha_diff_medias_t_ic_subtipo = input("Digite 'i' ou 'ii' para o caso das variâncias: ").lower()

                variancias_iguais_diff_media_t_ic_bool = True # padrão para variâncias iguais
                if escolha_diff_medias_t_ic_subtipo == 'ii':
                    variancias_iguais_diff_media_t_ic_bool = False
                elif escolha_diff_medias_t_ic_subtipo != 'i':
                    print("Escolha inválida para variâncias, assumindo variâncias iguais.")

                intervalo_nome = "Intervalo de Confiança t para a Diferença de Médias"
                nivel_confianca_input_diff_media_t_ic = float(input(f"   Nível de confiança [padrão: 0.95]: ") or str(parametros_anteriores_ic.get('nivel_confianca_diff_media_t_ic', 0.95)))
                media_amostral1_input_diff_media_t_ic = float(input(f"   Média amostral 1 (x̄1) [padrão: {parametros_anteriores_ic.get('media_amostral1_diff_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('media_amostral1_diff_media_t_ic', '')))
                media_amostral2_input_diff_media_t_ic = float(input(f"   Média amostral 2 (x̄2) [padrão: {parametros_anteriores_ic.get('media_amostral2_diff_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('media_amostral2_diff_media_t_ic', '')))
                desvio_padrao_amostral1_input_diff_media_t_ic = float(input(f"   Desvio padrão amostral 1 (s1) [padrão: {parametros_anteriores_ic.get('desvio_padrao_amostral1_diff_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('desvio_padrao_amostral1_diff_media_t_ic', '')))
                desvio_padrao_amostral2_input_diff_media_t_ic = float(input(f"   Desvio padrão amostral 2 (s2) [padrão: {parametros_anteriores_ic.get('desvio_padrao_amostral2_diff_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('desvio_padrao_amostral2_diff_media_t_ic', '')))
                tamanho_amostra1_input_diff_media_t_ic = int(input(f"   Tamanho da amostra 1 (n1) [padrão: {parametros_anteriores_ic.get('tamanho_amostra1_diff_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra1_diff_media_t_ic', '')))
                tamanho_amostra2_input_diff_media_t_ic = int(input(f"   Tamanho da amostra 2 (n2) [padrão: {parametros_anteriores_ic.get('tamanho_amostra2_diff_media_t_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra2_diff_media_t_ic', '')))


                parametros_input_ic = {
                    'nivel_confianca': nivel_confianca_input_diff_media_t_ic,
                    'media_amostral1': media_amostral1_input_diff_media_t_ic,
                    'media_amostral2': media_amostral2_input_diff_media_t_ic,
                    'desvio_padrao_amostral1': desvio_padrao_amostral1_input_diff_media_t_ic,
                    'desvio_padrao_amostral2': desvio_padrao_amostral2_input_diff_media_t_ic,
                    'tamanho_amostra1': tamanho_amostra1_input_diff_media_t_ic,
                    'tamanho_amostra2': tamanho_amostra2_input_diff_media_t_ic,
                    'variancias_iguais': variancias_iguais_diff_media_t_ic_bool,
                }
                nivel_confianca_para_print_ic = nivel_confianca_input_diff_media_t_ic
                resultados_ic = intervalo_confianca_diferenca_medias_t(**parametros_input_ic)
                # ... (persistência dos parâmetros) ...
                parametros_anteriores_ic['nivel_confianca_diff_media_t_ic'] = nivel_confianca_input_diff_media_t_ic
                parametros_anteriores_ic['media_amostral1_diff_media_t_ic'] = media_amostral1_input_diff_media_t_ic
                parametros_anteriores_ic['media_amostral2_diff_media_t_ic'] = media_amostral2_input_diff_media_t_ic
                parametros_anteriores_ic['desvio_padrao_amostral1_diff_media_t_ic'] = desvio_padrao_amostral1_input_diff_media_t_ic
                parametros_anteriores_ic['desvio_padrao_amostral2_diff_media_t_ic'] = desvio_padrao_amostral2_input_diff_media_t_ic
                parametros_anteriores_ic['tamanho_amostra1_diff_media_t_ic'] = tamanho_amostra1_input_diff_media_t_ic
                parametros_anteriores_ic['tamanho_amostra2_diff_media_t_ic'] = tamanho_amostra2_input_diff_media_t_ic
                parametros_anteriores_ic['variancias_iguais_diff_media_t_ic'] = variancias_iguais_diff_media_t_ic_bool


            elif escolha_diff_medias_ic_subtipo_principal == 'c':
                continue # Voltar ao menu anterior
            else:
                print("Escolha inválida para o tipo de Intervalo de Confiança para a Diferença de Médias.")
                continue

        elif escolha_diff_parametro_populacional == 'b': # Diferença de Proporções Binomiais
            print("\n--- Intervalo de Confiança para a Diferença de Proporções Binomiais ---")
            intervalo_nome = "Intervalo de Confiança para a Diferença de Proporções Binomiais"
            nivel_confianca_input_diff_prop_ic = float(input(f"   Nível de confiança [padrão: 0.95]: ") or str(parametros_anteriores_ic.get('nivel_confianca_diff_prop_ic', 0.95)))
            proporcao_amostral1_input_diff_prop_ic = float(input(f"   Proporção amostral 1 (p̂1) [padrão: {parametros_anteriores_ic.get('proporcao_amostral1_diff_prop_ic', '')}]: ") or str(parametros_anteriores_ic.get('proporcao_amostral1_diff_prop_ic', '')))
            proporcao_amostral2_input_diff_prop_ic = float(input(f"   Proporção amostral 2 (p̂2) [padrão: {parametros_anteriores_ic.get('proporcao_amostral2_diff_prop_ic', '')}]: ") or str(parametros_anteriores_ic.get('proporcao_amostral2_diff_prop_ic', '')))
            tamanho_amostra1_input_diff_prop_ic = int(input(f"   Tamanho da amostra 1 (n1) [padrão: {parametros_anteriores_ic.get('tamanho_amostra1_diff_prop_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra1_diff_prop_ic', '')))
            tamanho_amostra2_input_diff_prop_ic = int(input(f"   Tamanho da amostra 2 (n2) [padrão: {parametros_anteriores_ic.get('tamanho_amostra2_diff_prop_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra2_diff_prop_ic', '')))

            parametros_input_ic = {
                'nivel_confianca': nivel_confianca_input_diff_prop_ic,
                'proporcao_amostral1': proporcao_amostral1_input_diff_prop_ic,
                'proporcao_amostral2': proporcao_amostral2_input_diff_prop_ic,
                'tamanho_amostra1': tamanho_amostra1_input_diff_prop_ic,
                'tamanho_amostra2': tamanho_amostra2_input_diff_prop_ic,
            }
            nivel_confianca_para_print_ic = nivel_confianca_input_diff_prop_ic
            resultados_ic = intervalo_confianca_diferenca_proporcoes_binomial(**parametros_input_ic)
            # ... (persistência dos parâmetros) ...
            parametros_anteriores_ic['nivel_confianca_diff_prop_ic'] = nivel_confianca_input_diff_prop_ic
            parametros_anteriores_ic['proporcao_amostral1_diff_prop_ic'] = proporcao_amostral1_input_diff_prop_ic
            parametros_anteriores_ic['proporcao_amostral2_diff_prop_ic'] = proporcao_amostral2_input_diff_prop_ic
            parametros_anteriores_ic['tamanho_amostra1_diff_prop_ic'] = tamanho_amostra1_input_diff_prop_ic
            parametros_anteriores_ic['tamanho_amostra2_diff_prop_ic'] = tamanho_amostra2_input_diff_prop_ic

        elif escolha_diff_parametro_populacional == 'c':
            continue # Voltar ao menu principal
        else:
            print("Escolha inválida para o tipo de Diferença de Parâmetros Populacionais.")
            continue


    elif escolha_ic_tipo_principal == '3': # Intervalo de Confiança para a Razão de Variâncias
        print("\n--- Intervalo de Confiança para a Razão de Variâncias ---")
        intervalo_nome = "Intervalo de Confiança para a Razão de Variâncias"
        nivel_confianca_input_razao_var_ic = float(input(f"   Nível de confiança [padrão: 0.95]: ") or str(parametros_anteriores_ic.get('nivel_confianca_razao_var_ic', 0.95)))
        variancia_amostral1_input_razao_var_ic = float(input(f"   Variância amostral 1 (s1²) [padrão: {parametros_anteriores_ic.get('variancia_amostral1_razao_var_ic', '')}]: ") or str(parametros_anteriores_ic.get('variancia_amostral1_razao_var_ic', '')))
        variancia_amostral2_input_razao_var_ic = float(input(f"   Variância amostral 2 (s2²) [padrão: {parametros_anteriores_ic.get('variancia_amostral2_razao_var_ic', '')}]: ") or str(parametros_anteriores_ic.get('variancia_amostral2_razao_var_ic', '')))
        tamanho_amostra1_input_razao_var_ic = int(input(f"   Tamanho da amostra 1 (n1) [padrão: {parametros_anteriores_ic.get('tamanho_amostra1_razao_var_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra1_razao_var_ic', '')))
        tamanho_amostra2_input_razao_var_ic = int(input(f"   Tamanho da amostra 2 (n2) [padrão: {parametros_anteriores_ic.get('tamanho_amostra2_razao_var_ic', '')}]: ") or str(parametros_anteriores_ic.get('tamanho_amostra2_razao_var_ic', '')))

        parametros_input_ic = {
            'nivel_confianca': nivel_confianca_input_razao_var_ic,
            'variancia_amostral1': variancia_amostral1_input_razao_var_ic,
            'variancia_amostral2': variancia_amostral2_input_razao_var_ic,
            'tamanho_amostra1': tamanho_amostra1_input_razao_var_ic,
            'tamanho_amostra2': tamanho_amostra2_input_razao_var_ic,
        }
        nivel_confianca_para_print_ic = nivel_confianca_input_razao_var_ic
        resultados_ic = intervalo_confianca_razao_variancias_normal(**parametros_input_ic)
        # ... (persistência dos parâmetros) ...
        parametros_anteriores_ic['nivel_confianca_razao_var_ic'] = nivel_confianca_input_razao_var_ic
        parametros_anteriores_ic['variancia_amostral1_razao_var_ic'] = variancia_amostral1_input_razao_var_ic
        parametros_anteriores_ic['variancia_amostral2_razao_var_ic'] = variancia_amostral2_input_razao_var_ic
        parametros_anteriores_ic['tamanho_amostra1_razao_var_ic'] = tamanho_amostra1_input_razao_var_ic
        parametros_anteriores_ic['tamanho_amostra2_razao_var_ic'] = tamanho_amostra2_input_razao_var_ic


    elif escolha_ic_tipo_principal == '4': # Sair
        print("Saindo do script de intervalos de confiança.")
        break

    else:
        print("Escolha inválida. Digite um número de 1 a 4.")
        continue

    if resultados_ic:
        print(f"\n--- Resultados do {intervalo_nome} ---")
        inferior, superior = resultados_ic
        print(f"Intervalo de Confiança ({nivel_confianca_para_print_ic*100:.2f}%): ({inferior:.4f}, {superior:.4f})")
        print(f"Nível de Confiança: {nivel_confianca_para_print_ic}")

print("\nObrigado por usar o script de intervalos de confiança!")