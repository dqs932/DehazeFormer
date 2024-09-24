# DehazeFormer
论文：小波DehazeFormer网络的道路交通图像去雾

Paper：Wavelet dehazeformer network for road traffic image dehazing method

DOI:10. 37188/OPE.20243212.1915

Authors: Xia Ping, Li Ziyi, Lei Bangjun, ea al.

## Experimental environment and datasets（实验环境与数据集）
1 NVIDIA GeForce RTX3090 (24G)
Ubuntu20. 04, python3.8

Dadasets：Foggy_Cityscapes, 4K-HAZE, and DKITTI

## Acknowledgement(致谢)

本论文的实验数据得到了三峡大学先进计算中心的计算支持和帮助，在此表示诚挚感谢。

The numerical calculation of this paper is supported and assisted by the Advanced Computing Center of China Three Gorges University.

### Highlight

1. Network

![image](https://github.com/user-attachments/assets/a31ff7b4-8265-4c48-a808-1e3be80f6014)
![image](https://github.com/user-attachments/assets/76b26efc-eded-42ab-9444-958820d5b99a)

### OTB / UAV123 / DTB70 / TColor128 / NfS

| Dataset       | Success Score    | Precision Score |
|:-----------   |:----------------:|:----------------:|
| OTB2013       | 0.589            | 0.781            |
| OTB2015       | 0.578            | 0.765            |
| UAV123        | 0.523            | 0.731            |
| UAV20L        | 0.423            | 0.572            |
| DTB70         | 0.493            | 0.731            |
| TColor128     | 0.510            | 0.691            |
| NfS (30 fps)  | -                | -                |
| NfS (240 fps) | 0.520            | 0.624            |


## Installation

Install Anaconda, then install dependencies:

```bash
# install PyTorch >= 1.0
conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
# intall OpenCV using menpo channel (otherwise the read data could be inaccurate)
conda install -c menpo opencv
# install GOT-10k toolkit
pip install got10k
```

## Training the tracker

1. Setup the training dataset in `tools/train.py`. Default is the GOT-10k dataset located at `~/data/GOT-10k`.

2. Run:

```
python tools/train.py
```

## Evaluate the tracker

1. Setup the tracking dataset in `tools/test.py`. Default is the OTB dataset located at `~/data/OTB`.

2. Setup the checkpoint path of your pretrained model. Default is `pretrained/siamfc_alexnet_e50.pth`.

3. Run:

```
python tools/test.py
```

## Running the demo

1. Setup the sequence path in `tools/demo.py`. Default is `~/data/OTB/Crossing`.

2. Setup the checkpoint path of your pretrained model. Default is `pretrained/siamfc_alexnet_e50.pth`.

3. Run:

```
python tools/demo.py
```
