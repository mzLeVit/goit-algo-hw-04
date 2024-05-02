from pathlib import Path
file_c = Path('cats.txt')
def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    cat_data = {
                        "id": id.strip(),
                        "name": name.strip(),
                        "age": int(age.strip())
                    }
                    cats_list.append(cat_data)
                except ValueError:
                    print(f"Помилка: некоректний формат даних у рядку: {line.strip()}")
                except Exception as e:
                    print(f"Помилка обробки рядка: {line.strip()}: {e}")
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as e:
        print(f"Помилка: {e}")
    return cats_list

cats = get_cats_info('./cats.txt')
print(cats)