import os # Импортируем модуль os для работы с операционной системой

def split_file_path(file_path):
    # Используем функцию os.path.splitext() для разделения пути и расширения файла.
    # Эта функция возвращает кортеж из пути и расширения.
    file_name, file_extension = os.path.splitext(file_path)
    
    # Далее, используем функцию os.path.split() для разделения пути и имени файла.
    # Эта функция возвращает кортеж из пути и имени файла.
    path, file_name = os.path.split(file_name)
    
    # Возвращаем результат разделения в виде кортежа: путь, имя файла и расширение файла.
    return path, file_name, file_extension

# Пример использования функции:
file_path = "/home/user/documents/example.txt"
result = split_file_path(file_path)
print("Путь:", result[0])
print("Имя файла:", result[1])
print("Расширение файла:", result[2])