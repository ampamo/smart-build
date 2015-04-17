from _base import get_env_variable
from django.core.exceptions import ImproperlyConfigured

ENVIROMENT = {
	"DEVELOPMENT" : "DEVELOPMENT",
	"TEST"        : "TEST",
	"STAGING"     : "STAGING",
	"PRODUCTION"  : "PRODUCTION"
}

def get_server_type():
	enviroment_var = "SMARTBUILD_ENVIROMENT"
	enviroment = get_env_variable(enviroment_var)
	if enviroment == ENVIROMENT["DEVELOPMENT"]:
		return 'local'
	elif enviroment == ENVIROMENT["TEST"]:
		return 'test'
	elif enviroment == ENVIROMENT["STAGING"]:
		return 'staging'
	elif enviroment == ENVIROMENT["PRODUCTION"]:
		return 'production'
	else:
		error_msg = "The %s enviroment variable must be one of the next: %s" % (enviroment_var, ENVIROMENT.values())
		raise ImproperlyConfigured(error_msg)
