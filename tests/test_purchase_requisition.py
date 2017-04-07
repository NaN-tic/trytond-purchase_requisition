# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import unittest

import doctest

from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite
from trytond.tests.test_tryton import (doctest_setup, doctest_teardown,
    doctest_checker)


class PurchaseRequisitionTestCase(ModuleTestCase):
    'Test Purchase Requisition module'
    module = 'purchase_requisition'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            PurchaseRequisitionTestCase))
    suite.addTests(doctest.DocFileSuite(
            'scenario_purchase_requisition.rst',
            setUp=doctest_setup, tearDown=doctest_teardown, encoding='UTF-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE,
            checker=doctest_checker))
    return suite
