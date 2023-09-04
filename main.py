import argparse
from my_package.api_wrapper import ActivityApiWrapper
from my_package.database import ActivityDataBase


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch random activity or latest activities.')

    subparsers = parser.add_subparsers(title='Subcommands', dest='subcommand', description='Choose a subcommand', required=True)

    # Подкоманда 'new'
    parser_new = subparsers.add_parser('new', help='Команда для получения и сохранения новой активности')
    arguments = ('--activity', '--accessibility', '--type', '--participants', '--price',
                 '--key', '--price_min', '--price_max', '--accessibility_min', '--accessibility_max')
    [parser_new.add_argument(argument) for argument in arguments]

    # Подкоманда 'latest_activities'
    parser_latest = subparsers.add_parser('latest_activities', help='Команда для получения последних активностей')

    args = parser.parse_args()

    if args.subcommand == 'new':
        api_wrapper = ActivityApiWrapper()
        db_manager = ActivityDataBase('main_db.db')
        random_activity = api_wrapper.get_activity(args)
        db_manager.save_activity(random_activity)
        db_manager.close()
        print(random_activity)
    elif args.subcommand == 'latest_activities':
        db_manager = ActivityDataBase('main_db.db')
        latest_activities = db_manager.get_latest_activities()
        db_manager.close()
        print(*latest_activities, sep='\n')