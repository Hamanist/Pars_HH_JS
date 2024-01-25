from abc import ABC, abstractmethod


class VacancyParsing(ABC):
    """
    Абстрактный класс для парсинга HH и SJ
    """

    @abstractmethod
    def get_vacancies(self, word_search):
        """
        :return: Получаем вакансии
        """
        pass

    @abstractmethod
    def _pars(self, data):
        """
        :return: Список вакансий
        """
        pass
