usd = float(input("Єврики перевести в доляри "))
eur = float(input("Доляри в єврики: "))
e_r=0.85
print(f"Сумарно грошей в долярах:{usd + (eur / e_r)}")
print(f"Сумарно грошей вєвриках:{eur + (usd * e_r)}")

