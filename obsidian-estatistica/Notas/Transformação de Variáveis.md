As variáveis transformadas surgem quando aplicamos uma função matemática aos valores de uma variável aleatória original para definir uma nova medida. Conforme as fontes, o cálculo dos parâmetros (média e variância) dessa nova variável depende de a transformação ser linear ou não linear.

### 1. Transformações Lineares

Uma transformação é linear quando a nova variável ($X$) é definida por uma função do tipo **$X = a + b \cdot Y$**, onde $a$ e $b$ são constantes.

- **Cálculo da Variância:** A variância da variável transformada é o produto do **quadrado da constante multiplicativa** pela variância da variável original: $$\text{Var}(X) = b^2 \cdot \text{Var}(Y)$$ _Nota: A constante aditiva "$a$" não afeta a variância, pois apenas desloca a distribuição sem alterar a sua dispersão._
- **Valor Esperado:** $E(X) = a + b \cdot E(Y)$.
- **Aplicação Prática:** Um exemplo clássico das fontes é a **conversão de escalas de temperatura** (Fahrenheit para Celsius). No Problema 4.4, para converter a variância de ºF para ºC, utiliza-se a constante $b = 5/9$, resultando em $\text{Var}(ºC) = (5/9)^2 \cdot \text{Var}(ºF)$. Outra aplicação comum é o cálculo de **lucro líquido**, onde o lucro é uma função linear das vendas.

### 2. Transformações Não Lineares (Aproximação de Taylor)

Quando a função $\phi(Z)$ é não linear (ex: exponencial, quadrática ou logarítmica), o cálculo exato dos parâmetros é complexo. As fontes recomendam **linearizar a função** através do desenvolvimento em **série de Taylor** em torno do valor esperado ($\mu_Z$), utilizando apenas os dois primeiros termos.

- **Metodologia:** Aproxima-se a curva por uma reta tangente no ponto médio. A função fica aproximada por: $$\phi(Z) \approx \phi(\mu_Z) + (Z - \mu_Z) \cdot \left( \frac{d\phi}{dZ} \right)_{Z=\mu_Z}$$
- **Cálculo da Variância Aproximada:** $$\text{Var}(W) \approx \left( \frac{d\phi}{dZ} \right)^2_{Z=\mu_Z} \cdot \sigma^2_Z$$
- **Valor Esperado Aproximado:** $E(W) \approx \phi(\mu_Z)$.

### 3. Aplicações de Transformações Não Lineares

As fontes apresentam casos críticos onde essa aproximação é fundamental para engenharia e gestão:

- **Cálculo de Volumes:** No Problema 8.5, o volume de uma peça ($V = d_1 \cdot d_2 \cdot d_3$) é uma função não linear das suas dimensões. A variância do volume é estimada usando as derivadas parciais em relação a cada dimensão.
- **Custos de Manutenção:** Frequentemente modelados por funções exponenciais, como $X = 120 e^{0.02(C-\bar{C})}$. A variância do custo é calculada aplicando a regra da derivada da exponencial no ponto médio do consumo.
- **Teor de Humidade:** No Problema 5.4, o "peso do carvão seco" é calculado a partir de uma transformação não linear que envolve o peso húmido e a percentagem de humidade, exigindo a aproximação linear para determinar o desvio padrão final.

**Importante:** A qualidade desta aproximação depende da **curvatura da função** (quanto mais "reta" for a curva perto da média, melhor) e da **dispersão da variável original** (amostras com grande desvio padrão tornam a aproximação linear menos rigorosa).