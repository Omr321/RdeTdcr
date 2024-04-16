from flask import Flask, redirect, url_for
import urllib.parse

app = Flask(__name__)

# وظائف OAuth2 المختلفة
@app.route('/oauth/messages_read')
def oauth_messages_read():
    # ... (كود التوجيه)

@app.route('/oauth/activities_read')
def oauth_activities_read():
    # ... (كود التوجيه)

@app.route('/oauth/guilds_join')
def oauth_guilds_join():
    # ... (كود التوجيه)

@app.route('/oauth/gdm_join')
def oauth_gdm_join():
    # ... (كود التوجيه)

@app.route('/oauth/rpc_notification_read')
def oauth_rpc_notification_read():
    # ... (كود التوجيه)

@app.route('/oauth/rpc_voice_write')
def oauth_rpc_voice_write():
    # ... (كود التوجيه)

@app.route('/oauth/rpc_video_write')
def oauth_rpc_video_write():
    # ... (كود التوجيه)
  @app.route('/oauth/rpc.screenshare.read')
    def oauth_rpc_screenshare_read
   @app.route('/oauth/rpc_screenshare_read')
def oauth_rpc_screenshare_read():
    client_id = "1183756471687725056"
    redirect_uri = "http://localhost:5000/callback/rpc_screenshare_read"
    scope = "rpc.screenshare.read"
    oauth_url = f"https://discord.com/oauth2/authorize?client_id={client_id}&redirect_uri={urllib.parse.quote(redirect_uri)}&response_type=code&scope={scope}"
    
    return redirect(oauth_url)

if __name__ == '__main__':
    app.run(debug=True)
