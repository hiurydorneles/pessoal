lata = 0.350
garrafa = 0.600
litro = 2
compralata = int(input("digite quantas latas voce ira comprar: "))
compragarrafa = int(input("digite quantas garrafas voce ira comprar: "))
compralitro = int(input("digite quantos litroa voce ira comprar: "))
print ("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
totallata = compralata * lata
totalgarrafa = compragarrafa * garrafa
totallitro = compralitro * litro

total = totallata + totalgarrafa + totallitro
print ("voce comprou",total,"litros de refrigerante")