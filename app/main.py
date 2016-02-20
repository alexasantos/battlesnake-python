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
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    
    allSnakes = data.get("snakes")
    for i in allSnakes:
        if allSnakes[i].get("id") == "f795c973-42a3-400e-aadd-4f7bc540c24b":
            snake = allSnakes[i]


    return {
        'move': 'north',
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
