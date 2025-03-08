def luhn_algorithm(card_number):
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def validate_credit_card(card_number):
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False

    card_length = len(card_number)
    card_prefix = int(card_number[:6])

    card_types = [
        {"name": "MasterCard", "lengths": [16], "prefixes": list(range(51, 56)) + list(range(2221, 2721))},
        {"name": "Visa", "lengths": [13, 16, 19], "prefixes": [4]},
        {"name": "American Express", "lengths": [15], "prefixes": [34, 37]},
        {"name": "Diners Club", "lengths": [14], "prefixes": list(range(300, 306)) + [36, 38]},
        {"name": "Discover", "lengths": [16], "prefixes": [6011] + list(range(622126, 622926)) + list(range(644, 650)) + [65]},
        {"name": "EnRoute", "lengths": [15], "prefixes": [2014, 2149]},
        {"name": "JCB", "lengths": [16, 19], "prefixes": list(range(3528, 3590))},
        {"name": "Voyager", "lengths": [15], "prefixes": [8699]},
        {"name": "Hipercard", "lengths": [13, 16, 19], "prefixes": [606282, 637095, 637568, 637599, 637609, 637612]},
        {"name": "Aura", "lengths": [16], "prefixes": [50]},
    ]

    for card_type in card_types:
        if card_length in card_type["lengths"] and any(str(card_number).startswith(str(prefix)) for prefix in card_type["prefixes"]):
            return luhn_algorithm(card_number)

    return False

# Exemplo de uso:
cartao = "5388799166140127"
print(validate_credit_card(cartao))  # Deve retornar True se for válido