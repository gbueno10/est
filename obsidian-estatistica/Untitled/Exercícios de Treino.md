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