salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
allcosts = 0

for month in range(1, months+1):
    if month != 1:
        spend = spend + increase*spend
    allcosts += spend
money_capital = allcosts - months*salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital,2))
