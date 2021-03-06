import unittest
from testaccountUnit import AccountUnitTest
from testQuery import QueryTest
from testReports import ReportTest


def test_suite():
    """ Test Suite for omnitue module """

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(AccountUnitTest))
    test_suite.addTest(unittest.makeSuite(QueryTest))
    test_suite.addTest(unittest.makeSuite(ReportTest))
    return test_suite

mySuite = test_suite()

runner = unittest.TextTestRunner()
runner.run(mySuite)
