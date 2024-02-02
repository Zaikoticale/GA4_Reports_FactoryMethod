class GA4RerportDTO:
    def __init__(self, report_type, dimensions, metrics, row_limit, quota_usage, realtime, start_date, end_date):
        self.report_type = report_type
        self.dimensions = dimensions
        self.metrics = metrics
        self.row_limit = row_limit
        self.quota_usage = quota_usage
        self.realtime = realtime
        self.start_date = start_date
        self.end_date = end_date


class GA4_Query_Report:
    def __init__(self, report_type, dimensions, metrics, row_limit, quota_usage, realtime, start_date, end_date):
        self.report_type = report_type
        self.dimensions = dimensions
        self.metrics = metrics
        self.row_limit = row_limit
        self.quota_usage = quota_usage
        self.realtime = realtime
        self.start_date = start_date
        self.end_date = end_date    


