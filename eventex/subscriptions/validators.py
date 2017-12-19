from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 números.', 'length')

    if not verifying_digit_is_valid(value):
        raise ValidationError('CPF deve ser válido.', 'checker')


def verifying_digit_is_valid(value):
    # Checking the first digit.
    cpf = list(str(value))[0:-2]
    checkers = list(str(value))[-2:]
    sequence = range(10, 1, -1)
    sum_ = 0
    valid = True

    for a, b in zip(cpf, sequence):
        sum_ += int(a) * int(b)

    checker_st = (sum_ * 10) % 11
    checker_st = (0 if checker_st == 10 else checker_st)

    if checker_st != int(checkers[0]):
        valid = False
    else:
    # Checking the second digit.
        cpf = list(str(value))[0:-1]
        sequence = range(11, 1, -1)
        sum_ = 0

        for a, b in zip(cpf, sequence):
            sum_ += int(a) * int(b)

        checker_nd = (sum_ * 10) % 11
        checker_nd = (0 if checker_nd == 10 else checker_nd)

        if checker_nd != int(checkers[1]):
            valid = False

    return valid