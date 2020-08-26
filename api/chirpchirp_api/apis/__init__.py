from flask import Blueprint
from flask_restx import Api


# Initialize api with blueprint
blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
	blueprint, version="1.0", title="chirpchirp api",
	description="REST API backend for chirpchirp twitter analytics platform")