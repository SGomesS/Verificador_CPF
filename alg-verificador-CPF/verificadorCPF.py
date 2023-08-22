
while True:
    '''Variáveis principais'''
    cpf_digitado = input("Digite o número do seu CPF: ")  # Solicita o CPF ao usuário
    verificação_CPF = cpf_digitado if cpf_digitado.isdigit() and len(cpf_digitado) == 11 else print("Digite apenas números e exatamente 11 números")
    # Verifica se o CPF digitado contém apenas dígitos e possui 11 dígitos, caso contrário exibe mensagem de erro
    
    numeros_cpf = []
    contagem_regressiva_primeiro_digito = 10   
    contagem_regressiva_segundo_digito = 11
    soma_primeiro_digito = 0
    soma_segundo_digito = 0

    try:
        for numero_individual_CPF in verificação_CPF:
            numeros_cpf.append(numero_individual_CPF)
    except TypeError:
        continue  # Continua o loop caso ocorra um erro de tipo (geralmente devido a um CPF inválido)
    
    numeros_cpf_2 = numeros_cpf.copy()  # Copia da lista para verificar o segundo dígito do CPF
    
    del numeros_cpf[9::]  # Remove os 2 últimos dígitos do CPF para cálculo do primeiro dígito
    del numeros_cpf_2[10::]  # Remove o último dígito do CPF para cálculo do segundo dígito
    
    # Cálculo dos dígitos verificadores do primeiro dígito
    for numero_individual_CPF in numeros_cpf:
        soma_primeiro_digito += (int(numero_individual_CPF) * contagem_regressiva_primeiro_digito)
        contagem_regressiva_primeiro_digito -= 1
        
    soma_primeiro_digito *= 10
    verificação_primeiro_digito = (soma_primeiro_digito % 11) if (soma_primeiro_digito % 11) <= 9 else  0 
    
    # Cálculo dos dígitos verificadores do segundo dígito
    for numero_individual_CPF in numeros_cpf_2:
        soma_segundo_digito += (int(numero_individual_CPF) * contagem_regressiva_segundo_digito)
        contagem_regressiva_segundo_digito -= 1
        
    soma_segundo_digito *= 10
    verificação_segundo_digito = (soma_segundo_digito % 11) if (soma_segundo_digito % 11) <= 9 else  0 
    cpf_ja_verificado = "------CPF VÁLIDO------" if verificação_primeiro_digito == int(cpf_digitado[-2]) \
    and verificação_segundo_digito == int(cpf_digitado[-1]) else "------CPF INVÁLIDO------"
    # Verifica se os dígitos verificadores calculados coincidem com os dígitos do CPF
    
    print('\r\n')
    print(cpf_ja_verificado)  # Exibe se o CPF é válido ou inválido
    print('\r\n')
    
    inicio = input("Deseja realizar outra consulta? Sim/Não: ")
    inicio = inicio.capitalize()
    
    if inicio == 'Não':
        print("Finalizando.")
        break  # Encerra o loop se o usuário não quiser continuar


    