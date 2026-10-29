import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Не удалось прочитать файл задач. Будет создан новый список.")
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст.")
        return

    print("\nВаши задачи:")
    for number, task in enumerate(tasks, start=1):
        status = "Выполнено" if task["done"] else "В процессе"
        print(f"{number}. [{status}] {task['title']}")


def add_task(tasks):
    title = input("Введите название задачи: ").strip()
    if not title:
        print("Название задачи не может быть пустым.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Задача добавлена.")


def choose_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return None

    try:
        number = int(input("Введите номер задачи: "))
        if 1 <= number <= len(tasks):
            return number - 1
        print("Нет задачи с таким номером.")
    except ValueError:
        print("Введите целое число.")

    return None


def complete_task(tasks):
    index = choose_task(tasks)
    if index is None:
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Задача отмечена как выполненная.")


def delete_task(tasks):
    index = choose_task(tasks)
    if index is None:
        return

    removed_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Задача «{removed_task['title']}» удалена.")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== TaskList CLI ===")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Выполнить задачу")
        print("4. Удалить задачу")
        print("0. Выход")

        command = input("Выберите действие: ").strip()

        if command == "1":
            add_task(tasks)
        elif command == "2":
            show_tasks(tasks)
        elif command == "3":
            complete_task(tasks)
        elif command == "4":
            delete_task(tasks)
        elif command == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда. Выберите пункт от 0 до 4.")


if __name__ == "__main__":
    main()
