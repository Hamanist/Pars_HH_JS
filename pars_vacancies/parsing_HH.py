from typing import Optional, List

import requests

from pars_abc.abc_pars import VacancyParsing
from source import SourceType
from vacancies.hh import VacanciesHH


class ParsingHH(VacancyParsing):

    def get_vacancies(self, word_search) -> Optional[List[VacanciesHH]]:
        __url = 'https://api.hh.ru/vacancies/'
        __params = {
            'text': word_search,  # word_search
            'per_page': '20',
            'area': 113
        }
        response = requests.get(url=__url, params=__params)
        if response.status_code == 200:
            return self._pars(response.json())
        return None

    def _pars(self, data) -> Optional[List[VacanciesHH]]:
        answer = []
        for report in data['items']:
            answer.append(
                VacanciesHH(
                    job_title=report['name'],
                    company=report['employer']['name'],
                    url=report['alternate_url'],
                    salary_min=(report['salary'] or {}).get("from"),
                    salary_max=(report['salary'] or {}).get("to"),
                    requirements=report['snippet']['requirement'],
                    source=SourceType.hh
                )
            )

        return answer
