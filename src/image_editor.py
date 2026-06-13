from dataclasses import dataclass
from enum import Enum
from typing import Tuple

class RedactionEffect(Enum):
    BLUR = 1
    PIXELATE = 2

@dataclass
class RedactionBrush:
    size: int
    effect: RedactionEffect

class ImageEditor:
    def __init__(self, image_data: bytes):
        self.image_data = image_data
        self.redacted_areas = []

    def apply_redaction(self, x: int, y: int, brush: RedactionBrush):
        if brush.size < 5 or brush.size > 100:
            raise ValueError("Brush size must be between 5 and 100 pixels")
        self.redacted_areas.append((x, y, brush))

    def toggle_redaction(self, index: int):
        if index < 0 or index >= len(self.redacted_areas):
            raise IndexError("Invalid redaction index")
        self.redacted_areas[index] = (self.redacted_areas[index][0], self.redacted_areas[index][1], 
                                      RedactionEffect.BLUR if self.redacted_areas[index][2].effect == RedactionEffect.PIXELATE 
                                      else RedactionEffect.PIXELATE)

    def get_redacted_image(self):
        # Simulate image processing
        return self.image_data

def create_image_editor(image_data: bytes) -> ImageEditor:
    return ImageEditor(image_data)
