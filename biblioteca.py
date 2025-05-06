def imprime_nome(nome):
    print(f"Nome: {nome}")

def piramide(n):
    for x in range(1, n + 1):
        print((str(x) + " ") * x)

def contaVogais(texto):
    cont = 0
    for x in texto:
        if x.lower() in "aeiou":
            cont += 1
    print(cont)

def estoque(produto, quantidade, valorUnitario):
    return quantidade * valorUnitario

def numero(n):
    if n > 0:
        return "P"
    elif n < 0:
        return "N"
    else:
        return "Z"

def soma(n1, n2):
    res = n1 + n2
    print(res)

def soma2(*args):
    soma = sum(args)
    print(soma)

def textorev(t):
    cont = 0
    for x in range(len(t) - 1, -1, -1):
        print(t[x], end="")
        if t[x] != " ":
            cont += 1
    print("\nTotal de caracteres sem espaço:", cont)