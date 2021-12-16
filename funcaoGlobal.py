#Em Python, a indentação delimita a função.
#Criando uma função:

def algumaFuncao():
    global f
    f= "novoValor"
    print(f)

#Não esqueça de chamar a função para que ela seja executada.

algumaFuncao()
print(f)

#Quando dentro da função damos um novo valor para a variável, esta funciona como variável local;
#Quando dentro da função colocamos -> global e a variável, esta funciona como variável global.

