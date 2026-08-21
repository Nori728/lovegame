# 读取你原本的大酱剧情文件
file_path = "stories/dajiang.py"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # 1. 把网页带来的隐形空格 \xa0 全部换成普通空格
    line = line.replace("\xa0", " ")
    # 2. 把行首可能存在的制表符(Tab)统一换成 4 个标准空格（防止 tab 与 space 混用报错）
    # 如果你原本用的是 Tab，可以不用这一步，但通常统一成空格最稳妥
    new_lines.append(line)

# 写回文件
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("清理完成！")
