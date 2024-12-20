# ssd1306-bad-apple-esp32
> 使用esp32-cam 在 ssd1306 oled显示屏 上播放 bad apple， 附带视频帧转换成1306缓冲区可以使用的文件的代码

> 使用micropython

# 用法
```python
'''
  oled = SSD1306(...)
  badapp.hex文件由video2hex.py生成
'''
def ReadFile(file_name):
    with open(file_name, 'rb') as file:
        for line in file:
            yield line.strip()
for frame in ReadFile('badapple.hex'):
    oled.buffer = bytearray(frame)
    oled.show()
```
