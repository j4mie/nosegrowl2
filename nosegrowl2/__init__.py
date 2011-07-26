import os
import datetime
import subprocess
from warnings import warn
from nose.plugins import Plugin
from pkg_resources import resource_filename


__version__ = '0.1'


START_TITLE = 'Starting tests...'
START_ICON = resource_filename('nosegrowl2', 'start.png')

SUCCESS_TITLE = '%s tests run OK'
SUCCESS_MESSAGE = 'Completed in %s.%s seconds'
SUCCESS_ICON = resource_filename('nosegrowl2', 'success.png')

FAILURE_TITLE = '%s tests run. %s failures, %s errors'
FAILURE_ICON = resource_filename('nosegrowl2', 'failure.png')


def _check_growlnotify():
    """Check whether the growlnotify command-line too is installed"""
    try:
        subprocess.check_call(
            ['growlnotify', '--version'],
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE
        )
        return True
    except:
        warn(
            "Plugin NoseGrowl2 requires the command-line tool growlnotify. "
            "Please install from http://growl.info/extras.php#growlnotify "
            "or with `brew install growlnotify`."
        )
        return False


def _growl(title, message, icon):
    args = [
        'growlnotify',
        '--title', title,
        '--message', message,
        '--image', icon,
        '--name', 'nosegrowl2',
    ]
    subprocess.call(args)


class NoseGrowl(Plugin):

    name = 'growl'

    def configure(self, options, conf):
        super(NoseGrowl, self).configure(options, conf)
        self.enabled = _check_growlnotify()

    def begin(self):
        self.start_time = datetime.datetime.now()
        _growl(START_TITLE, '', START_ICON)

    def finalize(self, result):
        self.end_time = datetime.datetime.now()

        if result.wasSuccessful():
            time_taken = self.end_time - self.start_time
            _growl(
                SUCCESS_TITLE % result.testsRun,
                SUCCESS_MESSAGE % (
                    time_taken.seconds,
                    time_taken.microseconds,
                ),
                SUCCESS_ICON
            )
        else:
            failures = '\n'.join(["Failures: %s" % name for name, ex in result.failures])
            errors = '\n'.join(["Errors: %s" % name for name, ex in result.errors])
            failure_message = '\n'.join([failures, errors])
            _growl(
                FAILURE_TITLE % (
                    result.testsRun,
                    len(result.failures),
                    len(result.errors),
                ),
                failure_message,
                FAILURE_ICON
            )
