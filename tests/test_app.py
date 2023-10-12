#!/usr/bin/env python3
"""Test HTTP GET request"""

import sys

sys.path.append('.')
from app import app

def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, Python!'
