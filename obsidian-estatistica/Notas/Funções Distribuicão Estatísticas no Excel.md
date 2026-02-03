
Este guia consolida o uso das distribuições discretas, contínuas e teóricas, focando na consulta rápida de sintaxe e lógica de aplicação.

## 1. Tabelas de Referência Rápida

### A. Funções Essenciais (Inferência e Contínuas)

Utilize estas funções para a maioria dos problemas de Testes de Hipóteses e Intervalos de Confiança.

| **Distribuição**            | **Descobrir Probabilidade (.DIST)**           | **Descobrir Valor Crítico (.INV)**   |
| --------------------------- | --------------------------------------------- | ------------------------------------ |
| **Normal**                  | `NORM.DIST(x; média; desv_padrão; acumulado)` | `NORM.INV(prob; média; desv_padrão)` |
| **Normal Padronizada (Z)**  | `NORM.S.DIST(z; acumulado)`                   | `NORM.S.INV(prob)`                   |
| **t de Student**            | `T.DIST(x; graus_liberdade; acumulado)`       | `T.INV(prob; graus_liberdade)`       |
| **Qui-Quadrado ($\chi^2$)** | `CHISQ.DIST(x; graus_liberdade; acumulado)`   | `CHISQ.INV(prob; graus_liberdade)`   |
| **F **                      | `F.DIST(x; gl1; gl2; acumulado)`              | `F.INV(prob; gl1; gl2)`              |
| **Lognormal**               | `LOGNORM.DIST(x; média; desv; acumulado)`     | `LOGNORM.INV(prob; média; desv)`     |

### B. Distribuições Discretas (Contagem)

Modelam o número de ocorrências ou sucessos em ensaios.

|**Distribuição**|**Função de Probabilidade / Massa**|**Notas Importantes**|
|---|---|---|
|**Binomial**|`BINOM.DIST(sucessos; ensaios; prob_s; acumulado)`|Inversa: `BINOM.INV(ensaios; prob_s; alpha)`|
|**Poisson**|`POISSON.DIST(x; média; acumulado)`|Não possui função `.INV` nativa.|
|**Hipergeométrica**|`HYPGEOM.DIST(sucessos_am; n_am; sucessos_pop; N_pop; acumulado)`|Extração sem reposição.|
|**Binomial Negativa**|`NEGBINOM.DIST(falhas; sucessos_alvo; prob_s; acumulado)`|$y$ insucessos até ao $r$-ésimo sucesso.|
|**Geométrica**|Use `NEGBINOM.DIST` com `sucessos_alvo = 1`|Ou use a fórmula: $p \cdot q^{(y-1)}$.|

---

## 2. Lógica de Aplicação

### DIST vs. INV: Qual escolher?

- **Use `.DIST`** quando você **TEM** o valor da variável ($x$) e **QUER** a probabilidade ($\alpha$).
    
    - _Ex: Qual a chance de um valor ser menor que 10?_
        
- **Use `.INV`** quando você **TEM** a probabilidade ($\alpha$) e **QUER** o valor crítico ($x$ ou $z$).
    
    - _Ex: Qual o valor que deixa 5% de erro na cauda?_
        

### Argumento `CUMULATIVE` (TRUE vs. FALSE)

- **TRUE (1):** Acumula a área desde $-\infty$ até o ponto $x$. ($P(X \leq x)$). É o padrão para a maioria dos testes.
    
- **FALSE (0):** Calcula apenas o ponto exato. Nas discretas, dá a probabilidade de $X = x$. Nas contínuas, dá a densidade (raramente usado).
    

---

## 3. Gestão de Caudas e Testes

O Excel sempre calcula a **cauda esquerda** por padrão. Para outras situações:

- **Cauda Direita ($P(X > x)$):**
    
    - Fórmula: `1 - [Função.DIST]`
        
    - Atalhos: `T.DIST.RT`, `CHISQ.DIST.RT`, `F.DIST.RT`.
        
- **Bilateral (Duas Caudas):**
    
    - Valor de prova (p-value): `T.DIST.2T(x; gl)`.
        
    - Valor crítico: `T.INV.2T(prob; gl)`.
        

---

## 4. Notas Técnicas Adicionais

- **Distribuição Exponencial:** `EXP.DIST(x; lambda; acumulado)`.
    
- **Distribuição Uniforme:** Não existem funções nativas. Use as fórmulas diretas para área e valor crítico baseadas no intervalo $[a, b]$.
    
- **Distribuições de Anexo:** Multinomial e Normal Multivariada exigem cálculos matriciais manuais.
    
