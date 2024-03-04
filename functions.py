import os
import shutil
from settings import WORKING_DIRECTORY

class FileManager:
    def __init__(self):
        self.current_directory = WORKING_DIRECTORY

    def is_within_working_dir(self, path):
        normalized_path = os.path.realpath(path)
        normalized_working_dir = os.path.realpath(WORKING_DIRECTORY)
        return normalized_path.startswith(normalized_working_dir)


    def create_folder(self, name):
        path = os.path.join(self.current_directory, name)
        if not os.path.exists(path):
            os.makedirs(path)

    def delete_folder(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.exists(path) and os.path.isdir(path):
            os.rmdir(path)

    def change_directory(self, target):
        if target == "..":
            new_dir = os.path.dirname(self.current_directory)
            if self.is_within_working_dir(new_dir):
                self.current_directory = new_dir
                return True
            else:
                return False
        else:
            new_dir = os.path.join(self.current_directory, target)
            if os.path.exists(new_dir) and os.path.isdir(new_dir) and self.is_within_working_dir(new_dir):
                self.current_directory = new_dir
                return True
        return False

    def create_file(self, name):
        path = os.path.join(self.current_directory, name)
        with open(path, "w") as file:
            pass

    def write_to_file(self, name, text):
        path = os.path.join(self.current_directory, name)
        with open(path, "w") as file:
            file.write(text)

    def read_file(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.exists(path):
            with open(path, "r") as file:
                print(file.read())

    def delete_file(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.exists(path) and os.path.isfile(path):
            os.remove(path)

    def copy_file(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)

    def move_file(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)

    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.current_directory, old_name)
        new_path = os.path.join(self.current_directory, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
    
    def print_help(self):
        help_message = """
Доступные команды:
  mkdir <папка>        - Создать папку
  rmdir <папка>        - Удалить папку
  cd <папка>           - Сменить директорию
  mkfile <файл>        - Создать пустой файл
  write <файл> <текст> - Записать текст в файл
  read <файл>          - Прочитать файл
  rmfile <файл>        - Удалить файл
  cp <источник> <назначение> - Копировать файл
  mv <источник> <назначение> - Переместить файл
  rename <старое_имя> <новое_имя> - Переименовать файл
  help                 - Показать эту справку
  exit                 - Выйти из программы
        """
        print(help_message)