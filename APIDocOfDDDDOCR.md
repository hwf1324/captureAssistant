# ddddOCR接口说明文档

### 1.__init__(self, ocr: bool = True, det: bool = False, old: bool = False, beta: bool = False, use_gpu: bool = False, device_id: int = 0, show_ad=True, import_onnx_path: str = "", charsets_path: str = "")
* 函数功能：初始化ddddOcr
* 参数：

| 参数名              | 类型   | 是否必须 | 默认值   | 说明           |
|:-----------------|------|------|-------|--------------|
| ocr              | bool | 否    | True  | 是否开启ocr      |
| det              | bool | 否    | False | 是否开启目标检测     |
| old              | bool | 否    | False | 是否使用第一套ocr模型 |
| beta             | bool | 否    | False | 是否使用第二套ocr模型 |
| use_gpu          | bool | 否    | False | 是否使用gpu      |
| device_id        | int  | 否    | 0     | gpu的设备id     |
| show_ad          | bool | 否    | True  | 是否显示欢迎信息     |
| import_onnx_path | str  | 否    | empty | 训练模型         |
| charsets_path    | str  | 否    | empty | 字符路径         |

* 返回值：det
* 示例代码
```
det = ddddocr.DdddOcr(det=True)
```

### 2. classification(self, img, png_fix: bool = False, probability=False)  
* 函数功能：OCR基础识别  
* 参数:

| 参数名         |  类型  | 是否必须 | 默认值   | 说明              |
|:------------|:----:|:----:|-------|:----------------|
| img         | str  |  是   | null  | 图片路径            |
| png_fix     | bool |  否   | False | 是否处理透明黑色png格式图片 |  
| probability | bool |  否   | False | OCR概率输出         |

* 返回值：

| 类型  | 说明      |
|-----|---------|
| str | 图片中的验证码 |

* 示例代码
```
image = open(r"F:\Code\Project\Program\Engage2024\ddddocr\image\BasicOCR_image\4.png", "rb").read()
ocr.set_ranges("0123456789+-x/=")
result = ocr.classification(image, probability=True)
s = ""
for i in result['probability']:
    s += result['charsets'][i.index(max(i))]

print(s)
```

### 3.slide_match(self, target_bytes: bytes = None, background_bytes: bytes = None, simple_target: bool = False, flag: bool = False)
* 函数功能：滑块检测的第一种算法。通过滑块图像的边缘在背景图中计算找到相对应的坑位，可以分别获取到滑块图和背景图，滑块图为透明背景图
* 参数：

| 参数名              | 类型    | 是否必须 | 默认值   | 说明                              |
|------------------|-------|------|-------|---------------------------------|
| target_bytes     | bytes | 是    | None  | 读取的滑块图                          |
| background_bytes | bytes | 是    | None  | 读取的背景图                          |
| simple_target    | bool  | 否    | False | 如果滑块无过多背景部分，可以添加simple_target参数 |
| flag             | bool  | 否    | False | ?                               |

* 示例代码
```
    slide = ddddocr.DdddOcr(det=False, ocr=False)
    
    with open('target.jpg', 'rb') as f:
        target_bytes = f.read()
    
    with open('background.jpg', 'rb') as f:
        background_bytes = f.read()
    
    res = slide.slide_match(target_bytes, background_bytes, simple_target=True)
    
    print(res)
```

### 4.slide_comparison(self, target_bytes: bytes = None, background_bytes: bytes = None)
* 函数功能：滑块检测的第二种算法。通过比较两张图的不同之处进行判断滑块目标坑位的位置
* 参数：

| 参数名              | 类型    | 是否必须 | 默认值  | 说明     |
|------------------|-------|------|------|--------|
| target_bytes     | bytes | 是    | None | 读取的滑块图 |
| background_bytes | bytes | 是    | None | 读取的背景图 |

* 示例代码
```
    slide = ddddocr.DdddOcr(det=False, ocr=False)

    with open('bg.jpg', 'rb') as f:
        target_bytes = f.read()
    
    with open('fullpage.jpg', 'rb') as f:
        background_bytes = f.read()
    
    img = cv2.imread("bg.jpg")
    
    res = slide.slide_comparison(target_bytes, background_bytes)

    print(res)
```

### 5.OCR概率输出
为了提供更灵活的ocr结果控制与范围限定，项目支持对ocr结果进行范围限定