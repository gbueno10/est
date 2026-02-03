
## 📑 Resumo das Fórmulas de Variância Amostral ($s^2$)

### 1. Dados em Bruto (Individuais)

**Aplicação:** Quando você tem uma lista solta de números.

- **Fórmula Definição:** $s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$
- **Fórmula de Cálculo (Rápida):** $s^2 = \frac{1}{n-1} \left( \sum x_i^2 - n \bar{x}^2 \right)$

**O que significa cada termo:**

- $s^2$: Variância Amostral.
- $n$: Tamanho total da amostra (contagem de itens).
- $x_i$: Cada valor individual da lista.
- $\bar{x}$: Média aritmética simples.
    

---

### 2. Dados Agrupados Discretos (Frequências)

**Aplicação:** Quando os valores se repetem e estão organizados em "valor vs. quantas vezes ocorreu".

- **Fórmula:** $s^2 = \left( \frac{n}{n-1} \right) \sum f_k(x_k - \bar{x})^2$
    

**O que significa cada termo:**

- $x_k$: O valor da variável (ex: 0 gols, 1 golo).
    
- $f_k$: Frequência relativa ($\frac{\text{frequência absoluta}}{\text{total } n}$).
    
- $n$: Soma de todas as frequências absolutas (total de jogos/casos).
    
- $\bar{x}$: Média ponderada ($\sum x_k \cdot f_k$).
    

---

### 3. Dados Agrupados em Classes (Intervalos)

