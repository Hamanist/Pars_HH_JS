from base.vacancies import VacanciesBase
from source import SourceType


class VacanciesSJ(VacanciesBase):
    def __init__(self, job_title: str, company: str, url: str, requirements: str, source: SourceType, salary_min=0, salary_max=0):
        super().__init__(job_title, company, url, requirements, source, salary_min, salary_max)
        self.source = SourceType.sj
