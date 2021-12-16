#Aqui eu criei um índice para o array (enumerei os ítens);
#Para fazer esse índice usa o comando enumerate e cria a variável do índice.

def estruturaEnumeraArray():
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]
    for i, m in enumerate(meses):
        print(i, m)

#Chama a função:
estruturaEnumeraArray()
