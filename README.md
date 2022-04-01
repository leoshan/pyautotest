# pyautotest

一、安装准备工作（一次性）
	直接官网下载：https://www.python.org/downloads/windows/
	python -m pip install -U pyautogui
	将脚本放到python根目录下面

二、执行过程（第一次执行）
	1、WIN + R : 打开cmd,切换到python执行目录cd python28
	0、python get_mouse_position.py   // 获取刷新、关闭、详情的鼠标坐标，更新到auto.py中
	1、打开浏览器界面全屏，鼠标移动到相应的刷新、关闭、详情的坐标点。
	2、在漂移的确定界面，电脑截图“确定”按钮，保存图像名字为queding.png

三、日常执行
	1、WIN + R : 打开cmd,切换到python执行目录cd python28
	2、输入命令：python auto.py，需要结束按键盘上的Ctrl+C
