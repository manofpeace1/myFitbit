from fitbit_auth import authorization
import fitbit_get
import fitbit_post
import datetime

sleep_icon = '🛌'
food_icon = '🍔'
water_icon = '💧'


def show_summary():
    summary = f"""
    Today's Summary ({datetime.date.today()})

    {sleep_icon} {fitbit_get.sleep_result}

    {food_icon} {fitbit_get.food_result}

    {water_icon} {fitbit_get.water_result}
    """
    print(summary)


def log_start(item, log_type):

    while True:
        if item in ['food', 'water']:
            if item == 'food':
                user_input = input(f"\n{food_icon} Log Food (Calories) >>> ")
            elif item == 'water':
                user_input = input(f"\n{water_icon} Log Water (ml) >>> ")
            try:
                if int(user_input) > 0:
                    log_type(int(user_input))
                    break
                elif int(user_input) == 0:
                    pass
                    break
            except ValueError:
                print('Invalid input.')
        elif item in ['sleep']:
            user_input = input(f"\n{sleep_icon} Log Sleep (hour,HH:mm) >>> ")
            log_type(user_input)
            break


def run():
    authorization()
    fitbit_post.post_request_prepare()

    fitbit_get.get_sleep()
    fitbit_get.get_food()
    fitbit_get.get_water()
    show_summary()

    log_start('food', fitbit_post.log_food)
    log_start('water', fitbit_post.log_water)
    log_start('sleep', fitbit_post.log_sleep)


run()
