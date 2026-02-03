
### 1. Definição de Variáveis e Acontecimentos

O primeiro passo obrigatório em qualquer exame é a **declaração explícita da terminologia**.

- **Variáveis Aleatórias ($X$ ou $Y$):** Deve-se definir o que a variável mede (ex: $X$: Resistência à compressão das peças).
- **Acontecimentos:** Caso o problema envolva probabilidades antes do teste, definem-se os acontecimentos (ex: $S$: A peça é defeituosa).

---

### 2. Formulação das Hipóteses ($H_0$ e $H_1$)

As hipóteses são afirmações sobre parâmetros populacionais (como a média $\mu$ ou a proporção $p$) que serão testadas com dados amostrais.

- **Hipótese Nula ($H_0$):** Representa o _status quo_ ou a nulidade de efeito. **Nota fundamental:** A $H_0$ contém sempre o sinal de **igualdade** ($=, \leq, \geq$). Na prática de exame, utiliza-se habitualmente o "$=$" por ser o valor mais simples de testar contra a alternativa.
- **Hipótese Alternativa ($H_1$):** É a conjectura que o investigador pretende verificar. Contém sempre uma **desigualdade** ($<, >, \neq$).

---

### 3. Potência de Teste ($1-\beta$)

A **Potência de Teste** é a probabilidade de **rejeitar corretamente a $H_0$** quando ela é, de facto, falsa.

- É considerada uma "coisa boa", pois mede a capacidade do teste em detetar uma diferença real quando ela existe.
- Está diretamente ligada ao **Erro do Tipo II ($\beta$)**, que é a probabilidade de não rejeitar $H_0$ sendo ela falsa. Assim, $\text{Potência} = 1 - \beta$.
- Para aumentar a potência sem prejudicar o nível de significância ($\alpha$), a solução é **aumentar a dimensão da amostra ($N$)**.

---

### 4. Tomada de Decisão e Valor de Prova ($p\text{-value}$)

A decisão baseia-se na comparação entre o nível de significância ($\alpha$), fixado arbitrariamente, e o valor de prova calculado.

**Tabela de Decisão e Erros:**

|Realidade|Decisão: Não Rejeitar $H_0$|Decisão: Rejeitar $H_0$|
|:--|:--|:--|
|**$H_0$ Verdadeira**|Decisão Correcta ($1-\alpha$)|**Erro Tipo I** ($\alpha$)|
|**$H_0$ Falsa**|**Erro Tipo II** ($\beta$)|**Decisão Correcta/Potência** ($1-\beta$)|

**Regra de Decisão pelo Valor de Prova ($p\text{-value}$):**

O $p\text{-value}$ é a probabilidade de obter um resultado tão ou mais extremo que o observado, assumindo $H_0$ verdadeira.

|Comparação|Conclusão Estatística|Significado Prático|
|:--|:--|:--|
|**$p\text{-value} < \alpha$**|**Rejeitar $H_0$**|O resultado é **estatisticamente significativo**; há evidência para $H_1$.|
|**$p\text{-value} \geq \alpha$**|**Não Rejeitar $H_0$**|O teste é **inconclusivo**; não há evidência suficiente para mudar o _status quo_.|

**Lembrete de Exame:** Deve-se apresentar sempre o valor de prova (mesmo que aproximado) e uma conclusão escrita no contexto do enunciado.

---


Calcular a **Potência de Teste ($1-\beta$)** é essencial para medir a utilidade de um teste, ou seja, a sua capacidade de **rejeitar corretamente a hipótese nula ($H_0$)** quando ela é, de facto, falsa.

Aqui está o guia generalizado para o cálculo, seguindo o rigor metodológico das fontes:

---

### 🛡️ 1. O Ritual Inicial (Obrigatório)

Antes de qualquer cálculo de potência, você deve ter definido:

1. **Variáveis e Acontecimentos:** Ex: "$X$ é a resistência à compressão".
2. **Hipóteses:** $H_0: \theta = \theta_0$ (o _status quo_) e $H_1: \theta > \theta_0$ (ou $<, \neq$).
3. **Nível de Significância ($\alpha$):** Probabilidade do Erro Tipo I (rejeitar $H_0$ sendo ela verdadeira).

