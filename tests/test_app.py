# Test script for the Gradio application

import pytest
from src.app import create_app

def test_app_initialization():
    app = create_app()
    assert app is not None

def test_app_interface():
    app = create_app()
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_example_asset():
    app = create_app()
    response = app.test_client().get('/static/assets/example.txt')
    assert response.status_code == 200
    assert b'example content' in response.data  # Adjust based on actual content of example.txt

def test_css_loading():
    app = create_app()
    response = app.test_client().get('/static/css/styles.css')
    assert response.status_code == 200
    assert b'.your-css-class' in response.data  # Adjust based on actual CSS content