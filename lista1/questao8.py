altura_pessoa = float(input("Sua altura (m): "))
sombra_pessoa = float(input("Sombra da pessoa (m): "))
sombra_predio = float(input("Sombra do prédio (m): "))
altura_predio = (sombra_predio * altura_pessoa) / sombra_pessoa
print(f"Altura do prédio: {altura_predio}m")
