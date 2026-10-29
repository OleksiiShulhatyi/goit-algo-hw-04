def get_cats_info(path):
    """
    Читає файл з інформацією про котів (формат: "id,ім'я,вік")
    і повертає список словників з ключами "id", "name", "age".
    Якщо файл відсутній, повертає порожній список.
    """
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue # Пропускаємо порожні рядки
                
                try:
                    cat_id, name, age = line.split(',')
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Пропущено некоректний рядок: {line!r}")
                    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        
    return cats

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    for cat in cats_info:
        print(cat)