import unittest
from argparse import Namespace
from unittest.mock import patch
import tempfile
import os
from my_package.database import ActivityDataBase
from my_package.api_wrapper import ActivityApiWrapper


class TestActivityDatabase(unittest.TestCase):
    def setUp(self):
        # Создание временного файл для тестовой базы данных SQLite
        self.db_file = tempfile.mktemp()
        self.db = ActivityDataBase(self.db_file)

    def tearDown(self):
        # Закрытие соединения с базой данных и удаление временного файл
        self.db.close()
        os.remove(self.db_file)

    def test_save_and_get_activity(self):
        activity_data = {
            'activity': 'Test Activity',
            'accessibility': 0.5,
            'type': 'test',
            'participants': 2,
            'price': 10.0,
            'key': 123
        }

        self.db.save_activity(activity_data)
        latest_activities = self.db.get_latest_activities()

        # Проверяем что длина кортежа записей = 1 и данные в нем тоже верны
        self.assertEqual(len(latest_activities), 1)
        self.assertEqual(latest_activities[0][1], activity_data['activity'])


class TestActivityApiWrapper(unittest.TestCase):
    def setUp(self):
        self.api_wrapper = ActivityApiWrapper()

    @patch('requests.get')
    def test_get_activity(self, mock_get):
        mock_response = {
            'activity': 'Mock Activity',
            'accessibility': 0.7,
            'type': 'mock',
            'participants': 3,
            'price': 5.0,
            'key': 456
        }
        mock_get.return_value.json.return_value = mock_response

        # Вызываем метод get_activity с фиктивными данными
        result = self.api_wrapper.get_activity(Namespace(subcommand='new', activity=None, accessibility=None,
                                                         type=None, participants=None, price=None, key=None,
                                                         price_min=None, price_max=None, accessibility_min=None,
                                                         accessibility_max=None))

        self.assertEqual(result, mock_response)


if __name__ == '__main__':
    unittest.main()
