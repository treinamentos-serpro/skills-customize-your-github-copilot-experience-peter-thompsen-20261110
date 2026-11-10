# 📘 Atividade: Busca Linear em Python

## 🎯 Objetivo

Implemente a busca linear para encontrar valores em listas não ordenadas. Você vai praticar percorrer uma lista com loops e retornar resultados diferentes conforme o que encontrar.

## 📝 Tarefas

### 🛠️ Verificar se um valor está na lista

#### Descrição
Complete `contains_value(values, target)` no código inicial. Percorra os elementos da lista em ordem e retorne assim que encontrar o valor procurado.

#### Requisitos
O programa concluído deve:

- Retornar `True` quando `target` estiver na lista e `False` quando não estiver.
- Retornar `False` para uma lista vazia.
- Percorrer a lista sem usar `in` ou outros métodos prontos de busca.

Exemplos: `contains_value([8, 3, 5], 3)` retorna `True`; `contains_value([8, 3, 5], 4)` retorna `False`.

### 🛠️ Encontrar a posição do primeiro resultado

#### Descrição
Complete `find_index(values, target)` para localizar a posição do primeiro elemento igual ao valor procurado. As posições da lista começam em zero.

#### Requisitos
O programa concluído deve:

- Retornar o índice da primeira ocorrência de `target`.
- Retornar `-1` quando o valor não estiver na lista ou quando a lista estiver vazia.
- Percorrer a lista sem usar `list.index()` ou outros métodos prontos de busca.

Exemplos: `find_index([8, 3, 5], 3)` retorna `1`; `find_index([8, 3, 8], 8)` retorna `0`.
