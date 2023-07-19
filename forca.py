def jogar():
    print("************************************")
    print("*****BEM VINDO AO JOGO DE FORCA*****")
    print("************************************")

    palavra_secreta = "bolacha"
    acerto = False
    enforcou = False
    letras_acertadas = ["_","_","_","_","_","_","_"]

    while(not acerto and not enforcou):
        print(letras_acertadas)

        chute = input("Digite uma letra do alfabeto: ").lower().strip()

        for index, letra in enumerate(palavra_secreta):
            if chute == letra:
                letras_acertadas[index] = chute


    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()