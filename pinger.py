import requests
import schedule
import time
from win10toast import ToastNotifier
import json
from datetime import datetime


toaster = ToastNotifier()

def save_leaderboard(leaderboard, pos):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    filename = f"leaderboard_{timestamp}_{pos}.json"
    with open(filename, "w") as file:
        json.dump(leaderboard, file)

def ping_url():
    url = "http://3.70.97.142:5000/leaderboard"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Success")
            leaderboard = json.loads(response.text)['leaderboards']
            pos = 0
            for i in range(len(leaderboard)):
                if leaderboard[i]["team_name"]=="Pseudocode of duty":
                    pos = i+1
                    break
            msg = f"Your position is {pos}!"
            toaster.show_toast("Hacktrick Leaderboard",msg,duration=10)
            print(msg)
            save_leaderboard(leaderboard,pos)
        else:
            print(f"Error. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

schedule.every(15).minutes.do(ping_url)

ping_url()
while True:
    schedule.run_pending()
    time.sleep(1)
