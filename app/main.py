import bottle
import os


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
        'color': '#04B431',
        'head': "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fstorage.canoe.ca%2Fv1%2Fdynamic_resize%2Fsws_path%2Fsuns-prod-images%2F1297411412978_ORIGINAL.jpg%3Fquality%3D80%26size%3D650x&f=1"
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
    allSnakes = data.get(snakes)
    
    for i in allSnakes:
        if allSnakes[i].get(id) == "f795c973-42a3-400e-aadd-4f7bc540c24b":
            snake = allSnakes[i]


    return {
        'move': 'north',
        'taunt': snake.get(id)
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
