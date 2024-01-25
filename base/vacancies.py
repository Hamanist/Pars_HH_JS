from source import SourceType


class VacanciesBase:
    """
    Основной класс для работы для работы с вакансиями
    """

    job_title: str
    company: str
    url: str
    salary_min: int | float
    salary_max: int | float
    requirements: str
    source: SourceType

    def __init__(self, job_title: str,
                 company: str,
                 url: str,
                 requirements: str,
                 source: SourceType,
                 salary_min=0,
                 salary_max=0):
        self.job_title = job_title
        self.company = company
        self.url = url
        self.salary_min = salary_min or 0
        self.salary_max = salary_max or 0
        self.requirements = requirements
        self.source = source

    def __str__(self):
        return f'Должность {self.job_title} ' \
               f'в {self.company}\n' \
               f'Зарплата от {self.salary_min} до {self.salary_max}\n' \
               f'Требования: {self.requirements}\n' \
               f'Источник вакансии {self.source.value}'

    def __eq__(self, other):
        return self.salary_max == other.salary_max

    def __ne__(self, other):
        return self.salary_max != other.salary_max

    def __lt__(self, other):
        return self.salary_max < other.salary_max

    def __le__(self, other):
        return self.salary_max <= other.salary_max

    def __gt__(self, other):
        return self.salary_max > other.salary_max

    def __ge__(self, other):
        return self.salary_max >= other.salary_max

    def get_from_string(self):
        return ','.join(
            [self.job_title,
             self.company,
             self.url,
             str(self.salary_min),
             str(self.salary_max),
             self.requirements,
             self.source.value]) + '\n'

    def get_from_list(self):
        return str(self.job_title), str(self.company), str(self.url), str(self.salary_min), str(self.salary_max), \
            str(self.requirements).replace('\n', ' '), \
            str(self.source.value)
