# Cadastro de Pessoa e Cálculo de IMC

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte dos meus estudos iniciais em Python.

O objetivo é criar um sistema simples de cadastro de pessoas, coletando informações do usuário e realizando cálculos matemáticos a partir dos dados informados.

## ⚙️ Funcionalidades

- Solicita o nome do usuário.
- Solicita a idade.
- Solicita a altura.
- Solicita o peso.
- Exibe os dados cadastrados.
- Calcula o Índice de Massa Corporal (IMC).
- Calcula a idade que o usuário terá daqui a 5 anos.

## 🧠 Conceitos de Python utilizados

Durante o desenvolvimento, pratiquei:

- `def`: definição de funções.
- `input()`: entrada de dados.
- `int()`: conversão para números inteiros.
- `float()`: conversão para números decimais.
- Variáveis: armazenamento de informações.
- Operadores matemáticos: realização de cálculos.
- `**`: operador de potência.
- `print()`: exibição de informações.
- `f-strings`: formatação de textos e valores.

## 💻 Código

```python
def syscad():

    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

    print("=== CADASTRO DE PESSOA ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura}")
    print(f"Peso: {peso}")
    print(f"IMC: {peso / altura ** 2:.2f}")
    print(f"Sua idade daqui a 5 anos: {int(idade) + 5}")

syscad()
```

## 📐 Fórmula do IMC

O cálculo utilizado foi:

**IMC = Peso / Altura²**

Exemplo:

Uma pessoa com 60 kg e 1,70 m de altura:

```python
60 / 1.70 ** 2
```

Resultado: `20.76`

## 🎯 Objetivo de aprendizagem

Praticar os fundamentos da linguagem Python, desenvolver o raciocínio lógico e aprender a construir pequenos programas utilizando funções, variáveis, entradas de dados e operações matemáticas.


