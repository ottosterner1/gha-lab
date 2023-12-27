import pytest
from python_actions_test import github_testing_actions

def test_github_testing_actions():
    test_score = github_testing_actions()
    assert test_score == 3.0

