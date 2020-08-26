"""
Lee Alessandrini

This module will contain the driving method for the chirpchirp api.
"""
import os
from flask import Flask
from flask_executor import Executor


def create_app():
	"""
		This method will create and return the flask REST API application.
	"""
	# Instantiate the application
	app = Flask(
		__name__, static_url_path="")
	# Set application configuration
	app_settings = os.getenv("APP_SETTINGS")
	app.config["APP_CONFIG"] = app_settings
	# Register blueprints
	from .apis import blueprint
	app.register_blueprint(blueprint)
	# Shell context for flask cli
	app.shell_context_processor({"app": app})
	# Setup executor
	executor = Executor(app)

	return app