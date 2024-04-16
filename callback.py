from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "YOUR_WEBHOOK_URL"

@app.route('/callback')
def callback():
    code = request.args.get('code')
    
    # إذا تم استلام الكود بنجاح
    if code:
        user_info = get_user_info(code)
        
        # إرسال المعلومات إلى الـ Webhook
        send_to_webhook(user_info)
        
        return "Successfully sent to webhook"
    else:
        return "Error: No code provided", 400

def get_user_info(code):
    client_id = "1183756471687725056"
    client_secret = "NC9Hn1Sr83ZOR3oaFB3Z3pPLByM0dHH1"
    redirect_uri = "http://localhost:5000/callback"
    
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.post('https://discord.com/api/oauth2/token', data=payload, headers=headers)
    
    if response.status_code == 200:
        access_token = response.json()['access_token']
        
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        
        user_response = requests.get('https://discord.com/api/users/@me', headers=headers)
        
        if user_response.status_code == 200:
            return user_response.json()
    
    return None

def send_to_webhook(user_info):
    data = {
        'content': f"User ID: {user_info['id']}, Username: {user_info['username']}"
    }
    
    response = requests.post(WEBHOOK_URL, json=data)
    
    if response.status_code != 204:
        print(f"Failed to send to webhook: {response.text}")

if __name__ == '__main__':
    app.run(debug=True)
