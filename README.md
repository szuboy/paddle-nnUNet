简体中文 | [[EN](https://github.com/szuboy/paddle-nnUNet/blob/master/README_EN.md)]

<div align="center">

<p align="center">
    <img src="https://github.com/szuboy/paddle-nnUNet/blob/master/paddlennunet.png?raw=true" align="middle" width="450"/>
</p>

**飞桨nnUNet医学图像分割框架，一个基于PaddlePaddle翻译的nnUNet全新版本！**

![Build Status](https://github.com/szuboy/paddle-nnUNet/actions/workflows/python-package.yml/badge.svg)
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)
![python version](https://img.shields.io/badge/python-3.0+-orange.svg)
![support os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-yellow.svg)
![PyPI Status](https://pepy.tech/badge/paddle-nnunet/month)
</div>

## 这是paddle-nnUNet

UNet几乎是卷积神经网络在医学图像分割领域的最为成功的模型。而作为一个自适应框架，nnUNet无疑是在所有UNet改进和优化模型中最成功的一个。nnUNet原本是基于[Pytorch框架](https://github.com/MIC-DKFZ/nnUNet) 开发的，这是对应的`PaddlePaddle`翻译版本。如果想了解nnU-Net更多的信息，请阅读作者发表的[论文](https://www.nature.com/articles/s41592-020-01008-z) 。

## 安装方式

由于nnUNet采用动态图自动构建的，安装之前请确保飞桨框架版本大于`2.0`版本。我们的安装方法有两种:

**1、使用 PyPi 安装 paddle-nnUNet(推荐)**

```
pip install paddle-nnUNet
```

**2、使用 paddle-nnUNet 源码安装**

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

可通过`import paddlennunet`验证是否安装成功
```
Hello from the paddle-nnUNet. https://paddle-nnunet.readthedocs.io
```
如果看到上述输出打印信息：则说明安装成功；如果没有，需要检查是不是`paddlepaddle`版本问题或者是环境问题引起安装失败。

## 快速使用

### 数据转换

待补充

### 实验计划和预处理

待补充

### 模型的训练

待补充

### 详细的教程推荐

如果你还想了解更详细的教程解析，请参考[ReadTheDocs教程](https://paddle-nnunet.readthedocs.io/) ，这里啥都有讲！可用性不够好？也请让我们知道！

## 许可证书
本项目的发布受Apache 2.0 license许可认证。
