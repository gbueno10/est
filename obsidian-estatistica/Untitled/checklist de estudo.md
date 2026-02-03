
### 1. Probabilidade e Modelagem
*   **Teorema de Bayes e Probabilidade Condicional**:
    *   Cálculo de probabilidade inversa (ex: probabilidade de uma causa de morte dado um histórico familiar, ou de um e-mail ser spam dado que foi bloqueado).
    *   Probabilidades em cadeias de decisão ou filtragem (servidor de envio → servidor de destino → inbox).
*   **Transformação e Funções de Variáveis Aleatórias**:
    *   Cálculo de probabilidade de custos ou rendimentos baseados em funções não-lineares (ex: $X = 120 e^{0,02(C-\bar{C})}$).
    *   Determinação do valor esperado e desvio padrão de funções de variáveis conhecidas.
*   **Soma e Média de Variáveis**:
    *   Probabilidade de a soma de várias produções diárias (semanais/mensais) exceder um limite.
    *   Probabilidade de recursos totais (ex: água ou donativos) serem suficientes para cobrir um lote ou uma obra.

### 2. Distribuições de Probabilidade
*   **Distribuição Normal**:
    *   Cálculo de probabilidades em intervalos e caudas (ex: peso de garrafões, altura de alunos, produção de papel).
    *   Identificação de valores centrais ou limites para cumprir uma probabilidade máxima de erro.
*   **Distribuições Discretas (Binomial e Poisson)**:
    *   **Poisson**: Contagem de eventos por tempo ou lote (ex: táxis por hora, defeitos por turno, falhas de entrega).
    *   **Binomial**: Probabilidade de rejeição de lotes com base em amostras (quantos itens falham numa inspeção).
    *   **Aproximações**: Uso da Normal para aproximar somas de variáveis de Poisson ou outras distribuições.

### 3. Inferência Estatística (Onde as fórmulas são "invertidas")
*   **Dimensionamento de Amostra ($N$)**:
    *   Cálculo do $N$ mínimo para garantir uma **margem de erro máxima** (amplitude) num intervalo de confiança.
    *   Cálculo do $N$ necessário para que a probabilidade de rejeição seja superior a um valor.
    *   Cálculo do $N$ para garantir uma probabilidade de confiança mínima (ex: 99%) em resultados críticos.
*   **Intervalos de Confiança (I.C.)**:
    *   Construção de I.C. para médias (com variâncias iguais ou diferentes), proporções e variâncias.
    *   Uso do I.C. para verificar suspeitas ou conjeturas da empresa.
*   **Testes de Hipótese e Potência**:
    *   Comparação de duas populações (médias ou proporções) para verificar superioridade ou diferença.
    *   **Cálculo da Potência do Teste ($1-\beta$)**: Determinar a probabilidade de detectar uma diferença real quando ela existe.
    *   Teste de igualdade de variâncias (Teste F).
----




#### A. Módulo de Probabilidade e Bayes

