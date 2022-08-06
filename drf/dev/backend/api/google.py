import requests


def google(request):
    client_id = '772315920728-bgm3mgrkhre9dg2kt1vapap63cl3o3nn.apps.googleusercontent.com'
    redirect_uri = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    user_token = request.GET.get('code')
    print(user_token)
    token_request = requests.post(
        f"https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={redirect_uri}&prompt=consent&response_type=code&client_id={client_id}&scope=openid%20email%20profile&access_type=offline")
    token_response_json = token_request.json()
    print(token_response_json)
    access_token = token_response_json.get("access_token")
    id_token=token_response_json.get("id_token")
    print(access_token)
    print('id_token')
    return 200
