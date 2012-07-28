import datetime
from gntplib import Publisher, Resource
from nose.plugins import Plugin
from pkg_resources import resource_stream


__version__ = '0.3'

START_EVENT = 'Tests Starting'
START_TITLE = 'Starting tests...'
START_ICON = Resource(resource_stream('nosegrowl2', 'start.png').read())

SUCCESS_EVENT = 'Tests Passed'
SUCCESS_TITLE = '%s tests run OK'
SUCCESS_MESSAGE = 'Completed in %s.%s seconds'
SUCCESS_ICON = Resource(resource_stream('nosegrowl2', 'success.png').read())

FAILURE_EVENT = 'Test Failures'
FAILURE_TITLE = '%s tests run. %s failures, %s errors'
FAILURE_ICON = Resource(resource_stream('nosegrowl2', 'failure.png').read())

publisher = Publisher('nosegrowl2', [START_EVENT, SUCCESS_EVENT, FAILURE_EVENT], icon=START_ICON)
publisher.register()


class NoseGrowl(Plugin):

    name = 'growl'

    def configure(self, options, conf):
        super(NoseGrowl, self).configure(options, conf)

    def begin(self):
        self.start_time = datetime.datetime.now()
        publisher.publish(START_EVENT, START_TITLE, '', icon=START_ICON)

    def finalize(self, result):
        self.end_time = datetime.datetime.now()

        if result.wasSuccessful():
            time_taken = self.end_time - self.start_time
            title = SUCCESS_TITLE % result.testsRun
            message = SUCCESS_MESSAGE % (time_taken.seconds,
                                         time_taken.microseconds)
            publisher.publish(SUCCESS_EVENT, title, message, icon=SUCCESS_ICON)
        else:
            failures = '\n'.join(["Failures: %s" % name for name, ex in result.failures])
            errors = '\n'.join(["Errors: %s" % name for name, ex in result.errors])
            message = '\n'.join([failures, errors])
            title = FAILURE_TITLE % (result.testsRun,
                                      len(result.failures),
                                      len(result.errors))

            publisher.publish(FAILURE_EVENT, title, message, icon=FAILURE_ICON)
