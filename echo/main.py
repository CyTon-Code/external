"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def main(name: str, *value: tuple) -> int:
    """
        Этот plugin выводит текст
        В дальнейшем будем поддерживать кавычки - на самом деле parser не по
        пробелам а кав. перед передачей сюда аргументов.
        Еще нужно подумать о том чтобы использовать вызов команд внутри команд
        например: echo "Hello World" `file_open info.txt` - но нельзя
        использовать плагины одновременно с плагинами.
        :param name: имя команды плагина, как правило всегда лишние.
        :param value: кортеж строк для вывода.
        :return: - возвращает всегда результат числом.
    """

    del name
    print(*value)

    return 0
