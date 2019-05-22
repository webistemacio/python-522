
import flask

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():
    
    context = {
        'page': 'gitlab',
        'route': {
            'is_public': False
        },
    }

    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab', methods=[ 'POST' ])
def post_gitlab():
    pass