**Aplicação:** Quando os dados estão escondidos dentro de intervalos (ex: $[10, 20[$).

- **Fórmula:** $s^2 \approx \left( \frac{n}{n-1} \right) \sum f_k(M_k - \bar{x})^2$
    

**O que significa cada termo:**

- $M_k$: **Ponto Médio da Classe** $\left( \frac{\text{Limite Inferior} + \text{Limite Superior}}{2} \right)$.
    
- $f_k$: Frequência relativa daquela classe.
    
- $\bar{x}$: Média calculada usando os pontos médios ($\sum M_k \cdot f_k$).
    

---

## 📋 Guia de Aplicação (Qual usar?)

|**Se o enunciado te der...**|**Use a Fórmula...**|**Por que?**|
|---|---|---|
|Uma lista: $2, 5, 8, 10$|**Bruta (Rápida)**|É a mais direta para bater na calculadora comum.|
|Tabela com "Nº de erros" e "Nº de páginas"|**Agrupada Discreta**|Você ganha tempo tratando os erros como categorias.|
|Tabela com "Alturas [1.50, 1.60["|**Classes**|Você não sabe a altura exata, o $M_k$ é sua única saída.|
|Probabilidades $P(X=x)$ em vez de frequências|**Discreta ($n \to \infty$)**|Nesse caso, $s^2$ vira $\sigma^2$ e o termo $\frac{n}{n-1}$ desaparece.|

---

## 💡 Dica Extra: Desvio Padrão e Coeficiente de Variação

Muitas vezes a prova pede estes dois logo após a variância:

- **Desvio Padrão ($s$):** $s = \sqrt{s^2}$
    
- **Coeficiente de Variação ($CV$):** $CV = \frac{s}{\bar{x}} \times 100\%$ (Serve para comparar a dispersão entre grupos diferentes).
    

---

**Isso ajuda a fechar o seu material de consulta? Se quiser, posso gerar uma imagem com todas essas fórmulas organizadas em um "quadro" para você salvar.**


Tens razão! Para um guia de prova ser útil, precisas de ver o "antes" (o enunciado) e o "depois" (a fórmula aplicada). Aqui está a nota completa e definitiva, com a estrutura de **"Como o professor escreve"** vs. **"O que tu fazes"**.

---

# 📊 Guia Mestre: Variância Amostral ($s^2$)

Este guia serve para identificar o tipo de dados no enunciado e aplicar a fórmula correta.

---

## 1. Dados em Bruto (A Lista)

**Como identificar:** O enunciado dá uma lista simples de números.

> _Ex: "As idades de 5 alunos são: 18, 20, 20, 22, 25."_

- **Fórmula de Cálculo (A mais rápida):**
    
    $$s^2 = \frac{1}{n-1} \left( \sum x_i^2 - n \bar{x}^2 \right)$$
    
- **Aplicação:**
    
    1. $n = 5$ (são 5 números).
        
    2. $\bar{x} = (18+20+20+22+25)/5 = 21$.
        
    3. $\sum x_i^2 = 18^2 + 20^2 + 20^2 + 22^2 + 25^2 = 2253$.
        
    4. $s^2 = \frac{1}{4} (2253 - 5 \cdot 21^2) = \mathbf{12}$.
        

---

## 2. Dados Agrupados Discretos (Frequências)

**Como identificar:** O enunciado fala em "contagens" ou dá uma tabela de valores que se repetem.

> _Ex: "Numa equipa, 2 jogadores marcaram 0 golos, 4 marcaram 1 golo e 4 marcaram 2 golos."_

|**Valor (xk​)**|**Freq (nk​)**|**Freq. Relativa (fk​)**|
|---|---|---|
|0 golos|2|0.2|
|1 golo|4|0.4|
|2 golos|4|0.4|
|**Total**|**$n=10$**|**1.0**|

- **Fórmula:**
    
    $$s^2 = \frac{n}{n-1} \sum f_k(x_k - \bar{x})^2$$
    
- **Aplicação:**
    
    1. Média ($\bar{x}$) = $(0 \cdot 0.2) + (1 \cdot 0.4) + (2 \cdot 0.4) = 1.2$.
        
    2. Variância antes do ajuste = $0.2(0-1.2)^2 + 0.4(1-1.2)^2 + 0.4(2-1.2)^2 = 0.56$.
        
    3. Ajuste Amostral: $s^2 = \frac{10}{9} \cdot 0.56 = \mathbf{0.62}$.
        

---

## 3. Dados Agrupados em Classes (Intervalos)

**Como identificar:** O enunciado usa intervalos ou colchetes. Tu **não sabes** os valores exatos.

> _Ex: "O peso das malas varia entre [10, 20[ kg (5 malas) e [20, 30[ kg (5 malas)."_

|**Classe**|**Freq (nk​)**|**Ponto Médio (Mk​)**|
|---|---|---|
|$[10, 20[$|5|**15**|
|$[20, 30[$|5|**25**|

- **Fórmula:**
    
    $$s^2 \approx \frac{n}{n-1} \sum f_k(M_k - \bar{x})^2$$
    
- **Aplicação:**
    
    1. Trata o $M_k$ como se fosse o valor real.
        
    2. Calcula a média com os pontos médios: $\bar{x} = (15 \cdot 0.5) + (25 \cdot 0.5) = 20$.
        
    3. Calcula a variância: $s^2 = \frac{10}{9} [0.5(15-20)^2 + 0.5(25-20)^2] = \mathbf{27.78}$.
        

---

## 📋 Resumo Visual para a Prova

|**Se vires isto:**|**É este tipo:**|**O que usar como "x":**|
|---|---|---|
|$1, 5, 3, 2, 8$|**Bruto**|O próprio número.|
|"3 vezes o valor 10"|**Discreto**|O valor (10).|
|$[40, 50[$|**Classes**|O meio do intervalo (45).|

---



# 📊 Guia Unificado: Variância Amostral ($s^2$) - Do Enunciado ao Excel

Este guia foi desenhado para consulta rápida em exames. Ele ajuda a identificar o tipo de dado, escolher a fórmula e montar a tabela de cálculo (manual ou Excel).

## 1. Identificação Rápida: O que eu tenho em mãos?

|Se o enunciado apresentar...|Tipo de Dado|O que usar como "$x$"|
|---|---|---|
|Lista solta: $10, 12, 15, 11$|**Dados Brutos**|O próprio valor ($x_i$).|
|Tabela de contagem: "2 erros em 10 páginas"|**Agrupados Discretos**|O valor exato ($x_k$).|
|Tabela de faixas: $[100, 200[$|**Agrupados em Classes**|O Ponto Médio ($M_k = \frac{LimInf + LimSup}{2}$).|

## 2. Cenário A: Dados Brutos (Lista de Valores)

**Uso:** Quando você tem poucos dados e todos são conhecidos individualmente.

### 📝 Fórmulas

- **Média:** $\bar{x} = \frac{\sum x_i}{n}$
    
- **Variância Amostral:** $s^2 = \frac{1}{n-1} \left( \sum x_i^2 - n \bar{x}^2 \right)$
    

### 💻 Estrutura no Excel / Tabela Manual

|Coluna A ($x_i$)|Coluna B ($x_i^2$)|
|---|---|
|Valor 1|$x_1^2$|
|Valor 2|$x_2^2$|
|**SOMA (**$\sum x_i$**)**|**SOMA (**$\sum x_i^2$**)**|

**No Excel use:** `=VAR.S(intervalo_da_coluna_A)`

## 3. Cenário B: Dados Agrupados (Frequências Discretas)

**Uso:** Quando os valores se repetem e o professor dá o "número de ocorrências" ou "probabilidades".

### 📝 Fórmulas

- **Média:** $\bar{x} = \sum (x_k \cdot f_k)$
    
- **Variância Amostral:** $s^2 = \frac{n}{n-1} \sum f_k(x_k - \bar{x})^2$
    

### 💻 Estrutura no Excel (Colunas Necessárias)

Se o professor der apenas a Frequência Absoluta ($n_k$), você deve criar as colunas de apoio:

|A: Valor ($x_k$)|B: Freq ($n_k$)|C: Freq Rel ($f_k$)|D: $x_k \cdot f_k$|E: $(x_k - \bar{x})^2 \cdot f_k$|
|---|---|---|---|---|
|0|5|`=B2/Total_n`|`=A2 * C2`|`=(A2 - $Media)^2 * C2`|
|1|10|...|...|...|
|**TOTAL**|$n$|**1.0**|**Média (**$\bar{x}$**)**|**Soma da Variância**|

> **Cálculo Final:** Multiplique a soma da **Coluna E** por `(n / n-1)`.

## 4. Cenário C: Dados Agrupados em Classes (Intervalos)

**Uso:** Quando os dados estão em faixas. É uma aproximação.

### 📝 Fórmulas

- **Ponto Médio:** $M_k = \frac{LimiteInferior + LimiteSuperior}{2}$
    
- **Variância Amostral:** $s^2 \approx \frac{n}{n-1} \sum f_k(M_k - \bar{x})^2$
    

### 💻 Estrutura no Excel (Colunas Necessárias)

Você precisa extrair o ponto médio antes de tudo:

|A: Classe|B: Freq ($n_k$)|C: Ponto Médio ($M_k$)|D: $M_k \cdot f_k$|E: $(M_k - \bar{x})^2 \cdot f_k$|
|---|---|---|---|---|
|$[10, 20[$|5|**15**|`=C2 * (B2/n)`|`=(C2 - $Media)^2 * (B2/n)`|
|$[20, 30[$|8|**25**|...|...|
|**TOTAL**|$n$|-|**Média (**$\bar{x}$**)**|**Soma da Variância**|

> **Cálculo Final:** Multiplique a soma da **Coluna E** por `(n / n-1)`.

## 5. Resumo de Funções Úteis (Excel/Calculadora)

- **Média:** `=MÉDIA(intervalo)` ou `=AVERAGE(intervalo)`
    
- **Variância Amostral (**$s^2$**):** `=VAR.S(intervalo)` ou `=VAR.P` (se for população total).
    
- **Desvio Padrão (**$s$**):** `=DESVPAD.S(intervalo)` ou `SQRT(variancia)`.
    
- **Coeficiente de Variação:** `=(DesvioPadrão / Média) * 100`.
    

## ⚠️ Checklist Anti-Erro na Prova

1. **Identificou se é Amostra?** Se sim, o ajuste $\frac{n}{n-1}$ ou o divisor $n-1$ é obrigatório.
    
2. **Elevou ao quadrado?** Na variância, as distâncias são sempre ao quadrado. Se der valor negativo, você errou algo.
    
3. **Frequência vs Valor:** Não confunda o $x$ (o que está medindo) com o $n$ (quantas vezes mediu).
    
4. **Unidades:** Variância é $unidade^2$. Se pedir Desvio Padrão, tire a raiz quadrada no final!

---
# ⚽ Resolução Passo a Passo: Variância de Gols

Com base na imagem enviada, vamos organizar os dados e calcular a variância amostral ($s^2$).

## Passo 1: Organizar os Dados e Achar o Total ($n$)

Primeiro, somamos todos os jogos para descobrir o tamanho da amostra.

- **Gols (**$x_k$**):** 0, 1, 2, 3, 4, 5, 6, 7, 8
    
- **Jogos (**$n_k$**):** 4, 12, 18, 6, 5, 3, 1, 0, 1
    

**Cálculo do** $n$**:** $n = 4 + 12 + 18 + 6 + 5 + 3 + 1 + 0 + 1 = \mathbf{50}$

## Passo 2: Calcular a Média Amostral ($\bar{x}$)

Multiplicamos cada número de gols pelo seu respectivo número de jogos e dividimos pelo total.

|Gols ($x_k$)|Jogos ($n_k$)|$x_k \cdot n_k$|
|---|---|---|
|0|4|0|
|1|12|12|
|2|18|36|
|3|6|18|
|4|5|20|
|5|3|15|
|6|1|6|
|7|0|0|
|8|1|8|
|**TOTAL**|**50**|**115**|

**Média (**$\bar{x}$**):** $\bar{x} = \frac{115}{50} = \mathbf{2.3}$ gols por jogo.

## Passo 3: Tabela de Dispersão (O "Coração" da Variância)

Agora calculamos a distância de cada valor para a média, elevamos ao quadrado e multiplicamos pela frequência (jogos). _Fórmula da coluna:_ $n_k \cdot (x_k - 2.3)^2$

|$x_k$|$(x_k - \bar{x})^2$|Multiplicado por $n_k$|Resultado|
|---|---|---|---|
|0|$(0 - 2.3)^2 = 5.29$|$4 \cdot 5.29$|21.16|
|1|$(1 - 2.3)^2 = 1.69$|$12 \cdot 1.69$|20.28|
|2|$(2 - 2.3)^2 = 0.09$|$18 \cdot 0.09$|1.62|
|3|$(3 - 2.3)^2 = 0.49$|$6 \cdot 0.49$|2.94|
|4|$(4 - 2.3)^2 = 2.89$|$5 \cdot 2.89$|14.45|
|5|$(5 - 2.3)^2 = 7.29$|$3 \cdot 7.29$|21.87|
|6|$(6 - 2.3)^2 = 13.69$|$1 \cdot 13.69$|13.69|
|7|$(7 - 2.3)^2 = 22.09$|$0 \cdot 22.09$|0.00|
|8|$(8 - 2.3)^2 = 32.49$|$1 \cdot 32.49$|32.49|
|**SOMA**|||**128.50**|

## Passo 4: Cálculo Final da Variância Amostral ($s^2$)

Lembre-se: como é uma **amostra**, dividimos pelo fator de correção $n - 1$.

$$s^2 = \frac{\text{Soma das Dispersões}}{n - 1}$$$$s^2 = \frac{128.50}{50 - 1} = \frac{128.50}{49}$$

**Resultado Final:**

$$s^2 \approx \mathbf{2.6224}$$

### 📊 Resumo dos Resultados

- **Média (**$\bar{x}$**):** 2.30 gols
    
- **Variância Amostral (**$s^2$**):** 2.62
    
- **Desvio Padrão (**$s$**):** $\sqrt{2.62} \approx 1.62$ gols