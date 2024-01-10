from decimal import Decimal,getcontext,Context
import decimal

import time

new_context=Context(prec=7,rounding=decimal.ROUND_UP)
decimal.setcontext(new_context)

a=Decimal(0.3)
print(a)

print(a.quantize())