# -*- coding: utf-8 -*-

def get_filenames(path, value_from, value_to):
    """
        Допустим, у нас имеется структура файлов:
            path/
                01
                01.a
                02
                02.a

        В таком случае вызов get_filenames(path, 1, 2) вернёт:
            [(path/01, path/01.a), (path/02, path/02.a)]
    """
    result = []
    for i in range(value_from, value_to + 1):
        name = "0" + str(i) if i <= 9 else str(i)
        result.append((path + name, path + name + ".a"))
    return result
