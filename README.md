简体中文 | [[EN](https://github.com/szuboy/paddle-nnUNet/blob/master/README_EN.md)]

<div align="center">

<p align="center">
<img src="https://github.com/szuboy/paddle-nnUNet/blob/master/paddlennunet.png?raw=true" align="middle" width="420"/>
</p>

**飞桨nnUNet医学图像分割框架，端到端地完成模型的训练和测试全流程分割应用！**

![Build Status](https://github.com/szuboy/paddle-nnUNet/actions/workflows/python-package.yml/badge.svg)
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)
![python version](https://img.shields.io/badge/python-3.0+-orange.svg)
![support os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-yellow.svg)
</div>

## nnUNet

UNet几乎是卷积神经网络在医学图像分割领域的基线模型，同样地出现了许多基于UNet的改进版本，比如：V-Net和UNet++。作为是一种自适应框架，nnUNet无疑是在所有改进和优化模型中最成功的一个。nnUNet已经有[Pytorch版本](https://github.com/MIC-DKFZ/nnUNet) ，而这是对应的飞桨版本。

* **标准化基线**：nnU-Net是生物医学分割中第一个标准化的深度学习基准。在没有人工调参的情况下，研究人员可以在任意数量的数据集上将他们的算法与nnU-Net进行比较，为提出的改进提供有意义的证据。

* **开箱即用的分割方法**：nnU-Net是第一个用于最先进的生物医学分割的即插即用工具。没有分割经验的使用者同样可以开箱即用地使用nnU-Net来解决他们面对的3D分割问题，这是一个无需手动干预的过程。

* **模块化的图像分割框架**：nnU-Net是快速有效开发分割方法的框架。受益于模块化结构，新的体系结构和方法可以很容易地集成到nnU-Net中，使得研究人员可以在一个标准化环境中推出和评估他们的修改。

有关nnU-Net的更多信息，请阅读以下论文：
```
Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2020).
nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature Methods, 1-9.
```


## 使用教程

### 安装

待补充

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
