import os

def validar_e_limpar_notas(lista):
    if not lista:
        return []
    
    notas_validas = []
    for item in lista:
        try:
            nota = float(item)
            if 0 <= nota <= 10:
                notas_validas.append(nota)
        except (ValueError, TypeError):
            continue
    return notas_validas