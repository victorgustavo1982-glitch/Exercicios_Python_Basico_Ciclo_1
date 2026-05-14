# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
dias_numerais = int(input("Digite um número do dia da semana: "))

if dias_numerais == 1:
    print("Domingo")
elif dias_numerais == 2:
    print("Segunda-feira")
elif dias_numerais == 3:
    print("Terça-feira")
elif dias_numerais == 4:
    print("Quarta-feira")
elif dias_numerais == 5:
    print("Quinta-feira")
elif dias_numerais == 6:
    print("Sexta-feira")
elif dias_numerais == 7:
    print("Sábado")
else:
    print("Número errado")