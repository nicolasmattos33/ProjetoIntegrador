def calcular_media_aluno(notas):
    """ Sem nota, média zero. """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def classificar_desempenho(media):
    if media >= 9.0:
        return "DESTAQUE"
    elif media >= 7.0:
        return "APROVAÇÃO"
    else:
        return "RECUPERAÇÃO"