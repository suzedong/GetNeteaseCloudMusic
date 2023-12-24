# GetNeteaseCloudMusic

# 依赖于 [网易云音乐 API](https://github.com/Binaryify/NeteaseCloudMusicApi)
## 环境要求
需要 NodeJS 14+ 环境

## 安装
```
$ git clone git@github.com:Binaryify/NeteaseCloudMusicApi.git
$ cd NeteaseCloudMusicApi
$ npm install
```
或者
```
$ git clone https://github.com/Binaryify/NeteaseCloudMusicApi.git
$ cd NeteaseCloudMusicApi
$ npm install
```
## 运行
调用前务必阅读文档的调用前须知
```
$ node app.js
```
服务器启动默认端口为 3000,若不想使用 3000 端口,可使用以下命令: Mac/Linux
```
$ PORT=4000 node app.js
```
windows 下使用 git-bash 或者 cmder 等终端执行以下命令:
```
$ set PORT=4000 && node app.js
```
# 使用
```
python GetNeteaseCloudMusic.py 汽车音乐 1 10 ~/Downloads/GetMusic
```
# 打包成可在macOS下直接运行的程序
```
# 控制台程序
pyinstaller -F --collect-all pyfiglet GetNeteaseCloudMusic.py

# GUI程序
pyinstaller -F --windowed --collect-all pyfiglet GetNeteaseCloudMusicGUI.py
pyinstaller -F --noconfirm --windowed --collect-all pyfiglet GetNeteaseCloudMusicGUI.py

# GUI程序 带图标
pyinstaller -F --icon=AppIcon.appiconset/MyIcon.icns --noconfirm --windowed --collect-all pyfiglet GetNeteaseCloudMusicGUI.py
```
`pyinstaller -F --windowed --collect-all pyfiglet GetNeteaseCloudMusicGUI.py` 是一个使用 PyInstaller 打包包含 `pyfiglet` 库和 `GetNeteaseCloudMusicGUI.py` 脚本的命令。

具体解释如下：

- `pyinstaller` 是 PyInstaller 的命令行工具，用于将 Python 脚本打包成可执行文件。
- `-F` 参数指定将所有依赖项打包到一个单独的可执行文件中，而不是生成多个文件。
- `--windowed` 参数告诉 PyInstaller 创建一个没有命令行窗口的可执行文件，这意味着它将作为一个 GUI 应用程序运行。
- `--collect-all` 参数告诉 PyInstaller 收集所有的依赖项，包括那些在代码中动态导入的模块。
- `pyfiglet` 是要打包的库或模块的名称。
- `GetMusicGUI.py` 是要打包的 Python 脚本文件的名称。

综合起来，这个命令的目的是将 `GetNeteaseCloudMusicGUI.py` 脚本及其所有依赖项（包括 `pyfiglet` 库）打包成一个独立的可执行文件。打包后的可执行文件将作为一个没有命令行窗口的 GUI 应用程序运行，可以在适当的操作系统上直接运行，而无需安装 Python 和额外的依赖项。

请确保在执行此命令之前已经安装了 PyInstaller，并在命令行中可以访问到它。此外，你还需要在包含 `GetNeteaseCloudMusicGUI.py` 脚本的目录中执行此命令，以确保正确地打包所有依赖项。
