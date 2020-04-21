# 绘制简单折线图

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

# 绘制散点 设置散点大小、颜色 和 散点轮廓颜色   散点颜色也可 c = (0,0,1) 取值范围是0-1
plt.scatter(input_values,squares,s=300,edgecolors='red',c = 'yellow')
#使用颜色映射
#plt.scatter(input_values,squares,c = squares ,cmap = plt.cm.Blues, edgecolors='none',s= 40)

plt.plot(input_values,squares, linewidth=5)    # 列表传递给函数plot()    #linewidth = 图形线条粗细
plt.title("Squares Numbers", fontsize=24)      # 设置图标标题
plt.xlabel("Value", fontsize=24)               # 给x轴加标签
plt.ylabel("Square of Value", fontsize=24)     # 给y轴加标签
plt.axis([0,10,0,50])                           #设置坐标轴取值范围
plt.savefig('sqares_plot.png',bbox_inches = 'tight')    #将图表保存到文件中并命名  二参表示将图表多余空白区剪裁掉
plt.show()



