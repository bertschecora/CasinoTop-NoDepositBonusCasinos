import random

print("Онлайн казино с бездепозитным бонусом - Демо!")
spins = 5
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {5 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для нового шанса...")
print("Крути онлайн с бездепом в топ-казино!")
