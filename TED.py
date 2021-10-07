
def tedCalc(z, x, y, c):
    if (c.upper()=="A"):
        print(f"Média aritmetica:  {((z + x + y)/3)}")
    elif(c.upper()=="P"):
        print(f"Média ponderada com pesos de 5, 3 e 2: {((z*5+x*3+y*2)/10)}")
    else:
        print(f"Média harmônica é aproximadamente {(3 / (1/z + 1/x + 1/y))}")

while True:
    n1= float(input("Insira uma nota \n"))
    n2= float(input("Insira uma nota \n"))
    n3= float(input("Insira uma nota \n"))
    Caracter = input("Digite qual media, A = aritmética, P = ponderada e H = harmonica \n")
    tedCalc(n1, n2, n3, Caracter)
    repetir = input("Deseja repetir?(s ou n) \n")
    if(repetir.upper()=="N"):
        print("Programa encerrado")
        break










