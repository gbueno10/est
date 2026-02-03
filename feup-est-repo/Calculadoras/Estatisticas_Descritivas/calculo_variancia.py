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

def calcular_variancia_bruta(dados):
    """
    Calcula a média, variância amostral e desvio padrão para uma lista de valores (Dados Brutos).
    Equação: s² = Σ(xi - x̄)² / (n - 1)
    """
    dados = np.array(dados)
    n = len(dados)
    
    if n < 2:
        print("❌ Erro: A amostra deve ter pelo menos 2 elementos para calcular a variância amostral.")
        return None
    
    # Média Amostral (x̄)
    media = np.mean(dados)
    
    # Variância Amostral (s²) - ddof=1 aplica a correção de Bessel (n-1)
    # Sem ddof=1, o numpy calcula a variância populacional (dividido por n)
    variancia = np.var(dados, ddof=1)
    
    # Desvio Padrão Amostral (s)
    desvio_padrao = np.std(dados, ddof=1)
    
    return {
        "n": n,
        "media": media,
        "variancia": variancia,
        "desvio_padrao": desvio_padrao
    }

def calcular_variancia_agrupada(valores, frequencias):
    """
    Calcula a média, variância e desvio padrão para dados agrupados por frequências.
    Utiliza a média ponderada e o fator de correção amostral n/(n-1).
    """
    # Validação de segurança: Checa se os tamanhos das listas batem antes de converter
    if len(valores) != len(frequencias):
        print(f"❌ ERRO DE ENTRADA: O tamanho das listas não coincide!")
        print(f"   Valores (xi): {len(valores)} itens")
        print(f"   Frequências (ni): {len(frequencias)} itens")
        print("💡 Verifique se você não esqueceu de algum valor ou frequência.")
        return None

    xi = np.array(valores)
    ni = np.array(frequencias)
    
    n = np.sum(ni)
    if n < 2:
        print("❌ Erro: O tamanho total da amostra (n) deve ser pelo menos 2.")
        return None
    
    # Média Ponderada: x̄ = Σ(xi * ni) / n
    media = np.sum(xi * ni) / n
    
    # Variância Amostral Agrupada: s² = [Σ ni * (xi - x̄)²] / (n - 1)
    # Cálculo detalhado para a tabela
    desvios_quad = (xi - media)**2
    contrib_var = ni * desvios_quad
    
    variancia = np.sum(contrib_var) / (n - 1)
    desvio_padrao = np.sqrt(variancia)
    
    # PRINT DA TABELA DE APOIO (Útil para conferir cálculos manuais)
    print("\n" + "="*60)
    print(f"{'xi':>6} | {'ni':>6} | {'(xi - x̄)':>10} | {'ni*(xi - x̄)²':>12}")
    print("-"*60)
    for i in range(len(xi)):
        print(f"{xi[i]:6.2f} | {ni[i]:6d} | {(xi[i] - media):10.4f} | {contrib_var[i]:12.4f}")
    print("="*60)
    print(f"Σ ni = n = {n}")
    print(f"Σ ni*(xi - x̄)² = {np.sum(contrib_var):.4f}")
    
    return {
        "n": n,
        "media": media,
        "variancia": variancia,
        "desvio_padrao": desvio_padrao
    }

def exibir_resultados(titulo, res):
    """Auxiliar para imprimir os resultados formatados."""
    if not res: return
    print(f"\n--- {titulo} ---")
    print(f"Tamanho da Amostra (n): {res['n']}")
    print(f"Média (x̄): {res['media']:.4f}")
    print(f"Variância Amostral (s²): {res['variancia']:.4f}")
    print(f"Desvio Padrão Amostral (s): {res['desvio_padrao']:.4f}")

# --- EXEMPLOS DE USO ---

if __name__ == "__main__":
    # Exemplo 1: Dados Brutos (Notas, Alturas, etc)
    #lista_exemplo = [18, 20, 20, 22, 25]
    #res_a = calcular_variancia_bruta(lista_exemplo)
    #exibir_resultados("CENÁRIO A: DADOS BRUTOS", res_a)

    # Exemplo 2: Dados Agrupados (Frequências)
    # Ex: Número de gols marcados em uma temporada
    gols = [0,1,2,3,4,5,6,7,8]      # xk
    jogos = [4,12,18,6,5,3,1,0,1]     # nk (frequência absoluta)
    res_b = calcular_variancia_agrupada(gols, jogos)
    exibir_resultados("CENÁRIO B: DADOS AGRUPADOS", res_b)
