import os
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from src.view.ga4_report_dto import GA4_Query_Report  

class GA4Exception(Exception):
    '''Base class for GA4 exceptions'''

class GA4Connection:
    def __init__(self):
        load_dotenv()  
        self.service_account_file = os.getenv("SERVICE_ACCOUNT_FILE")
        self.credentials = Credentials.from_service_account_file(self.service_account_file, scopes=["https://www.googleapis.com/auth/analytics.readonly"])
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.service_account_file
        self.property_id = os.getenv("GA4_PROPERTY_ID")
        self.client = BetaAnalyticsDataClient()

    def query_report(self, ga4_query_report: GA4_Query_Report):
        date_range = DateRange(start_date=ga4_query_report.start_date, end_date=ga4_query_report.end_date)
        dimensions = [Dimension(name=dim_name) for dim_name in ga4_query_report.dimensions]
        metrics = [Metric(name=metric_name) for metric_name in ga4_query_report.metrics]
        request = RunReportRequest(property=f"properties/{self.property_id}", date_ranges=[date_range], dimensions=dimensions, metrics=metrics)
        response = self.client.run_report(request)
        return response
