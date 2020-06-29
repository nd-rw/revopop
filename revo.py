import re
from gazpacho import get, Soup
import time

def get_detailed_gym_info(gym_name):
    url = 'https://revofitness.com.au/'
    html = get(url)
    soup = Soup(html)
    clubs = soup.find('div', {'class': 'club'}, strict=True)
    nums_only = re.compile('[^0-9.]')
    str_return = True
    
    for club in clubs:
        if club.find('h4').text == gym_name:
            #print(club)
            specified_gym = club
    
    num_people = int(specified_gym.find('span', {'class': 'the-number'}).text)
    floor_space = int(nums_only.sub('', specified_gym.find('h6').text))
    ppl_per_metre = round(floor_space / num_people, 2)
    if str_return == True:
        gym_status_str = f'There are currently {num_people} people in the gym, with approx. {ppl_per_metre}m² of space each.'
        print(gym_status_str)
        return gym_status_str
    else:
        return {'gym_name': gym_name, 'num_people': num_people, 'floor_space': floor_space, 'ppl_per_metre': ppl_per_metre}

def get_gym_event():
    # TODO hard-coded to "Victoria Park", update to make function more generic

    url = 'https://revofitness.com.au/'
    gym_name = 'Victoria Park'
    html = get(url)
    soup = Soup(html)
    clubs = soup.find('div', {'class': 'club'}, strict=True)
    
    for club in clubs:
        if club.find('h4').text == gym_name:
            specified_gym = club
    
    # TODO add a beter empty/null/NA check here
    if specified_gym.find('span', {'class': 'the-number'}).text == 'N/A':
        num_people = 0
    else:
        num_people = int(specified_gym.find('span', {'class': 'the-number'}).text)
    curr_unix_time = int(time.time())
    
    return {'gym_name': gym_name, 'num_people': num_people, 'unix_time': curr_unix_time}