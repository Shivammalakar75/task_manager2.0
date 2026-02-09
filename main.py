from storage.file_manager import load_users, save_users
from auth.authentication import sign_up, log_in

CURRENT_USER = None


def task_menu(users):
    global CURRENT_USER

    while CURRENT_USER:
        print(f"\nWELCOME {CURRENT_USER.username.upper()}")
        print("1. ADD TASK")
        print("2. VIEW TASKS")
        print("3. VIEW PENDING TASKS")
        print("4. VIEW COMPLETED TASKS")
        print("5. UPDATE TASK")
        print("6. MARK TASK AS COMPLETED")
        print("7. DELETE TASK")
        print("8. LOG OUT")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                title = input("Title: ")
                desc = input("Description: ")
                CURRENT_USER.add_task(title, desc)
                save_users(users)

            case "2":
                CURRENT_USER.print_tasks()

            case "3":
                CURRENT_USER.print_tasks(
                    CURRENT_USER.get_tasks("Pending")
                )

            case "4":
                CURRENT_USER.print_tasks(
                    CURRENT_USER.get_tasks("Completed")
                )

            case "5":
                tid = int(input("Task ID: "))
                task = CURRENT_USER.find_task(tid)

                if task:
                    task.description = input("New description: ")
                    save_users(users)
                else:
                    print("Task not found!")

            case "6":
                tid = int(input("Task ID: "))
                task = CURRENT_USER.find_task(tid)

                if task:
                    task.mark_completed()
                    save_users(users)
                else:
                    print("Task not found!")

            case "7":
                tid = int(input("Task ID: "))
                CURRENT_USER.delete_task(tid)
                save_users(users)

            case "8":
                CURRENT_USER = None
                print("Logged out!")

            case _:
                print("Invalid choice!")


def main_menu():
    global CURRENT_USER

    users = load_users()

    while True:
        print("\nTASK MANAGEMENT SYSTEM")
        print("1. SIGN UP")
        print("2. LOG IN")
        print("3. EXIT")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                sign_up(users)

            case "2":
                CURRENT_USER = log_in(users)

                if CURRENT_USER:
                    task_menu(users)

            case "3":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice!")


if __name__ == "__main__":
    main_menu()