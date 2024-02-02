from src.usecase.ga4_report_generate_usecase import ExecuteGA4ReportUseCase
from src.infraestructure.ga4_report_conection import GA4Connection, GA4Exception
from src.view.ga4_report_dto import GA4_Query_Report, GA4RerportDTO

class GA4Controller:
    def __init__(self, use_case: ExecuteGA4ReportUseCase):
        self.use_case = use_case
        self.connection = GA4Connection()

    def query_report(self, ga4_query_report: GA4RerportDTO):
        try:
            # Llamar al método execute_report en tu use_case
            return self.use_case.execute_report(
                ga4_query_report.report_type,
                ga4_query_report.start_date,
                ga4_query_report.end_date
            )
        except GA4Exception as e:
            raise e
