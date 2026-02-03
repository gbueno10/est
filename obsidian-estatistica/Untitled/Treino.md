Com base no **Guia Temático 2012-2025** e na análise dos exercícios estruturantes das fontes, selecionei os problemas mais recorrentes em exames da FEUP para você treinar hoje. Esta seleção foca nos "clássicos" que cobrem o ritual obrigatório de resolução exigido pelos professores.

Como os **Testes Não-Paramétricos foram excluídos**, o foco deve ser total na modelagem inicial e na inferência estatística paramétrica ($Z, t, \chi^2, F$).

---

### 🎲 PARTE 1: Teoria da Probabilidade e Modelagem

Estes exercícios cobrem o início da prova (geralmente a Questão 1), focando no Teorema de Bayes e em transformações de variáveis.

1. **Teorema de Bayes (O Clássico):**
    
    - **Problema 3.8 (Máquinas A, B, C):** Essencial para treinar o cálculo da probabilidade inversa (saber a máquina dado que a peça é defeituosa).
    - **Problema 3.7 (Barómetro):** Ótimo para treinar a **Árvore de Resultados** e lidar com previsões erradas.
    - _Dica:_ Veja a resolução do problema de **acidentes aéreos (3.9)** para entender diagnósticos de falha.
2. **Transformação Não Linear (Aproximação de Taylor):**
    
    - **Problema 5.4 (Peso do Carvão Seco):** Um dos mais importantes para treinar o cálculo de valor esperado e desvio padrão quando a função não é linear.
    - **Problema 8.5 (Volume de Peças):** Treina a aplicação de derivadas parciais para encontrar a variância aproximada de um volume.
3. **Soma de Produções (Uso do TLC):**
    
    - **Problema 8.2 (Lojas Porto e Lisboa):** Fundamental para calcular a probabilidade de a **soma das vendas em 200 dias** exceder um limite, usando a aproximação Normal.

---

### 📈 PARTE 2: Distribuições e Amostragem

Foco no uso do Excel/Calculadora e na identificação do modelo correto (Binomial vs. Poisson vs. Normal).

4. **Binomial e Rejeição de Lotes:**
    
    - **Problema 6.3 (Calços de Travão):** Treina o critério de aceitação de remessas com base em amostras pequenas.
5. **Poisson (Eventos por Unidade):**
    
    - **Problema 6.7 (Máquinas):** Focado na contagem de avarias por hora.
    - _Aproximação:_ Veja o **Problema 7.4** para entender quando aproximar uma Binomial por uma Normal ($Np > 7$ e $Nq > 7$).

---

### ⚖️ PARTE 3: Inferência Estatística (I.C. e Testes de Hipótese)

Esta é a parte com maior peso na nota. As questões aqui frequentemente exigem "inverter" a fórmula para achar o $N$.

6. **Dimensionamento de Amostra ($N$):**
    
    - **Problema 10.7 (Tensão de Rotura):** Calcular o $N$ mínimo para uma **amplitude máxima** do I.C. de 60 psi.
    - **Problema 10.8 (Horário de Sábado):** Dimensionamento para **Proporção**, usando o "pior caso" ($\hat{p}=0.5$) se não houver amostra piloto.
7. **Intervalos de Confiança (I.C.):**
    
    - **Problema 10.2 (Cabos - Amostra Pequena):** Uso obrigatório da distribuição **t de Student** ($GL=9$) para médias.
    - **Problema 10.5 (Agências A e B):** Treina a **diferença de médias** entre duas populações independentes.
8. **Testes de Hipótese e Potência ($1-\beta$):**
    
    - **Problema 11.1 (Pneus):** O ritual completo: $H_0$, $H_1$, Estatística e p-value.
    - **Problema 11.8 (Molde de Injeção):** **CRÍTICO.** É o melhor exercício das fontes para treinar o cálculo do **Erro Tipo II ($\beta$)** e da **Potência** do teste.
    - **Problema 11.2 (Anéis de Metal):** Treina a comparação de médias precedida pelo teste de **razão de variâncias (Teste F)**.

---

### 💡 Checklist de Revisão Rápida para amanhã:

- **Definição das variáveis:** Nunca esqueça de escrever "Seja X o peso..." no início da resposta.
- **p-value:** Se $p < \alpha$, rejeita-se $H_0$.
- **Amostras Emparelhadas:** Se os dados forem do mesmo objeto (antes/depois), use a variável diferença $\Delta = X_A - X_B$ (Problema 11.6).
- **Fórmulas:** Tenha as estatísticas de teste de médias e proporções à mão, pois são as mais cobradas.