# 更新日志

2021.12.28 更新学期号

2021.09.13 添加选课时间段

2021.06.22 更新学期号，同时增加多选课

2020.12.29 增加验证码识别功能，修改学期号

2020.6.19 新增GPL3.0协议，使用规范见下文使用须知条例

2020.6.12 修复部分错误，增加异常输出，方便排查错误

2020.6.11 修复 2020 年 6 月选课失败的错误

# 使用须知

- 本项目只适用于编程学习用途，不得用于实际选课阶段，请在下载后24小时内删除！
- 不得随意传播本项目至任何公开场合（包括但不限于QQ群、微信群、贴吧论坛等）
- 因用户使用或修改项目源码而产生的一切责任与本人无关，本人不负任何连带责任
- 若不同意以上使用条例，请停止clone本项目并不得通过任何途径使用本项目
- 本项目源码以及条例解释权归本人所有


# 序言

有学弟来找我说选课很困难，选不到课很难受

作为学长知道之前的选课之痛

所以顺手花了几分钟给学弟写了一个选课脚本

# 反选课机制

由于你川新版教务系统会对没有进行查询就进行`POST`选课操作的选课行为进行精准打击

会请你到教务处喝 🍵

因此本脚本每次选课前都会进行课程查询，以及对于选课`tokenValue`的正则提取

对于剩余课程量大于 0 的课程才会进行选择

从而绕过了反选课机制

# 错误处理

由于你川的 🥔 服务器，可能会导致选课过程中某一步没有请求到数值而就将数值`POST`过去

同样会被检测到

所以我在每一步都增加了异常捕捉，如果出现异常就退出当前选课循环，进入新的选课过程中

避免了因服务器的原因而导致被请喝 🍵

# Pyhton

本脚本可适用于`Python3.6`环境下，不支持`Python2`环境

# 依赖安装

就三个依赖库就不写`requestsments.txt`文档了

如果不需要验证码自动识别功能则无需安装`muggle_ocr`库

```shell
pip install Pillow
pip install requests
pip install muggle_ocr
```
>目前muggle_ocr已经无法通过官方pip安装，请通过豆瓣源安装 `pip install muggle_ocr -i https://pypi.douban.com/simple/`
# 使用方法

每个新学期使用，请务必在`config.py`文件中修改学期号，即修改`selectcourse_xueqi`变量！！！格式为`"2021-2022-1-1"`分为四段，前两段是学年，第三段是学期号，秋季为1，春季为2，最后一段无实际意义，保留为1即可。

配置`config.txt`文件，然后按要求输入即可

![](images/demo.png)

例如：

```
2077777777777
666666
摸鱼学导论;面向GitHub程序设计
114514;1919810
01 02 03 04 05 06 07 08 09;10
9:30 21:59
```
课程之间用 `;` 隔开，单门课程课序号用 `空格` 隔开，注意不要有多余的空格，否则可能会导致选课失败。
最后一行是设置选课时间，时间用空格隔开~~暂时未支持多门课分别的选择时段~~

> 注意！请确保你要选的课不是限选！（同时保证信息正确）
>
> 注意！请确保你要选的课不是限选！（同时保证信息正确）
>
> 注意！请确保你要选的课不是限选！（同时保证信息正确）
>
> 否则会选课失败！

配置完毕后

![](https://a2u13-pic.oss-cn-chengdu.aliyuncs.com/pic/20200310164323.png)

> 最好在命令行下运行`python main.py`，会极大减少出现字符编码的错误的情况
>
> 比如`UnicodeEncodeError: 'ascii' codec can't encode characters in position`等错误

他会选择与设置课程号和课序号一致的课程进行选择，从而防止了选错课程

如果选课结果显示`ok`，但在教务系统没有出现这门课，请稍等片刻刷新即可

出现`result:ok`是肯定选中课程了的

选课就是这么简单~

# 最后

有问题可以发`issue`，我看到后会及时回复

如果您觉得本项目对你有帮助的话，可以给本项目一个`star`来鼓励一下~
