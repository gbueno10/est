# Copilot Instructions for Statistical Distributions & Hypothesis Testing

## Project Overview
**EST** (Estatística) is an educational Python project providing calculators for statistical distributions and hypothesis tests in Portuguese. The codebase comprises Jupyter notebooks for interactive exploration and a supporting Python module for parametric test calculations.

### Key Components
- **[Distribuicoes/](Distribuicoes/)**: Interactive notebooks for continuous (Normal, t, Chi-square, F, Exponential, Uniform) and discrete (Binomial, Poisson, Geometric) distributions
- **[Testes/](Testes/)**: Hypothesis testing notebook covering parametric tests (t-test, Z-test, F-test, Chi-square)
- **[Testes_de_Hipotese_calc.py](Testes_de_Hipotese_calc.py)**: Library with 20+ test functions returning dictionaries with test statistics, p-values, critical values, and power analysis

## Architecture & Data Flow
**Distribution Notebooks → Test Calculations → Hypothesis Testing Notebook**

1. **Distribution Calculators** (`Distribuicoes/` notebooks): Use `scipy.stats` to compute PDFs/PMFs, CDFs, quantiles, and visualize results with matplotlib
2. **Hypothesis Test Engine** ([Testes_de_Hipotese_calc.py](Testes_de_Hipotese_calc.py)): Dictionary-based return pattern enables programmatic access to all test outputs (test statistic, p-value, critical values, power)
3. **Test Application** ([Testes/](Testes/) notebooks): Import and call calculation functions; visualize test results

## Critical Conventions & Patterns

### Naming Conventions (Portuguese + descriptive)
- Test functions: `teste_<distribution>_<parameter>_<scope>_parametros` (e.g., `teste_t_media_uma_amostra_parametros`)
- Variables: `tipo_teste` ('duas_caudas'/'cauda_esquerda'/'cauda_direita'), `alfa` (significance level), `graus_de_liberdade` (degrees of freedom)
- Returns: Always a **dictionary** with keys: `estatistica_teste`, `p_valor`, `hipotese_rejeitada`, `alfa`, `tipo_teste`, `valor_critico`, `power` (optional)

### Distribution Calculation Pattern
All distribution functions follow this pattern:
```python
def calcular_<distribuição>(param1=default, param2=default, tipo='cdf', x=value, p=0.95):
    dist = stats.<scipy_dist>(param1, param2)
    print(f"📊 <DIST_NAME> (params)")
    # tipo: 'cdf', 'sf', 'ppf', 'isf', 'interval', 'two_tailed'
    # Visualization with matplotlib showing filled areas under curves
    fig, ax = plt.subplots(figsize=(10, 4))
    # ... plotting code ...
    ax.legend()  # NO plt.show() - causes kernel hang in Jupyter!
```
**CRITICAL**: Never use `plt.show()` in notebooks - it causes kernel hangs. Use `%matplotlib inline` in setup cell instead. Always include **emoji annotations** (📊 for distribution, ❌ for errors) and **matplotlib visualizations** with shaded regions.

### Test Output Structure
Every test function returns a dictionary for consistent programmatic access:
```python
{
    'estatistica_teste': float,
    'p_valor': float,
    'hipotese_rejeitada': bool,  # p_valor < alfa
    'valor_critico': float or tuple,  # tuple for two-tailed
    'graus_de_liberdade': int,
    'power': float or None  # if alternative parameter provided
}
```

## Supported Test Families

### Parametric Tests (Implemented)
- **One-sample**: t-test, Z-test, Chi-square variance
- **Two-sample independent**: t-test (equal/unequal variance), Z-test, F-test for variances
- **Two-sample dependent/paired**: t-test
- **k-samples**: ANOVA (one-way)
- **Power Analysis**: Integrated into all tests via optional `_alternativa` parameters

### scipy.stats Mapping
- Normal: `stats.norm(mu, sigma)`
- t-distribution: `stats.t(df)`
- Chi-square: `stats.chi2(df)`
- F-distribution: `stats.f(dfn, dfd)`

## Developer Workflows

### Running Notebooks
1. Open notebook in VS Code
2. Select Python kernel (uses local `scipy`, `numpy`, `matplotlib`)
3. **MUST run Setup cell first** - includes `%matplotlib inline` magic command
4. Run Funções cell to load all calculation functions
5. Run individual distribution/test cells as needed

**Common Issues:**
- **Kernel hangs/restarts**: Check for `plt.show()` calls - remove them (graphs auto-display with `%matplotlib inline`)
- **Indentation errors**: Ensure function calls in test cells have no leading spaces
- **Style warnings**: `seaborn-v0_8-darkgrid` may not exist; code uses try/except fallback to 'default'

### Adding a New Test
1. Define function in [Testes_de_Hipotese_calc.py](Testes_de_Hipotese_calc.py) following naming/return conventions
2. Add test cells to [Testes/Testes_de_Hipotese_NoWidgets.ipynb](Testes/Testes_de_Hipotese_NoWidgets.ipynb)
3. Include visualization of test statistic distribution and rejection region
4. Document parameter interpretation in docstring

### Adding a Distribution
1. Create function in `Distribuicoes/*` notebook cell
2. Support all calculation types: `cdf`, `sf`, `ppf`, `isf`, `interval`, `two_tailed`
3. Generate matplotlib plot with:
   - Probability density/mass function line
   - Filled region(s) for calculated probability
   - Legend and labels
   - **End with `ax.legend()` - NEVER `plt.show()`**
   - Consistent styling (try `seaborn-v0_8-darkgrid`, fallback to `default`)

### Notebook Setup Cell Pattern
Every notebook must start with:
```python
%matplotlib inline  # CRITICAL - enables inline plots without plt.show()
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo dos gráficos
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    plt.style.use('default')
```

## Dependencies & Environment
- **numpy**: 1.24.0+ (array operations)
- **scipy**: 1.10.0+ (probability distributions, statistical functions)
- **matplotlib**: 3.7.0+ (visualization)
- **seaborn**: 0.12.0+ (optional, improved plot styling)

Install via: `pip install -r requirements.txt`

## Integration Points & External Dependencies
- **scipy.stats**: All probability distributions and quantile functions
- **matplotlib**: Visualization layer; all outputs via `plt.show()`
- No external APIs or databases; fully self-contained computational library
