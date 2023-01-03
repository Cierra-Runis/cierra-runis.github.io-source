---
title: 有关 Gitalk 的 403 错误
tags: Gitalk
abbrlink: 32726
date: 2021-10-22 12:34:15
updated: 2023-01-03 10:31:07
---

在此先感谢胡哥哥、魏凯学长以及谢欣泽大佬的帮助~

根据所使用的 `TeXt theme` 的 [官方文档](https://tianqi.name/jekyll-TeXt-theme/docs/zh/quick-start) 的介绍：

> 要想启用 `Gitalk` 作为评论系统，首先你需要一个 `GitHub Application`，如果没有 [点击这里](https://github.com/settings/applications/new) 申请。然后将相应的参数添加到 `_config.yml` 配置中：
>
> ```yaml
> comments:
>   provider: gitalk
>   gitalk:
>     clientID    : "github-application-client-id"
>     clientSecret: "github-application-client-secret"
>     repository  : "github-repo"
>     owner       : "github-repo-owner"
>     admin: # Github repo owner and collaborators, only these guys can initialize github issues, IT IS A LIST.
>       - "your-github-id"
>       - "the-other-admin-github-id"
> ```
>

按照要求，填入如下图的信息

![](https://bu.dusays.com/2023/01/03/63b3e62edfd55.png)

![](https://bu.dusays.com/2023/01/03/63b3e64932213.png)

然后我只能在主页右上角的 `关于` 页面的最下方找到 `Gitalk` 的入口，如下图

![](https://bu.dusays.com/2023/01/03/63b3e656e704f.png)

使用 `Github` 登录后，得下图 `403` 错误

>若想直接解决问题请 [点击跳转](#jump)

![Image](/Image/2021-10-22/bug4.png)

据猜测，这是我的问题，因为有可能把地址填错什么的。经过询问和谢欣泽大佬的排查，首先注意到

```yaml
admin: # Github repo owner and collaborators, only these guys can initialize github issues, IT IS A LIST.
      - "your-github-id"
      - "the-other-admin-github-id"
```

中前面的 `-` 被我丢了，以及 `https://cierra-runis.github.io/Blog114514.github.io/` 后面 `Blog114514.github.io` 为简明起见应在 `Github` 里将项目名改为前面的 `cierra-runis.github.io`，也重新开了一个 `OAuth Apps`

但最后还是回到了 `403` 问题上，看来应该是别的什么。

谢佬在用开发者工具后发现了信息不返回的情况，最后在 `TeXt Theme` 的 [Issue](https://github.com/kitian616/jekyll-TeXt-theme/issues/350) 找到了同样的问题

![](https://bu.dusays.com/2023/01/03/63b3e66b94a66.png)

<span id="jump">根据指引</span>找到了 [这个博客](https://cuiqingcai.com/30010.html)，但根据他最后提供（让我们可以白嫖）的

```yaml
proxy: https://netnr-proxy.cloudno.de/https://github.com/login/oauth/access_token
```

还是没有解决问题，但眼尖一些可以找到

```yaml
proxy: https://cors-anywhere.azm.workers.dev/https://github.com/login/oauth/access_token
```

当当——大功告成，`About` 界面的评论可以使用了

但还有普通页面的呢？

只要在 `markdown` 文件的头部加上

```markdown
key: [你为这个页面的评论区起的名字]
```

即可~
