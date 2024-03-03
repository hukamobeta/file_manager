from functions import FileManager

def main():
    fm = FileManager()
    commands = {
        "mkdir": fm.create_folder,
        "rmdir": fm.delete_folder,
        "cd": fm.change_directory,
        "mkfile": fm.create_file,
        "write": fm.write_to_file,
        "read": fm.read_file,
        "rmfile": fm.delete_file,
        "cp": fm.copy_file,
        "mv": fm.move_file,
        "rename": fm.rename_file,
        "help": fm.print_help
    }

    while True:
        command_input = input(f"{fm.current_directory}> ").strip().split(" ", 1)
        if not command_input:
            continue

        command = command_input[0]
        args = command_input[1] if len(command_input) > 1 else ""
        args = args.split(" ") if args else []

        if command == "exit":
            break
        elif command == "help":
            fm.print_help()
        elif command in commands:
            func = commands[command]
            try:
                if command == "cd":
                    if not fm.change_directory(*args):
                        print("Попытка выхода за рабочую директорию")
                elif command == "write" and len(args) >= 2:
                    func(args[0], " ".join(args[1:]))
                elif len(args) == 1:
                    func(*args)
                elif len(args) == 2:
                    func(args[0], args[1])
                else:
                    func()
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Неизвестная или некорректная команда")

if __name__ == "__main__":
    main()
