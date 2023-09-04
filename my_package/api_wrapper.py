import requests


class ActivityApiWrapper:
    """Класс для работы с активностями"""
    site_path = "https://www.boredapi.com/api/activity"

    def get_activity(self, filters=None):
        """Запрос для вывода новой активности"""
        filters_dict = vars(filters)
        params = dict()
        for key, value in filters_dict.items():
            if value is not None:
                params[key] = value
        del params['subcommand']

        response = requests.get(self.site_path, params=params)
        return response.json()
