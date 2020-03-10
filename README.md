# 序言



有学弟来找我说选课很困难，选不到课很难受

作为学长知道之前的选课之痛

所以顺手花了几分钟给学弟写了一个选课脚本



为了确保不滥用，同时为了防止多课程选择导致`DDOS`

设置每次只可以选择一门课，选到后会自动退出



# 反选课机制

由于你川新版教务系统会对没有进行查询就进行`POST`选课操作的选课行为进行精准打击

会请你到教务处喝🍵（现在疫情获取会给你打☎️）

因此本脚本每次选课前都会进行课程查询，以及对于选课`tokenValue`的正则提取

对于剩余课程量大于0的课程才会进行选择

从而绕过了反选课机制



# 错误处理

由于你川的🥔服务器，可能会导致选课过程中某一步没有请求到数值而就将数值`POST`过去

同样会被检测到

所以我在每一步都增加了异常捕捉，如果出现异常就退出当前选课循环，进入新的选课过程中

避免了因服务器的原因而导致被请喝🍵



# Pyhton

本脚本可适用于`Python3.6`环境下，不支持`Python2`环境



# 依赖安装

就两个依赖库就不写`requestsments.txt`文档了

```shell
pip install Pillow
pip install requests
```



# 使用方法

![](https://a2u13-pic.oss-cn-chengdu.aliyuncs.com/pic/20200310164032.png)

配置`config.txt`文件，然后按要求输入即可

即可

> 注意！请确保你要选的课不是限选！
>
> 注意！请确保你要选的课不是限选！
>
> 注意！请确保你要选的课不是限选！
>
> 否则会选课失败！

配置完毕后

![](https://a2u13-pic.oss-cn-chengdu.aliyuncs.com/pic/20200310164323.png)

在`main.py`文件中启动脚本，输入验证码即可开始选课！

他会选择与设置课程号一致的课程进行选择，从而防止了选错课程

选课就是这么简单~



# 最后

有问题可以发`issue`，我看到后会及时回复

如果您觉得本项目对你有帮助的话，可以给本项目一个`star`来鼓励一下~



请学弟学妹合理选课，不要滥用脚本

因本脚本使用而出现的一切法律责任，与作者无关

