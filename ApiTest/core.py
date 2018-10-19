import re

class CoreTests:

    def assert_regexp_equal(self, actual, expected, msg):
        if re.match(expected, actual) is not None:
            pass
        else:
            raise AssertionError('{0}. {1}\n not equal\n {2}'.format(msg, actual, expected.pattern))
