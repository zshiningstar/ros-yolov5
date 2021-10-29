### 一.检测代码参数详解
* 1.weights: 指定网络模型,对应的V5.0版本的网络模型:https://github.com/ultralytics/yolov5/releases/tag/v5.0;训练模型输入
* 2.source:是输入的来源,当其是文件夹时,此文件夹下的所有图片都会被处理并保存;只检测单张图片时,输入为这个照片的路径;视频也可以检测:输入视频路径,可以输入youtube视频连接直接检测;
* 3.image-size:指定图像大小,在训练时对图片进行缩放为指定大小,训练结束输出时还原;
* 4.conf:置信度,即当我检测的这个区域时,只有可信度大于设置的阈值时才会显示将其框出来;
* 5.iou置信度:检测时,一个物体有多个框,iou置信度将取出最优的框将其显示,iou=1时全部重合,大于此阈值的框时提取一个最优的框;
* 6.device:使用的设备

* 7.view-img:命令行后加上这个,运算后会直接显示结果

* 8.classes:只想要某一个类别时,命令行后加--classes 0:只检测某个类别
* 9.augment:增强检测
* 10.project:运行结果保存在哪里

### 二.训练yolov5神经网络
#### (1) 本地训练yolov5
* 1.weights:不指定,默认设置为空;
* 2.cfg: 模型的结构采用什么;
* 3.data:指定的训练数据集;
* 4.hyp: 超参数;
* 5.epochs:轮数;
#### (2) 云端GPU训练yolov5
云端GPU:google colab:  https://colab.research.google.com/?utm_source=scs-index
* 上传yolov5代码压缩包,在里面解压: !unzip 名字 -d 路径
* 安装:pip install -r requirments.txt
* 加载tensorboard: %load_ext tensorboard
* 启动tensorboard：%tensorboard --logdir=runs/train
* 开始训练：!python train.py --rect（最后训练好的模型都在runs文件夹下）

### 三.自制数据集并训练
#### (1) 标注
* 在线标注工具： https://www.makesense.ai/ 标注结束导出即可
* 创建对应结构文件夹 ![image](https://user-images.githubusercontent.com/53174131/135563959-5dfac001-1fbf-4567-aaca-f61d5cc47a72.png)
#### (2) yaml数据集文件创建
* ----
#### (3) 更改训练程序路径进行训练即可
