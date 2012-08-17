from maze import Maze
from PIL import Image, ImageDraw

BG_COLOR = (0, 255, 0)
FG_COLOR = (255, 255, 255)
BG_COLOR = '#A66000'
FG_COLOR = '#A66B00'

ZOOM = 2

width = 1366 / 2
height = 768 / 2


m = Maze(width, height)
im = Image.new('RGB', (m.width, m.height))

draw = ImageDraw.Draw(im)
for x in range(m.width):
    for y in range(m.height):
        if m.maze[y][x] == 1:
            color = BG_COLOR
        else:
            color = FG_COLOR
        draw.point((x, y), fill=color)

if ZOOM > 1:
    new_size = (m.width * ZOOM, m.height * ZOOM)
    im = im.resize(new_size)

im.save('wallpaper.png')



