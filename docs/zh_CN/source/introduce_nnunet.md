# 认识 nnUNet

## 为什么是 nnUNet
毫无疑问，UNet<sup>[1](#ref1)</sup> 几乎是卷积神经网络在医学图像分割领域的基线模型，也出现了许多 UNet 的改进版本，
如：V-Net<sup>[2](#ref2)</sup>，UNet++<sup>[3](#ref3)</sup>，nnU-Net<sup>[4](#ref4)</sup>，U2-Net<sup>[5](#ref5)</sup> 等。
但在所有改进版本中，nnUNet 作为是一种自适应框架，使用者只需要输入数据，nnUNet 动根据图像几何结构在网络架构、预训练、训练、推理方向上调整自身结构，
实现全自动分割流程，取得许多分割任务的 SOTA，成为许多创新方法对比的又一个 baseline。

nnUNet 框架下包含了数据预处理、网络框架设计、预测结果后处理、参数自动推理，这是一个深度学习医学图像分割，
甚至是医学图像处理的一个非常好的学习示例，如果你也想来入坑，那就让我们开始吧！

<hr>

## nnUNet 工作流程
不同于自然图像，医学图像含有着许多特有的属性信息，如：模态（X-ray、CT、MRI）、体素大小（SpacingSize）、窗宽窗位（Window Width and Widow Level），
nnUnet 基于图像的这些“**指纹**”来自动推理预处理和网络参数，而这恰恰就是 nnUNet 最迷人的一个重要点，其工作流程：

![avatar](_static/images/nnUNet-workflow.jpg "图1.nnUNet的工作流程")

给定一个新的分割任务，nnUNet 会提取“数据集指纹”（粉红色）；进而，根据“数据指纹”启发式推断的数据相关“基于规则的参数”（绿色）；
最后，根据预定义的“固定参数”（蓝色）来确定训练和测试策略，并确定是否需要后处理的“经验参数”（黄色），自动完成全流程操作！

[comment]: <> (<hr>)

[comment]: <> (## 流程参数)

[comment]: <> (nnUNet 是一个相对臃肿的框架，自动化的流程中有着许多配置的参数，现在来看看每一类别（图像指纹、规则参数、固定参数、经验参数）的详细信息：)


[comment]: <> (#### 图像指纹（Data fingerprint）)

[comment]: <> (提取图像和感兴趣区域 ROI（Region of Interest，ROI）的描述值，建立图像指纹库，以使 nnUNet 在面对不同数据分割任务时，适应数据特有属性，尽可能地发挥出下游模型的最大性能：)

[comment]: <> (- 体素大小的分布（Distribution of spacings）：)

[comment]: <> (- ROI 形状的中值大小（Median shape）：)

[comment]: <> (- ROI 体素的强度分布（Intensity distribution）:)

[comment]: <> (- 图像的模态（Image modality）：)

[comment]: <> (#### 规则参数（Rule-based parameters）)

[comment]: <> (自适应是 nnUNet 的核心创新点，恰恰就是基于图像指纹参数启发式推理图像预处理和模型架构相关的的参数，让数据定义管道，使数据决定模型，即为规则参数：)

[comment]: <> (- 标注采样策略（Annotation resampling strategy）：)

[comment]: <> (- 图像采样策略（Image resampling strategy）：)

[comment]: <> (- 图像采样的体素大小（Image target spacing）：)

[comment]: <> (- 图像归一化策略（Intensity normalization）：)

[comment]: <> (#### 固定参数（Fixed parameters）)

[comment]: <> (nnUNet 流程内部预定义模型架构、模型学习策略、数据扩增方式等固定参数，自动地完成深度学习分割模型的训练测试，规则参数有：)

[comment]: <> (- 网络结构模板（Architecture template）：)

[comment]: <> (- 优化器（Optimizer）：)

[comment]: <> (- 训练步骤（Training procedure）：)

[comment]: <> (- 推理步骤（Inference procedure）：)

[comment]: <> (- 学习率（Learning rate）：)

[comment]: <> (- 数据扩增策略（Data augmentation）：)

[comment]: <> (- 损失函数（Loss function）：)

[comment]: <> (#### 经验参数（Empirical parameters）)

[comment]: <> (经验参数主要使用在预测结果的后处理操作中，进一步优化网络模型预测结果...)

[comment]: <> (- 待补充)

**参考文献**

<div id="reference">
<span id='ref1'>[1] U-net: Convolutional networks for biomedical image segmentation.</span>

<span id='ref2'>[2] V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation.</span>

<span id='ref3'>[3] UNet++: A Nested U-Net Architecturefor Medical Image Segmentation.</span>

<span id='ref4'>[4] nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.</span>

<span id='ref5'>[5] U2-Net: A Bayesian U-Net Model with Epistemic Uncertainty Feedback for Photoreceptor Layer Segmentation in Pathological OCT Scans.</span>
</div>

