import fitbit_auth
import requests
import datetime


def post_request_prepare():
    global headers, date_today, endpoint
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {fitbit_auth.ACCESS_TOKEN}"
    }
    date_today = datetime.date.today()

    endpoint = 'https://api.fitbit.com'


def post_request_send(url):
    post_request = requests.post(url,
                                 headers=headers
                                 )
    print(f'response code: {post_request.status_code}\n')
    print(post_request.json())


def log_food(calorie):
    api_version = 1
    foodId = 717845813
    mealTypeId = 7  # 7 = Anytime
    unitId = 270
    amount = calorie / 100
    log_food_url = f'{endpoint}/{api_version}/user/-/foods/log.json?foodId={foodId}&mealTypeId={mealTypeId}&unitId={unitId}&amount={amount}&date={date_today}'

    post_request_send(log_food_url)


def log_water(ml):
    api_version = 1
    amount = ml
    unit = 'ml'
    log_water_url = f'{endpoint}/{api_version}/user/-/foods/log/water.json?amount={amount}&unit={unit}&date={date_today}'

    post_request_send(log_water_url)


def log_sleep(duration_startTime):
    duration = duration_startTime.split(",")[0]
    startTime = duration_startTime.split(",")[1]
    api_version = 1.2
    duration_millisec = int(duration) * 3600000

    log_sleep_url = f'{endpoint}/{api_version}/user/-/sleep.json?startTime={startTime}&duration={duration_millisec}&date={date_today}'

    post_request_send(log_sleep_url)
