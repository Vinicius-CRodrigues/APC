def criar_validador_idade(idade_minima, idade_maxima):
    return lambda idade: True if idade >= idade_minima and idade <= idade_maxima else False


