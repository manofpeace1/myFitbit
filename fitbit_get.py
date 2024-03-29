import fitbit
import fitbit_auth
from datetime import date, timedelta


def days_ago(num):
    global days_ago_date
    days_ago_date = date.today() - timedelta(days=num)


def get_sleep():
    sleep_log = fitbit_auth.auth2_client.sleep(
        date=None, user_id=None, data=None)

    global sleep_result
    if len(sleep_log['sleep']) == 0:
        sleep_result = 'Sleep log not found.'
    else:
        def sleep_start_end(
            key): return sleep_log['sleep'][0][key].split("T")[1][0:5]
        sleep_start = sleep_start_end('startTime')
        sleep_end = sleep_start_end('endTime')
        sleep_length = sleep_log['summary']['totalTimeInBed'] / 60
        sleep_result = f"""You slept {float(sleep_length)} hours.
    | slept: {sleep_start}
    | wokeup: {sleep_end}"""


def get_food():
    food_log = fitbit_auth.auth2_client.foods_log(
        date=None, user_id=None, data=None)
    food_calorie_limit = food_log['goals']['estimatedCaloriesOut']
    food_calorie_goal = food_log['goals']['calories']
    food_calorie_intake = food_log['summary']['calories']

    global food_result
    food_result = f"""You can eat {food_calorie_goal - food_calorie_intake} calories more.
    | limit: {food_calorie_limit}
    | goal: {food_calorie_goal} ({food_calorie_goal - food_calorie_limit})
    | consumed: {food_calorie_intake}"""


def get_food_30days():
    global food_30days_result
    food_30days_result = []

    i = 0
    while i < 30:
        i += 1
        days_ago(i)
        food_log = fitbit_auth.auth2_client.foods_log(
            date=days_ago_date, user_id=None, data=None)
        food_calorie_goal = food_log['goals']['calories']
        food_calorie_intake = food_log['summary']['calories']
        food_30days_result.append(
            f"{days_ago_date},{food_calorie_goal},{food_calorie_intake}")


def get_water():
    water_log = fitbit_auth.auth2_client.foods_log_water(
        date=None, user_id=None, data=None)
    water_goal = 1900
    water_total = water_log['summary']['water'] * \
        29.5735  # OZ to ML = 1:29.5735

    global water_result
    water_result = f"""You should drink {int(water_goal - water_total)}ml more.
    | consumed: {int(water_total)}ml"""


def search_food(food_name):
    # Useful when creating new food input
    global food
    food = fitbit_auth.auth2_client.search_foods(food_name)
    print(food)
