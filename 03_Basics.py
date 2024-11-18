# print(float(2**53))
# print(float(2**53 + 1))
# print(float(2**53 + 2))
# print(float(2**53 + 3))
# print(float(2**53 + 4))
# print(float(2**53 + 5))
# print(float(2**53 + 6))




print((0.8 - 0.7) == 0.1)
print(0.8 - 0.7)

#####################################

from decimal import Decimal

print((Decimal(0.8) - Decimal(0.7)) == Decimal(0.1))
print((Decimal("0.8") - Decimal("0.7")) == Decimal("0.1"))

print(Decimal(0.8), Decimal("0.8"))

import decimal
print(decimal.getcontext())
print(Decimal("100") / Decimal("3"))
decimal.getcontext().prec = 4
print(Decimal("100") / Decimal("3"))


## Rounding Examples ###########################################################
print("\n", "#"*80, "\n")
print("ROUNDING EXAMPLES\n")

def round_it(x, ndigits, strategy=decimal.ROUND_HALF_UP):
    dec_num = decimal.Decimal(str(x))
    decimal.getcontext().rounding = strategy
    rounded = dec_num.quantize(decimal.Decimal(f'1e-{ndigits}'))
    # rounded = round(x, ndigits)
    print(f"round({dec_num}, {ndigits}, {strategy})".ljust(35), f" --> {rounded}")
    
# towards '+inf'
round_it(4.2, ndigits=0, strategy=decimal.ROUND_CEILING)
round_it(5.8, ndigits=0, strategy=decimal.ROUND_CEILING)
print("")

# towards '-inf'
round_it(4.2, ndigits=0, strategy=decimal.ROUND_FLOOR)
round_it(-5.8, ndigits=0, strategy=decimal.ROUND_FLOOR)
print("")

# away from '0'
round_it(4.2, ndigits=0, strategy=decimal.ROUND_UP)
round_it(-5.8, ndigits=0, strategy=decimal.ROUND_UP)
print("")

# towards '0'
round_it(4.2, ndigits=0, strategy=decimal.ROUND_DOWN)
round_it(-5.8, ndigits=0, strategy=decimal.ROUND_DOWN)
print("")

# towards nearest integer; ties towards  '0'
round_it(4.5, ndigits=0, strategy=decimal.ROUND_HALF_DOWN)
round_it(5.5, ndigits=0, strategy=decimal.ROUND_HALF_DOWN)
round_it(-4.5, ndigits=0, strategy=decimal.ROUND_HALF_DOWN)
round_it(-5.5, ndigits=0, strategy=decimal.ROUND_HALF_DOWN)
print("")

# towards nearest integer; ties away from '0'
round_it(4.5, ndigits=0, strategy=decimal.ROUND_HALF_UP)
round_it(5.5, ndigits=0, strategy=decimal.ROUND_HALF_UP)
round_it(-4.5, ndigits=0, strategy=decimal.ROUND_HALF_UP)
round_it(-5.5, ndigits=0, strategy=decimal.ROUND_HALF_UP)
print("")

# towards nearest integer; ties towards nearest even integer
round_it(4.5, ndigits=0, strategy=decimal.ROUND_HALF_EVEN)
round_it(5.5, ndigits=0, strategy=decimal.ROUND_HALF_EVEN)
round_it(-4.5, ndigits=0, strategy=decimal.ROUND_HALF_EVEN)
round_it(-5.5, ndigits=0, strategy=decimal.ROUND_HALF_EVEN)
print("")

# towards nearest integer; ties away from '0'
# rounds ties to the nearest multiple of 0.05. 
# If the number is exactly halfway between two multiples of 0.05, it will round up.
round_it(4.2, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(-5.8, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(4.5, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(-5.5, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(5.235, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(-5.235, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(5.234, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(-5.234, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(5.236, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(-5.236, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(5.23, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(-5.23, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(5.25, ndigits=0, strategy=decimal.ROUND_05UP)
round_it(-5.25, ndigits=0, strategy=decimal.ROUND_05UP)
