# Teste da pesquisa com 10 entrevistados.
# Simula as respostas digitadas e confere as contagens finais.

import builtins

from pesquisa_opiniao import realizar_pesquisa

# (nome, idade, opinião)
entrevistados = [
    ("Ana", "25", "1"),
    ("Bruno", "34", "2"),
    ("Carla", "41", "3"),
    ("Diego", "19", "1"),
    ("Elisa", "52", "1"),
    ("Fábio", "28", "3"),
    ("Gabriela", "37", "2"),
    ("Hugo", "45", "1"),
    ("Isabela", "23", "2"),
    ("João", "60", "3"),
]

respostas = []
for nome, idade, opiniao in entrevistados:
    respostas += [nome, idade, opiniao]

# Inclui entradas inválidas no 1º entrevistado para testar a validação
respostas[1:3] = ["vinte", "25", "5", "1"]

entradas = iter(respostas)


def input_simulado(mensagem=""):
    valor = next(entradas)
    print(mensagem + valor)
    return valor


builtins.input = input_simulado

excelente, ruim = realizar_pesquisa(10)

assert excelente == 4, f"Esperado 4 EXCELENTE, obtido {excelente}"
assert ruim == 3, f"Esperado 3 RUIM, obtido {ruim}"
print("\nTESTE OK: 4 EXCELENTE e 3 RUIM, como esperado.")
