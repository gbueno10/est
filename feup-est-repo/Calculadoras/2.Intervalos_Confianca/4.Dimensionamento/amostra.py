import scipy.stats as stats
import numpy as np

def dimensionar_n_media(
    erro_maximo = 0.5,           # erro máximo permitido (E)
    desvio_padrao = 2.0,         # desvio padrão populacional (σ) ou estimativa de S
    nivel_confianca = 0.95,      # nível de confiança (1-α)
    M = None                     # tamanho da população (M) se for finita
):
    """
    Calcula o tamanho mínimo da amostra (n) para estimar a média com um erro E.
    """
    alfa = 1 - nivel_confianca
    z = stats.norm.ppf(1 - alfa/2)
    
    n0 = (z * desvio_padrao / erro_maximo)**2
    
    if M is not None:
        n = (n0 * M) / (n0 + (M - 1))
    else:
        n = n0
        
    n_final = int(np.ceil(n))
    
    print(f"📐 DIMENSIONAMENTO DE AMOSTRA (MÉDIA)")
    print(f"Erro Máximo (E): {erro_maximo}")
    print(f"Confiança: {nivel_confianca*100:.1f}% (Z={z:.3f})")
    print(f"Tamanho de Amostra Necessário (n): {n_final}")
    
    return n_final

def dimensionar_n_proporcao(
    erro_maximo = 0.05,          # erro máximo (ex: 5% = 0.05)
    p_estimado = 0.5,            # estimativa de p (usar 0.5 para pior caso)
    nivel_confianca = 0.95,      # nível de confiança (1-α)
    M = None                     # tamanho da população (M) se for finita
):
    """
    Calcula o tamanho mínimo da amostra (n) para estimar a proporção com um erro E.
    """
    alfa = 1 - nivel_confianca
    z = stats.norm.ppf(1 - alfa/2)
    
    n0 = (z**2 * p_estimado * (1 - p_estimado)) / (erro_maximo**2)
    
    if M is not None:
        n = (n0 * M) / (n0 + (M - 1))
    else:
        n = n0
        
    n_final = int(np.ceil(n))
    
    print(f"📐 DIMENSIONAMENTO DE AMOSTRA (PROPORÇÃO)")
    print(f"Erro Máximo (E): {erro_maximo}")
    print(f"p estimado: {p_estimado} (0.5 = conservador)")
    print(f"Tamanho de Amostra Necessário (n): {n_final}")
    
    return n_final

def dimensionar_n_diferenca_medias(
    erro_maximo = 1.0,           # erro máximo na diferença (E)
    sigma1 = 2.0,                # desvio padrão pop 1
    sigma2 = 2.5,                # desvio padrão pop 2
    nivel_confianca = 0.95       # nível de confiança
):
    """
    Tamanho de amostra para cada grupo (n1=n2=n) para estimar a diferença de médias.
    """
    alfa = 1 - nivel_confianca
    z = stats.norm.ppf(1 - alfa/2)
    n = (z**2 * (sigma1**2 + sigma2**2)) / (erro_maximo**2)
    n_final = int(np.ceil(n))
    
    print(f"📐 DIMENSIONAMENTO (DIFERENÇA DE MÉDIAS)")
    print(f"n planejado para CADA grupo: {n_final}")
    return n_final

def dimensionar_n_variancia(
    erro_relativo = 0.10,        # ex: 10% de erro em relação a s²
    nivel_confianca = 0.95
):
    """
    Dimensionamento aproximado para a variância baseado em erro relativo.
    """
    alfa = 1 - nivel_confianca
    z = stats.norm.ppf(1 - alfa/2)
    # Aproximação: n ≈ 1 + 2*(z/erro_relativo)**2
    n = 1 + 2 * (z / erro_relativo)**2
    n_final = int(np.ceil(n))
    
    print(f"📐 DIMENSIONAMENTO (VARIÂNCIA - APROXIMADO)")
    print(f"n necessário para erro relativo de {erro_relativo*100:.1f}%: {n_final}")
    return n_final

if __name__ == "__main__":
    print("--- Exemplos de Dimensionamento ---")
    
    # Dimensionamento para a Média
    dimensionar_n_media(
        erro_maximo = 0.2,       # erro máximo permitido (E)
        desvio_padrao = 1.5,     # desvio padrão (σ) ou estimativa s
        nivel_confianca = 0.95,  # nível de confiança (1-α)
        M = 1000                 # tamanho da população finita (opcional)
    )
    print()
    
    # Dimensionamento para a Proporção
    dimensionar_n_proporcao(
        erro_maximo = 0.03,      # erro máximo (ex: 3% = 0.03)
        p_estimado = 0.5,        # estimativa de p (0.5 para caso conservador)
        nivel_confianca = 0.95,  # nível de confiança (1-α)
        M = None                 # tamanho da população (opcional)
    )
    print()

    # Dimensionamento para a Diferença de Médias
    dimensionar_n_diferenca_medias(
        erro_maximo = 1.0,       # erro máximo na diferença (E)
        sigma1 = 2.0,            # σ da população 1
        sigma2 = 2.5,            # σ da população 2
        nivel_confianca = 0.95   # nível de confiança (1-α)
    )
    print()

    # Dimensionamento para a Variância
    dimensionar_n_variancia(
        erro_relativo = 0.10,    # erro relativo (ex: 10% = 0.10)
        nivel_confianca = 0.95   # nível de confiança (1-α)
    )
    dimensionar_n_diferenca_medias(erro_maximo=0.5, sigma1=2.0, sigma2=2.0)
    print()
    dimensionar_n_variancia(erro_relativo=0.10)
