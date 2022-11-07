import logging
import uuid


class PullgerLogging:
    __slots__ = ('logger', 'logger_name_full')

    class LogRecord:
        __slots__ = ('uuid', 'msg_private', 'msg_public')

        def __init__(self, msg_private, msg_public=None):
            self.uuid = uuid.uuid4()
            self.msg_private = f'REG:[{self.uuid}] {msg_private}'
            if msg_public is not None:
                self.msg_public = f'{msg_public} More information on server log by REG:[{self.uuid}]'
            else:
                self.msg_public = None

    def __init__(self, logger_tree):
        self.logger_name_full = '.'.join(logger_tree.LOGGER_NAME_LIST)
        self.logger = logging.getLogger(self.logger_name_full)

    def debug(self, msg_private, msg_public=None, **kwargs):
        logRecord = self.LogRecord(msg_private=msg_private, msg_public=msg_public)
        self.logger.debug(msg=logRecord.msg_private, **kwargs)
        return logRecord

    def info(self, msg_private, msg_public=None, **kwargs):
        logRecord = self.LogRecord(msg_private=msg_private, msg_public=msg_public)
        self.logger.info(msg=logRecord.msg_private, **kwargs)
        return logRecord

    def error(self, msg='no message', **kwargs):
        self.logger.error(msg=msg, **kwargs)

    def critical(self, msg='no message', **kwargs):
        self.logger.critical(msg=msg, **kwargs)

    def log(self, level, msg):
        self.logger.log(level=level, msg=msg)
