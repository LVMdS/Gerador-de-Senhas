import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~~@#$%^&*()-_=+[]{}/:<>?"

while True:
    try:
        len = int(input("Tamanho da semha: "))
        qty = int(input("Quantidade de senhas: "))
    except ValueError:
        print("Entrada invalida!")
    else:
        for x in range (0,qty):
            Passwd = ""
            for x in range (0,len):
                passchar = random.choice(char)
                Passwd = Passwd + passchar
            print("Senha gerada: ", Passwd)
        break