import re

#Armazenamento do alfabeto.
maiuscula=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
minuscula=[letra.lower() for letra in maiuscula]

#função para criptografar.
def criptografando (letra):
    if letra in maiuscula:
        index= (maiuscula.index(letra)+3)%len(maiuscula)
        return maiuscula[index]
    elif letra in minuscula:
        index= (minuscula.index(letra)+3)%len(minuscula)
        return minuscula[index]
    else:
        return letra
    
#função para verificar senha 

def verificar_chave (chave):
    comprimento = 4
    tem_maiuscula = re.search(r'[A-z]',chave)
    tem_minuscula = re.search(r'[a-z]',chave)
    tem_numero =re.search(r'[0-9]',chave)
    #verificaçao de comprimento da senha 
    if len(chave)!=comprimento:
        return False
    if not tem_maiuscula:
        return False
    if not tem_minuscula:
        return False
    if not tem_numero:
        return False
    return True


#leitura e armazenamento de chave de segurança com regras.
print("Digite uma chave de segurança para criptografar seu texto.\nA chave deve conter 4 caracteres.\nDeve ter pelo menos 1 letra maiuscula.\nDeve ter pelo menos 1 letra minuscula.\nDeve ter pelo menos 1 número.")
key=input()
while verificar_chave(key)==False:
    print('ERRO01. A senha digitada não atende aos requisitos.\nDigite novamente :')
    key=input()

#leitura e armazenamento da entrada.
texto=input("Digite a mensagem que será criptografada :")

#processamento. 
texto_criptografado= ""
for x in texto:
    texto_criptografado+= criptografando(x)

print(texto)
print("texto criptografado :\n"+ texto_criptografado)
