import csv
from typing import List

from pars_vacancies.parsing_HH import ParsingHH
from pars_vacancies.parsing_SJ import ParsingSJ
from vacancies.hh import VacanciesHH
from vacancies.sj import VacanciesSJ


class Catalog:
    list_hh: List[VacanciesHH] = []
    list_sj: List[VacanciesSJ] = []

    def upload_vacancies(self):
        self.list_hh = ParsingHH().get_vacancies()
        self.list_sj = ParsingSJ().get_vacancies()

    def save_to_file(self):
        with open('./vacancies.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                ('job_title', 'company', 'url', 'salary_min', 'salary_max', 'requirements', 'source')
            )
        if self.list_hh or self.list_hh:
            with open('./vacancies.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerows(
                    ([report.get_from_list() for report in self.list_hh + self.list_sj])
                )

    def read_from_file(self):
        with open('./vacancies.csv', 'r') as file:
            reader = csv.DictReader(file)
            answer = []
            for i in reader:
                answer.append(i)
            return answer
