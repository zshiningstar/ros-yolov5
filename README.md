### 1 环境依赖
- conda安装yolov5虚拟环境
   - 参考:
     https://github.com/zshiningstar/yolov5/blob/mydata/README
     
### 2 程序运行

 - 程序启动
 #enter into your conda env
```
roslaunch ros_yolo ego_cam_detect.launch
```

#### 3 自定义msg消息

 - float32 confidence #置信度
 - Bbox2d bbox        #左上右下坐标位置
 - string label       #标签
 - int32 id           #分类结果,数字代表类别
