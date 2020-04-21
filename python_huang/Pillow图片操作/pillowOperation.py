from PIL import Image, ImageFilter
from PIL import Image

# 创建图片
image = Image.new('RGB', (60, 30), color=(73, 109, 137))
image.save('pil_color.png')

# 打开一个jpg图像文件
image = Image.open('img/xuexi.jpg')

# 显示图片信息
print(image.format)     # 图片的文件格式；
print(image.size)       # 图片的长宽像素
print(image.width)      # 图片的宽度，像素
print(image.height)     # 图片的高度
print(image.mode)       # 图片的颜色模式
print(image.filename)   # 图片的名称
print(image.info)       # 图片的产品信息

# 显示图片
image.show()

# 转换图片格式   jpg、png，还支持gif、pdf、eps、psd等，甚至 webp，
image = Image.open('hackwork.jpg')
image.save('hackwork.png')

# 修改图片大小  图片可能会不协调
image = Image.open('img/xuexi.jpg')         # 打开需要修改的图片
new_image = image.resize((400, 400))        # resize修改大小
new_image.save('img/xuexi1.jpg')            # 修改后的图片另存为

# 缩略图
image = Image.open('img/xuexi.jpg')         # 打开需要缩略的图片
image.thumbnail((100, 100))                 # thumbnail缩略大小
image.save('img/xuexi2.jpg')                # 缩略后的图片另存为

# 旋转图片
colorImage = Image.open("img/xuexi.jpg")
rotated = colorImage.rotate(180)                      # 旋转
rotated.show()

transposed = colorImage.transpose(Image.ROTATE_90)    # 旋转
transposed.show()

# 裁剪图片
image = Image.open("img/xuexi.jpg")     # 打开图片
box = (100, 100, 500, 500)              # 设置裁剪大小
cropedImage = image.crop(box)           # 裁剪crop（）
cropedImage.save("xuexi3.jpg")          # 裁剪后另存为

# 将一张图片粘贴到另外一张图片(合并图片)
image = Image.open('img/xuexi.jpg')       # 打开图片
logo = Image.open('img/fansi.jpg')        # 打开图片
image_copy = image.copy()                 # 复制图片
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))  # 粘贴位置
image_copy.paste(logo, position)          # 粘贴
image_copy.save('img/pasted_image.jpg')   # 粘贴后另存为

# 打开一个jpg图像文件，注意是当前路径:
image = Image.open('img/xuexi.jpg')
# 应用模糊滤镜:
image2 = image.filter(ImageFilter.BLUR)
# 高斯模糊
image3 = image.filter(ImageFilter.GaussianBlur)
# 边缘增强
image4 = image.filter(ImageFilter.EDGE_ENHANCE)
# 找到边缘
image5 = image.filter(ImageFilter.FIND_EDGES)
# 浮雕
image6 = image.filter(ImageFilter.EMBOSS)
# 轮廓
image7 = image.filter(ImageFilter.CONTOUR)
# 锐化
image8 = image.filter(ImageFilter.SHARPEN)
# 平滑
image9 = image.filter(ImageFilter.SMOOTH)
# 细节
image10 = image.filter(ImageFilter.DETAIL)