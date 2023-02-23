## Introduction

VisImages-Detection is an open source visualization detection tool trained from VisImages Dataset, which is a comprehensive visualization dataset built from IEEE VIS publications.
This repo is forked from [MMDetection](https://github.com/open-mmlab/mmdetection), an open source object detection toolbox based on PyTorch. 

## Installation

**Step 1.** Install [MMCV](https://github.com/open-mmlab/mmcv). 
We recommend to install with pip  depending on the type of system, CUDA version, PyTorch version, and MMCV version following the official [documentation](https://mmcv.readthedocs.io/en/latest/get_started/installation.html#install-mmcv-full)

For example, installing MMCV 1.7.0 with cuda 11.7 and torch1.13 can use the following script.
```shell
pip install mmcv-full==1.7.0 -f https://download.openmmlab.com/mmcv/dist/cu117/torch1.13/index.html
```
Installing MMCV 1.7.0 with cpu and torch1.13 can use the following script.
```shell
pip install mmcv-full==1.7.0 -f https://download.openmmlab.com/mmcv/dist/cpu/torch1.13/index.html
```

Or you can install using [MIM](https://github.com/open-mmlab/mim).
```shell
pip install -U openmim
mim install mmcv-full
```

**Step 2.** Install VisImages-Version MMDetection.

```shell
cd visimages-detection
pip install -v -e .
# "-v" means verbose, or more output
# "-e" means installing a project in editable mode,
# thus any local modifications made to the code will take effect without reinstallation.
```

## Inference
We provide some sample codes to run an inference demo for visualization detection.

**Step 1.** We need to download config and checkpoint files from [Google Drive](https://drive.google.com/file/d/1xi62-MxjivDjBAzHxL7OCghH9xOOzaiq/view?usp=sharing) and unzip the file to the `work_dir/` directory.

You will find two files `faster_rcnn_r50_fpn_1x_Visualization_Detect.py` and `visimages-best.pth` in the folder `work_dir/faster_rcnn_r50_fpn_1x_Visualization_Detect/`.

**Step 2.** Verify the inference demo.

Option (a). Run the following command.

```shell
python demo/image_demo.py demo/demo.jpg work_dirs/faster_rcnn_r50_fpn_1x_Visualization_Detect/faster_rcnn_r50_fpn_1x_Visualization_Detect.py work_dirs/faster_rcnn_r50_fpn_1x_Visualization_Detect/visimages-best.pth --device cpu --out-file result.jpg
```

You will see a new image `result.jpg` on your current folder.

Option (b). Open you python interpreter and copy&paste the following codes.

```python
from mmdet.apis import init_detector, inference_detector

config_file = 'work_dirs/faster_rcnn_r50_fpn_1x_Visualization_Detect/faster_rcnn_r50_fpn_1x_Visualization_Detect.py'
checkpoint_file = 'work_dirs/faster_rcnn_r50_fpn_1x_Visualization_Detect/visimages-best.pth'
model = init_detector(config_file, checkpoint_file, device='cpu')  # or device='cuda:0'
inference_detector(model, 'demo/demo.jpg')
```

You will see a list of arrays printed, indicating the detected bounding boxes.

## Training
TODO

## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```
@article{deng2022visimages,
  author={Deng, Dazhen and Wu, Yihong and Shu, Xinhuan and Wu, Jiang and Fu, Siwei and Cui, Weiwei and Wu, Yingcai},
  journal={IEEE Transactions on Visualization and Computer Graphics}, 
  title={{VisImages}: A Fine-Grained Expert-Annotated Visualization Dataset}, 
  year={2022},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/TVCG.2022.3155440}}
```
