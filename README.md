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

UNet可以说是卷积神经网络在医学图像分割领域的最为成功的模型。而作为一个自适应框架，nnUNet无疑是在所有UNet改进和优化模型中最出色的一个。nnUNet原本是基于[Pytorch框架](https://github.com/MIC-DKFZ/nnUNet) 开发的，这是对应的`PaddlePaddle`翻译版本。如果想了解nnU-Net更多的信息，请阅读作者发表的[论文](https://www.nature.com/articles/s41592-020-01008-z) 。

## 安装方式

由于nnUNet采用动态图自动构建的，安装之前请确保飞桨框架版本大于`2.0`版本。同时，Python 2不受支持，请确保您使用的是 Python 3，安装方法有两种:

* 用作**标准化基线、开箱即用的分割算法**或使用预训练模型运行**推理**：

    ```
    pip install paddle-nnUNet
    ```

* 用作集成**框架**（这将会创建nnU-Net代码的副本，以便根据需要对其进行修改）：

    ```
    git clone https://github.com/szuboy/paddle-nnUNet.git
    cd padle-nnUNet
    python install -e .
    ```

请注意，这些命令只是执行Python脚本，如果是在虚拟环境中安装了nnU-Net，则在执行命令时必须激活此环境。


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
