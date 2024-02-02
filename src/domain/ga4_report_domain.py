from abc import ABC, abstractmethod
from src.view.ga4_report_dto import GA4RerportDTO

class GA4Report(ABC):
    @abstractmethod
    def create_query_report(self, *args, **kwargs):
        pass

class activeUserspPerDayReport(GA4Report):
    def create_query_report(self, start_date, end_date):
        return GA4RerportDTO(
            report_type="activeUserspPerDay",
            dimensions=["date",],
            metrics=["activeUsers"],
            row_limit=1000000000,
            quota_usage=False,
            realtime=False,
            start_date=start_date,
            end_date=end_date,
        )

class GA4ReportFactory:
    @staticmethod
    def create_report(report_type, *args, **kwargs):
        if report_type == "activeUserspPerDay":
            return activeUserspPerDayReport().create_query_report(*args, **kwargs)
        else:
            raise ValueError("Invalid report type")
