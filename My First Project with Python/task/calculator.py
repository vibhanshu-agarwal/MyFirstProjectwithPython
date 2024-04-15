# Write your code here
total = 0
item_prices = {
    "Bubblegum:" : 202,
    "Toffee:" : 118,
    "Ice cream:" : 2250,
    "Milk chocolate:" : 1680,
    "Doughnut:" : 1075,
    "Pancake:" : 80
}
print("Earned amount:")
for item, value in item_prices.items():
    print(item, "$" + str(value))
    total += value

print()
print("Income:", "$" + str(total))
staff_expenses = int(input("Staff expenses:"))
other_expenses = int(input("Other expenses:"))
net_income = total - staff_expenses - other_expenses
print("Net income: $" + str(net_income))
