![](https://raw.githubusercontent.com/gusantos1/singledispatch-object-storage/main/img/foto1.png)


## Single-dispatch generic functions
Uma **função genérica é composta por múltiplas funções** que implementam a mesma operação para **tipos diferentes**. A escolha da implementação correta durante a chamada da função está diretamente relacionada ao **tipo do primeiro argumento**, o qual foi registrado durante a implementação. Em python, esse padrão é conhecido como **Single-dispatch**.

---
O **Single-dispatch** está alinhado com vários princípios fundamentais de boas práticas no desenvolvimento de software, incluindo o **Princípio Aberto-Fechado (Open-Closed Principle)**. No contexto apresentado, isso significa que a função *enviar_dados* é projetada para ser **aberta para extensão**, permitindo a adição de novos comportamentos, ao mesmo tempo que mantém as **implementações existentes fechadas para modificação**.

[![Código Singledispatch](https://raw.githubusercontent.com/gusantos1/singledispatch-object-storage/main/img/foto3.png)](https://raw.githubusercontent.com/gusantos1/singledispatch-object-storage/main/img/foto3.png)

---
Ao receber o tipo do primeiro objeto, que no contexto é o armazenamento de destino, o 'despachante' **invoca a implementação de maneira coesa**, reduzindo os efeitos colaterais comuns em má implementações com controles de fluxo encadeados.
[![Comportamento do Singledispatch](https://raw.githubusercontent.com/gusantos1/singledispatch-object-storage/main/img/foto2.png)](https://raw.githubusercontent.com/gusantos1/singledispatch-object-storage/main/img/foto2.png)

---

### Interessado em explorar sobre o Single-dispatch


**PEP 443 – Single-dispatch generic functions**  
https://peps.python.org/pep-0443/

**functools — Higher-order functions and operations on callable objects** https://docs.python.org/3/library/functools.html#functools.singledispatch