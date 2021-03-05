"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ != "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def main(name: str, *value: tuple) -> int:
    """
        Этот модуль выводит текст
        В дальнейшем будем поддерживать кавычки - на самом деле parser не по
        пробелам а кав. перед передачей сюда аргументов.
        Еще нужно подумать о том чтобы использовать вызов команд внутри команд
        например: echo "Hello World" `file_open info.txt` - но нельзя
        использовать плагины одновременно с плагинами.
    """

    del name
    for i in value:
        print(i, end=" ")

    return 0
