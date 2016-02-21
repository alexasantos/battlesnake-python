import bottle
import os

snake = [] #init snake
direction = "north"

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')

def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#8E4585',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
   
    # TODO: Do things with data

    return {
        'taunt': 'gmorn bro'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    nextMove = ""
    
    allSnakes = data.get("snakes")
    for tempsnake in allSnakes:
        if tempsnake.get("id") == "f795c973-42a3-400e-aadd-4f7bc540c24b":
            snake = tempsnake

    #find edges of board
    height = data.get("height")
    width = data.get("width")
    
    coords = snake.get("coords") #this is a list
    head = coords[0] #list of two numbers

    if head[0] == 1:
        print("I'm on x cood 1")
        if direction == 'west':
            if head[1] == 1:
                nextMove = 'south'
            else:
                nextMove = 'north'
        elif direction == 'north' and head[1] == 0:
            nextMove = 'east'
        elif direction == 'south' and head[1] == height-2:
            nextMove = 'east'
    elif head[0] == width-2:
        if direction == 'east':
            if head[1] == height-2:
                nextMove = 'north'
            else:
                nextMove = 'south'
        elif direction == 'north' and head[1] == 1:
            nextMove = 'west'
        elif direction == 'south' and head[1] == height-2:
            nextMove = 'west'
    elif head[1] == 1:
        if direction == 'north':
            if head[0] == width-2:
                nextMove = 'west'
            else:
                nextMove = 'east'
        elif direction == 'east' and head[0] == width-2:
            nextMove = 'south'
        elif direction == 'west' and head[0] == 1:
            nextMove = 'south'
    elif head[1] == height-2:
        if direction == 'south':
            if head[0] == width-2:
                nextMove = 'west'
            else:
                nextMove = 'east'
        elif direction == 'east' and head[0] == 1:
            nextMove = 'north'
        elif direction == 'west' and head[0] == width-2:
            nextMove = 'north'
        
    else:
        nextMove = direction
    
    direction = nextMove
    
    return {
        'move': nextMove,
        'taunt': "are you jesus because i want to snail you"
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
