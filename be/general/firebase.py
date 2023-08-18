import pyrebase
import requests


firebaseConfig = {
    "apiKey": "AIzaSyCxpGkBUnUDYsjkELhdWXkcg9z9NwhX_UY",
    "authDomain": "mykiot-19eb7.firebaseapp.com",
    "databaseURL": "https://mykiot-19eb7-default-rtdb.firebaseio.com",
    "projectId": "mykiot-19eb7",
    "storageBucket": "mykiot-19eb7.appspot.com",
    "messagingSenderId": "166049269755",
    "appId": "1:166049269755:web:9e2ca7a72ac1a10d9b2d5e",
    "measurementId": "G-WZQTHNN623"
}
# Try connect to firebase
try:
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    database = firebase.database()
except:
    pass

# FCM clound messaging
def send_notification_topic(title, content, code, topic, data):
    payload = { 
        "notification" : {
            "click_action" : "FLUTTER_NOTIFICATION_CLICK", 
            "body" : content, 
            "title" : title, 
            "code": code,
            "icon" : None
        }, 
        "data": data,
        "to" : "/topics/{}".format(topic)
    }
    header = {
        "Content-Type": "application/json",
        "Authorization": "key=AAAAJqlOx_s:APA91bGq18rDK3UqJxP2i0e2k5kf8Pj-Y5pzf4fOcTR6iO_RdYRxKLFXhrcwoeBLSIOiA0wS7g-bZxLkf0GjkLIhVDNL7i2hCdys5bCMJltHz2KoxCu1m7fLsZ0SXhx0EoHO7xFx1gy9"
    }
    try:
        response = requests.post('https://fcm.googleapis.com/fcm/send', json=payload, headers=header).json()
    except: 
        pass