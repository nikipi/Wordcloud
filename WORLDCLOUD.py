from wordcloud import WordCloud
import matplotlib.pyplot as plt

import re

with open('/Users/apple/Desktop/Yulu.txt') as c:
    '''抽取文本中的英文部分并小写化，并将空格作为分隔拼接为长字符串'''
    text = ' '.join([word.group().lower() for word in re.finditer('[a-zA-Z]+', c.read())])

'''查看前100个字符'''
print(text[:500])
'''
wordcloud = WordCloud(background_color='white', # 背景色为白色
                      height=400, # 高度设置为400
                      width=800, # 宽度设置为800
                      scale=20, # 长宽拉伸程度设置为20
                      prefer_horizontal=0.9999).generate(text)
plt.figure(figsize=[8, 4])
plt.imshow(wordcloud)
plt.axis('off')

plt.savefig('图6.png', dpi=600, bbox_inches='tight', quality=95)
plt.show()
'''

from PIL import Image
import numpy as np

usa_mask = np.array(Image.open('/Users/apple/Desktop/FUCK.png'))
'''从文本中生成词云图'''
wordcloud = WordCloud(background_color='white', # 背景色为白色
                      height=700, # 高度设置为400
                      width=1600, # 宽度设置为800
                      scale=40, # 长宽拉伸程度程度设置为20
                      prefer_horizontal=0.9999,
                      mask=usa_mask # 添加蒙版
                     ).generate(text)
plt.figure(figsize=[8, 4])
plt.imshow(wordcloud)
plt.axis('off')
'''保存到本地'''
plt.savefig('/Users/apple/Desktop/图8.png', dpi=600, bbox_inches='tight', quality=95)
plt.show()