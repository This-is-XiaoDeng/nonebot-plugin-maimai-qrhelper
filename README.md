# nonebot-plugin-maimai-qrhelper

***~~实际上这就是一个图片获取插件,但大家就当他是一个能让Bot快捷获取登录二维码图片的插件吧！(bushi)~~***

此插件的灵感来源于[LeiSureLy](https://github.com/LeiSureLyYrsc),由我的好大爹[XiaoDeng](https://github.com/This-is-XiaoDeng/)替我编写了此Nonebot插件！

服务端提供者为[Cdm2883](https://github.com/Cdm2883/)大佬！

[BiliBili原视频](https://bilibili.com/BV1kT421r74M)

## Documentation

See [Docs](https://nonebot.dev/)

## env.prod变量
***必须*****command_start=[""]**

**qrhelper_get_picurl=["http://127.0.0.1:16643/get-qr"]**
可多个填写,用','分割,递进顺序为1,2,3,4......

**qrhelper_admin=[""]**

**qehelper_command=[""]**
**↑默认getqr**

## How 2 use?
1.根据[Nonebot快速上手](https://nonebot.dev/docs/quick-start)安装Nonebot脚手架
2.驱动器选择:**fastapi**,**httpx**
(如需正向ws请添加**websockets**)
3.适配器选择:**Onebot V11**
4.依赖/虚拟环境全部写***y***然后回车
5.在Bot文件夹打开终端,输入**nb plugin install nonebot_plugin_alconna**
6.打开文件夹中的**pyproject.yaml**,修改其中的:
**plugins_dir=["plugins"]**
然后在文件夹中创建名为**plugins**的文件夹
7.放入本仓库的**nonebot_plugin_maimai_helper**到**plugins**里
8.回到根目录,填写**env.prod**变量信息,填写完后,打开终端,输入**nb run**打开Bot
9.大功告成！

## 指令
**getqr** 默认**qrhelper_command**指令
必须填写**qrhelper_admin**才能拥有权限使用此指令
必须填写**command_start**才能响应此命令
比如 #getqr 1/2/3/4等 

**~~我承认我(LeiSureLy)MarkDown写的很烂，见谅！！！~~**

## LICENSE

此仓库遵循**MIT**开源协议
