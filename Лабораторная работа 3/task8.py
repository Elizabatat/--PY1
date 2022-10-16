money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

delta = salary - spend
while money_capital + delta >= spend:
    money_capital += delta
    spend = spend * (1+increase )

    month += 1

print(month)

