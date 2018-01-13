from PIL import (Image,
                 ImageDraw)


IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080

WHITE = (255, 255, 255)
GUIDE_SIZE = 50

image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT))
draw = ImageDraw.Draw(image)

# Draw guide boxes
half_w = IMAGE_WIDTH / 2.0
half_h = IMAGE_HEIGHT / 2.0
half_guide = GUIDE_SIZE / 2.0

# top guide
draw.rectangle([(half_w - half_guide, 0),
                (half_w + half_guide, GUIDE_SIZE)],
               fill=WHITE)
# right guide
draw.rectangle([(IMAGE_WIDTH - GUIDE_SIZE, half_h - half_guide),
                (IMAGE_WIDTH, half_h + half_guide)],
               fill=WHITE)
# bottom guide
draw.rectangle([(half_w - half_guide, IMAGE_HEIGHT - GUIDE_SIZE),
                (half_w + half_guide, IMAGE_HEIGHT)],
               fill=WHITE)
# left guide
draw.rectangle([(0, half_h - half_guide),
                (GUIDE_SIZE, half_h + half_guide)],
               fill=WHITE)

image.show()
