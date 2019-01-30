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


![ramen-timer1](https://user-images.githubusercontent.com/38623336/51949798-59eb2d80-2471-11e9-990d-2535f113d7fb.png)

180カウントして停止

![ramen-timer2](https://user-images.githubusercontent.com/38623336/51949799-59eb2d80-2471-11e9-877b-ec59e5466762.png)

#参考
https://github.com/ryuichiueda/robosys2018
