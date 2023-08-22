# Algoritmo CPF v1.0



Como funciona a verificação do CPF ?

A verificação dos dígitos de um CPF (Cadastro de Pessoas Físicas) é baseada em um cálculo matemático. Cálculo do Primeiro Dígito Verificador :

Os nove primeiros dígitos do CPF (XXX.XXX.XXX) são multiplicados por uma sequência de pesos começando por 10 e decrescendo de 1. A soma dos produtos é calculada. O resultado da soma é multiplicado por 10 e o resto da divisão por 11 é obtido. Se o resultado for igual a 10, o primeiro dígito verificador é 0. Caso contrário, ele é o próprio resultado da divisão.

Cálculo do Segundo Dígito Verificador:

O cálculo é semelhante ao do primeiro dígito, mas os nove primeiros dígitos agora incluem o primeiro dígito verificador calculado anteriormente. Os produtos dos dígitos pelos pesos são somados. O resultado da soma é multiplicado por 10 e o resto da divisão por 11 é obtido. Se o resultado for igual a 10, o segundo dígito verificador é 0. Caso contrário, ele é o próprio resultado da divisão. Verificação Final:

Os dígitos verificadores calculados (primeiro e segundo) são comparados com os dois últimos dígitos do CPF original. Se eles coincidirem, o CPF é considerado válido. Caso contrário, o CPF é inválido ou contém erros.
