# Pesquisa de Opinião - TudoWeb

Programa em Python que coleta e exibe o resultado de uma pesquisa de satisfação
com o atendimento ao cliente da empresa de marketing **TudoWeb**.

## Funcionamento

Para cada um dos **50 entrevistados** (laço `for`), o programa solicita:

- Nome
- Idade
- Opinião sobre o atendimento:
  - `1` - EXCELENTE
  - `2` - BOM
  - `3` - RUIM

A opinião é verificada com estruturas de decisão (`if / elif / else`), e entradas
inválidas (idade não numérica ou opção fora de 1-3) são pedidas novamente com `while`.

Ao final, são exibidas:

- a) Quantidade de respostas **EXCELENTE**
- b) Quantidade de respostas **RUIM**

## Como executar

```bash
python pesquisa_opiniao.py
```

## Teste com 10 entrevistados

O arquivo `teste_10_entrevistados.py` executa a pesquisa com 10 entrevistados,
simulando as respostas digitadas (inclusive entradas inválidas), e confere se o
resultado é 4 EXCELENTE e 3 RUIM.

```bash
python teste_10_entrevistados.py
```

Também é possível testar manualmente alterando `TOTAL_ENTREVISTADOS = 50` para
`10` no arquivo `pesquisa_opiniao.py`.

### Resultado do teste

```
========================================
          RESULTADO DA PESQUISA
========================================
Total de entrevistados: 10
a) Respostas EXCELENTE: 4
b) Respostas RUIM: 3

TESTE OK: 4 EXCELENTE e 3 RUIM, como esperado.
```
