import pandas as pd


df = pd.read_csv('DadosEmpresa.csv')

print("\n Este é o print das colunas e primeiras linhas dos dados: \n ")

print(df.head())

print("\n Empresas com opcao_pelo_simples == SIM: \n")

df_opcao_pelo_sim = (df.query('opcao_pelo_simples == "SIM"'))
print(len(df_opcao_pelo_sim.index))

print("\n Soma do capital_social de todas as empresas: \n")

print(df["capital_social"].sum(axis = 0))

print("\n Empresas com capital_social entre 10.000 e 20.000: \n")

df_capital_social = (df.query('capital_social > 10000 & capital_social < 20000'))

print(df_capital_social)

df_enderecos = pd.read_csv('DadosEndereco.csv')

print("\n Dados de enderecos (os 5 primeiros): \n")
print(df_enderecos.head())

print("\n Merge entre os dois datasets:\n")

df_merge = pd.merge(df,df_enderecos,on = "cnpj")
print(df_merge.head())

print("\n Empresas de Curitiba e gerando arquivo: \n")
df_curitiba = (df_merge.query('municipio == "CURITIBA"'))
print(df_curitiba)

df_curitiba.to_csv('EmpresasCuritiba.csv')
