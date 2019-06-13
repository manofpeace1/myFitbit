import config
import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

yesterday = str((datetime.datetime.now() -
                 datetime.timedelta(days=1)).strftime("%Y%m%d"))

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True,
                             access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


fit_statsHR = auth2_client.intraday_time_series(
    'activities/heart', base_date='2019-05-29', detail_level='15min')

time_list = []
val_list = []
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_list.append(i['value'])
    time_list.append(i['time'])
heartdf = pd.DataFrame({'Heart Rate': val_list, 'Time': time_list})

print(heartdf)
