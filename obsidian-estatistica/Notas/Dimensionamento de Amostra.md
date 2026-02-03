
# 📐 Guia de Dimensionamento de Amostra ($N$)

## 1. O Conceito Universal

Todo Intervalo de Confiança segue a estrutura:

> **I.C. = Estimativa Pontual $\pm$ Erro Amostral**

Onde:

- **Estimativa:** É o dado que você já tem (ex: $\bar{x}$ ou $\hat{p}$).
- **Erro ($E$):** É a semiamplitude do intervalo. Representa o erro máximo que você aceita cometer com a confiança especificada.
- **Amplitude ($A$):** É o intervalo total (de ponta a ponta). Logo, **$A = 2 \times \text{Erro}$**.

---

## 2. O Ritual de Resolução (A Métrica do Isolar)

Para dimensionar a amostra, o problema terá que lhe dar o **Alfa ($\alpha$)** e a **Precisão Desejada** (seja o Erro máximo ou a Amplitude máxima).

**Passo a Passo:**

1. Escreva a fórmula do erro para o caso específico (Média ou Proporção).
2. Coloque o $N$ "em evidência" dentro da fórmula.
3. Substitua os dados e **isole o $N$**.
4. **Regra de Ouro:** O resultado de $N$ deve ser sempre arredondado para o **inteiro superior** ($N_{min}$) para garantir que a condição de precisão seja cumprida.

---

## 3. Aplicação Prática: Caso a Caso

### A. Para o Valor Esperado ($\mu$)

Geralmente assume-se uma amostra grande (Normal).

- **Fórmula do Erro:** $E = z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{N}}$
- **Desenvolvimento para isolar $N$:** $$N \geq \left( \frac{z_{\alpha/2} \cdot \sigma}{E} \right)^2$$
- _Nota:_ Se o dado for a **Amplitude ($A$)**, lembre-se que $E = A/2$.

### B. Para a Proporção Binomial ($p$)

- **Fórmula do Erro:** $E = z_{\alpha/2} \cdot \sqrt{\frac{p(1-p)}{N}}$
- **Desenvolvimento para isolar $N$:** $$N \geq \frac{z_{\alpha/2}^2 \cdot p(1-p)}{E^2}$$
- **E se eu não tiver o valor de $p$? (Pior Caso):** As fontes recomendam assumir **$p = 0.5$**. Este é o valor que maximiza a variância e garante que o tamanho da amostra será suficiente para qualquer proporção real (é o cenário mais conservador).

---

## 4. Exemplos de Exame para Treinar

- **Problema 10.7 (Tensão de Rotura):** Conhecido $\sigma = 70$, pretende-se amplitude $A = 60$ com 99% de confiança. Aplicando a lógica de isolar, chega-se a $N \geq 36.1 \rightarrow \mathbf{N_{min} = 37}$.
- **Problema 10.8 (Sondagem):** Pretende-se margem de erro de 3 pontos percentuais ($E = 0.03$). Sem amostra piloto, usa-se $p = 0.5$. O cálculo resulta em $\mathbf{N_{min} = 349}$.

### 💡 Dica TDAH para o Teste:

Se o enunciado pedir para "não exceder uma amplitude de X", ele está a dizer que **$2 \times \text{Erro} \leq X$**. Escreva isso no rascunho primeiro e o desenvolvimento matemático sairá naturalmente sem precisar decorar fórmulas gigantes de $N$.


Este guia de dimensionamento de amostra foi elaborado com base nas metodologias apresentadas nas fontes, focando no cálculo do tamanho mínimo da amostra ($N$) para garantir a precisão e confiança exigidas em problemas de inferência estatística.

### 1. Lógica Fundamental do Dimensionamento

Dimensionar uma amostra é uma decisão crítica, pois amostras muito grandes desperdiçam recursos e amostras insuficientes não permitem retirar conclusões válidas. A dimensão necessária de uma amostra ($N$) é influenciada por dois fatores principais:

- **Precisão do Intervalo de Confiança:** Quanto menor a **amplitude** desejada para o intervalo (maior precisão), maior deve ser o tamanho da amostra.
- **Nível de Confiança ($1-\alpha$):** Quanto maior a confiança exigida (ex: 99% em vez de 95%), maior será o $N$ necessário.
- **Representatividade:** Independentemente do cálculo, a amostra deve ser sempre **aleatória** para garantir que as inferências sobre a população sejam robustas.

---

### 2. Dimensionamento para o Valor Esperado ($\mu$)

Para determinar o $N$ necessário para estimar a média populacional com uma margem de erro ou amplitude máxima especificada:

#### A. Quando o desvio padrão populacional ($\sigma$) é conhecido:

1. Utilize a fórmula da amplitude do I.C. bilateral baseada na distribuição **Normal (Z)**: $Amplitude = 2 \cdot z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{N}}$.
2. Isole o $N$ para que a amplitude seja menor ou igual ao valor máximo permitido ($E$): $N \ge \left( \frac{2 \cdot z_{\alpha/2} \cdot \sigma}{E} \right)^2$.
3. **Exemplo:** Para um desvio padrão de 70 psi e amplitude máxima de 60 psi a 99% de confiança, o cálculo resulta em $N \ge 37$.

#### B. Quando $\sigma$ é desconhecido:

1. Comece por assumir que a amostra será de **grande dimensão**, utilizando o desvio padrão amostral ($S$) como estimativa de $\sigma$ e a distribuição Normal.
2. Caso o $N$ obtido seja pequeno, deve-se proceder de forma iterativa utilizando a distribuição **t de Student** ($t_{N-1}$), embora isso raramente ocorra em dimensionamentos iniciais de larga escala.

---

### 3. Dimensionamento para a Proporção Binomial ($p$)

Este é o caso mais frequente em sondagens e controlo de qualidade, onde se deseja uma margem de erro em pontos percentuais.

#### Passo a Passo:

1. Defina a amplitude máxima permitida. Se a margem de erro for de 3 pontos percentuais, a amplitude é 0,06.
2. **Cenário 1 - Com Amostra Piloto:** Use a estimativa da proporção ($\hat{p}$) obtida na amostra piloto para calcular o $N$.
3. **Cenário 2 - Sem Amostra Piloto (Pior Caso):** Quando não se conhece $p$, assume-se **$\hat{p} = 0,5$**. Este valor maximiza a variância do estimador e garante que o $N$ calculado será suficiente para qualquer proporção real, sendo a abordagem mais conservadora.
4. **Populações Finitas ($M$):** Se a amostra for retirada de uma população finita sem reposição e a dimensão $N$ for considerável em relação a $M$, deve-se incluir o **fator de redução** $\frac{M-N}{M-1}$ na fórmula.

---
