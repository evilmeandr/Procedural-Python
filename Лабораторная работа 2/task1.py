money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 1

while money_capital > spend:
    money_capital += salary
    if count != 1:
        spend = spend + increase*spend
    money_capital -= spend
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)