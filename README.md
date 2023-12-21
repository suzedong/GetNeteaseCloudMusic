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