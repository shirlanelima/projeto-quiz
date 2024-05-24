print("Seja bem vindo ao quiz da Lane!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S" :
  quit()

score = 0

print("Começando...") 
print("Qual é a capital da Austrália? \n A) Sydney \n B) Melbourne \n C) Canberra \n D) Brisbane \n")
answer_1 = input("Resposta: ")

if answer_1 == "C":
  print("Correto!")
  score = score + 1
else:
  print("Incorreto!")

print("Em que ano começou a Primeira Guerra Mundial? \n A) 1912 \n B) 1914 \n C) 1916 \n  D) 1918 \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
  print("Correto!")
  score = score + 1
else:
  print("Incorreto!")

print("Qual é o elemento químico com o símbolo 'O'? \n A) Ouro \n B) Oxigênio \n C) Osmio \n D) Oxalato \n")
answer_3 = input("Resposta: ")

if answer_3 == "B":
  print("Correto!")
  score = score + 1
else:
  print("Incorreto!")

print("Qual filme ganhou o Oscar de Melhor Filme em 2020? \n  A) 1917 \n  B) Joker \n  C) Parasita \n D) Era Uma Vez em... Hollywood \n")
answer_4 = input("Resposta: ")

if answer_4 == "C":
  print("Correto!")
  score = score + 1
else:
  print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/4")