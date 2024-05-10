
tabela = pd.read_csv('gasolina.csv')
with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(data=tabela, x='dia', y='venda', palette='dark')
  grafico.set(title='Preço médio da gasolina em São Paulo - Julho 2021', xlabel='Dia', ylabel='Preço médio(R$)');
  
