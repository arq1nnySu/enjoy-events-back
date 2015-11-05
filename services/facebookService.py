from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from api import app, USERS, User

SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = '687026038097556'
FACEBOOK_APP_SECRET = 'f1258179572be6ecfd0d498494b80139'

oauth = OAuth()
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='http://localhost:5000/fb/login/authorized',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)


@app.route('/fb/login')
def login():
    return facebook.authorize(callback=url_for('/fb/login/authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@app.route('/fb/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    return 'Logged in as id=%s name=%s redirect=%s' % \
        (me.data['id'], me.data['name'], request.args.get('next'))


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')
