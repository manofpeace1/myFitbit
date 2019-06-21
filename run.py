from fitbit_auth import authorization
import fitbit_get
import fitbit_post
import datetime


def show_summary():
    summary = f"""
    Today's Summary ({datetime.date.today()})

    🛌 {fitbit_get.sleep_result}

    🍔 {fitbit_get.food_result}

    💧 {fitbit_get.water_result}
    """
    print(summary)


def log_food_input():
    while True:
        food_user_input = input("\n🍔 Log Food (Calories) >>> ")
        try:
            if int(food_user_input) > 0:
                fitbit_post.log_food(int(food_user_input))
                break
            elif int(food_user_input) == 0:
                pass
                break
        except ValueError:
            print("Invalid input.")


def log_water_input():
    while True:
        water_user_input = input("\n💧 Log Water (ml) >>> ")
        try:
            if int(water_user_input) > 0:
                fitbit_post.log_water(int(water_user_input))
                break
            elif int(water_user_input) == 0:
                pass
                break
        except ValueError:
            print("Invalid input.")


def run():
    authorization()

    fitbit_get.get_sleep()
    fitbit_get.get_food()
    fitbit_get.get_water()
    show_summary()

    fitbit_post.post_request_prepare()
    log_food_input()
    log_water_input()


run()
