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
                    