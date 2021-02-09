# PIL

## crop image

```
from PIL import Image

filename = r'screencapture-joinquant-research-2020-11-19-15_36_46.jpg'
img = Image.open(filename)
size = img.size

height = [0, 2800, 4300, 10300, 16300, 22300]
for i in range(len(height)):

    if i+1 >= len(height):
        break

    sub_img = img.crop((0, height[i], size[0], height[i+1]))
    sub_img.save('tmp_{0}.png'.format(i))
```
