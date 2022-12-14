def reduce_fraction(fraction,export=tuple):
    num = 1
    den = float(num/fraction)
    
    if den % 1 == 0:
        return int(num),int(den)
    else:
        while den % 1 != 0:
            num += 1
            den = num/fraction

        return int(num),int(den)

def fraction_from_decimal(decimal):
    num = 1
    den = float(num/decimal)

    if den % 1 == 0:
        return int(num),int(den)
    else:
        while den % 1 != 0:
            num += 1
            den = num/decimal

        return int(num),int(den)