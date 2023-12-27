def calculate(p, q):
    try:
        if p < 0 or q < 0:
            raise ValueError("введи додатні значення")
        
        total_cost = p * q
        return total_cost
    except ValueError as e:
        return str(e)

try:
    p = float(input("Введіть ціну товару: "))
    q = float(input("Введіть кількість товару: "))
    
    
    
    if isinstance({calculate(p, q)}, float):
        print(f"Вартість товару: {calculate(p, q)}")
    else:
        print({calculate(p, q)})
except ValueError:
    print("Помилка: введіть коректні числові значення для ціни та кількості.")
