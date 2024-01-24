

class GA4_Query_Report(self,dimensions,metrics,row_limit,quota_usage,realtime,start_date,end_date):
    def __init__(self, dimensions, metrics, row_limit, quota_usage, realtime, start_date, end_date):
        self.dimensions = dimensions
        self.metrics = metrics
        self.row_limit = row_limit
        self.quota_usage = quota_usage
        self.realtime = realtime
        self.start_date = start_date
        self.end_date = end_date    

