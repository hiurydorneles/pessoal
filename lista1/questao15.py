salario = float (input("digite o salário fixo do funcionário: "))
venda = float (input("digite o valor de suas vendas: "))
valor_comissão = venda * 0.04
comissão = salario + valor_comissão 

print ("o valor da comissao ficou de R$",valor_comissão)
print ("o salario com a comissao adicionada ficou no valor de R$",comissão)