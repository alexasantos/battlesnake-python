import bottle
import os


snake = [] #init snake

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
    for i in allSnakes:
        if allSnakes[i].get("id") == "f795c973-42a3-400e-aadd-4f7bc540c24b":
            snake = allSnakes[i]

    #find edges of board
    height = data.get("height")
    width = data.get("width")
    
    coords = snake.get("coords") #this is a list
    head = coords[0] #list of two numbers
    
    if head[0] == width-1 or head[0] == 0:
        nextMove = "north"
    if head[1] == height-1 or head[1] == 0:
        nextMove = "east"
        
    
    return {
        'move': nextMove,
        'taunt': 'bloop' #snake.get("id")
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
