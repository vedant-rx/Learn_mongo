from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
url =os.getenv("URL")
print(url)

client = MongoClient(url)

db_name = client["ytmanager"]
video_collection = db_name["videos"]
print(video_collection)

def list_all_videos():
    for vid in video_collection.find():
        print(f"video id is {vid['_id']}, Name: {vid['name']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("YT Manager \n")
        print(" 1. List all videos \n")
        print(" 2. Add a new video \n")
        print(" 3. Update a video \n")
        print(" 4. Delete a video \n")
        print(" 5. Exit \n")
        choice = input("enter your choice: \n")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the video name")
                time = input("Enter the video time")
                add_video(name, time)
            case '3':
                id = input("Enter the video id")
                name = input("Enter the updated video name")
                time = input("Enter the updated video time")
                update_video(id, name, time)
            case '4':
                id = input("Enter the video id to be deleted")
                delete_video(id)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()