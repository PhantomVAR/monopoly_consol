class Decor:
    """декоратр добавляет указанные знаки в указанном количестве и меняет цвет текста в консоли
    если указан HEADER OKBLUE OKCYAN OKGREEN WARNING FAIL BOLD UNDERLINE
    пример вызова: @Decor("=", 80, "WARNING")"""
    __colors = {'HEADER': '\033[95m', 'OKBLUE': '\033[94m', 'OKCYAN': '\033[96m',
              'OKGREEN': '\033[92m', 'WARNING': '\033[93m', 'FAIL': '\033[91m',
              'ENDC': '\033[0m', 'BOLD': '\033[1m', 'UNDERLINE': '\033[4m',
              "": ""}

    def __init__(self, delimiter: str = "", col: int = 0, color: str = ""):
        self.delimiter = delimiter
        self.col = col
        self.color = color

    def __call__(self, func):
        def exec_fanc(*args, **kwargs):
            beg_color = ""
            end_color = ""
            if self.color != "":
                beg_color = self.__colors.get(self.color)
                end_color = self.__colors.get("ENDC")
            print(beg_color + self.delimiter * self.col)
            res = func(*args)
            print(self.delimiter * self.col + end_color)
            return res
        return exec_fanc