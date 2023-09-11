# Пример входных данных
names = ["Gays", "Rik", "Morti"]
rates = [2023, 2027, 777]
bonuses = ["10.25%", "5.5%", "12%"]

# Генератор словаря
result = {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

print(result)