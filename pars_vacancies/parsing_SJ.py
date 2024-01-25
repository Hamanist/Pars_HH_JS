import os
from typing import Optional, List

import requests
from dotenv import load_dotenv

from pars_abc.abc_pars import VacancyParsing
from source import SourceType
from vacancies.sj import VacanciesSJ

load_dotenv()


class ParsingSJ(VacancyParsing):

    def get_vacancies(self, word_search) -> Optional[List[VacanciesSJ]]:
        __headers = {
            'X-Api-App-Id': os.getenv('SJ_API')
        }
        __url = 'https://api.superjob.ru/2.0/vacancies'
        params = {
            'count': 20,
            'keyword': word_search
        }
        response = requests.get(url=__url, headers=__headers, params=params)
        if response.status_code == 200:
            return self._pars(response.json())
        return None

    def _pars(self, data):
        answer = []
        for report in data['objects']:
            answer.append(
                VacanciesSJ(
                    job_title=report['profession'],
                    company=(report['client'] or {}).get('title'), #(report['salary'] or {}).get("from")
                    url=report['link'],
                    salary_min=report['payment_from'],
                    salary_max=report['payment_to'],
                    requirements=report['candidat'],
                    source=SourceType.sj
                )
            )

        return answer
