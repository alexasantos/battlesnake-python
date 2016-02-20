import bottle
import os


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
Health = 100

def index():
    head_url = 'https://www.google.ca/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiNrYS9rIfLAhUBz2MKHdhZA18QjRwIBw&url=http%3A%2F%2Ftheultralinx.com%2Ftag%2Fgif%2F&psig=AFQjCNE-U5WU-jW1hh5iKxSp_aT6bp4uPQ&ust=1456092250871705' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#04B431',
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
    do = 'north'
    data = bottle.request.json
    if snake.get(health) > 70:
        do = 'east'
    else:
        do = 'west'

    return {
        'move': do
        'taunt': 'battlesnake-python!'
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
