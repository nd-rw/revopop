from revo import get_gym_event, get_detailed_gym_info
from bonescraper import create_sqlite_event_query, update_sqlite, print_sqlite_rows
import time

if __name__ == '__main__':
    curr_event = get_gym_event()
    update_query = create_sqlite_event_query(curr_event, 'gym_population')
    print(update_query)