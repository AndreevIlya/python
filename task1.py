class Date:
    __day: int
    __month: int
    __year: int

    @classmethod
    def parse_date(cls, date: str):
        cls.__day = int(date[0:date.index(":")])
        date = date[date.index(":") + 1:]
        cls.__month = int(date[0:date.index(":")])
        date = date[date.index(":") + 1:]
        cls.__year = int(date)

    @classmethod
    def validate(cls) -> bool:
        if cls.__month in (1, 3, 5, 7, 8, 10, 12) and 0 < cls.__day < 32:
            return True
        if cls.__month in (4, 6, 9, 11) and 0 < cls.__day < 31:
            return True
        if cls.__month == 2 and 0 < cls.__day < 29:
            return True
        if Date.__is_leap_year(cls.__year) and cls.__month == 2 and 0 < cls.__day < 30:
            return True
        return False

    @staticmethod
    def __is_leap_year(year: int) -> bool:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    @classmethod
    def show_date(cls) -> str:
        return f"{cls.__day}:{cls.__month}:{cls.__year}"


date_str = input("Enter date in dd:mm:yyyy format: ")

Date.parse_date(date_str)

if Date.validate():
    print(f'Date {Date.show_date()} is valid.')
else:
    print(f'Date {Date.show_date()} is not valid.')
