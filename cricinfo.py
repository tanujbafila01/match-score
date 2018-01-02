from bs4 import BeautifulSoup
import requests
import urllib.response,urllib.request, urllib.parse, urllib.error
import json
from multiprocessing import Process
import time

#returns a list of all matchces on Live Criciet scores page on espncricinfo
def list_of_all_matches():
    page=urllib.request.urlopen('http://www.espncricinfo.com/ci/engine/match/index.html?view=live')
    soup=BeautifulSoup(page,'html.parser')
    all_matches = soup.find_all('span',{'class':"match-no"})
    match_detail=[]
    for line in all_matches:
        match_info=(str(line.find('a')['href']))
        match_name=(match_info.split('/')[1]).replace('-',' ')
        match_id=(match_info.split('/')[-1]).split('.')[0]
        match_detail.append((match_name+'_'+match_id))
    return match_detail

def get_score(match_id):
    url='http://www.espncricinfo.com/sunfoil-series-2016-17/engine/match/'+str(match_id)+'.json'
    match_page_json = requests.get(url).json()
    match_summary=match_page_json["match"]["current_summary"]
    return str(match_summary)


def doWork():
    while True:
        print(get_score(1073405)+'      '+str(time.asctime(time.localtime(time.time()))))
        time.sleep(60)

if __name__=='__main__':
    p=Process(target=doWork)
    p.start()
    while True:
        time.sleep(120)

all_matches= list_of_all_matches()
for item in all_matches:
    if 'india' in str.lower(item.split('_')[0]):
        score = get_score(item.split('_')[1])




'''if json_obj["centre"]["batting"][0]["live_current_name"]=="striker":
        batsman_strike = json_obj["centre"]["batting"][0]["known_as"]
        batsman_strike_runs = json_obj["centre"]["batting"][0]["runs"]
        batsman_strike_balls = json_obj["centre"]["batting"][0]["balls_faced"]
    return map(str, [batsman_strike, batsman_strike_runs, batsman_strike_balls])'''


'''match_soup=BeautifulSoup(match_page,'html.parser')
team1_name=match_soup.find('div',attrs={'class':"team-1-name"})
team2_name=match_soup.find('div',attrs={'class':"team-2-name"})
first_inning_score=match_soup.find('span',attrs={'class':"innings-1-score innings-current"})
second_inning_score=match_soup.find('span',attrs={'class':"innings-2-score"})
print team1_name.text,team2_name.text
print first_inning_score'''
