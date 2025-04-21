def valorInput(texto, valor):
    novoValor = input(f"{texto} : {valor} = ")
    if novoValor == "":
        return valor
    else:
        return novoValor 