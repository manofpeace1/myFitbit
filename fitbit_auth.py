import config
import fitbit
import gather_keys_oauth2 as Oauth2


def authorization():
    CLIENT_ID = config.CLIENT_ID
    CLIENT_SECRET = config.CLIENT_SECRET

    global ACCESS_TOKEN
    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

    global auth2_client
    auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True,
                                 access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)