import sys
sys.path.insert(0, '../src')
from image_editor import ImageEditor, RedactionBrush, RedactionEffect
import pytest

def test_create_image_editor():
    image_data = b"image_data"
    editor = ImageEditor(image_data)
    assert editor.image_data == image_data

def test_apply_redaction():
    image_data = b"image_data"
    editor = ImageEditor(image_data)
    brush = RedactionBrush(10, RedactionEffect.BLUR)
    editor.apply_redaction(10, 20, brush)
    assert len(editor.redacted_areas) == 1

def test_apply_redaction_invalid_size():
    image_data = b"image_data"
    editor = ImageEditor(image_data)
    brush = RedactionBrush(3, RedactionEffect.BLUR)
    with pytest.raises(ValueError):
        editor.apply_redaction(10, 20, brush)

def test_toggle_redaction():
    image_data = b"image_data"
    editor = ImageEditor(image_data)
    brush = RedactionBrush(10, RedactionEffect.BLUR)
    editor.apply_redaction(10, 20, brush)
    editor.toggle_redaction(0)
    assert len(editor.redacted_areas) == 1

def test_toggle_redaction_invalid_index():
    image_data = b"image_data"
    editor = ImageEditor(image_data)
    with pytest.raises(IndexError):
        editor.toggle_redaction(0)

def test_get_redacted_image():
    image_data = b"image_data"
    editor = ImageEditor(image_data)
    assert editor.get_redacted_image() == image_data
