# 一、项目背景
captchaAssistant是一款专门针对残障人士推出的验证码自动化操作工具。如今验证码越来越复杂，要求的操作越来越高，对于残障人士浏览网页上网是一个不小的挑战。本软件最大限度的替残障人士完成验证码的自动化验证操作，降低验证码操作门槛。

# 二、测试时间
- ddddOCR功能验证：2024/8/10
- API测试
- 验证码获取测试
- 验证码填写验证

# 三、测试平台
Windows平台

# 四、测试内容
## ddddOCR功能验证  
ddddOCR共有三个功能：基本OCR功能、滑块检测功能、目标检测功能  

1. 基本OCR功能验证  
测试用例1  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![1.png](..%2Fddddocr%2Fimage%2FBasicOCR_image%2F1.png)  
&nbsp;&nbsp;&nbsp;&nbsp;输出：jepv  
测试用例2  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![4.png](..%2Fddddocr%2Fimage%2FBasicOCR_image%2F4.png)  
&nbsp;&nbsp;&nbsp;&nbsp;输出：5739  
测试用例3  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![5.png](..%2Fddddocr%2Fimage%2FBasicOCR_image%2F5.png)  
&nbsp;&nbsp;&nbsp;&nbsp;输出：kdqu
2. 滑块检测功能验证  
测试用例1  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![1_target.png](..%2Fddddocr%2Fimage%2FSliderDetection%2F1_target.png)、![1_background.png](..%2Fddddocr%2Fimage%2FSliderDetection%2F1_background.png)  
&nbsp;&nbsp;&nbsp;&nbsp;输出：{'target_x': 1, 'target_y': 45, 'target': [215, 45, 260, 91]}  
3. 目标检测功能验证  
测试用例1  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![1.png](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F1.png)  
&nbsp;&nbsp;&nbsp;&nbsp;输出验证码图片：![1_result.jpg](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F1_result.jpg)  
测试用例2  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![2.jpg](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F2.jpg)  
&nbsp;&nbsp;&nbsp;&nbsp;输出验证码图片：![2_result.jpg](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F2_result.jpg)  
测试用例3  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![3.bmp](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F3.bmp)  
&nbsp;&nbsp;&nbsp;&nbsp;输出验证码图片：![3_result.bmp](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F3_result.bmp)  
测试用例4  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![4.jpg](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F4.jpg)  
&nbsp;&nbsp;&nbsp;&nbsp;输出验证码图片：![4_result.jpg](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F4_result.jpg)  
测试用例5  
&nbsp;&nbsp;&nbsp;&nbsp;输入验证码图片：![5.png](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F5.png)  
&nbsp;&nbsp;&nbsp;&nbsp;输出验证码图片：![5_result.png](..%2Fddddocr%2Fimage%2FTargetDetection_image%2F5_result.png)  
 
## API测试
## 验证码获取测试
## 验证码填写验证
## 完整功能测试
1. 测试网站  
1.）https://zp.hunau.edu.cn/base/frame/recruitVerfication.jsp （数字验证码）  
2.）https://im.qq.com/index/ （点选图片，逻辑描述，比如说文具）  
3.）https://weibo.com/newlogin （点选图片，简笔画）  
4.）https://www.zhihu.com/signin?next=%2F （滑块验证）  

# 五、测试结果
1. ddddOCR功能验证  
ddddOCR基本满足要求。除目标检测功能验证测试用例3外，都能正确识别