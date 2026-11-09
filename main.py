students_db = [
    {"id": 1, "name": "Алексей", "grades": [5, 4, 5, 3]},
    {"id": 2, "name": "Мария", "grades": [4, 5, 4]},
    {"id": 3, "name": "Иван", "grades": []},
    {"id": 4, "name": "Ольга", "grades": [3, 2, 3, "4"]},
]


def get_average_grade(student):
    # Считает средний балл студента
    return sum(student["grades"]) / len(student["grades"])


def find_student_by_id(student_id):
    # Ищет студента по ID
    for student in students_db:
        if student["id"] == student_id:
            return student
    return None


def add_new_student(name, grades_str):
    # Добавляет нового студента. Оценки передаются строкой через запятую (например: '4,5,3')
    grades = [int(g.strip()) for g in grades_str.split(",")]
    new_id = len(students_db) + 1
    new_student = {"id": new_id, "name": name, "grades": grades}
    students_db.append(new_student)
    print(f" Студент {name} успешно добавлен с ID {new_id}!")


def print_report():
    # Выводит красивый отчет по всем студентам
    print("\n--- ОТЧЕТ УСПЕВАЕМОСТИ ---")
    for student in students_db:
        avg = get_average_grade(student)
        print(f"[{student['id']}] {student['name']} | Средний балл: {avg:.2f}")
        
 def delete_student(student_id):
    # Удаляет студента из базы данных по его ID
    student = find_student_by_id(student_id)
    if student:
        students_db.remove(student)
        print(f" Студент {student['name']} (ID {student_id}) успешно удален!")
        return True
    else:
        print(" Студент с таким ID не найден.")
        return False


def main():
    while True:
        print("\n Меню:")
        print("1. Показать отчет")
        print("2. Найти студента по ID")
        print("3. Добавить студента")
        print("4. Удалить студента по ID")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print_report()
        elif choice == "2":
            sid = input("Введите ID студента: ")
            student = find_student_by_id(sid)
            if student:
                print(f"Найдено: {student['name']}, Оценки: {student['grades']}")
            else:
                print("Студент не найден")
        elif choice == "3":
            name = input("Имя студента: ")
            grades = input("Оценки через запятую (например: 4,5,3): ")
            add_new_student(name, grades)
        elif choice == "4":
            sid = input("Введите ID студента для удаления: ")
            delete_student(sid)
        elif choice == "5":
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()