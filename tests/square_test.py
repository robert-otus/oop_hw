from figures.square import Square


def test_name(square_fixture):
    assert square_fixture == Square("square", 4).figure_name()


def test_angle(square_ang_fixture):
    n = square_ang_fixture // Square("square", 4).angle_quantity()
    print(n)


def test_angle2(another_ang_fixture):
    sl = another_ang_fixture
    sl.append(Square("square", 4).angle_quantity())
    print(sorted(sl))


def test_area(another_ang_fixture):
    sl = another_ang_fixture
    if Square("square", 4).area_sq(2) in sl:
        print("Present in the list")
    else:
        print("It's not in the list")


def test_per(square_ang_fixture):
    assert square_ang_fixture > Square("square", 4).square_perim(2)


