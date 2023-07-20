from random import randrange

def jogar():
    
    tentativas = 6
    chutes_enviados = []
    apresentacao()
    palavras = ler_palavras_do_arquivo("./palavras.txt")
    palavra_secreta = escolher_palavra_aleatoria(palavras)
    caracteres_palavra = inicializador_de_caracteres(palavra_secreta)

    while True:

        exibir_situacao_palavra(caracteres_palavra)

        if len(chutes_enviados) > 0:
            print(f"CHUTES: {' '.join(chutes_enviados)}")

        chute = receber_chute()
        print("\n")

        if chute_valido(chute):

            chutes_enviados.append(chute)

            if chute in palavra_secreta:
                print("Seu chute existe na palavra secreta!")
                caracteres_palavra = processar_tentativa(chute, palavra_secreta, caracteres_palavra)

            else:
                print("Seu chute não existe na palavra secreta!")
                tentativas -= 1

                if tentativas == 0:
                    mensagem_perdedor()
                    break

                print(f"Você ainda possui {tentativas} tentativas.")

        else:

            print("Chute inválido. Digite apenas uma letra do alfabeto!")
        
        if "_" not in caracteres_palavra:
            exibir_situacao_palavra(caracteres_palavra)
            mensagem_ganhador()
            break

        print("\n")

    print(f"A palavra era {palavra_secreta}!\n")
    print("Fim de jogo.")

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

def exibir_situacao_palavra(caracteres_palavra):
    palavra_formatada = " ".join(caracteres_palavra)
    print(f"PALAVRA: {palavra_formatada}")

def processar_tentativa(chute, palavra_secreta, caracteres_palavra):
    for index, letra in enumerate(palavra_secreta):
        if chute == letra:
            caracteres_palavra[index] = chute
    return caracteres_palavra

def chute_valido(chute):
    return len(chute) == 1 and chute.isalpha()

def inicializador_de_caracteres(palavra_secreta):
    caracteres = ["_" for _ in palavra_secreta]
    return caracteres

def receber_chute():
    chute = input("Digite uma letra do alfabeto: ").strip().lower()
    return chute

def mensagem_perdedor():
    print("\nVOCÊ FOI ENFORCADO!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           \n")

def mensagem_ganhador():
    print("\nVOCÊ ESCAPOU DA FORCA!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \n")

if __name__ == "__main__":
    jogar()
