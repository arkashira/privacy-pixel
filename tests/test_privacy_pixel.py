from privacy_pixel import PrivacyPixel, ToolbarButton

def test_get_toolbar_buttons():
    privacy_pixel = PrivacyPixel()
    buttons = privacy_pixel.get_toolbar_buttons()
    assert len(buttons) == 3
    for button in buttons:
        assert isinstance(button, ToolbarButton)

def test_check_contrast_ratio():
    privacy_pixel = PrivacyPixel()
    assert privacy_pixel.check_contrast_ratio("#000000", "#FFFFFF")
    assert not privacy_pixel.check_contrast_ratio("#FFFFFF", "#FFFFFF")

def test_check_aria_labels():
    privacy_pixel = PrivacyPixel()
    assert privacy_pixel.check_aria_labels()
    privacy_pixel.toolbar_buttons[0].aria_label = ""
    assert not privacy_pixel.check_aria_labels()

def test_check_tab_order():
    privacy_pixel = PrivacyPixel()
    assert privacy_pixel.check_tab_order()
