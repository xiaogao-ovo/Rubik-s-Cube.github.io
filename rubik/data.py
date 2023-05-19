# 模板路径
import rubik
template_path = rubik.__file__.replace("__init__.py", "assets/template.png")

# 颜色和小面位置相互转化（字典）
color_to_facet = {"white":"U", "red":"L", "blue":"F", "green":"B", "orange":"R", "yellow":"D"}

facet_to_color = {val:key for key, val in color_to_facet.items()}

init_state = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

# 上，左，右，处在三个位置时各颜色的数值
color_table = {'U': ((252, 244, 252), (222, 215, 222), (198, 192, 198)),
          'L': ((236, 56, 35), (208, 50, 30), (186, 44, 27)),
          'F': ((64, 168, 198), (56, 148, 174), (51, 132, 155)),
          'B': ((128, 200, 55), (113, 176, 49), (101, 157, 44)),
          'R': ((252, 138, 10), (222, 122, 9), (198, 109, 8)),
          'D': ((252, 237, 71), (222, 208, 63), (198, 186, 56))}

# 魔方展开图
# init_txt: 仅用于展示索引信息
init_txt = """
             |************|
             |*U1**U2**U3*|
             |************|
             |*U4**U5**U6*|
             |************|
             |*U7**U8**U9*|
             |************|
 ************|************|************|************
 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
 ************|************|************|************
 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
 ************|************|************|************
 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
 ************|************|************|************
             |************|
             |*D1**D2**D3*|
             |************|
             |*D4**D5**D6*|
             |************|
             |*D7**D8**D9*|
             |************|
"""

# inds_txt: 用于代入索引
inds_txt = """
          |*********|
          |*U1**U2**U3*|
          |*********|
          |*U4**U5**U6*|
          |*********|
          |*U7**U8**U9*|
          |*********|
 *********|*********|*********|*********
 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
 *********|*********|*********|*********
 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
 *********|*********|*********|*********
 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
 *********|*********|*********|*********
          |*********|
          |*D1**D2**D3*|
          |*********|
          |*D4**D5**D6*|
          |*********|
          |*D7**D8**D9*|
          |*********|
"""

# compact_init_txt: 初始状态
compact_init_txt = """
          -----
        | U U U |
        | U U U |
        | U U U |
---------------------------------
| L L L | F F F | R R R | B B B |
| L L L | F F F | R R R | B B B |
| L L L | F F F | R R R | B B B |
---------------------------------
        | D D D |
        | D D D |
        | D D D |
          -----
"""

# compact_inds_txt: 用于代入索引
compact_inds_txt = """
          -----
        | U1 U2 U3 |
        | U4 U5 U6 |
        | U7 U8 U9 |
---------------------------------
| L1 L2 L3 | F1 F2 F3 | R1 R2 R3 | B1 B2 B3 |
| L4 L5 L6 | F4 F5 F6 | R4 R5 R6 | B4 B5 B6 |
| L7 L8 L9 | F7 F8 F9 | R7 R8 R9 | B7 B8 B9 |
---------------------------------
        | D1 D2 D3 |
        | D4 D5 D6 |
        | D7 D8 D9 |
          -----
"""

face_inds_txt = """
  -----
| {} {} {} |
| {} {} {} |
| {} {} {} |
  -----
"""