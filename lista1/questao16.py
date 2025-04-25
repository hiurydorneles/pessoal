peso = float(input("digite o seu peso: "))
valor_engordar = peso * 0.15
valor_emagrecer = peso * 0.20

emagrecer = peso - valor_emagrecer
engordar = peso + valor_engordar

print ("se a voce emagrecer 20% vai pesar",emagrecer,"KGs")
print ("se a voce emagrecer 15% vai pesar",engordar,"KGs")