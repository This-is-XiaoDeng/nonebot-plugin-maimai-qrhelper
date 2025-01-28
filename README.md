# nonebot-plugin-maimai-qrhelper
**~~实际上这就是一个图片获取插件,但大家就当他是一个能让Bot快捷获取登录二维码图片的插件吧！(bushi)~~**

此插件的灵感来源于[LeiSureLy](https://github.com/LeiSureLyYrsc),由我的好大爹[XiaoDeng](https://github.com/This-is-XiaoDeng/)替我编写了此Nonebot插件！

服务端提供者为[Cdm2883](https://github.com/Cdm2883/)大佬！

服务端/客户端下载地址:[MaimaiHelper](https://github.com/SomeUtils/MaimaiHelper)

BiliBili原视频(旧): <https://bilibili.com/BV1kT421r74M>

> [!IMPORTANT]
> 此插件只能用于私聊，群聊无法获取图片(安全原因)

## 优点
~~MaiMai服务端没有鉴权，因此可以通过Bot代发送图片避免地址的泄露，不需要开放公网端口！~~
(我的Java技术栈朋友很少，所以出现了这个插件）

通过向机器人发送指令快捷获取登录二维码图片，是给亲人好友帮忙签到，在没有微信上的手机出勤的有力插件！

## env.prod变量
自由配置`command_start=[""]`

```env.prod
DRIVER=~fastapi+~websockets+~httpx

#二维码获取地址
qrhelper_get_picurl=["http://127.0.0.1:16643/maimaihelper?token=DO_NOT_USE_DEFAULT_TOKEN"]

#插件主人 只接受来自"123456"的命令
qrhelper_admin=["123456"]

#反向ws地址/端口配置
HOST=0.0.0.0
PORT=8080

#可选正向ws
#ONEBOT_WS_URLS=["ws://127.0.0.1:6700"]
```

## How 2 use?
> [!NOTE]
> 此教程只讲述Onebot-V11适配器的安装

#### 全自动操作（或许吧）-仅限Windows

按顺序点击1 2 3脚本，然后完事

#### 手动操作

1.克隆此仓库

```git
git clone https://github.com/This-is-XiaoDeng/nonebot-plugin-maimai-qrhelper
```

2.在cmd输入以下指令安装pdm包管理工具

```命令提示符(?)
pip install pdm
```

若下载超时，可考虑添加镜像源,以下示例[pip清华源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

```pip清华源
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

3.在仓库目录打开cmd，输入以下内容进行安装

```命令提示符(?)
pdm install
```

4.安装完毕后，输入

```命令提示符(?)
pdm run bot.py
```

就可以成功启动机器人，然后根据自身情况配置env.prod

## 指令

`/getqr` 默认`qrhelper_command`指令

必须填写`qrhelper_admin`才能拥有权限使用此指令

必须填写`command_start`才能响应此命令

指令示例`#getqr 1`(只输入/getqr会报错)

**~~我承认我(LeiSureLy)MarkDown写的很烂，见谅！！！~~**(README modified by [chun-awa](https://github.com/chun-awa))

## LICENSE
此仓库遵循 [MIT License](https://github.com/This-is-XiaoDeng/nonebot-plugin-maimai-qrhelper/blob/main/LICENSE).
