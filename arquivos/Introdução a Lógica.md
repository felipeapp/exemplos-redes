# 📘 Introdução à Lógica

## 1. O que é Lógica?

Lógica é o estudo de como tomar decisões com base em informações.

Na computação, usamos lógica para:

- decidir o que fazer
- combinar condições
- controlar o fluxo de um programa

---

## 2. Proposições

Uma **proposição** é uma senteça que pode ser:

- **Verdadeira (V)** ou
- **Falsa (F)**

### Exemplos:

- "Está chovendo" → ✔️ Proposição
- "Hoje é segunda-feira" → ✔️ Proposição
- "Feche a porta" → ❌ Não é proposição (é uma ordem)

---

## 3. Conectivos Lógicos

Servem para combinar proposições:

- E (AND)
- Ou (OR)
- Não (NOT)

---

### 3.1 E (AND)

Só é verdadeiro quando **todas as condições são verdadeiras**.

| A   | B   | A E B |
| --- | --- | ----- |
| V   | V   | V     |
| V   | F   | F     |
| F   | V   | F     |
| F   | F   | F     |

**Exemplo:**
"Vou sair se estiver com sol E eu tiver dinheiro"

---

### 3.2 OU (OR)

É verdadeiro quando **pelo menos uma condição é verdadeira**.

| A   | B   | A OU B |
| --- | --- | ------ |
| V   | V   | V      |
| V   | F   | V      |
| F   | V   | V      |
| F   | F   | F      |

**Exemplo:**
"Vou assistir filme se estiver chovendo OU se não tiver nada para fazer"

---

### 3.3 NÃO (NOT)

Inverte o valor lógico.

| A   | NÃO A |
| --- | ----- |
| V   | F     |
| F   | V     |

**Exemplo:**
"NÃO está chovendo"

---

## 4. Operações Lógicas

Podemos combinar várias condições.

**Exemplo:**

"Vou sair se NÃO estiver chovendo E eu tiver dinheiro"

---

## 5. Tabela-Verdade

Mostra todas as combinações possíveis.

| Não está chovendo | Tenho dinheiro | Vou sair |
| ----------------- | -------------- | -------- |
| V                 | V              | F        |
| V                 | F              | F        |
| F                 | V              | V        |
| F                 | F              | F        |

---

## 6. Argumentos Lógicos

Um argumento usa proposições para chegar a uma conclusão.

### Exemplo:

- Se está chovendo, então levo guarda-chuva
- Está chovendo
- Logo, levo guarda-chuva

---

## 7. Ligação com Programação

Esses conceitos aparecem diretamente em código:

```python
if not esta_chovendo and tenho_dinheiro:
    print("Vou sair")
```

---

## 8. Exercícios Resolvidos

### Exercício 1

Classifique como proposição ou não:

- "Está frio" → ✔️ Proposição (pode ser verdadeiro ou falso)
- "Feche a janela" → ❌ Não é proposição (é uma ordem)
- "Hoje é domingo" → ✔️ Proposição

---

### Exercício 2

Constuir tabela-verdade de A OU B:

| A   | B   | A OU B |
| --- | --- | ------ |
| V   | V   | V      |
| V   | F   | V      |
| F   | V   | V      |
| F   | F   | F      |

---

### Exercício 3

Constuir tabela-verdade de A E (NÃO B):

| A   | B   | NÃO B | A E (NÃO B) |
| --- | --- | ----- | ----------- |
| V   | V   | F     | F           |
| V   | F   | V     | V           |
| F   | V   | F     | F           |
| F   | F   | V     | F           |

---

### Exercício 4

Diferencie E e OU e cite exemplos.

- **E (AND):** todas as condições precisam ser verdadeiras
- **OU (OR):** basta uma condição ser verdadeira

Exemplos:

- "Vou sair se tiver dinheiro E não estiver chovendo"
- "Vou sair se tiver dinheiro OU se não estiver chovendo"
