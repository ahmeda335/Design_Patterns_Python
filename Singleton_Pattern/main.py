from actions import Authenticate, Error, Debug, Success


success = Success()
success.log()
print(success.logger.logs, '\n')

error = Error()
error.log()
print(error.logger.logs, '\n')

debug = Debug()
debug.log()
print(debug.logger.logs, '\n')

authenticate = Authenticate()
authenticate.log()
print(authenticate.logger.logs, '\n')


