import random
import json


def replace(lyrics):
    wordMap = json.loads(open('wordMap.json').read())
    count = 0
    for k in wordMap.keys():
        if lyrics.find(k) >= 0:
            count += 1
        lyrics = lyrics.replace(k, wordMap[k])

    return lyrics, count


def getCheer():
    # load all songs
    songs = json.loads(open('allsongs').read())
    # pick random song in album
    song = random.choice(songs)
    # get lyrics for random song
    lyrics = song['lyrics'].lower()

    # lines shouldn't be blank
    lines = [l for l in lyrics.split('\n') if len(l) != 0]
    # lines shouldn't have parens or brackets
    lines = [l for l in lines if l.find('(') == -1]
    lines = [l for l in lines if l.find(')') == -1]
    lines = [l for l in lines if l.find('[') == -1]
    lines = [l for l in lines if l.find(']') == -1]

    if len(lines) < 10:
        return getCheer()
    start = random.choice(range(len(lines) - 9))
    nine = lines[start:start+9]
    lyrics = '\n'.join(nine)

    # replace naughty werds :P
   # lyrics, count = replace(lyrics)
    #if count < 2 or lyrics.find('TRUDGE') == -1:
     #   return getCheer()
# why would you ever want to replace them?
        
    # replace new lines with breaks becasue HTML
    return lyrics.replace('\n', '<br>')
    
