import pygame
import numpy as np
import re


# 读
with open("demo/display.drf", "r") as file:
    content = file.read()
    cross_match = re.search(
        r"\(\s*display\s+cross\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    if cross_match:
        cross_data = re.findall(r"\((.*?)\)", cross_match.group(1))
        cross_arr = [list(map(int, row.strip().split())) for row in cross_data]
        cross_arr = np.array(
            [[1 if (i + j) % 2 == 0 else 0 for i in range(16)] for j in range(16)]
        )


drf = {
    "display": {
        "bitMap": {
            "blank": {"arr": [[0] * 16] * 16},
            "solid": {"arr": [[1] * 16] * 16},
            "dots": {
                "arr": [
                    [
                        [0 if (i + j) % 2 == 0 else 1 for i in range(16)]
                        if j % 3 != 1
                        else [0] * 16
                        for j in range(16)
                    ]
                ]
            },
            "hLine": {"arr": [[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]] * 16},
            "vLine": {"arr": [[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]] * 16},
            "cross": {"arr": cross_arr},
        }
    }
}
bitmap = drf["display"]["bitMap"]
pygame.init()

bitmap_width = len(bitmap["blank"]["arr"][0])
bitmap_height = len(bitmap["blank"]["arr"])

window_width = 560
window_height = 560
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bitmap Display")
surface = pygame.Surface((bitmap_width * 16, bitmap_height * 4))

# blank
blank_data = bitmap["blank"]["arr"]
print("Blank Data:")
for row in blank_data:
    print(row)
# solid
solid_data = bitmap["solid"]["arr"]
print("Solid Data:")
for row in solid_data:
    print(row)
# dots
dots_data = np.array(bitmap["dots"]["arr"])
print("Dots Data:")
print(dots_data)
# hLine
hLine_data = np.array(bitmap["hLine"]["arr"]).T
print("hLine Data:")
print(hLine_data)
# vLine
vLine_data = np.array(bitmap["vLine"]["arr"])
print("vLine data:")
print(vLine_data)
# cross
cross_data = np.array(bitmap["cross"]["arr"])
print("cross data:")
print(cross_data)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    for y in range(bitmap_height):
        for x in range(bitmap_width):
            if dots_data[0][y][x] == 1:
                color = (0, 0, 0)  # 黑色
            else:
                color = (255, 255, 255)  # 白色
            pygame.draw.rect(surface, color, (x, y, 1, 1))
            # 根据不同数组的数据添加不同颜色的像素点
        if solid_data[y][x] == 1:
            color = (255, 0, 0)  # 红色
            pygame.draw.rect(surface, color, (x + bitmap_width, y, 1, 1))
        if blank_data[y][x] == 1:
            color = (0, 255, 0)  # 绿色
            pygame.draw.rect(surface, color, (x + bitmap_width * 2, y, 1, 1))
        if hLine_data[y][x] == 1:
            color = (0, 0, 255)  # 蓝色
            pygame.draw.rect(surface, color, (x + bitmap_width * 3, y, 1, 1))
        if vLine_data[y][x] == 1:
            color = (255, 255, 0)  # 黄色
            pygame.draw.rect(surface, color, (x + bitmap_width * 4, y, 1, 1))
        if cross_data[y][x] == 1:
            color = (255, 0, 255)  # 紫色
            pygame.draw.rect(surface, color, (x + bitmap_width * 5, y, 1, 1))

    # 缩放
    scaled_surface = pygame.transform.scale(surface, (window_width, window_height))
    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()
