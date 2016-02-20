import bottle
import os


snake = [] #init snake

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')

def index():
    head_url = 'https://www.google.ca/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiNrYS9rIfLAhUBz2MKHdhZA18QjRwIBw&url=http%3A%2F%2Ftheultralinx.com%2Ftag%2Fgif%2F&psig=AFQjCNE-U5WU-jW1hh5iKxSp_aT6bp4uPQ&ust=1456092250871705' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#8E4585',
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
