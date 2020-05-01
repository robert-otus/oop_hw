from figures.triangle import Triangle


def test_name(figure_fixture):
    t = figure_fixture + Triangle("triangle", 3).figure_name()
    print(t)


def test_len(another_ang_fixture):
    assert len(another_ang_fixture) == Triangle("ractangular", 3).angle_quantity()


def test_presence(another_ang_fixture):
    r = another_ang_fixture
    if Triangle("square", 3).triangle_perim(1, 2, 2) in r:
        print("Present in the list")
    else:
        print("It's not in the list")


def test_compare(angle_fixture):
    assert angle_fixture > Triangle("square", 3).area_tri(4, 6, 8)


def test_compare2(another_ang_fixture):
    assert another_ang_fixture[1] * 2 == Triangle("square", 3).triangle_perim(3, 7, 6)

