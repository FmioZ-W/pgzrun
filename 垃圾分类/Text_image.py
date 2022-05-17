'''向图片上写入垃圾说明，生成图片'''
from PIL import Image, ImageDraw, ImageFont

# 创建图像
img = Image.open("D:\\1-pythonProject\\垃圾分类\\images\\libriry_in.png")
# 新建绘图对象
draw = ImageDraw.Draw(img)
# 选择文字字体和大小
setFont = ImageFont.truetype("D:\\1-pythonProject\\垃圾分类\\fonts\\myrb.ttf", 75)
fillColor = (0, 0, 0)  # 文字颜色：黑色
pos = (0, 0)          # 文本左上角位置 (离左边界距离， 离上边界距离)

# #可回收垃圾说明
text1 = "\n可回收物指适宜回收利用和资源化利\n用的生活废弃物。\n\n可回收物主要品种包括：废纸、废弃\n塑料瓶、废金属、废包装物、废旧纺\n织物、废弃电器电子产品、废玻璃、\n废纸塑铝复合包装等"
draw.text(pos, text1, font=setFont, fill=fillColor)
save_path = 'images\\circle_waste.info.png'
img.save(save_path)

#有害垃圾说明
# 创建图像
img = Image.open("D:\\1-pythonProject\\垃圾分类\\images\\libriry_in.png")
# 新建绘图对象
draw = ImageDraw.Draw(img)
text2 = "\n有害垃圾指对人体健康或者自然环境\n造成直接或者潜在危害生活的废弃物。\n\n常见的有害垃圾包括废灯管、废油漆、\n杀虫剂、废弃化妆品、过期药品、废\n电池、废灯泡、废水银温度计等，\n\n有害垃圾需按照特殊正确的方法安全\n处理"    # 写入的文本，若要换行，字符串中添加'\n'
draw.text(pos, text2, font=setFont, fill=fillColor)
save_path = 'images\\harmful_waste_info.png'
img.save(save_path)

#干垃圾说明
# 创建图像
img = Image.open("D:\\1-pythonProject\\垃圾分类\\images\\libriry_in.png")
# 新建绘图对象
draw = ImageDraw.Draw(img)
text3 = "\n干垃圾有纸巾、牙签、拖把、抹布、\n一次性筷子、陶瓷类、废弃物、清扫\n渣、土陶瓷、碗碟、大块骨头、硬壳、\n塑料袋、A4纸、包装袋、快递包装\n袋、热饮杯盖、纽扣、无汞干电池、\n面膜、大肉骨头、卫生巾、卫生纸、\n湿纸巾、旧浴缸、盆子等。\n\n干垃圾指除可回收垃圾、有害垃圾、\n湿垃圾以外的其它生活废弃物。"
draw.text(pos, text3, font=setFont, fill=fillColor)
save_path = 'images\\dry_waste_info.png'
img.save(save_path)

#湿垃圾说明
img = Image.open("D:\\1-pythonProject\\垃圾分类\\images\\libriry_in.png")
# 新建绘图对象
draw = ImageDraw.Draw(img)
text4 = "\n湿垃圾又称为厨余垃圾、有机垃圾，\n即易腐垃圾，指食材废料、剩菜剩饭、\n过期食品、瓜皮果核、花卉绿植、中\n药药渣等易腐的生物质生活废弃物。\n\n其主要来源为家庭厨房、餐厅、饭店、\n食堂、市场及其他与食品加工有关的\n行业。"
draw.text(pos, text4, font=setFont, fill=fillColor)
save_path = 'images\\wet_waste_info.png'
img.save(save_path)

#游戏说明
img = Image.open("D:\\1-pythonProject\\垃圾分类\\images\\background_main.png")
# 新建绘图对象
draw = ImageDraw.Draw(img)
text_main = "\n↑ ↓ ← → 键操控人物\n\n点击鼠标左键拾取垃圾\n\n点击垃圾桶扔进垃圾\n\n全部分类正确则游戏胜利"
draw.text(pos, text_main, font=setFont, fill=fillColor)
save_path = 'images\\game_info.png'
img.save(save_path)


#按钮
setFont_button = ImageFont.truetype("D:\\1-pythonProject\\垃圾分类\\fonts\\myrb.ttf", 33)
pos_button = (0,5)
#游戏开始
img = Image.open("D:\\1-pythonProject\\垃圾分类\\images\\game_begin.png")
# 新建绘图对象
draw = ImageDraw.Draw(img)
text_begin = "开始游戏"
draw.text(pos_button, text_begin, font=setFont_button, fill=fillColor)
save_path = 'images\\game_begin_text.png'
img.save(save_path)

#退出游戏
img = Image.open("D:\\1-pythonProject\\垃圾分类\\images\\game_end.png")
draw = ImageDraw.Draw(img)
text_end = "退出游戏"
draw.text(pos_button, text_end, font=setFont_button, fill=fillColor)
save_path = 'images\\game_end_text.png'
img.save(save_path)

#游戏说明按钮
img = Image.open("D:\\1-pythonProject\\垃圾分类\\images\\game_information.png")
draw = ImageDraw.Draw(img)
text_end = "游戏说明"
draw.text((40,50), text_end, font=setFont_button, fill=fillColor)
save_path = 'images\\game_book_text.png'
img.save(save_path)