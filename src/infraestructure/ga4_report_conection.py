import os
from dotenv import load_dotenv 
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.auth.exceptions import DefaultCredentialsError

class GA4Connection():
    def __init__(self):
        load_dotenv() 
        self.client = self.get_client()

    def get_client(self):
        try:
            credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

            if not credentials_path:
                root_folder = os.getenv("ROOT_FOLDER", default=".")
                os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(root_folder, "notCredentials.json")

            return BetaAnalyticsDataClient()
        except DefaultCredentialsError as e:
            print(f"Error al obtener las credenciales: {e}")
            raise Exception("Error en la conexión a Google Analytics") from e

        except Exception as e:
            print(f"Error general: {e}")
        finally:
            pass

GA4Connection()
