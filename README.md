# ros_ramen-timer
ロボットシステム学課題２
rosbridgeを用いてwebブラウザに180秒カウントするタイマーを表示する

#実行方法
```bash
$ sudo apt install ros-kinetic-rosbridge-suite
$ cd ~/catkin_ws/src
$ git clone https://github.com/Kazuma0716/ros_ramen-timer.git
$ cd ~/catkin_ws
$ catkin_make
$ roslaunch ros_ramen-timer ramen-timer.launch
```
インターネットブラウザで$ http://ラズパイのIPアドレス:8000 にアクセス


