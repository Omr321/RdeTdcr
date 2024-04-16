from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    
    # إذا تم استلام الكود بنجاح
    if code:
        access_token = get_access_token(code)
        
        # هنا يُمكنك استخدام الـ access_token للوصول إلى المعلومات من Discord API
        # مثلاً، يمكنك استخدامه للحصول على معلومات المستخدم
        
        return f"Access Token: {access_token}"
    else:
        return "Error: No code provided", 400

def get_access_token(code):
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
        return response.json()['access_token']
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
