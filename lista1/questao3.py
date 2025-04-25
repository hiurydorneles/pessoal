normal = float (input("quantas horas voce trabalha: "))
extra = float (input("quntas horas extras voce fez: "))
horanormal = normal * 10
horaextra = extra * 15
salariobruto = horanormal + horaextra
salarioliquido = salariobruto * 0.9
print ("========================================================")
print ("o valor do salário bruto é de: ", salariobruto)
print ("========================================================")
print ("o salario liquido é de: ",salarioliquido)
print ("========================================================")