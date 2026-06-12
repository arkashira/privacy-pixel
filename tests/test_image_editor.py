import pytest
from image_editor import Image, ImageEditor

def test_crop():
    image = Image(b'123', 100, 100)
    editor = ImageEditor(image)
    editor.crop(10, 10, 50, 50)
    assert editor.get_image().width == 50
    assert editor.get_image().height == 50

def test_rotate():
    image = Image(b'123', 100, 100)
    editor = ImageEditor(image)
    editor.rotate(90)
    assert editor.get_image().width == 100
    assert editor.get_image().height == 100

def test_flip():
    image = Image(b'123', 100, 100)
    editor = ImageEditor(image)
    editor.flip(True)
    assert editor.get_image().width == 100
    assert editor.get_image().height == 100

def test_undo_redo():
    image = Image(b'123', 100, 100)
    editor = ImageEditor(image)
    editor.crop(10, 10, 50, 50)
    editor.undo()
    assert editor.get_image().width == 100
    assert editor.get_image().height == 100
    editor.redo()
    assert editor.get_image().width == 50
    assert editor.get_image().height == 50

def test_performance():
    image = Image(b'123' * 12000000, 4000, 3000)
    editor = ImageEditor(image)
    import time
    start = time.time()
    editor.crop(100, 100, 2000, 2000)
    editor.rotate(90)
    editor.flip(True)
    assert time.time() - start < 0.2
