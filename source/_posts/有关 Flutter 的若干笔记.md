---
title: 有关 Flutter 的若干笔记
tags: Flutter
abbrlink: 495
date: 2022-11-19 13:13:13
updated: 2023-01-03 10:31:07
---

## `Flutter` 介绍

`Flutter` 是 `Google` 推出并开源的移动应用开发框架，主打跨平台、高保真、高性能。开发者可以通过 `Dart` 语言开发 `App` ，一套代码同时运行在 `iOS` 和 `Android` 平台。`Flutter` 提供了丰富的组件、接口，开发者可以很快地为 `Flutter` 添加 `Native` 扩展。

在此记录些常用资料

> [官方网站](https://flutter.dev/)
>
> [官方英文文档](https://docs.flutter.dev/)
>
> [官方中文文档](https://flutter.cn/docs)
>
> [官方 Package 站](https://pub.dev/)
>
> [Flutter 实战（第二版）](https://book.flutterchina.club/)

## 个人经验

### 使用 `index.dart` 文件简化导入

假定文件目录结构如下

```plaintext
lib
│  index.dart
│  main.dart
│
├─routes
│      index.dart
│      *.dart
│
├─states
│      index.dart
│      *.dart
│
└─widgets
       index.dart
       *.dart
```

则在 `index.dart` 内 `export` 所有子文件夹下的 `index.dart` 文件

```dart
export 'states/index.dart';
export 'routes/index.dart';
export 'widgets/index.dart';
export 'main.dart';
```

在 `routes/index.dart` 内 `export` 所有该文件夹下的 `*.dart` 文件

```dart
export '*.dart';
```

在所有 `*.dart` 文件（包括 `main.dart` 文件）内尽绝大可能 `import 'package:mercurius/index.dart';` 即可简化导入

同时当要引入外部包时，只要在 `index.dart` 文件内导入即可

```dart
// flutter 相关
export 'package:flutter/material.dart';
export 'package:flutter/rendering.dart';

// dart 相关
export 'dart:async';
export 'dart:convert';
export 'dart:math';
export 'dart:io';

// 外部包相关
export 'package:provider/provider.dart';
export 'package:package_info_plus/package_info_plus.dart';
export 'package:dio/dio.dart';
```

#### 构建号错误问题

`Flutter` 使用 `android/app/build.gradle` 来打包 `apk` ，且其引入了 `flutter.gradle` 如 `D:/flutter/packages/flutter_tools/gradle/flutter.gradle`

约在 `flutter.gradle` 的 `810` 行

```gradle
def addFlutterDeps = { variant ->
            if (shouldSplitPerAbi()) {
                variant.outputs.each { output ->
                    def abiVersionCode = ABI_VERSION.get(output.getFilter(OutputFile.ABI))
                    if (abiVersionCode != null) {
                        output.versionCodeOverride =
                            abiVersionCode * 1000 + variant.versionCode
                    }
                }
            }
```

我们知道 `Flutter` 将判断是否使用了 `split-per-abi` 命令, 是则在 `ABI_VERSION` 选择一个版本 `*1000` 再加上构建号

官方解释见 [此处](https://developer.android.com/studio/build/configure-apk-splits)

我们只需修改 `ABI_VERSION` `map` 如下

```gradle
private static final Map ABI_VERSION = [
    (ARCH_ARM32)        : 0,
    (ARCH_ARM64)        : 0,
    (ARCH_X86)          : 0,
    (ARCH_X86_64)       : 0,
]
```

## 感想

- `Flutter` 的使用非常简单，上手也快，非常有意思

- 自己写了个 `Flutter` 项目，这里是发布用仓库 [mercurius warehouse](https://github.com/Cierra-Runis/mercurius_warehouse)
