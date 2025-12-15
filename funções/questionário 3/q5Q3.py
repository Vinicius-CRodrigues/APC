def compose(*func):
    def composta(x):
        resultado = x
        for i in reversed(func):
            resultado = i(resultado)
        return resultado
    return composta