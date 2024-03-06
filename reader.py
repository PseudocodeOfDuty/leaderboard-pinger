import csv 
import json

DIR = './data'

last_path = DIR + "/leaderboard_2024-03-05 23-59-20_3.json"

with open(last_path, 'r') as file:
    last = json.load(file)

def calc_eagle(t,j=1,alpha_e=2):
    return (0.7 * j - 0.3 / 213 * t + 0.3) * (1 + 0.2 * alpha_e) * 60

def get_alpha_e(s,j,t):
    s /= 60
    div = (0.7 * j - 0.3 / 213 * t + 0.3)
    s /= div
    s = (1-s)*-1
    s /= 0.2
    return s


def calc_fox(t,b=14,n=3,alpha_f=3,beta_f=0.9):
    return 16 * alpha_f / n + 12 * beta_f + 0.2 * b - 0.04 * t + 8

def get_b_fox(t,s,n=3,alpha_f=3,beta_f=0.9):
    s += -8 + 0.04 * t - 12 * beta_f - 16 * alpha_f / n
    s /= 0.2
    return int(round(s,0))
        
csv_file_path = 'final_leaderboard.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Rank','Team Name', 'Eagle Time','Eagle Score', 'Fox Time','Fox Score', 'Fox Budget','Total Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i,team in enumerate(last[:8]):
        name = team["team_name"]
        t_eagle = team['eagle_total_time_in_secs']
        s_eagle = team['eagle_score']
        s_fox = team['fox_score']
        t_fox = team['fox_total_time_in_secs']
        writer.writerow({
            'Rank' : i,
            'Team Name': name,
            'Eagle Time': t_eagle, 
            'Eagle Score': s_eagle,
            'Fox Time': t_fox, 
            'Fox Score': s_fox,
            'Fox Budget': get_b_fox(t_fox,s_fox),
            'Total Score': team['total_score']})


#1.AIMfinity   
#2.Azkaban     
#3.Psuedocode  
#4.Spaceship   
#5.CipherSphere
#6.Kickers     
#7.Dropouts    
#8.Main Void   