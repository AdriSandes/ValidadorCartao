# Validador de Cartão de Crédito

Este projeto é um validador de cartões de crédito desenvolvido como parte de um desafio da DIO para treinamento de utilização da ferramenta GitHub Copilot.

## Descrição

O projeto consiste em uma função Python que valida números de cartões de crédito com base nas seguintes regras:

1. **MasterCard**
   - Comprimento: 16 dígitos
   - Prefixos: 51–55, 2221–2720
   - Verificação: Algoritmo de Luhn

2. **Visa**
   - Comprimento: 13, 16 ou 19 dígitos
   - Prefixos: 4
   - Verificação: Algoritmo de Luhn

3. **American Express**
   - Comprimento: 15 dígitos
   - Prefixos: 34, 37
   - Verificação: Algoritmo de Luhn

4. **Diners Club**
   - Comprimento: 14 dígitos
   - Prefixos: 300–305, 36, 38
   - Verificação: Algoritmo de Luhn

5. **Discover**
   - Comprimento: 16 dígitos
   - Prefixos: 6011, 622126–622925, 644–649, 65
   - Verificação: Algoritmo de Luhn

6. **EnRoute**
   - Comprimento: 15 dígitos
   - Prefixos: 2014, 2149
   - Verificação: Algoritmo de Luhn

7. **JCB**
   - Comprimento: 16 ou 19 dígitos
   - Prefixos: 3528–3589
   - Verificação: Algoritmo de Luhn

8. **Voyager**
   - Comprimento: 15 dígitos
   - Prefixos: 8699
   - Verificação: Algoritmo de Luhn

9. **Hipercard**
   - Comprimento: 13, 16 ou 19 dígitos
   - Prefixos: 606282, 637095, 637568, 637599, 637609, 637612
   - Verificação: Algoritmo de Luhn

10. **Aura**
    - Comprimento: 16 dígitos
    - Prefixos: 50
    - Verificação: Algoritmo de Luhn

## Como Usar

Para usar a função de validação, basta chamar a função `validate_credit_card` passando o número do cartão como uma string. Veja o exemplo abaixo:

```python
cartao = "4111111111111111"
print(validate_credit_card(cartao))  # Deve retornar True se for válido
