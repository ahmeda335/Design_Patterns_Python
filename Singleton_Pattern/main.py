from actions.authenticate import Authenticate
from actions.debug import Debug
from actions.error import Error
from actions.success import Success


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


