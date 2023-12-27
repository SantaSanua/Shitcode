
my_list=input("Введіть елементи списку через пробіл: ").split()
index=input("Введіть індекс неугодного елемента для видалення: ")
try:
 index = int(index)
except:
 print("індекс задано некоректним значенням")
if index < 0 or index >= len(my_list):
    raise ValueError("індекс виходить за межі списку")
index1=index-1
removed_element = my_list.pop(index1)
print(f"Ліст після видалення неугодного елемента з індексом {index}: {my_list}")
