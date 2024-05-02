from pathlib import Path

file_s = 'salary.txt'
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            salary_total = 0
            for line in lines:
                developer_salary = line.split(",")[1]
                salary_total += int(developer_salary)
            salary_avg = salary_total / len(lines)
            return salary_total, salary_avg
    except FileNotFoundError:
        print(f'File {path} not found')
    except Exception as e:
        print(f'{e}')
    except TypeError:
        print (f'Oops, TypeError')


total, avrg = total_salary('./salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avrg}")
