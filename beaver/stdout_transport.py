# -*- coding: utf-8 -*-
import beaver.transport
import beaver.utils


class StdoutTransport(beaver.transport.Transport):

    def __init__(self, beaver_config, file_config, logger=None):
        super(StdoutTransport, self).__init__(beaver_config, file_config, logger=logger)
        self._stdout = beaver.utils.setup_custom_logger('stdout', formatter=False, output=beaver_config.get('output'))

    def callback(self, filename, lines, **kwargs):
        timestamp = self.get_timestamp(**kwargs)

        for line in lines:
            self._stdout.info(self.format(filename, timestamp, line))
