import json,sys,unittest
sys.path.insert(0,sys.argv[1])
class ExitAwareResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.system_exits = 0
    def addFailure(self, test, error):
        self.system_exits += issubclass(error[0], SystemExit)
        super().addFailure(test, error)
    def addError(self, test, error):
        self.system_exits += issubclass(error[0], SystemExit)
        super().addError(test, error)
    def addSubTest(self, test, subtest, error):
        if error is not None:
            self.system_exits += issubclass(error[0], SystemExit)
        super().addSubTest(test, subtest, error)
suite=unittest.defaultTestLoader.discover(sys.argv[1],pattern='tests_submission.py')
def leaves(tests):
    for test in tests:
        if isinstance(test, unittest.TestSuite): yield from leaves(test)
        else: yield test
found=list(leaves(suite))
import_failures=sum(isinstance(test, unittest.loader._FailedTest) for test in found)
discovered=len(found)-import_failures
result=unittest.TextTestRunner(verbosity=1, resultclass=ExitAwareResult).run(suite)
print('TEST_RESULT '+json.dumps(dict(discovered=discovered,import_failures=import_failures,run=result.testsRun,system_exits=result.system_exits,failures=len(result.failures),errors=len(result.errors),skipped=len(result.skipped),expected=len(result.expectedFailures),unexpected=len(result.unexpectedSuccesses))))
