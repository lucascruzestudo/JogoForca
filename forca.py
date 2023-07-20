def jogar():
    print("************************************")
    print("*****BEM VINDO AO JOGO DE FORCA*****")
    print("************************************")

    palavra_secreta = "bolacha"
    venceu = False
    enforcou = False
    erros = 0
    letras_acertadas = ["_","_","_","_","_","_","_"]

    while(not venceu and not enforcou):
        print(f"\n{letras_acertadas}")

        chute = input("Digite uma letra do alfabeto: ").strip().lower()

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = chute
        else:
            print("Letra não existe na palavra secreta!")
            erros += 1

        venceu = "_" not in letras_acertadas
        
        enforcou = erros == 6

    if(venceu):
        print("Você ganhou!")
    else:
        print("Acabaram suas tentativas!")
        
    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()