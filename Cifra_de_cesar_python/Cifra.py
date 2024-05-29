#Armazenamento do alfabeto
maiuscula=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
minuscula=[letra.lower() for letra in maiuscula]

#função para criptografar 
def criptografando (letra):
    if letra in maiuscula:
        index= (maiuscula.index(letra)+3)%len(maiuscula)
        return maiuscula[index]
    elif letra in minuscula:
        index= (minuscula.index(letra)+3)%len(minuscula)
        return minuscula[index]
    else:
        return letra

#leitura e armazenamento da entrada
texto=input("Digite a mensagem que será criptografada :")

#processamento 
texto_criptografado= ""
for x in texto:
    texto_criptografado+= criptografando(x)

print(texto)
print("texto criptografado :\n"+ texto_criptografado)

    
    
    
    
        

        
    

            


