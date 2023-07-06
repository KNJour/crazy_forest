from django.shortcuts import render, redirect
import random

status = "green"
area_list = ['forest', 'castle', 'village', 'temple', 'field', 'swamp', 'bog', 'river', 'stream', 'woods', 'cave', 'mountain', 'valley', 'desert', 'oasis', 'dungeon', 'ruins', 'graveyard', 'cemetery', 'tomb', 'crypt', 'catacombs',]

adjective_list = ['forbidden', 'haunted', 'seemingly-friendly', 'mysterious', 'ominous', 'dark', 'enchanted', 'magical', 'totally cool', 'very very not cool', 'spooky', 'scary', 'creepy', 'deadly', 'dangerous', 'unsettling', 'lovely', 'gross', 'wet', 'colorful', 'lame-looking', 'cursed', 'smelly', 'cold', 'scorching', 'rad as hell', 'boring', 'dull', 'dank', 'bright', 'offputting', 'nondescript', 'fun', 'not fun', 'unfun', 'uncool', 'cool', 'uninteresting', 'interesting', 'unremarkable', 'remarkable', 'unmemorable', 'memorable', 'forgettable', 'angry', 'fierce', 'pure evil', 'probably not that bad', 'man-eating', 'nuclear' 'bananas', 'brain eating', 'lame']

noun_list = ['fun', 'happiness', 'death', 'cruelty', 'danger', 'coolness', 'lameness', 'time','space', 'the universe', 'the multiverse', 'the void', 'the abyss', 'the beyond', 'the unknown', 'the unknowable', 'the unnameable', 'the unpronounceable', 'fury', 'love', 'solitude', 'togetherness', 'safety', 'lies', 'craziness', 'turtles', 'bananas', 'brains', 'life', 'ice', 'fire', 'water', 'earth', 'air', 'the elements', 'harmony', 'impeccable style']

monster_list = ['goblin', 'orc', 'ogre', 'troll', 'dragon', 'giant', 'spider', 'rat', 'snake', 'giant_snake', 'bat', 'giant frog', 'lizard', 'scorpion', 'crab', 'flying fish', 'bird', 'giant worm', 'giant ant', 'giant bee', 'giant wasp', 'giant mosquito', 'centipede', 'millipede', 'slug', 'snail', 'octopus', 'squid', 'jellyfish', 'amoeba', 'mushroom', 'plant', 'talking tree', 'fairy', 'elf', 'dwarf', 'turtle', 'giraffe', 'B52 Bomber', 'cat', 'dog', 'wolf', 'bear', 'lion', 'tiger', 'shark', 'whale', 'dolphin', 'seal', 'walrus', 'penguin', 'polar bear', 'panda', 'koala', 'kangaroo', 'sloth', 'sasquatch', 'yeti', 'unicorn', 'hippogriff', 'griffin', 'phoenix', 'hydra', 'chimera', 'minotaur', 'cyclops', 'medusa', 'sphinx', 'kraken', 'leviathan', 'loch ness monster', 'mothman']

good_verbs = ['helped', 'aided', 'assisted', 'healed', 'cured', 'rescued', 'protected', 'defended', 'guarded', 'shield' 'assisted', 'helped', 'saved']

attack_verbs = ['attacked', 'somehow clawed', 'eaten alive, screaming', 'mauled', 'savaged', 'preached to about our lord jesus christ', 'screamed at', 'yelled at', 'insulted', 'mocked', 'made fun of', 'laughed at', 'told an untasteful joke', 'told a sad story', 'told a scary story', 'told a very boring story', 'punched', 'kicked', 'farted on', 'spit on', 'peed on', 'pooped on', 'jumped', 'ganked', 'shot', 'ruined your whole worldview', 'pumbled', 'beat up', 'slapped', 'slapped around', 'slapped silly', 'slapped upside the head', 'slapped upside the face', 'slapped upside the butt', 'slapped upside the back', 'almost murdered', 'challenged to a fierce rap battle']

# Generates the area info, danger level, gold amount possible, monsters, and the name
def area_generator():
    area = {
        'danger': random.randint(1, 10),
        'monster': random.choice(monster_list),
    }
    if area['danger'] <= 3:
        area['color'] = 'green'
        area['gold'] = random.randint(5, 35)
    elif area['danger'] <= 6:
        area['color'] = 'yellow'
        area['gold'] = random.randint(30, 65)
    else:
        area['color'] = 'red'
        area['gold'] = random.randint(60, 110)

    format = random.randint(1, 7)
    if format == 1 or format == 6:
        area['name'] = "The " + random.choice(adjective_list) + " " + random.choice(area_list)
    elif format == 2 or format == 7:
        area['name'] = "The " + random.choice(area_list) + " of " + random.choice(noun_list)
    elif format == 3:
        area['name'] = "The " + random.choice(adjective_list) + " " + random.choice(area_list) + " of " + random.choice(noun_list)
    elif format == 4:
        area['name'] = "The " + random.choice(adjective_list) + " " + random.choice(area_list) + " of " + random.choice(adjective_list) + " " + random.choice(noun_list)
    elif format == 5:
        monster = random.choice(monster_list)
        area['name'] = "the " + random.choice(area_list) + " of " + random.choice(adjective_list) + " " + monster + "s"
        area['monster'] = monster
    return area

def event_generator(danger, gold, monster, name):

intro = {
            'message': "You Find Yourself Trapped in the Random Forest. Pay the Goblin at Camp 500 gold to escape or find the key hidden in the forest! Numbers display the Danger Level of the area, the higher the number the more likely you are to be attacked by a monster! Rest at camp to give the goblin your gold and recover health, but beware, you may be attacked!",
            'color': "white"
        }
event_log = [intro]

def index(request):
    # checks if session has gold amount or health then assigns default value
    if 'event' in request.session:
        event_log.append(request.session['event'])
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'health' not in request.session:
        request.session['health'] = 100
    # updates color of status to yellowm, red, or green depending on health
    if request.session['health'] <=70:
        status = "yellow"
    elif request.session['health'] <= 30:
        status = "red"
    else:
        status = "green"
    # populates directions with area info
    request.session['up'] = area_generator()
    request.session['down'] = area_generator()
    request.session['left'] = area_generator()
    request.session['right'] = area_generator()
    # updates data dictionary with session values
    data = {
        'statuscolor': status,
        'event_log': event_log,
    }
    print(data['statuscolor'])
    return render(request, 'index.html', data)

def search(request):
    direction = request.POST['direction']
    roll = random.randint(1, 12)
    if roll <= request.session[direction]['danger']:
        request.session['event'] = {
            'message': "You are attacked by a " + request.session[direction]['monster'] + "!",
            'color': "red"
        }
        request.session['health'] -= 10
    return redirect('/')

def camp(request):
    request.session['event'] = {
        'message': "You Rest at Camp and Recover 50 Health",
        'color': "white"
    }
    return redirect('/')

def restart(request):
    request.session.flush()
    event_log = [intro]
    return redirect('/')