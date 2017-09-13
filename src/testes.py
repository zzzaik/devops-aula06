import jogovelha
import sys

erroInicializar = False

jgo = jogovelha.inicalizar()

if len(jogo) != 3:
    erroInicializar = True
else:
    for linha in jogo:
        if len(linha) != 3:
            erroInicializar = True
        else:
            for elemento in linha:
                if elemento != '.':
                    erroInicializar = True

if erroInicializar:
    sis.exit(1)
else:
    sis.exit(0)
