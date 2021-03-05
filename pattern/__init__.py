"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def main(*args: tuple) -> int:
    """
        Этот plugin сделан как шаблон для написания других.
        В дальнейшем будем поддерживать кавычки - на самом деле parser не по
        пробелам а кав. перед передачей сюда как аргументы.
        Еще нужно подумать о том чтобы использовать вызов команд внутри команд
        например: echo "Hello World" `file_open info.txt` - но нельзя
        использовать плагины одновременно с плагинами - особенно если не sys.path.

        :param args: кортеж строк - аргументы.
        :return: - возвращает всегда результат числом.
    """

    return 0
