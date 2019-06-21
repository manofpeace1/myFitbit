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

    endpoint = 'https://api.fitbit.com/1/user/-/'


def log_food(calorie):
    foodId = '717845813'
    mealTypeId = 7  # 7 = Anytime
    unitId = 270
    amount = calorie / 100
    url = f'{endpoint}foods/log.json?foodId={foodId}&mealTypeId={mealTypeId}&unitId={unitId}&amount={amount}&date={date_today}'

    post_request = requests.post(url,
                                 headers=headers
                                 )
    print(f'response code: {post_request.status_code}\n')


def log_water(ml):
    amount = ml
    unit = 'ml'
    url = f'{endpoint}foods/log/water.json?amount={amount}&unit={unit}&date={date_today}'

    post_request = requests.post(url,
                                 headers=headers
                                 )
    print(f'response code: {post_request.status_code}\n')
