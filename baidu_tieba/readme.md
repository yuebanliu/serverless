> 通过腾讯scf(serverleess cloud function )来实现百度贴吧的定时签到

代码来自[https://github.com/LiteraturePro/Serverless-Python](https://github.com/LiteraturePro/Serverless-Python)

## 执行环境

[腾讯云函数](https://cloud.tencent.com/product/scf)

#### 创建应用
控制台->函数服务->自定义创建->[事件函数、python3.6、在线编辑、高级配置->[内存64M、执行超时时间15]]->确定

#### 编辑代码

进入函数管理->函数代码

将index.py的代码拷贝粘贴进去替换原来的代码

#### 补充配置

将代码中的 `sckey` 、`tbs` 、`cookie`补充，就可以部署运行，查看结果了

#### 创建定时器

为了让云函数每天定时执行

切换到 触发管理-> 创建触发器->触发周期改为自定义`55 3 * * *`->提交

自定义的是一个crontab定时器，上面是指每天3点55触发执行。


## server酱推送

[server酱](https://sct.ftqq.com/)

对云函数执行结果进行推送，推到微信，具体去上面地址查看