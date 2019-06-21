import datetime
import fitbit_api


def run():
    fitbit_api.authorization()
    fitbit_api.get_sleep()
    fitbit_api.get_food()
    fitbit_api.get_water()

    print(f"""
    Today's Summary ({datetime.date.today()})

    🛌 {fitbit_api.sleep_result}

    🍔 {fitbit_api.food_result}

    💧 {fitbit_api.water_result}
    """)


run()
