# CRNN_kreas

**文本识别分为两部分：文本定位与文本序列识别。这个repo主要是做的后者。**

这是一个基于CRNN的文本序列识别项目，目前正在测试数字串的识别。之后会加入更多的文字识别。

其中src文件夹下面存储的是源码，data下面存储的是数据，predicted_results下面存的是当前在测试集上面的测试结果。

在300w+的中文数据集上训练之后,得到了0.99的精度.(整个label都预测正确才认为正确)

#### File Description

| File               | Description                |
| ------------------ | -------------------------- |
| vgg_bgru_ctc.py    | 网络模型文件               |
| vgg_blstm_ctc.py   | 网络模型文件               |
| resnet_bgru_ctc.py | 网络模型文件               |
| train.py           | 训练函数                   |
| predicts.py        | 预测函数                   |
| data_generator.py  | 数据生成函数，节省内存空间 |
| dicts.py           | 字符字典                   |
| utils.py           | 辅助函数                   |
| predicted_results  | 一些预测的结果             |
| trained_weights    | 训练好的模型               |



#### 参考文献：

##### 论文：

CRNN：https://arxiv.org/abs/1507.05717

CTC：http://people.idsia.ch/~santiago/papers/icml2006.pdf

##### 博客：

CRNN：

https://zhuanlan.zhihu.com/p/43534801

CTC：

https://www.cnblogs.com/qcloud1001/p/9041218.html，

https://distill.pub/2017/ctc/

https://towardsdatascience.com/intuitively-understanding-connectionist-temporal-classification-3797e43a86c

##### git：

https://github.com/Liumihan/CRNN-Keras

https://github.com/Liumihan/keras_ocr