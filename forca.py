from random import randrange

def apresentacao():
    print("************************************")
    print("*****BEM VINDO AO JOGO DE FORCA*****")
    print("************************************\n")

def ler_palavras_do_arquivo(caminho_arquivo):
    palavras = []
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().lower())
    return palavras

def escolher_palavra_aleatoria(palavras):
    indice_aleatorio = randrange(0, len(palavras))
    return palavras[indice_aleatorio]

def exibir_letras_formatadas(letras_formatadas):
    palavra_formatada = " ".join(letras_formatadas)
    print(f"PALAVRA: {palavra_formatada}")

def processar_tentativa(chute, palavra_secreta, letras_formatadas):
    for index, letra in enumerate(palavra_secreta):
        if chute == letra:
            letras_formatadas[index] = chute
    return letras_formatadas

def chute_valido(chute):
    return len(chute) == 1 and chute.isalpha()

def jogar():
    tentativas = 6
    chutes_enviados = []
    apresentacao()
    palavras = ler_palavras_do_arquivo("./palavras.txt")
    palavra_secreta = escolher_palavra_aleatoria(palavras)
    letras_formatadas = ["_" for _ in palavra_secreta]

    while True:
        exibir_letras_formatadas(letras_formatadas)

        if len(chutes_enviados) > 0:
            print(f"CHUTES: {' '.join(chutes_enviados)}")

        chute = input("Digite uma letra do alfabeto: ").strip().lower()
        print("\n")

        if chute_valido(chute):
            chutes_enviados.append(chute)
            if chute in palavra_secreta:
                print("Seu chute existe na palavra secreta!")
                letras_formatadas = processar_tentativa(chute, palavra_secreta, letras_formatadas)
            else:
                print("Seu chute não existe na palavra secreta!")
                tentativas -= 1

                if tentativas == 0:
                    print("Acabaram suas tentativas!")
                    break

                print(f"Você ainda possui {tentativas} tentativas.")
        else:
            print("Chute inválido. Digite apenas uma letra do alfabeto!")
        
        if "_" not in letras_formatadas:
            exibir_letras_formatadas(letras_formatadas)
            print("Você ganhou!")
            break

        print("\n")

    print(f"A palavra era {palavra_secreta}!\n")
    print("Fim de jogo.")

if __name__ == "__main__":
    jogar()
