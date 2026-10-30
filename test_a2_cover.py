import unittest
import os
from PIL import Image

class TestA2Cover(unittest.TestCase):
    def test_cover_image_exists_and_dimensions(self):
        cover_path = "/Users/jainamshah/Downloads/Learning French/scribd_raw/images/1_a2.jpg"
        self.assertTrue(os.path.exists(cover_path), "1_a2.jpg does not exist")
        with Image.open(cover_path) as im:
            self.assertEqual(im.size, (904, 1169))
            self.assertEqual(im.mode, "RGB")

    def test_cover_badge_content(self):
        cover_path = "/Users/jainamshah/Downloads/Learning French/scribd_raw/images/1_a2.jpg"
        if not os.path.exists(cover_path):
            self.fail("1_a2.jpg does not exist")
        with Image.open(cover_path) as im:
            # Check that pill area contains white text pixels
            crop = im.crop((365, 324, 538, 376))
            white_pixels = sum(
                1
                for x in range(crop.width)
                for y in range(crop.height)
                if all(c > 240 for c in crop.getpixel((x, y)))
            )
            self.assertGreater(white_pixels, 100, "Pill badge does not contain white text")

if __name__ == "__main__":
    unittest.main()
