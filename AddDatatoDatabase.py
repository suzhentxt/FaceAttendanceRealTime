import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-5cd37-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "090126":
        {
            "name": "To Trinh",
            "class": "11 KC",
            "starting_year": 2021,
            "total_attendance": 39,
            "standing": "3",
            "year": 2,
            "last_attendance_time": "2023-05-11 06:50:27"
        },
    "280726":
        {
            "name": "Ha Xuan Thien",
            "class": "11 Tin",
            "starting_year": 2021,
            "total_attendance": 34,
            "standing": "1",
            "year": 2,
            "last_attendance_time": "2023-05-11 06:50:27"
        },
    "963852":
        {
            "name": "Elon Musk",
            "class": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "1",
            "year": 2,
            "last_attendance_time": "2023-05-11 06:50:27"
        }
}

for key, value in data.items():
    ref.child(key).set(value)