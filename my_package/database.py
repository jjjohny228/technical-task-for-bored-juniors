import sqlite3


class ActivityDataBase:
    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS activities ("
                         "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                         "activity TEXT,"
                         "accessibility REAL,"
                         "type TEXT,"
                         "participants INTEGER,"
                         "price REAL,"
                         "key INTEGER)")

    def save_activity(self, some_activity):
        """Сохранение активности в БД"""
        self.cur.execute("INSERT INTO activities (activity, accessibility, type, participants, price, key) "
                         "VALUES (?, ?, ?, ?, ?, ?)",
                         (some_activity['activity'], some_activity['accessibility'], some_activity['type'],
                          some_activity['participants'], some_activity['price'], some_activity['key'])
                         )
        self.connection.commit()

    def get_latest_activities(self):
        """Получение 5 последних активностей из БД"""
        activities = self.cur.execute("SELECT * FROM activities ORDER BY id DESC LIMIT 5").fetchall()
        if not activities:
            return ("Нет записей в базе данных",)
        return activities

    def close(self):
        """Закрытие соединения с БД"""
        self.connection.close()