---

### 📐 2. Passo a Passo do Cálculo da Potência

Para calcular a potência, é forçoso transformar a desigualdade de $H_1$ numa **igualdade específica** (um valor realístico que se suspeita ser o verdadeiro), denotado como $\theta_1$.

#### **Passo A: Determinar a Região Crítica sob $H_0$**

Primeiro, você descobre qual é o "muro" (valor crítico) que separa a aceitação da rejeição de $H_0$.

- Utilize o valor de $\alpha$ (ex: 5%) e a distribuição da Estatística de Teste ($ET$) assumindo $H_0$ verdadeira.
- **Fórmula do Valor Crítico ($X_c$):** Se for um teste de média com $\sigma$ conhecido, $X_c = \mu_0 \pm z_{\alpha} \cdot \frac{\sigma}{\sqrt{n}}$.

#### **Passo B: Caracterizar a Distribuição sob $H_1$**

Agora, esqueça a curva de $H_0$. Desenhe (ou imagine) uma nova curva centrada no valor alternativo $\theta_1$.

- O desvio padrão (erro padrão) geralmente permanece o mesmo ($\frac{\sigma}{\sqrt{n}}$), mas o centro da distribuição desloca-se para $\theta_1$.

#### **Passo C: Calcular a Probabilidade de Rejeição**

A potência é a área da curva de **$H_1$** que cai dentro da **região de rejeição** de $H_0$.

- **Teste Unilateral à Direita:** $\text{Potência} = P(X > X_c \mid \mu = \mu_1)$.
- **Teste Unilateral à Esquerda:** $\text{Potência} = P(X \leq X_c \mid \mu = \mu_1)$.
- **Matematicamente (Z):** $\text{Potência} = P\left(Z > \frac{X_c - \mu_1}{\sigma/\sqrt{n}}\right)$.

---

### 📊 3. Expressão Geral para o Erro Tipo II ($\beta$)

Muitas vezes é mais fácil calcular primeiro o erro $\beta$ (área de não rejeição sob a curva $H_1$) e depois fazer $1 - \beta$.

- **Para testes unilaterais à média:** $$\beta(\mu_1) = P\left[ ET < ET(\alpha) - \frac{|\mu_0 - \mu_1|}{\sigma/\sqrt{n}} \right]$$.
- **Para testes bilaterais:** Pode-se aproximar considerando apenas a cauda mais próxima do valor alternativo, usando $\alpha/2$ na fórmula.

---

### 💡 4. Factores que Affectam a Potência

De acordo com os manuais, a potência aumenta quando:

1. **Aumenta o Nível de Significância ($\alpha$):** Mas cuidado, isso aumenta o risco de Erro Tipo I.
2. **Aumenta o Tamanho da Amostra ($n$):** É a única forma de diminuir simultaneamente $\alpha$ e $\beta$, pois reduz a variância da estatística de teste.
3. **Aumenta o Afastamento:** Quanto maior a distância entre a realidade ($\theta_1$) e a hipótese nula ($\theta_0$), mais fácil é para o teste detectar a diferença.

---

### 📝 Exemplo Prático (Problema 11.8)

- **Cenário:** $H_0: \mu = 5.18$ vs $H_1: \mu < 5.18$. Valor crítico calculado $X_c = 5.06$.
- **Valor Real:** Supondo $\mu_1 = 4.90$.
- **Cálculo:** A potência é a probabilidade de obter um valor $\leq 5.06$ na curva centrada em $4.90$.
- **Resultado:** Padronizando $Z = \frac{5.06 - 4.90}{0.25/\sqrt{12}} = 2.22$. A potência é $P(Z < 2.22) = 98.7%$.

**Nota Final:** Para testes de variância ou quando se usa a distribuição $t$ de Student com amostras pequenas, o cálculo de $\beta$ não é imediato e pode exigir técnicas de simulação ou cálculos iterativos.