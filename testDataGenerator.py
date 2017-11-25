import json

data = {}
data['quests'] = []
data['characters'] = []

quest = {}
quest['task'] = "Feed the dog"
quest['time'] = '2h 7m'
quest['xp'] = '10,000'
quest['progressText'] = ''
quest['progressProgress'] = ''
quest['progressTarget'] = ''
quest['status'] = 'active'
data['quests'].append(quest)

quest = {}
quest['task'] = "Play with the dog"
quest['time'] = '37h 18m'
quest['xp'] = '10,000'
quest['progressText'] = 'Fetches'
quest['progressProgress'] = '0'
quest['progressTarget'] = '10'
quest['status'] = 'active'
data['quests'].append(quest)

#note:
#status can be "active", "completed". and "claimed"

character = {}
character['icon'] = "wifi.png"
character['hp'] = "80"
character['maxhp'] = "100"
character['level'] = 0
character['xp'] = 0
character ['nextLevel'] = 0
data['characters'].append(character)

character = {}
character['icon'] = "piggy.png"
character['hp'] = "100"
character['maxhp'] = "100"
character['level'] = 17
character['xp'] = 386000
character ['nextLevel'] = 500000
data['characters'].append(character)

dogdatastring = json.dumps(data)

with open('dogfile.json', 'w') as outfile:
	json.dump(data, outfile)

with open('dogfile.json','r') as infile:
	dogdata = json.load(infile)