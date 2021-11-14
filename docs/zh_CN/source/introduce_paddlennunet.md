
# 你好，paddle-nnUNet!
这是我第一次接触百度飞浆（paddlepadddle）平台，之前有接触过TensorFlow、Keras和Pytorch，
由于 nnUNet 是动态更改网络配置，因此本项目是基于 Python 3.0+ 和 paddle ≥ 2.0 支持动态图的版本来进行开发，
如果你想来尝试 paddle-nnUNet，请检查 paddle 版本是否符合要求。

paddle-nnUNet 是将原来基于 pytorch 版本的 nnUnet 全部代码重写移植到 paddle 平台上，含有全部功能以及更多的解释和建议。

## 安装
我们有两种方法按照paddle-nnUNet:

- **使用 PyPi 安装 paddle-nnUNet(推荐)**

```
pip install paddle-nnUNet
```

- **使用 paddle-nnUNet 源码安装**

首先，使用 ```git``` 来克隆 paddle-nnUNet
```
git clone https://github.com/szuboy/paddle-nnUNet.git
```
然后，```cd``` 到 paddle-nnUNet 的文件夹
```
cd paddle-nnUNet
```
最后，运行安装命令
```
python setup.py install
```

## 技术支持
你可以在 [Github issues](https://github.com/szuboy/paddle-nnUNet/issues) 里中提问，在提问之前请确保你阅读过本文档，
作者是一个拥抱开源的开发者，他一定会一一回复的。

如果你觉得本文档对你的研究和使用有所帮助，欢迎为本文档的 [Github](https://github.com/szuboy/paddle-nnUNet) 加颗星哦，以鼓励作者进一步完善文档内容，提高文档质量。
