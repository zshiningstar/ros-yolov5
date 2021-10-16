参考:https://github.com/qianmin/yolov5_ROS
### 1 环境依赖
- conda安装yolov5虚拟环境
   - 参考:
     https://github.com/zshiningstar/yolov5/blob/mydata/README
     
     ```
     pip install netifaces
   ```
### 2 程序运行
- 调用ros自带usb_cam功能包

```
 #enter into your conda env
roslaunch ros_yolo yolo_detect.launch
```


- 调用笔记本摄像头
   - 发布图片话题时相关格式须为:
      - 高度:480
      - 宽度:640
      - step:640*3
    
 - 程序启动
 
```
 #enter into your conda env
roslaunch ros_yolo ego_cam_detect.launch
```

#### 4 自定义msg消息

...