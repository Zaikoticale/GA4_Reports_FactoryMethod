import os
import pandas as pd
from src.infraestructure.ga4_report_conection import GA4Connection
from src.view.ga4_report_controller import GA4Controller
from src.usecase.ga4_report_generate_usecase import ExecuteGA4ReportUseCase
from src.domain.ga4_report_domain import GA4ReportFactory
from datetime import datetime, timedelta

start_date_str = "2023-07-01"
end_date_str = "2023-12-01"

start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

backup_folder = "backup"
os.makedirs(backup_folder, exist_ok=True)

ga4_connection = GA4Connection()
execute_use_case = ExecuteGA4ReportUseCase(ga4_connection)
ga4_controller = GA4Controller(execute_use_case)

current_date = start_date
while current_date <= end_date:
    current_date_str = current_date.strftime("%Y-%m-%d")

    report_folder = os.path.join(backup_folder, f'report_{current_date_str}')
    os.makedirs(report_folder, exist_ok=True)

    # users_report = GA4ReportFactory.create_report(
    #     report_type="users",
    #     start_date=current_date_str,
    #     end_date=current_date_str
    # )
    # users_result = ga4_controller.query_report(users_report)
    # users_df = pd.DataFrame(users_result['rows'], columns=users_result['headers'])
    # users_folder = os.path.join(report_folder, 'usuarios')
    # os.makedirs(users_folder, exist_ok=True)
    # users_df.to_csv(os.path.join(users_folder, f'users_report_{current_date_str}.csv'), index=False)
    # print(f"Users report for {current_date_str} saved to '{users_folder}/users_report_{current_date_str}.csv'")

    # page_views_report = GA4ReportFactory.create_report(
    #     report_type="page_views",
    #     start_date=current_date_str,
    #     end_date=current_date_str
    # )
    # page_views_result = ga4_controller.query_report(page_views_report)
    # page_views_df = pd.DataFrame(page_views_result['rows'], columns=page_views_result['headers'])
    # page_views_folder = os.path.join(report_folder, 'page_views')
    # os.makedirs(page_views_folder, exist_ok=True)
    # page_views_df.to_csv(os.path.join(page_views_folder, f'page_views_report_{current_date_str}.csv'), index=False)
    # print(f"Page Views report for {current_date_str} saved to '{page_views_folder}/page_views_report_{current_date_str}.csv'")

    activeUserspPerDayReport = ga4_controller.query_report(
        GA4ReportFactory.create_report(
            report_type="activeUserspPerDay",
            start_date=current_date_str,
            end_date=current_date_str
        )
    )
    activeUserspPerDay_df = pd.DataFrame(activeUserspPerDayReport['rows'], columns=activeUserspPerDayReport['headers'])
    activeUserspPerDay_folder = os.path.join(report_folder, 'activeUserspPerDay')
    os.makedirs(activeUserspPerDay_folder, exist_ok=True)
    activeUserspPerDay_df.to_csv(os.path.join(activeUserspPerDay_folder, f'activeUserspPerDay_report_{current_date_str}.csv'), index=False)
    print(f"activeUserspPerDay report for {current_date_str} saved to '{activeUserspPerDay_folder}/activeUserspPerDay_report_{current_date_str}.csv'")

    current_date += timedelta(days=1)
