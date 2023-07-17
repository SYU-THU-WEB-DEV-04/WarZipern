import pygame
import numpy as np
import re


# Read
with open("demo/display.drf", "r") as file:
    content = file.read()
    cross_match = re.search(
        r"\(\s*display\s+cross\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    grid_match = re.search(r"\(\s*display\s+grid\s+\((.*?)\)\s+\)", content, re.DOTALL)
    slash_match = re.search(
        r"\(\s*display\s+slash\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    backSlash_match = re.search(
        r"\(\s*display\s+backSlash\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    hZigZag_match = re.search(
        r"\(\s*display\s+hZigZag\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    vZigZag_match = re.search(
        r"\(\s*display\s+vZigZag\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    hCurb = re.search(r"\(\s*display\s+hCurb\s+\((.*?)\)\s+\)", content, re.DOTALL)
    vCurb = re.search(r"\(\s*display\s+vCurb\s+\((.*?)\)\s+\)", content, re.DOTALL)
    brick = re.search(r"\(\s*display\s+brick\s+\((.*?)\)\s+\)", content, re.DOTALL)
    dagger = re.search(r"\(\s*display\s+dagger\s+\((.*?)\)\s+\)", content, re.DOTALL)
    triangle = re.search(
        r"\(\s*display\s+triangle\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    x = re.search(r"\(\s*display\s+x\s+\((.*?)\)\s+\)", content, re.DOTALL)
    dot1 = re.search(r"\(\s*display\s+dot1\s+\((.*?)\)\s+\)", content, re.DOTALL)
    dot2 = re.search(r"\(\s*display\s+dot2\s+\((.*?)\)\s+\)", content, re.DOTALL)
    dot3 = re.search(r"\(\s*display\s+dot3\s+\((.*?)\)\s+\)", content, re.DOTALL)
    dot4 = re.search(r"\(\s*display\s+dot4\s+\((.*?)\)\s+\)", content, re.DOTALL)
    stipple0 = re.search(
        r"\(\s*display\s+stipple0\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    stipple1 = re.search(
        r"\(\s*display\s+stipple1\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    stipple2 = re.search(
        r"\(\s*display\s+stipple2\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    stipple3 = re.search(
        r"\(\s*display\s+stipple3\s+\((.*?)\)\s+\)", content, re.DOTALL
    )
    z2 = re.search(r"\(\s*display\s+z2\s+\((.*?)\)\s+\)", content, re.DOTALL)
    z3 = re.search(r"\(\s*display\s+z3\s+\((.*?)\)\s+\)", content, re.DOTALL)
    y3 = re.search(r"\(\s*display\s+y3\s+\((.*?)\)\s+\)", content, re.DOTALL)
    z4 = re.search(r"\(\s*display\s+z4\s+\((.*?)\)\s+\)", content, re.DOTALL)
    y4 = re.search(r"\(\s*display\s+y4\s+\((.*?)\)\s+\)", content, re.DOTALL)
    y5 = re.search(r"\(\s*display\s+y5\s+\((.*?)\)\s+\)", content, re.DOTALL)
    z5 = re.search(r"\(\s*display\s+z5\s+\((.*?)\)\s+\)", content, re.DOTALL)
    z6 = re.search(r"\(\s*display\s+z6\s+\((.*?)\)\s+\)", content, re.DOTALL)
    y6 = re.search(r"\(\s*display\s+y6\s+\((.*?)\)\s+\)", content, re.DOTALL)
    z7 = re.search(r"\(\s*display\s+z7\s+\((.*?)\)\s+\)", content, re.DOTALL)
    y7 = re.search(r"\(\s*display\s+y7\s+\((.*?)\)\s+\)", content, re.DOTALL)
    z8 = re.search(r"\(\s*display\s+z8\s+\((.*?)\)\s+\)", content, re.DOTALL)
    y8 = re.search(r"\(\s*display\s+y8\s+\((.*?)\)\s+\)", content, re.DOTALL)
    z9 = re.search(r"\(\s*display\s+z9\s+\((.*?)\)\s+\)", content, re.DOTALL)
    y9 = re.search(r"\(\s*display\s+y9\s+\((.*?)\)\s+\)", content, re.DOTALL)
    z10 = re.search(r"\(\s*display\s+z10\s+\((.*?)\)\s+\)", content, re.DOTALL)
    zd = re.search(r"\(\s*display\s+zd\s+\((.*?)\)\s+\)", content, re.DOTALL)
    yd = re.search(r"\(\s*display\s+yd\s+\((.*?)\)\s+\)", content, re.DOTALL)
    ut = re.search(r"\(\s*display\s+ut\s+\((.*?)\)\s+\)", content, re.DOTALL)
    u = re.search(r"\(\s*display\s+u\s+\((.*?)\)\s+\)", content, re.DOTALL)
    ud = re.search(r"\(\s*display\s+ud\s+\((.*?)\)\s+\)", content, re.DOTALL)
    utv = re.search(r"\(\s*display\s+utv\s+\((.*?)\)\s+\)", content, re.DOTALL)
    # cross
    cross_data = re.findall(r"\((.*?)\)", cross_match.group(0))
    cross_arr = [list(map(int, row.strip().split())) for row in cross_data]
    cross_arr = np.array(cross_arr)
    # grid
    grid_data = re.findall(r"\((.*?)\)", grid_match.group(0))
    grid_arr = [list(map(int, row.strip().split())) for row in grid_data]
    grid_arr = np.array(grid_arr)
    # slash
    slash_data = re.findall(r"\((.*?)\)", slash_match.group(0))
    slash_arr = [list(map(int, row.strip().split())) for row in slash_data]
    slash_arr = np.array(slash_arr)
    # backSlash
    backSlash_data = re.findall(r"\((.*?)\)", backSlash_match.group(0))
    backSlash_arr = [list(map(int, row.strip().split())) for row in backSlash_data]
    backSlash_arr = np.array(backSlash_arr)
    # hZigZag
    hZigZag_data = re.findall(r"\((.*?)\)", hZigZag_match.group(0))
    hZigZag_arr = [list(map(int, row.strip().split())) for row in hZigZag_data]
    hZigZag_arr = np.array(hZigZag_arr)
    # vZigZag
    vZigZag_data = re.findall(r"\((.*?)\)", vZigZag_match.group(0))
    vZigZag_arr = [list(map(int, row.strip().split())) for row in vZigZag_data]
    vZigZag_arr = np.array(vZigZag_arr)
    # hCurb
    hCurb_data = re.findall(r"\((.*?)\)", hCurb.group(0))
    hCurb_arr = [list(map(int, row.strip().split())) for row in hCurb_data]
    hCurb_arr = np.array(hCurb_arr)
    # vCurb
    vCurb_data = re.findall(r"\((.*?)\)", vCurb.group(0))
    vCurb_arr = [list(map(int, row.strip().split())) for row in vCurb_data]
    vCurb_arr = np.array(vCurb_arr)
    # brick
    brick_data = re.findall(r"\((.*?)\)", brick.group(0))
    brick_arr = [list(map(int, row.strip().split())) for row in brick_data]
    brick_arr = np.array(brick_arr)
    # dagger
    dagger_data = re.findall(r"\((.*?)\)", dagger.group(0))
    dagger_arr = [list(map(int, row.strip().split())) for row in dagger_data]
    dagger_arr = np.array(dagger_arr)
    # triangle
    triangle_data = re.findall(r"\((.*?)\)", triangle.group(0))
    triangle_arr = [list(map(int, row.strip().split())) for row in triangle_data]
    triangle_arr = np.array(triangle_arr)
    # x
    x_data = re.findall(r"\((.*?)\)", x.group(0))
    x_arr = [list(map(int, row.strip().split())) for row in x_data]
    x_arr = np.array(x_arr)
    # dot1
    dot1_data = re.findall(r"\((.*?)\)", dot1.group(0))
    dot1_arr = [list(map(int, row.strip().split())) for row in dot1_data]
    dot1_arr = np.array(dot1_arr)
    # dot2
    dot2_data = re.findall(r"\((.*?)\)", dot2.group(0))
    dot2_arr = [list(map(int, row.strip().split())) for row in dot2_data]
    dot2_arr = np.array(dot2_arr)
    # dot3
    dot3_data = re.findall(r"\((.*?)\)", dot3.group(0))
    dot3_arr = [list(map(int, row.strip().split())) for row in dot3_data]
    dot3_arr = np.array(dot3_arr)
    # dot4
    dot4_data = re.findall(r"\((.*?)\)", dot4.group(0))
    dot4_arr = [list(map(int, row.strip().split())) for row in dot4_data]
    dot4_arr = np.array(dot4_arr)
    # stipple0
    stipple0_data = re.findall(r"\((.*?)\)", stipple0.group(0))
    stipple0_arr = [list(map(int, row.strip().split())) for row in stipple0_data]
    stipple0_arr = np.array(stipple0_arr)
    # stipple1
    stipple1_data = re.findall(r"\((.*?)\)", stipple1.group(0))
    stipple1_arr = [list(map(int, row.strip().split())) for row in stipple1_data]
    stipple1_arr = np.array(stipple1_arr)
    # stipple2
    stipple2_data = re.findall(r"\((.*?)\)", stipple2.group(0))
    stipple2_arr = [list(map(int, row.strip().split())) for row in stipple2_data]
    stipple2_arr = np.array(stipple2_arr)
    # stipple3
    stipple3_data = re.findall(r"\((.*?)\)", stipple3.group(0))
    stipple3_arr = [list(map(int, row.strip().split())) for row in stipple3_data]
    stipple3_arr = np.array(stipple3_arr)
    # z2
    z2_data = re.findall(r"\((.*?)\)", z2.group(0))
    z2_arr = [list(map(int, row.strip().split())) for row in z2_data]
    z2_arr = np.array(z2_arr)
    # z3
    z3_data = re.findall(r"\((.*?)\)", z3.group(0))
    z3_arr = [list(map(int, row.strip().split())) for row in z3_data]
    z3_arr = np.array(z3_arr)
    # y3
    y3_data = re.findall(r"\((.*?)\)", y3.group(0))
    y3_arr = [list(map(int, row.strip().split())) for row in y3_data]
    y3_arr = np.array(y3_arr)
    # z4
    z4_data = re.findall(r"\((.*?)\)", z4.group(0))
    z4_arr = [list(map(int, row.strip().split())) for row in z4_data]
    z4_arr = np.array(z4_arr)
    # y4
    y4_data = re.findall(r"\((.*?)\)", y4.group(0))
    y4_arr = [list(map(int, row.strip().split())) for row in y4_data]
    y4_arr = np.array(y4_arr)
    # y5
    y5_data = re.findall(r"\((.*?)\)", y5.group(0))
    y5_arr = [list(map(int, row.strip().split())) for row in y5_data]
    y5_arr = np.array(y5_arr)
    # z5
    z5_data = re.findall(r"\((.*?)\)", z5.group(0))
    z5_arr = [list(map(int, row.strip().split())) for row in z5_data]
    z5_arr = np.array(z5_arr)
    # z6
    z6_data = re.findall(r"\((.*?)\)", z6.group(0))
    z6_arr = [list(map(int, row.strip().split())) for row in z6_data]
    z6_arr = np.array(z6_arr)
    # y6
    y6_data = re.findall(r"\((.*?)\)", y6.group(0))
    y6_arr = [list(map(int, row.strip().split())) for row in y6_data]
    y6_arr = np.array(y6_arr)
    # z7
    z7_data = re.findall(r"\((.*?)\)", z7.group(0))
    z7_arr = [list(map(int, row.strip().split())) for row in z7_data]
    z7_arr = np.array(z7_arr)
    # y7
    y7_data = re.findall(r"\((.*?)\)", y7.group(0))
    y7_arr = [list(map(int, row.strip().split())) for row in y7_data]
    y7_arr = np.array(y7_arr)
    # z8
    z8_data = re.findall(r"\((.*?)\)", z8.group(0))
    z8_arr = [list(map(int, row.strip().split())) for row in z8_data]
    z8_arr = np.array(z8_arr)
    # y8
    y8_data = re.findall(r"\((.*?)\)", y8.group(0))
    y8_arr = [list(map(int, row.strip().split())) for row in y8_data]
    y8_arr = np.array(y8_arr)
    # z9
    z9_data = re.findall(r"\((.*?)\)", z9.group(0))
    z9_arr = [list(map(int, row.strip().split())) for row in z9_data]
    z9_arr = np.array(z9_arr)
    # y9
    y9_data = re.findall(r"\((.*?)\)", y9.group(0))
    y9_arr = [list(map(int, row.strip().split())) for row in y9_data]
    y9_arr = np.array(y9_arr)
    # z10
    z10_data = re.findall(r"\((.*?)\)", z10.group(0))
    z10_arr = [list(map(int, row.strip().split())) for row in z10_data]
    z10_arr = np.array(z10_arr)
    # zd
    zd_data = re.findall(r"\((.*?)\)", zd.group(0))
    zd_arr = [list(map(int, row.strip().split())) for row in zd_data]
    zd_arr = np.array(zd_arr)
    # yd
    yd_data = re.findall(r"\((.*?)\)", yd.group(0))
    yd_arr = [list(map(int, row.strip().split())) for row in yd_data]
    yd_arr = np.array(yd_arr)
    # ut
    ut_data = re.findall(r"\((.*?)\)", ut.group(0))
    ut_arr = [list(map(int, row.strip().split())) for row in ut_data]
    ut_arr = np.array(ut_arr)
    # u
    u_data = re.findall(r"\((.*?)\)", u.group(0))
    u_arr = [list(map(int, row.strip().split())) for row in u_data]
    u_arr = np.array(u_arr)
    # ud
    ud_data = re.findall(r"\((.*?)\)", ud.group(0))
    ud_arr = [list(map(int, row.strip().split())) for row in ud_data]
    ud_arr = np.array(ud_arr)
    # utv
    utv_data = re.findall(r"\((.*?)\)", utv.group(0))
    utv_arr = [list(map(int, row.strip().split())) for row in utv_data]
    utv_arr = np.array(utv_arr)


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
            "grid": {"arr": grid_arr},
            "slash": {"arr": slash_arr},
            "backSlash": {"arr": backSlash_arr},
            "hZigZag": {"arr": hZigZag_arr},
            "vZigZag": {"arr": vZigZag_arr},
            "hCurb": {"arr": hCurb_arr},
            "vCurb": {"arr": vCurb_arr},
            "brick": {"arr": brick_arr},
            "dagger": {"arr": dagger_arr},
            "triangle": {"arr": triangle_arr},
            "x": {"arr": x_arr},
            "dot1": {"arr": dot1_arr},
            "dot2": {"arr": dot2_arr},
            "dot3": {"arr": dot3_arr},
            "dot4": {"arr": dot4_arr},
            "stipple0": {"arr": stipple0_arr},
            "stipple1": {"arr": stipple1_arr},
            "stipple2": {"arr": stipple2_arr},
            "stipple3": {"arr": stipple3_arr},
            "z2": {"arr": z2_arr},
            "z3": {"arr": z3_arr},
            "y3": {"arr": y3_arr},
            "z4": {"arr": z4_arr},
            "y4": {"arr": y4_arr},
            "y5": {"arr": y5_arr},
            "z5": {"arr": z5_arr},
            "z6": {"arr": z6_arr},
            "y6": {"arr": y6_arr},
            "z7": {"arr": z7_arr},
            "y7": {"arr": y7_arr},
            "z8": {"arr": z8_arr},
            "y8": {"arr": y8_arr},
            "z9": {"arr": z9_arr},
            "y9": {"arr": y9_arr},
            "z10": {"arr": z10_arr},
            "zd": {"arr": zd_arr},
            "yd": {"arr": yd_arr},
            "ut": {"arr": ut_arr},
            "u": {"arr": u_arr},
            "ud": {"arr": ud_arr},
            "utv": {"arr": utv_arr},
        }
    }
}
bitmap = drf["display"]["bitMap"]
pygame.init()
# 位图数据宽和高
bitmap_width = len(bitmap["blank"]["arr"][0])
bitmap_height = len(bitmap["blank"]["arr"])
# 调整为720*720
window_width = 1440
window_height = 790
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
# grid
grid_data = np.array(bitmap["grid"]["arr"])
print("grid data:")
print(grid_data)
# slash
slash_data = np.array(bitmap["slash"]["arr"])
print("slash data:")
print(slash_data)
# backSlash
backSlash_data = np.array(bitmap["backSlash"]["arr"])
print("backSlash data:")
print(backSlash_data)
# hZigZag
hZigZag_data = np.array(bitmap["hZigZag"]["arr"])
print("hZigZag data:")
print(hZigZag_data)
# vZigZag
vZigZag_data = np.array(bitmap["vZigZag"]["arr"])
print("vZigZag data:")
print(vZigZag_data)
# hCurb
hCurb_data = np.array(bitmap["hCurb"]["arr"])
print("hCurb data:")
print(hCurb_data)
# vCurb
vCurb_data = np.array(bitmap["vCurb"]["arr"])
print("vCurb data:")
print(vCurb_data)
# brick
brick_data = np.array(bitmap["brick"]["arr"])
print("brick data:")
print(brick_data)
# dagger
dagger_data = np.array(bitmap["dagger"]["arr"])
print("dagger data:")
print(dagger_data)
# triangle
triangle_data = np.array(bitmap["triangle"]["arr"])
print("triangle data:")
print(triangle_data)
# x
x_data = np.array(bitmap["x"]["arr"])
print("x data:")
print(x_data)
# dot1
dot1_data = np.array(bitmap["dot1"]["arr"])
print("dot1 data:")
print(dot1_data)
# dot2
dot2_data = np.array(bitmap["dot2"]["arr"])
print("dot2 data:")
print(dot2_data)
# dot3
dot3_data = np.array(bitmap["dot3"]["arr"])
print("dot3 data:")
print(dot3_data)
# dot4
dot4_data = np.array(bitmap["dot4"]["arr"])
print("dot4 data:")
print(dot4_data)
# stipple0
stipple0_data = np.array(bitmap["stipple0"]["arr"])
print("stipple0 data:")
print(stipple0_data)
# stipple1
stipple1_data = np.array(bitmap["stipple1"]["arr"])
print("stipple1 data:")
print(stipple1_data)
# stipple2
stipple2_data = np.array(bitmap["stipple2"]["arr"])
print("stipple2 data:")
print(stipple2_data)
# stipple2
stipple3_data = np.array(bitmap["stipple3"]["arr"])
print("stipple3 data:")
print(stipple3_data)
# z2
z2_data = np.array(bitmap["z2"]["arr"])
print("z2 data:")
print(z2_data)
# z3
z3_data = np.array(bitmap["z3"]["arr"])
print("z3 data:")
print(z3_data)
# y3
y3_data = np.array(bitmap["y3"]["arr"])
print("y3 data:")
print(y3_data)
# z4
z4_data = np.array(bitmap["z4"]["arr"])
print("z4 data:")
print(z4_data)
# y4
y4_data = np.array(bitmap["y4"]["arr"])
print("y4 data:")
print(y4_data)
# y5
y5_data = np.array(bitmap["y5"]["arr"])
print("y5 data:")
print(y5_data)
# z5
z5_data = np.array(bitmap["z5"]["arr"])
print("z5 data:")
print(z5_data)
# z6
z6_data = np.array(bitmap["z6"]["arr"])
print("z6 data:")
print(z6_data)
# y6
y6_data = np.array(bitmap["y6"]["arr"])
print("y6 data:")
print(y6_data)
# z7
z7_data = np.array(bitmap["z7"]["arr"])
print("z7 data:")
print(z7_data)
# y7
y7_data = np.array(bitmap["y7"]["arr"])
print("y7 data:")
print(y7_data)
# z8
z8_data = np.array(bitmap["z8"]["arr"])
print("z8 data:")
print(z8_data)
# y8
y8_data = np.array(bitmap["y8"]["arr"])
print("y8 data:")
print(y8_data)
# z9
z9_data = np.array(bitmap["z9"]["arr"])
print("z9 data:")
print(z9_data)
# y9
y9_data = np.array(bitmap["y9"]["arr"])
print("y9 data:")
print(y9_data)
# z10
z10_data = np.array(bitmap["z10"]["arr"])
print("z10 data:")
print(z10_data)
# zd
zd_data = np.array(bitmap["zd"]["arr"])
print("zd data:")
print(zd_data)
# yd
yd_data = np.array(bitmap["yd"]["arr"])
print("yd data:")
print(yd_data)
# ut
ut_data = np.array(bitmap["ut"]["arr"])
print("ut data:")
print(ut_data)
# u
u_data = np.array(bitmap["u"]["arr"])
print("u data:")
print(u_data)
# ud
ud_data = np.array(bitmap["ud"]["arr"])
print("ud data:")
print(ud_data)
# utv
utv_data = np.array(bitmap["utv"]["arr"])
print("utv data:")
print(utv_data)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 绘制位图
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
            else:
                color = (255, 255, 255)  # 白色
            pygame.draw.rect(surface, color, (x + bitmap_width, y, 1, 1))
            if blank_data[y][x] == 1:
                color = (0, 255, 0)  # 绿色
            else:
                color = (255, 255, 255)  # 白色
            pygame.draw.rect(surface, color, (x + bitmap_width * 2, y, 1, 1))
            if hLine_data[y][x] == 1:
                color = (0, 0, 255)  # 蓝色
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 3, y, 1, 1))
            if vLine_data[y][x] == 1:
                color = (255, 255, 0)  # 黄色
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 4, y, 1, 1))
            if cross_data[y][x] == 1:
                color = (255, 0, 255)  # 紫色
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 5, y, 1, 1))
            if y < len(grid_data) and x < len(grid_data[y]) and grid_data[y][x] == 1:
                color = (0, 204, 102)  # 绿色
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 6, y, 1, 1))

            if slash_data[y][x] == 1:
                color = (217, 230, 255)  # silver
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 7, y, 1, 1))
            if backSlash_data[y][x] == 1:
                color = (255, 255, 204)  # cream
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 8, y, 1, 1))
            if hZigZag_data[y][x] == 1:
                color = (255, 191, 242)  # pink
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 9, y, 1, 1))
            if vZigZag_data[y][x] == 1:
                color = (0, 255, 0)  # lime
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 10, y, 1, 1))
            if y < len(hCurb_data) and x < len(hCurb_data[y]) and hCurb_data[y][x] == 1:
                color = (255, 230, 191)  # tan
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 11, y, 1, 1))
            if y < len(vCurb_data) and x < len(vCurb_data[y]) and vCurb_data[y][x] == 1:
                color = (0, 230, 230)  # cyan
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 12, y, 1, 1))
            if y < len(brick_data) and x < len(brick_data[y]) and brick_data[y][x] == 1:
                color = (255, 128, 0)  # orange
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 13, y, 1, 1))
            if (
                y < len(dagger_data)
                and x < len(dagger_data[y])
                and dagger_data[y][x] == 1
            ):
                color = (153, 0, 230)  # purple
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 14, y, 1, 1))
            if (
                y < len(triangle_data)
                and x < len(triangle_data[y])
                and triangle_data[y][x] == 1
            ):
                color = (191, 64, 38)  # brown
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 15, y, 1, 1))
            if y < len(x_data) and x < len(x_data[y]) and x_data[y][x] == 1:
                color = (140, 140, 166)  # slate
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x + bitmap_width * 16, y, 1, 1))
            if dot1_data[y][x] == 1:
                color = (217, 204, 0)  # gold
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x, y + bitmap_height, 1, 1))
            if dot2_data[y][x] == 1:
                color = (230, 31, 13)  # maroon
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width, y + bitmap_height, 1, 1)
            )
            if dot3_data[y][x] == 1:
                color = (94, 0, 230)  # violet
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 2, y + bitmap_height, 1, 1)
            )
            if dot4_data[y][x] == 1:
                color = (38, 140, 107)  # forest
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 3, y + bitmap_height, 1, 1)
            )
            if (
                y < len(stipple0_data)
                and x < len(stipple0_data[y])
                and stipple0_data[y][x] == 1
            ):
                color = (128, 38, 38)  # chocolate
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 4, y + bitmap_height, 1, 1)
            )
            if (
                y < len(stipple1_data)
                and x < len(stipple1_data[y])
                and stipple1_data[y][x] == 1
            ):
                color = (51, 51, 153)  # navy
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 5, y + bitmap_height, 1, 1)
            )
            if (
                y < len(stipple2_data)
                and x < len(stipple2_data[y])
                and stipple2_data[y][x] == 1
            ):
                color = (224, 224, 224)  # winBack
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 6, y + bitmap_height, 1, 1)
            )
            if (
                y < len(stipple3_data)
                and x < len(stipple3_data[y])
                and stipple3_data[y][x] == 1
            ):
                color = (128, 0, 0)  # winFore
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 7, y + bitmap_height, 1, 1)
            )
            if z2_data[y][x] == 1:
                color = (51, 51, 51)  # winText
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 8, y + bitmap_height, 1, 1)
            )
            if z3_data[y][x] == 1:
                color = (166, 166, 166)  # winColor1
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 9, y + bitmap_height, 1, 1)
            )
            if y3_data[y][x] == 1:
                color = (115, 115, 115)  # winColor2
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 10, y + bitmap_height, 1, 1)
            )
            if z4_data[y][x] == 1:
                color = (189, 204, 204)  # winColor3
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 11, y + bitmap_height, 1, 1)
            )
            if y4_data[y][x] == 1:
                color = (204, 204, 204)  # winColor4
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 12, y + bitmap_height, 1, 1)
            )
            if y5_data[y][x] == 1:
                color = (199, 199, 199)  # winColor5
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 13, y + bitmap_height, 1, 1)
            )
            if z5_data[y][x] == 1:
                color = (199, 199, 199)  # winColor5B
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 14, y + bitmap_height, 1, 1)
            )
            if z6_data[y][x] == 1:
                color = (0, 24, 242)  # joy1
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 15, y + bitmap_height, 1, 1)
            )
            if y6_data[y][x] == 1:
                color = (255, 255, 255)  # white
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 16, y + bitmap_height, 1, 1)
            )
            if z7_data[y][x] == 1:
                color = (217, 230, 255)  # silver
            else:
                color = (255, 255, 255)
            pygame.draw.rect(surface, color, (x, y + bitmap_height * 2, 1, 1))
            if y7_data[y][x] == 1:
                color = (255, 255, 204)  # cream
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width, y + bitmap_height * 2, 1, 1)
            )
            if z8_data[y][x] == 1:
                color = (255, 191, 242)  # pink
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 2, y + bitmap_height * 2, 1, 1)
            )
            if y8_data[y][x] == 1:
                color = (255, 0, 255)  # magenta
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 3, y + bitmap_height * 2, 1, 1)
            )
            if z9_data[y][x] == 1:
                color = (0, 255, 0)  # lime
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 4, y + bitmap_height * 2, 1, 1)
            )
            if y9_data[y][x] == 1:
                color = (255, 230, 191)  # tan
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 5, y + bitmap_height * 2, 1, 1)
            )
            if z10_data[y][x] == 1:
                color = (0, 230, 230)  # cyan
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 6, y + bitmap_height * 2, 1, 1)
            )
            if y < len(zd_data) and x < len(zd_data[y]) and zd_data[y][x] == 1:
                color = (204, 204, 217)  # gray
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 7, y + bitmap_height * 2, 1, 1)
            )
            if y < len(yd_data) and x < len(yd_data[y]) and yd_data[y][x] == 1:
                color = (255, 255, 0)  # yellow
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 8, y + bitmap_height * 2, 1, 1)
            )
            if y < len(ut_data) and x < len(ut_data[y]) and ut_data[y][x] == 1:
                color = (255, 128, 0)  # orange
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 9, y + bitmap_height * 2, 1, 1)
            )
            if y < len(u_data) and x < len(u_data[y]) and u_data[y][x] == 1:
                color = (0, 204, 102)  # green
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 10, y + bitmap_height * 2, 1, 1)
            )
            if y < len(ud_data) and x < len(ud_data[y]) and ud_data[y][x] == 1:
                color = (153, 0, 230)  # purpleB
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 11, y + bitmap_height * 2, 1, 1)
            )
            if y < len(utv_data) and x < len(utv_data[y]) and utv_data[y][x] == 1:
                color = (217, 204, 0)  # goldB
            else:
                color = (255, 255, 255)
            pygame.draw.rect(
                surface, color, (x + bitmap_width * 12, y + bitmap_height * 2, 1, 1)
            )

    # 缩放表面到窗口大小
    scaled_surface = pygame.transform.scale(surface, (window_width, window_height))
    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()
