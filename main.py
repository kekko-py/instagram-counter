import requests
from playsound import playsound
import os

dirname, filename = os.path.split(os.path.abspath(__file__))

def instagram(user):
    url = 'https://www.instagram.com/' + user
    r = requests.get(url).text
    start = '"edge_followed_by":{"count":'
    end = '},"followed_by_viewer"'
    follower = r[r.find(start)+len(start):r.rfind(end)]
    return follower

if __name__ == '__main__':
    print("Programma Sviluppato da @kekko.py")
    print("Cerca kekko.py su TikTok per altri progetti\n\n")
    user = input("Il tuo Username: ")
    print("Analisi di "+user+" Iniziata \n____________________________________")
    iniziali = int(instagram(user))
    while True:
        nuovi = int(instagram(user))
        if nuovi>iniziali:
            print("Nuovo Follower!!!!")
            playsound(f'{dirname}/alert.mp3')
        iniziali=nuovi

