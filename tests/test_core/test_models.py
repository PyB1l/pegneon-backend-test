# -*- coding: utf-8 -*-
"""core App test suit
"""

import pytest


@pytest.mark.django_db
def test_company_model(company_factory, department_factory):
    """Use pytest DI for unit testing
    """
    pass
