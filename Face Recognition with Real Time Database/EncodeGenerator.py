import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import  db
from firebase_admin import storage

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://face-attendace-in-real-time-default-rtdb.firebaseio.com/',
    'storageBucket':'face-attendace-in-real-time.appspot.com'
})


# Importing the students images
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
studentIds=[]

for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # Take only the id from the file name
    studentIds.append(os.path.splitext(path)[0])
    # create a directory in the storage and add the images to it as the id is the name
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    bloc = bucket.blob(fileName)
    bloc.upload_from_filename(fileName)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds =[encodeListKnown,studentIds]
print("Encoding Complete !")

file = open("EncodeFile.p","wb")
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved !")
