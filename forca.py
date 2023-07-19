def jogar():
    print("************************************")
    print("*****BEM VINDO AO JOGO DE FORCA*****")
    print("************************************")

    palavra_secreta = "bolacha"
    acerto = False
    enforcou = False

    while(not acerto and not enforcou):
        print("Jogando...")

        chute = input("Digite uma letra do alfabeto: ").lower().strip()

        for index, letra in enumerate(palavra_secreta):
            if chute == letra:
                print(f"A letra {chute} existe na palavra, na posição {index+1}!")


    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()