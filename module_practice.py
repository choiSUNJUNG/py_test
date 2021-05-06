# 방식 1
# import module
# module.price(2)
# module.price_morning(4)
# module.price_soldier(5)
# -------------------------------------------------
# 방식 2
# import module as mo
# mo.price(2)
# mo.price_morning(4)
# mo.price_soldier(5)
# ----------------------------------------------------
# 방식 3
# from module import *
# price(2)
# price_morning(4)
# price_soldier(5)
#------------------------------------------------
# 방식 4
# from module import price, price_morning
# price(2)
# price_morning(4)
# price_soldier(5)
# ---------------------------------------------------
# 방식 5 : soldier only
from module import price_soldier as army #price_soldier를 간단히 'army'로 대체
army(10)
