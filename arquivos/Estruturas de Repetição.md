# Estudo Dirigido: Estruturas de Repetição em Python

## Introdução

As estruturas de repetição permitem executar um mesmo bloco de código várias vezes. Elas são fundamentais no desenvolvimento de algoritmos e programas, pois evitam repetição desnecessária de código e permitem automatizar tarefas.

Em Python, as principais estruturas de repetição são:

- `while`
- `for`

Também serão apresentados alguns comandos e funções importantes relacionados a repetições:

- `range()`
- `break`
- `continue`

---

# 1. Operadores de Atribuição

Antes de estudar as estruturas de repetição, é importante compreender os operadores de atribuição acumulativa.

Esses operadores permitem atualizar o valor de uma variável de forma simplificada.

Por exemplo, o operador `+=` soma um valor à variável atual.

### Exemplo

```python
contador = 1
contador += 1
print(contador)
```

### Resultado

```text
2
```

O código acima equivale a:

```python
contador = 1
contador = contador + 1
print(contador)
```

O mesmo se aplica para as demais operações aritméticas, como por exemplo, `+=`, `-=`, `*=`, `/=`, etc.

---

# 2. Estrutura `while`

A estrutura `while` executa um bloco de código enquanto uma condição for verdadeira.

---

## Estrutura básica

```python
while condição:
    bloco_de_codigo
```

---

## Exemplo

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

### Saída

```text
1
2
3
4
5
```

---

## Explicação

- A variável `contador` inicia com valor `1`
- O bloco será executado enquanto `contador <= 5`
- A cada repetição, o valor do contador aumenta em `1`
- Quando o contador passa a valer `6`, a condição se torna falsa e o loop termina.

---

## Loop infinito

Um loop infinito ocorre quando a condição nunca se torna falsa.

### Exemplo

```python
while True:
    print("Executando...")
```

Nesse caso, o programa continuará executando indefinidamente.

---

# 3. Estrutura `for`

A estrutura `for` é utilizada para percorrer elementos de uma sequência.

---

## Estrutura básica

```python
for variável in sequência:
    bloco_de_codigo
```

---

## Exemplo

```python
for nome in ("Ana", "Carlos", "João"):
    print(nome)
```

### Saída

```text
Ana
Carlos
João
```

---

## Explicação

A variável `nome` recebe, a cada repetição, um elemento da sequência.

---

# 4. Função `range()`

A função `range()` é frequentemente utilizada com a estrutura `for` para gerar sequências numéricas.

---

## Exemplo

```python
for numero in range(5):
    print(numero)
```

### Saída

```text
0
1
2
3
4
```

---

## Funcionamento do `range()`

### Um parâmetro

```python
range(5)
```

Gera números de `0` até `4`.

---

### Dois parâmetros

```python
range(1, 6)
```

Gera números de `1` até `5`.

---

### Três parâmetros

```python
range(início, fim, passo)
```

### Exemplo

```python
for numero in range(0, 10, 2):
    print(numero)
```

### Saída

```text
0
2
4
6
8
```

Nesse caso, o contador aumenta de `2` em `2`.

---

# 5. Comando `break`

O comando `break` interrompe imediatamente a execução do loop.

---

## Exemplo

```python
for numero in range(10):
    if numero == 5:
        break

    print(numero)
```

### Saída

```text
0
1
2
3
4
```

---

## Explicação

Quando `numero` passa a valer `5`, o comando `break` encerra o loop.

---

# 6. Comando `continue`

O comando `continue` interrompe apenas a repetição atual e passa para a próxima iteração.

---

## Exemplo

```python
for numero in range(5):
    if numero == 2:
        continue

    print(numero)
```

### Saída

```text
0
1
3
4
```

---

## Explicação

Quando `numero` vale `2`, o `print()` não é executado. O loop continua normalmente nas próximas repetições.

---

# 7. Diferença entre `while` e `for`

| Estrutura | Utilização                                                                        |
| --------- | --------------------------------------------------------------------------------- |
| `while`   | Quando a repetição depende de uma condição                                        |
| `for`     | Quando se deseja percorrer elementos ou repetir uma quantidade conhecida de vezes |

---

# 8. Exemplos Clássicos

## Exemplo 1: Tabuada

O programa abaixo exibe a tabuada do número `5`.

```python
numero = 5

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
```

### Saída

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

## Exemplo 2: Soma de números

O programa realiza a soma dos números de `1` até `5`.

```python
soma = 0

for numero in range(1, 6):
    soma += numero

print(soma)
```

### Saída

```text
15
```

### Explicação

A variável `soma` acumula os valores durante as repetições.

---

## Exemplo 3: Contagem regressiva

O programa realiza uma contagem regressiva de `10` até `0`.

```python
contador = 10

while contador >= 0:
    print(contador)
    contador -= 1
```

### Saída

```text
10
9
8
7
6
5
4
3
2
1
0
```

---

# Exercícios

## 1.

Faça um programa que exiba os números de `1` até `10` usando `while`.

---

## 2.

Faça um programa que exiba os números pares de `0` até `20` usando `for`.

---

## 3.

Faça a tabuada de um número informado pelo usuário.

---

## 4.

Mostre os números de `10` até `1` usando `for`.

---

## 5.

Peça nomes ao usuário até que ele digite `"sair"`.
