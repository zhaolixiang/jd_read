# jd_read
京东阅读 下载已经购买的书籍
未完待续。。

>参考：https://github.com/LoserJL/Screenshot_iPad_to_pdf

## 如何使用
step0: 下载代码, 并安装依赖

```bash
git clone https://github.com/zhaolixiang/jd_read.git
cd jd_read
```

step1:
登录[京东读书](https://e.jd.com/), 拷贝页面 cookie 中的 thor 值, 到 `index.js` 的 `thor` 变量里

![](./assets/step1.jpg)

step2: 在我的已购电子书页面, 点击 "在线阅读" 按钮
![](./assets/step2.jpg)

step3: 记住页面 URL 地址中的 `bookId` 和 `readType` 参数, 例如: `https://cread.jd.com/read/startRead.action?bookId=30506710&readType=3`

程序会自动将导出的章节存储到 `output` 目录.

## 使用说明
+ 此脚本不会保存或者上传你的 Cookie;
+ 如有侵权请联系我删除!

## LICENSE
Apache License