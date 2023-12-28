def save_grades_to_file():
    subjects = input("Введіть предмети навчання через пробіл: ").split()
    grades = []

    for subject in subjects:
        grades_for_subject = input(f"Введіть оцінки за предмет '{subject}' через пробіл: ").split()
        grades.append((subject, grades_for_subject))

    with open("оцінки.txt", "w") as file:
        for subject, grades_list in grades:           
            file.write(f"{subject}: {' '.join(grades_list)}\n")

    print("Дані збережено у файлі 'оцінки.txt'.")

def calculate_total_grade():
    total_grade = 0

    try:
        with open("оцінки.txt", "r") as file:
            for line in file:
                subject, grades_str = line.strip().split(": ")
                grades_list = [int(grade) for grade in grades_str.split()]
                total_grade += sum(grades_list)
    except FileNotFoundError:
        print("Файл 'оцінки.txt' не знайдено. Будь ласка, збережіть оцінки перед обчисленням загального балу.")

    return total_grade

save_grades_to_file()

print(f"Загальний бал: { calculate_total_grade()}")
