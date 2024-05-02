import pandas as pd
import seaborn as sns

df_gasolina = pd.read_csv('gasolina.csv')

gasolina = sns.lineplot(x='dia', y='venda', data=df_gasolina)
gasolina.set(title='Vendas de Gasolina por Dia', xlabel='Dia', ylabel='Venda (em unidades)')
gasolina.get_figure().savefig(fname='gasolina.png', bbox_inches='tight')