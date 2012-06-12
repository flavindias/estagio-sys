def validar_cpf(cpf):
    digitos = [int(c) for c in cpf if c.isdigit()]
    if len(digitos) == 11:
        a,b,c,d,e,f,g,h,i,j,k = digitos
        numeros = [a,b,c,d,e,f,g,h,i]
        r = range(10, 1, -1)
        soma = sum([x * y for x, y in zip(numeros, r)])
        resto = soma % 11
        dv1 = (11 - resto if 11 - resto < 10 else 0)
        numeros = [a,b,c,d,e,f,g,h,i,dv1]
        r = range(11, 1, -1)
        soma = sum([x*y for x, y in zip(numeros, r)])
        resto = soma % 11
        dv2 = (11 - resto if 11 - resto < 10 else 0)
        return dv1 == j and dv2 == k
    return False
