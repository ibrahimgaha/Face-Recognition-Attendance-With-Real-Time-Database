import firebase_admin
from firebase_admin import credentials
from firebase_admin import  db
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://face-attendace-in-real-time-default-rtdb.firebaseio.com/'
})

ref = db.reference("Students")
data = {
    "12347": {
        "name": "Elon Musk",
        "Major": "Robotics",
        "Starting_Year": 2010,  # Consistent key
        "Total_Attendance": 6,
        "Standings": "G",
        "Year": 4,
        "Last_Attendance_Time": "2024-09-08 13:54:34"
    },
    "45612": {
        "name": "Hafedh Gaha",
        "Major": "HyperFrequency",
        "Starting_Year": 2012,  # Change this key to be consistent
        "Total_Attendance": 13,
        "Standings": "VG",
        "Year": 10,
        "Last_Attendance_Time": "2024-03-16 12:10:19"
    },
    "85410": {
        "name": "Ibrahim Gaha",
        "Major": "Developer",
        "Starting_Year": 2024,  # Change this key as well
        "Total_Attendance": 3,
        "Standings": "VG",
        "Year": 2,
        "Last_Attendance_Time": "2024-07-11 11:34:49"
    },
    "89105": {
        "name": "Ines Sahtout",
        "Major": "Architecture",
        "Starting_Year": 2015,  # Change this key as well
        "Total_Attendance": 9,
        "Standings": "G",
        "Year": 6,
        "Last_Attendance_Time": "2021-03-02 13:42:26"
    }
}

for key,value in data.items():
    ref.child(key).set(value)
