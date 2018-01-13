import itertools
import math
from PIL import (Image,
                 ImageDraw)


WHITE = (255, 255, 255)

IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080

GUIDE_SIZE = 50

BUFFER_X = 50 + GUIDE_SIZE
BUFFER_Y = 50 + GUIDE_SIZE

COLOR_BOX_X = 150
COLOR_BOX_Y = 150
COLOR_BOX_BUFFER = 50

NUM_COLORS = 512 # best if multiple of 256
NUM_COLORS_PER_CHANNEL = math.ceil(math.pow(NUM_COLORS, 1.0/3.0))
COLOR_INTERVAL = int(256 / NUM_COLORS_PER_CHANNEL)


def draw_guides(draw):
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


possible_color_values = [v for v in range(0, 256, COLOR_INTERVAL)]
colors = [(r, g, b) for r in possible_color_values \
                    for g in possible_color_values \
                    for b in possible_color_values]

# rectagles are drawn by the coordinates of their
# upper left corner and a lower right corner
upper_left_xs = range(BUFFER_X,
                      IMAGE_WIDTH - (BUFFER_X + COLOR_BOX_X),
                      COLOR_BOX_X + COLOR_BOX_BUFFER)
upper_left_ys = range(BUFFER_Y,
                      IMAGE_HEIGHT - (BUFFER_Y + COLOR_BOX_Y),
                      COLOR_BOX_Y + COLOR_BOX_BUFFER)
upper_left_coords = [(x, y) for x in upper_left_xs \
                            for y in upper_left_ys]
lower_right_coords = [(x + COLOR_BOX_X, 
                       y + COLOR_BOX_Y) \
                               for x in upper_left_xs \
                               for y in upper_left_ys]
coords = [list(c) for c in zip(upper_left_coords, lower_right_coords)]
boxes_per_image = len(coords)
colors_for_images = [colors[i:i+boxes_per_image] \
                     for i in range(0, len(colors), boxes_per_image)] 

for idx, colors in enumerate(colors_for_images):
    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT))
    draw = ImageDraw.Draw(image)
    
    draw_guides(draw)

    for coord, color in zip(coords, colors):
        draw.rectangle(coord, fill=color)

    image.save("./out/test_img_" + str(idx) + ".bmp")
