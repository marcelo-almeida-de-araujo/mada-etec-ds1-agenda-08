# Pesquisa de Opinião - TudoWeb
# Coleta nome, idade e opinião sobre o atendimento de cada entrevistado
# e, ao final, exibe a quantidade de respostas EXCELENTE e RUIM.

TOTAL_ENTREVISTADOS = 50  # para testar, altere para 10


def ler_idade():
    idade = input("Idade: ")
    while not idade.isdigit():
        print("Idade inválida. Digite apenas números.")
        idade = input("Idade: ")
    return int(idade)


def ler_opiniao():
    print("Opinião sobre o atendimento:")
    print("  1 - EXCELENTE")
    print("  2 - BOM")
    print("  3 - RUIM")
    opiniao = input("Digite a opção (1, 2 ou 3): ")
    while opiniao not in ("1", "2", "3"):
        print("Opção inválida. Digite 1, 2 ou 3.")
        opiniao = input("Digite a opção (1, 2 ou 3): ")
    return int(opiniao)


def realizar_pesquisa(total):
    qtd_excelente = 0
    qtd_bom = 0
    qtd_ruim = 0

    print("=" * 40)
    print("   PESQUISA DE ATENDIMENTO - TUDOWEB")
    print("=" * 40)

    for i in range(1, total + 1):
        print(f"\nEntrevistado {i} de {total}")
        nome = input("Nome: ")
        idade = ler_idade()
        opiniao = ler_opiniao()

        if opiniao == 1:
            qtd_excelente += 1
            descricao = "EXCELENTE"
        elif opiniao == 2:
            qtd_bom += 1
            descricao = "BOM"
        else:
            qtd_ruim += 1
            descricao = "RUIM"

        print(f"Registrado: {nome}, {idade} anos - {descricao}")

    print("\n" + "=" * 40)
    print("          RESULTADO DA PESQUISA")
    print("=" * 40)
    print(f"Total de entrevistados: {total}")
    print(f"a) Respostas EXCELENTE: {qtd_excelente}")
    print(f"b) Respostas RUIM: {qtd_ruim}")

    return qtd_excelente, qtd_ruim


if __name__ == "__main__":
    realizar_pesquisa(TOTAL_ENTREVISTADOS)
