from figures.ract import Ractangular


def test_name(figure_fixture):
    t = figure_fixture + Ractangular("ractangular", 4).figure_name()
    print(t)


def test_angle(angle_fixture):
    n = angle_fixture % Ractangular("ractangular", 4).angle_quantity()
    print(n)


def test_angle2(angle_fixture):
    n = Ractangular("ractangular", 4).angle_quantity() - angle_fixture
    print(n)


def test_angle3(angle_fixture):
    d = {}
    d[angle_fixture] = Ractangular("ractangular", 4).angle_quantity()
    print(d)


def test_perim(another_ang_fixture):
    assert len(another_ang_fixture) != Ractangular("ractangular", 4).ract_perim(1, 1)

