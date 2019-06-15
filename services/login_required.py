import functools

import flask

import logging

logging.basicConfig(
	filename='app.log',
	level=logging.Debug,
	format='%(asctime)s [%(levelname)s] %(name)s' +
		'[%(funcName)s] [%(filename)s] %(lineno)s %(message)s'
	)

def  login_access(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		message = flask.session.get('email') or 'Não Autorizado'
		logging.debug(message)
		return function(*args, **kwargs)
	return wrapper


def  login_required(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		if 'email' not in flask.session:
			return flask.redirect('/sign-in')
		return function(*args, **kwargs)
	return wrapper


