# coding = utf-8
from os import path
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread

d = path.dirname('')
text = open('E:/Python/fenci.txt',mode='r',encoding='utf8').read()
bg_pic = imread('E:/Python/bg_pic.jpg')

# 生成词云
wordcloud = WordCloud(mask=bg_pic, background_color='white', scale=1.5,
                      font_path=r'E:\Python\FZYTK.TTF').generate(text)
image_colors = ImageColorGenerator(bg_pic)
# 显示词云图片

plt.imshow(wordcloud.recolor(color_func=image_colors))
plt.axis('off')
plt.show()

# 保存图片
wordcloud.to_file('E:\Python\picture.jpg')
