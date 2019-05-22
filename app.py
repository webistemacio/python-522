
import sys
import os

import flask
import ldap3

import blueprints.auth
import blueprints.docker
import blueprints.gitlab
import blueprints.jenkins

app = flask.Flask(__name__)

app.register_blueprint(blueprints.auth.blueprint)
app.register_blueprint(blueprints.docker.blueprint)
app.register_blueprint(blueprints.gitlab.blueprint)
app.register_blueprint(blueprints.jenkins.blueprint)

@app.route('/')
def index():
    return flask.redirect('/docker')
    
if __name__ == '__main__':

    try:
        user = 'cn=admin,dc=dexter,dc=com,dc=br'
        password = '4linux'

        server = ldap3.Server('ldap://localhost')
        connection = ldap3.Connection(server, user, password, auto_bind=True)
    except ldap3.core.exceptions.LDAPSocketOpenError:
        pass

    current_module = os.path.dirname(os.path.curdir)
    sys.path.append(current_module)

    app.run(debug=True)