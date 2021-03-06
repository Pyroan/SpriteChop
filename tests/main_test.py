import spritechop.__main__ as sc
from PIL import Image


def test_image_equality():
    """Images with the same pixels should equal each other,
        as long as Pillow doesn't break
    """
    a = Image.new("RGBA", (1, 1))
    b = Image.new("RGBA", (1, 1))
    assert a == b

    b.putpixel((0, 0), (1, 0, 0, 1))
    assert a != b

    a.putpixel((0, 0), (1, 0, 0, 1))
    assert a == b


def test_unused_areas():
    """Areas with no visible pixels shouldn't output files"""
    assert len(sc.chop("tests/json/2x2.json", False)) == 2


def test_names():
    files = sc.chop("tests/json/4colors.json", False)
    assert files == ["t_red.png", "t_blue.png", "t_green.png", "t_purple.png"]

    files = sc.chop("tests/json/2x2.json", False)
    assert files == ["2x2_0.png", "2x2_1.png"]
