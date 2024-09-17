import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lê os dados do arquivo
    df = pd.read_csv('https://raw.githubusercontent.com/rokidory/boilerplate-sea-level-predictor/main/epa-sea-level.csv')

    # Cria o gráfico de dispersão (scatter plot)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Cria a primeira linha de melhor ajuste
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(df['Year'].min(), 2051)
    y_values = [intercept + slope * x for x in x_values]
    plt.plot(x_values, y_values, 'r')  # Desenha a linha de ajuste em vermelho

    # Cria a segunda linha de melhor ajuste a partir do ano 2000
    df_2000 = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_values = range(df_2000['Year'].min(), 2051)
    y_values = [intercept + slope * x for x in x_values]
    plt.plot(x_values, y_values, 'g')  # Desenha a linha de ajuste em verde

    # Adiciona rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Salva o gráfico e retorna o eixo para testes (NÃO MODIFIQUE)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
