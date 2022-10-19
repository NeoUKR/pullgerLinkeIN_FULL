from pullgerLogin.general import PullgerLogging
from . import _loggerTree


class LogClass(PullgerLogging):
    pass


logger = LogClass(_loggerTree)