- **O que automatizar**: O Teorema de Bayes para probabilidades "inversas".
- **Dica Prática**: Crie uma função que aceite $P(A)$, $P(B|A)$ e $P(B|\bar{A})$ para retornar $P(A|B)$.
- **Transformações**: Implemente a aproximação por **Série de Taylor** para funções não-lineares, calculando o valor esperado $E[W] \approx \phi(\mu_z)$ e a variância $Var(W) \approx (\phi'(\mu_z))^2 \cdot \sigma^2_z$.

#### B. Módulo de Distribuições (O "Macro")

- **O que automatizar**: Cálculos de probabilidade acumulada (CDF) e valores críticos (Inverse CDF/PPF) para as distribuições **Normal, t-Student, Qui-Quadrado e F**.
- **Aproximações**: Crie verificadores automáticos para saber se deve usar Normal ou Poisson para aproximar uma Binomial (ex: $N \geq 20$ e $Np > 7$).

#### C. Módulo de Inferência (Onde as fórmulas "invertem")

- **Cálculo de $N$**: Funções para isolar o tamanho da amostra necessário para atingir uma margem de erro específica em médias e proporções.
- **Exemplo**: Para um erro $E$ e confiança $1-\alpha$: $N \geq \left( \frac{Z_{\alpha/2} \cdot \sigma}{E} \right)^2$.
- **Potência ($1-\beta$)**: Script que calcula a área sob a curva de $H_1$ que cai na região de rejeição de $H_0$. Use a fórmula geral: $\beta(\mu_1) = P\left( Z < Z_{\alpha} - \frac{|\mu_0 - \mu_1|}{\sigma/\sqrt{n}} \right)$.

---


### 3. Checklist de Preparação Final

#### Conteúdo de Probabilidade e Variáveis

- [ ] **Bayes**: Script testado com exemplos de diagnóstico médico.
- [ ] **Soma de Variáveis**: Fórmula para $Var(\sum X_i) = \sum Var(X_i)$ se independentes.
- [ ] **Lognormal**: Conversão de parâmetros $(\mu_x, \sigma_x)$ para $(\mu_v, \sigma^2_v)$ usando $ln$.

#### Conteúdo de Inferência Estatística

- [ ] **Tabela de Estatísticas de Teste**: Lista completa de fórmulas para $Z_{calc}$ e $t_{calc}$.
- [ ] **Diferença de Médias (Variâncias Diferentes)**: Nota sobre o **Teste de Welch**.
- [ ] **Dimensionamento ($N$)**: Calculadora Python para isolar $N$ em intervalos de confiança de proporção (pior caso: $p=0.5$).
- [ ] **Potência do Teste**: Guia visual de como o valor crítico de $H_0$ se torna o ponto de corte para a área de $\beta$ em $H_1$.

#### Configuração Tecnológica (Pen Drive)

- [ ] **Python Portátil**: Garantir que o ambiente (como Jupyter ou VS Code) rode sem internet.
- [ ] **Bibliotecas**: Ter `scipy.stats`, `numpy` e `matplotlib` instaladas (essenciais para CDF, INV e gráficos) [histórico da conversa].
- [ ] **Base de Dados do Obsidian**: Pasta de notas indexada para pesquisa rápida (`Ctrl+O`).

### Dica TDAH para a Prova

Nos testes de hipótese, siga sempre o "ritual" dos 4 passos descrito nas fontes: 1. Definir Hipóteses; 2. Identificar Estatística/Distribuição; 3. Definir Regra de Decisão ($\alpha$); 4. Calcular e Concluir com o **p-value**. O Python garantirá o passo 4, enquanto o Obsidian garante os passos 1, 2 e 3.


Com base nos exames mais recentes (2020 a 2025) e nos problemas estruturados do livro, selecionei os exercícios que cobrem exatamente o que o professor tem cobrado e no nível de dificuldade esperado.

Esta seleção foi pensada para você testar suas **calculadoras Python** e seus **guias no Obsidian**.

---

### Bloco 1: Probabilidade e Teorema de Bayes (20% da prova)

Estes exercícios focam na "probabilidade inversa", o clássico da Questão 1.

- **Problema 3.7 (Barômetro/Previsão do Tempo):** Excelente para praticar a montagem da árvore de decisão e aplicar Bayes para descobrir a probabilidade de "sol dado que a previsão é chuva".
- **Problema 3.8 (Máquinas A, B e C):** Treina o cálculo da probabilidade de uma peça defeituosa ter vindo de uma máquina específica (em especial a de menor produção).
- **Exame 25-26, Questão 1 (Histórico de Doença Cardíaca):** Este é o modelo mais atual. Trabalha com uma amostra de 1000 homens e exige separar claramente os grupos com e sem histórico familiar.

### Bloco 2: Modelagem e Transformação de Variáveis (30% da prova)

Foco em funções não-lineares e somas de variáveis (muito comum em problemas de "lotes").

- **Exame 25-26, Questão 2 (Custo de Manutenção):** **Obrigatório.** Trabalha com a fórmula $X = 120 e^{0.02(C-\bar{C})}$. Você precisará usar a **aproximação por Série de Taylor** para achar o valor esperado e a variância.
- **Problema 8.2 (Duas lojas, 200 dias):** Treina a aplicação do **Teorema do Limite Central** para a soma de vendas em um período longo. É o exercício ideal para validar sua calculadora de "Soma de Variáveis Normais".
- **Problema 5.4 (Peso do Carvão Seco):** Um exercício clássico de transformação de variáveis onde o erro de umidade e o erro da balança se combinam.

### Bloco 3: Inferência Estatística (50% da prova - O Coração)

Aqui estão os exercícios que exigem o "ritual" dos 4 passos e as inversões (N e Potência).

- **Exame 20-21, Questão 3 (Altura de Alunos UP):** **O mais completo.** Ele pede:
    1. Teste de hipótese para médias com **variâncias diferentes (Welch)**.
    2. Teste para verificar se as **variâncias são iguais (Teste F)**.
    3. Cálculo da **Potência do Teste** se a média real mudar.
    4. Construção de **Intervalo de Confiança para a Variância**.
- **Problema 11.9 (Máquinas A e B - Veios):** Compara duas populações tanto na **precisão (variância)** quanto na **proporção de defeituosos**.
- **Problema 10.7 e 10.8 (Dimensionamento):** Focados puramente em **descobrir o N**. O 10.7 foca em tensão de rotura (média) e o 10.8 em horários de aulas (proporção).

### Bloco 4: Não-Paramétricos e Ajuste

Para quando o professor pede para "verificar a normalidade" ou "repetir sem assumir normalidade".

- **Problema 12.3 (Atrasos de Comboios):** Treina o teste de **Kolmogorov-Smirnov (Lilliefors)** para verificar se os dados seguem uma distribuição Normal.
- **Problema 12.9 (Frequência vs. Sucesso):** Ótimo para praticar o **Coeficiente de Spearman** e testar se existe associação direta entre duas variáveis quantitativas sem assumir normalidade .

---

### Dicas para a sua Revisão com Obsidian + Python:

1. **Isolamento do N:** No Obsidian, tenha uma nota clara: "Como isolar N quando a amplitude do I.C. é dada". Use o **Problema 10.7** para conferir se sua fórmula no Python está batendo com o resultado de $N=37$.
2. **O p-value Bilateral:** Lembre-se que se o seu script Python cuspir a área de apenas uma cauda e o teste for $\neq$, você deve multiplicar por 2. Use o **Problema 11.9** para validar isso.
3. **Welch vs. Pool:** Tenha um _if-else_ no seu código Python: "Se o Teste F rejeitar a igualdade de variâncias, use a fórmula de Welch para os graus de liberdade". O **Exame 20-21 (Questão 3)** é o seu padrão de teste para isso.

### Bloco 1: Probabilidade e Teorema de Bayes (20% da prova)

Estes exercícios focam na "probabilidade inversa", o clássico da Questão 1.

- **Problema 3.7 (Barômetro/Previsão do Tempo):** Excelente para praticar a montagem da árvore de decisão e aplicar Bayes para descobrir a probabilidade de "sol dado que a previsão é chuva".
- **Problema 3.8 (Máquinas A, B e C):** Treina o cálculo da probabilidade de uma peça defeituosa ter vindo de uma máquina específica (em especial a de menor produção).
- **Exame 25-26, Questão 1 (Histórico de Doença Cardíaca):** Este é o modelo mais atual. Trabalha com uma amostra de 1000 homens e exige separar claramente os grupos com e sem histórico familiar.

### Bloco 2: Modelagem e Transformação de Variáveis (30% da prova)

Foco em funções não-lineares e somas de variáveis (muito comum em problemas de "lotes").

- **Exame 25-26, Questão 2 (Custo de Manutenção):** **Obrigatório.** Trabalha com a fórmula $X = 120 e^{0.02(C-\bar{C})}$. Você precisará usar a **aproximação por Série de Taylor** para achar o valor esperado e a variância.
- **Problema 8.2 (Duas lojas, 200 dias):** Treina a aplicação do **Teorema do Limite Central** para a soma de vendas em um período longo. É o exercício ideal para validar sua calculadora de "Soma de Variáveis Normais".
- **Problema 5.4 (Peso do Carvão Seco):** Um exercício clássico de transformação de variáveis onde o erro de umidade e o erro da balança se combinam.

### Bloco 3: Inferência Estatística (50% da prova - O Coração)

Aqui estão os exercícios que exigem o "ritual" dos 4 passos e as inversões (N e Potência).

- **Exame 20-21, Questão 3 (Altura de Alunos UP):** **O mais completo.** Ele pede:
    1. Teste de hipótese para médias com **variâncias diferentes (Welch)**.
    2. Teste para verificar se as **variâncias são iguais (Teste F)**.
    3. Cálculo da **Potência do Teste** se a média real mudar.
    4. Construção de **Intervalo de Confiança para a Variância**.
- **Problema 11.9 (Máquinas A e B - Veios):** Compara duas populações tanto na **precisão (variância)** quanto na **proporção de defeituosos**.
- **Problema 10.7 e 10.8 (Dimensionamento):** Focados puramente em **descobrir o N**. O 10.7 foca em tensão de rotura (média) e o 10.8 em horários de aulas (proporção).

### Bloco 4: Não-Paramétricos e Ajuste

Para quando o professor pede para "verificar a normalidade" ou "repetir sem assumir normalidade".

- **Problema 12.3 (Atrasos de Comboios):** Treina o teste de **Kolmogorov-Smirnov (Lilliefors)** para verificar se os dados seguem uma distribuição Normal.
- **Problema 12.9 (Frequência vs. Sucesso):** Ótimo para praticar o **Coeficiente de Spearman** e testar se existe associação direta entre duas variáveis quantitativas sem assumir normalidade .

---

### Dicas para a sua Revisão com Obsidian + Python:

1. **Isolamento do N:** No Obsidian, tenha uma nota clara: "Como isolar N quando a amplitude do I.C. é dada". Use o **Problema 10.7** para conferir se sua fórmula no Python está batendo com o resultado de $N=37$.
2. **O p-value Bilateral:** Lembre-se que se o seu script Python cuspir a área de apenas uma cauda e o teste for $\neq$, você deve multiplicar por 2. Use o **Problema 11.9** para validar isso.
3. **Welch vs. Pool:** Tenha um _if-else_ no seu código Python: "Se o Teste F rejeitar a igualdade de variâncias, use a fórmula de Welch para os graus de liberdade". O **Exame 20-21 (Questão 3)** é o seu padrão de teste para isso.