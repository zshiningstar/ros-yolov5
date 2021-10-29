参考:https://github.com/qianmin/yolov5_ROS
### 1 环境依赖
- conda安装yolov5虚拟环境
   - 参考:
     https://github.com/zshiningstar/yolov5/blob/mydata/README
     
### 2 程序运行
- 调用ros自带usb_cam功能包
 #enter into your conda env
```
roslaunch ros_yolo yolo_detect.launch
```
- 自建节点
   - 发布图片话题时相关格式须为:
      - 高度:480
      - 宽度:640
      - step:640*3
    
 - 程序启动
 #enter into your conda env
```
roslaunch ros_yolo ego_cam_detect.launch
```

#### 4 自定义msg消息

 - float32 confidence #置信度
 - Bbox2d bbox        #左上右下坐标位置
 - string label       #标签
 - int32 id           #分类结果,数字代表类别
