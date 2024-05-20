def enumerate_list(list):
    result= []
    for i in list:
        if i:
            result.append(f"{len(result)}. {i}")
    return result


def enumerate_backwards(list):
    resultado= []
    for i in list:
        if i:
            resultado.append(f"{len(resultado)}. {i[::-1]}")
    return resultado
