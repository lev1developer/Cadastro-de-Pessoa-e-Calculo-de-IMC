def syscad():

    nome = input("digite seu nome: ")
    idade = input("digite sua idade: ")
    altura = float(input("digite sua altura: "))
    peso = float(input("digite seu peso: "))

    print("===CADASTRO DE PESSOA===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura}")
    print(f"Peso: {peso}")
    print(f"imc: {peso / altura ** 2:.2f}")
    print(f"sua idade daqui 5 anos: {int(idade) + 5}")

syscad()