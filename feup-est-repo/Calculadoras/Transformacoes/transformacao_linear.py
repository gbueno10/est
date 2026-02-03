import numpy as np

def calcular_transformacao_linear(
    mu_y = 3.5,         # Média da variável original E(Y)
    var_y = 1.1,        # Variância da variável original Var(Y)
    a = 0,              # Constante aditiva (deslocamento)
    b = 168             # Coeficiente multiplicativo (escala)
):
    """
    Calcula as propriedades de X = a + b*Y
    """
    # 1. Valor Esperado de X
    mu_x = a + b * mu_y
    
    # 2. Variância de X
    var_x = (b**2) * var_y
    
    # 3. Desvio Padrão de X
    std_x = np.sqrt(var_x)
    
    print(f"📊 RESULTADOS PARA X = {a} + {b}Y")
    print(f"{'='*40}")
    print(f"Y Original:    E(Y) = {mu_y:.4f}  | Var(Y) = {var_y:.4f} | DP(Y) = {np.sqrt(var_y):.4f}")
    print(f"X Transformada: E(X) = {mu_x:.4f}  | Var(X) = {var_x:.4f} | DP(X) = {std_x:.4f}")
    print(f"{'='*40}")

def calcular_propriedades_estatisticas(
    mu_x = 3.5,         # Média da variável original E(X)
    var_x = 1.1,        # Variância da variável original Var(X)
    n = 168,            # Multiplicador ou número de repetições
    b = 0,              # Constante aditiva (opcional)
    tipo = "soma_independente" # 'soma_independente' (soma de n i.i.d) ou 'transformacao_linear' (n*X + b)
):
    """
    Calcula propriedades de uma nova variável Y baseada em X.
    """
    # 1. A Média é igual nos dois casos
    mu_y = n * mu_x + b
    
    # 2. A Variância depende do tipo
    if tipo == "soma_independente":
        var_y = n * var_x 
        descricao = f"SOMA de {n} variáveis independentes"
    elif tipo == "transformacao_linear":
        var_y = (n**2) * var_x
        descricao = f"TRANSFORMAÇÃO LINEAR Y = {n}X + {b}"
    else:
        raise ValueError("Tipo inválido. Use 'soma_independente' ou 'transformacao_linear'")
    
    std_y = np.sqrt(var_y)
    
    print(f"📊 {descricao}")
    print(f"{'='*40}")
    print(f"X Original: E(X) = {mu_x:.4f} | Var(X) = {var_x:.4f}")
    print(f"Nova Média E(Y): {mu_y:.4f}")
    print(f"Nova Variância Var(Y): {var_y:.4f}")
    print(f"Novo Desvio Padrão DP(X): {std_y:.4f}")
    print(f"{'='*40}")

if __name__ == "__main__":
    # Exemplo: X = a + bY
    calcular_transformacao_linear(
        mu_y = 3.5,               # valor esperado de Y [E(Y)]
        var_y = 1.1,              # variância de Y [Var(Y)]
        a = 0,                    # constante aditiva (deslocamento)
        b = 168                   # coeficiente multiplicativo (escala)
    )
    
    print("\n")
    
    # Exemplo: Propriedades de somas ou múltiplos
    calcular_propriedades_estatisticas(
        mu_x = 3.5,               # valor esperado de X [E(X)]
        var_x = 1.1,              # variância de X [Var(X)]
        n = 168,                  # número de repetições ou multiplicador
        b = 0,                    # constante aditiva (opcional)
        tipo = "soma_independente" # 'soma_independente' (n i.i.d) ou 'transformacao_linear' (nX + b)
    )
