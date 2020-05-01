import pytest


@pytest.fixture
def square_fixture():
    s = "This is the square"
    return s


@pytest.fixture
def angle_fixture():
    num = 16
    return num


@pytest.fixture
def another_ang_fixture():
    l1 = [1, 8, 3]
    return l1


@pytest.fixture
def figure_fixture():
    s = "What type of figure is this?\n"
    return s


