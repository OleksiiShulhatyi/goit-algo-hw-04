def total_salary(path):
    """
    Читає файл із зарплатами розробників (формат: "Прізвище,зарплата")
    і повертає кортеж: (загальна сума, середня зарплата).
    Якщо файл відсутній або не містить коректних даних, повертає (0, 0).
    """
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                
                try:
                    _, salary_str = line.split(',')
                    total += int(salary_str)
                    count += 1
                except ValueError:
                    print(f"Пропущено некоректний рядок: {line!r}")
                    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return (0, 0)

    if count == 0:
        return (0, 0)
    
    return (total, total / count)

if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума зарплат: {total}, Середня зарплата: {average}")