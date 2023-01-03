---
title: RenPy 的相关问题
tags: renpy
abbrlink: 25222
date: 2022-01-14 16:46:23
updated: 2023-01-03 10:31:07
---

## 问题

1. ### 所有的对话文件都要放到 script.rpy 文件中吗？

    答：当然不。

    解决方法：例如在 rpy 文件夹下新建 main_story.rpy 文件存放主线剧情，branch_story.rpy 存放主线的分支剧情。

    以下为 script.rpy 的部分代码。

    ```python
    # 开始
    label start:
         # 上略
         jump chapter0 # 这里跳转至main_story.rpy中的chapter0标签
         #
         return
    ```

    以下为 main_story.rpy 的部分代码。

    ```python
    # 这里存放主线剧情

    # 序章
    label chapter0:
    # 上略
         menu :
              "要和说这件事吗？"
              "告诉他吧":
                    $ said_reason = 1
                    call _2_1_A    # 这里跳转至branch_story.rpy中的_2_1_A标签
              "不用告诉":
                    $ said_reason = 0
                    call _2_1_B    # 这里跳转至branch_story.rpy中的_2_1_B标签
         # 下略
         return
    ```

    以下为 branch_story.rpy 的部分代码。

    ```python
    # 这里存放主线的分支剧情

    # 第二章第一个选项
    label _2_1_A:
         # 内容略
         return

    # 第二章第一个选项选A的后加剧情
    label _2_1_A_plus:
         # 内容略
         return
    ```

2. ### 怎么修改程序图标呢？

    答：如下例，在该文件夹下新增 android_foreground.jpg, android_background.jpg, icon.ico

    任务栏的图标 window_icon.png 在 gui 文件夹下：

    ![](https://bu.dusays.com/2023/01/03/63b3e6a2d3177.png)

    其中，前两者大小要求见官方文档，用于安卓安装包和手机桌面的图标；后者大小为 42×42 用于启动游戏 exe 文件的图标。

    这里，我在实践过程中发现我 250×250 的 png 只显示了同心的 160×160 的区域，按这个比例修改即可。

3. ### 手机端和电脑端的界面不一样（甚至不显示头像），如何让手机端显示电脑端的界面？

    答：在 screens.rpy 文件中，将如下内容删除。

    ```python
    ################################################################################
    ## 移动设备界面
    ################################################################################
    
    # 下略
    ```

    将如下内容

    ```python
         if renpy.variant("pc"):
              textbutton _("退出") action Quit(confirm=not main_menu)
         # 中略
         if not renpy.variant("small"):
              add SideImage() xalign 0.0 yalign 1.0
    ```

    改为

    ```python
         textbutton _("退出") action Quit(confirm=not main_menu)
         # 中略
         add SideImage() xalign 0.0 yalign 1.0
    ```

    在 gui.rpy 文件中，将如下内容删除。

    ```python
    ################################################################################
    ## 移动设备界面
    ################################################################################
    
    # 下略
    ```
