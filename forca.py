import random

palavras = ['pera', 'manga', 'mamao', 'melancia', 'melao', 'banana', 'kiwi', 'pessego', 'laranja', 'limao', 'framboesa', 'damasco', 'morango', 'tangerina', 'abacaxi']

palavra = random.choice(palavras)

letras_erradas = []

letras_corretas = []

while True:
    palavra_escondida = ''.join(letra if letra in letras_corretas else '_' for letra in palavra)
    print(f'Palavra: {palavra_escondida}')

    if palavra_escondida == palavra:
        print('Parabéns! Você acertou a palavra!')
        break

    letra = input('Digite uma letra: ').lower()

    if letra in letras_corretas or letra in letras_erradas:
        print('Você já tentou essa letra. Tente outra.')
        continue

    if letra in palavra:
        letras_corretas.append(letra)
    else:
        letras_erradas.append(letra)
        print('Letra errada!')

    if len(letras_erradas) == 5:
        print('Você errou demais! Fim de jogo.')
        print(f'A palavra era: {palavra}')
        break
