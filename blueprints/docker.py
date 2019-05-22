
import flask

blueprint = flask.Blueprint('docker', __name__)

@blueprint.route('/docker', methods=[ 'GET' ])
def get_docker():    

    context = {
        'page': 'docker',
        'route': {
            'is_public': False
        },
    }

    return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start', methods=[ 'POST' ])
def start_docker():
    return ''

@blueprint.route('/docker/stop', methods=[ 'POST' ])
def stop_docker():
    return ''

