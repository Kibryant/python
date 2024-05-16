def format_cpf(cpf: str):
    cpf = ''.join(filter(str.isdigit, cpf))
    formatted_cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    return formatted_cpf
