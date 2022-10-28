# Judger Core | 评测机内核

### Install | 安装
```bash
sudo apt-get install libseccomp-dev
mkdir build && cd build && cmake .. && make
sudo make install
cd ..  # 回到项目根目录
cd wrapper
sudo python3 setup.py install
```

### Thanks | 鸣谢
QingdaoU/Judger 提供的底层实现
