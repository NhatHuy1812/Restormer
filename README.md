# Restormer

A PyTorch implementation of Restormer based on CVPR 2022 paper
[Restormer: Efficient Transformer for High-Resolution Image Restoration](https://arxiv.org/abs/2111.09881).

![Network Architecture](result/structure.png)

## Requirements

- [Anaconda](https://www.anaconda.com/download/)

- [PyTorch](https://pytorch.org)

```
pip install -r requirements.txt
```

## Dataset

Format:
```                           
|-- data     
    |-- SR
        |-- train
            |-- input
                sr-1.jpg
                ...
            `-- output
                sr-1.jpg
                ...
        `-- test                                                        
    |-- DN
        same as SR
```
