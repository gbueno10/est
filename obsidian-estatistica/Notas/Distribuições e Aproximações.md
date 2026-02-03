## 💡 Tabela de Critérios de Aproximação (Resumo Rápido)

| De (Original)       | Para (Aproximada) | Critério Exigido                           |
| :------------------ | :---------------- | :----------------------------------------- |
| **Hipergeométrica** | **Binomial**      | $M \geq 10N$                               |
| **Binomial**        | **Poisson**       | $N \geq 20$ e ($Np \leq 7$ ou $Nq \leq 7$) |
| **Binomial**        | **Normal**        | $N \geq 20, Np > 7, Nq > 7$                |
| **Poisson**         | **Normal**        | $\lambda > 10$                             |
| **t-Student**       | **Normal**        | $GL \to \infty$                            |
- **Amostra Grande:** Considerada quando $N \ge 30$ (regra geral) ou $N \ge 50$ (para distribuições muito assimétricas).

### 1. Distribuição Binomial $B(N, p)$

- **Conceito:** Contagem de sucessos em $N$ experiências independentes.
- **Exercício Típico:** **Problema 6.1 (i)** – Calcular a probabilidade de um piloto terminar 2 de 6 grandes prémios, com $p=0.20$.
- **Outro Exemplo:** **Problema 6.3** – Cálculo da probabilidade de rejeição de uma remessa de 10 calços de travão.

### 2. Distribuição de Poisson $Poisson(\lambda)$

- **Conceito:** Eventos raros por unidade de tempo ou espaço.
- **Exercício Típico:** **Problema 6.7 (ii)** – Número de avarias por hora num conjunto de 20 máquinas com taxa horária $\lambda=5$.
- **Outro Exemplo:** **Exemplo do papel** – Cálculo de defeitos em rolos de papel de 100m ou 500m.

### 3. Distribuição Hipergeométrica $H(M, N, p)$

- **Conceito:** Extração sem reposição de populações finitas.
- **Exercício Típico:** **Problema 6.6** – Extração de 5 peças em bloco de um lote de 50 peças.
- **Aproximação para Binomial:** Ocorre quando a população $M$ é muito maior que a amostra $N$ ($M \ge 10N$).
- **Exercício de Aproximação:** **Problema 10.4** – Número de operários que conhecem normas de segurança numa empresa de 4000 funcionários.

### 4. Distribuição Normal $N(\mu, \sigma^2)$

- **Conceito:** Variáveis contínuas e base para o Teorema do Limite Central.
- **Exercício Típico:** **Problema 8.2** – Vendas diárias em lojas do Porto e Lisboa, calculando a probabilidade da soma de vendas.
- **Aproximação da Binomial pela Normal:** Requer $N \ge 20$, $Np > 7$ e $Nq > 7$.
- **Exercício de Aproximação:** **Problema 7.4** – Avaliação da qualidade de peças onde a Binomial é aproximada pela Normal para facilitar o cálculo.

### 5. Distribuição Exponencial Negativa $EN(\lambda)$

- **Conceito:** Tempo ou espaço entre ocorrências sucessivas.
- **Exercício Típico:** **Problema 5.3** – Distância entre o centro do alvo e onde o dardo cai ($X$ com $\lambda=2$).
- **Aplicação Monte Carlo:** **Problema 8.6** – Geração de amostras aleatórias de uma distribuição exponencial para caracterizar a média amostral.

### 6. Distribuição Lognormal $LN(\mu_V, \sigma^2_V)$

- **Conceito:** Quando o logaritmo da variável ($V = \ln X$) segue uma distribuição Normal.
- **Exercício Típico:** **Problema 7.3** – Rendimento mensal de agricultores, exigindo a padronização da variável transformada $V$.

### 7. Distribuição Binomial Negativa e Geométrica

- **Conceito:** Insucessos até ao $r$-ésimo sucesso.
- **Exercício Típico:** **Problema 6.10 (i)** – Probabilidade de ganhar um jogo de dados ao fim de um determinado número de lançamentos.



