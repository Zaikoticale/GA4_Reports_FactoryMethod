from src.domain.ga4_report_domain import GA4ReportFactory
from src.infraestructure.ga4_report_conection import GA4Connection, GA4Exception
from src.view.ga4_report_dto import GA4_Query_Report


class ExecuteGA4ReportUseCase:
    def __init__(self, connection: GA4Connection):
        self.connection = connection

    def execute_report(self, report_type, start_date, end_date):
        report = GA4ReportFactory.create_report(report_type, start_date, end_date)

        try:
            result = self.connection.query_report(report)
            # Extract the headers' names from dimension_headers and metric_headers
            headers = [header.name for header in result.dimension_headers] + [header.name for header in result.metric_headers]
            # Extract the rows of data
            rows = [[value.value for value in row.dimension_values] + [value.value for value in row.metric_values] for row in result.rows]
            result_dict = {
                'rows': rows,
                'headers': headers
            }
            return result_dict
        except GA4Exception as e:
            raise e

