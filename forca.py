def jogar():
    print("************************************")
    print("*****BEM VINDO AO JOGO DE FORCA*****")
    print("************************************")

    palavra_secreta = "bolacha"
    venceu = False
    enforcou = False
    erros = 0
    letras_acertadas = ["_","_","_","_","_","_","_"]

    while(True):
        print(f"\n{letras_acertadas}")

        chute = input("Digite uma letra do alfabeto: ").strip().lower()

        if chute in palavra_secreta and len(chute) == 1:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = chute
        else:
            print("Seu chute não existe na palavra secreta!")
            erros += 1
            print(f"Você possui {6-erros} tentativas")

            if erros >= 6:
                print("Acabaram suas tentativas!")
                break

        if "_" not in letras_acertadas:
            print("Você ganhou!")
            break
        
    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()