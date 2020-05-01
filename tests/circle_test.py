from figures.circle import Circle


def test_name(figure_fixture):
    t = figure_fixture + Circle("circle", 0).figure_name()
    print(t)


def test_diff_types(figure_fixture):
    t = figure_fixture + Circle("circle", 0).angle_quantity()
    print(t)


def test_angles(angle_fixture):
    s = angle_fixture + Circle("circle", 0).angle_quantity()
    print(s)


def test_lst(another_ang_fixture):
    a = another_ang_fixture
    a.append(Circle("circle", 0).area_cir(2))
    print(a)


def test_sum(angle_fixture):
    sm = angle_fixture + Circle("circle", 0).circle_perim(2)
    print(sm)
