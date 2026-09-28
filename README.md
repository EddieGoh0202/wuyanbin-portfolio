# 吴炎斌 · AI 产品与 Agent 作品集

围绕真实业务问题，展示从产品设计、Agent 编排、工作流到可交互工具的个人实践。

**[访问个人作品集](https://eddiegoh0202.github.io/wuyanbin-portfolio/)**

## 项目一览

| 项目 | 内容 | 入口 |
| --- | --- | --- |
| 产品转型：智能舆情系统 MVP | 自然语言入口、动态工作区与智能服务流程 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=mvp) |
| 舆情智能分析与监测 Agent | AI 主驾、监测方案、事件研判与报告的交互展示 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=opinion) |
| 实验室设备时空地理围栏管理 | 预约、签到、超时释放与通知流程 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=lab) |
| 学生反馈洞察工作流 | 四路分析、17 个节点与图文示例报告 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=feedback) |
| 公众号文章仿写 Agent | 结构学习、参考语料与两篇生成成稿 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=writing) |
| **360 周报生成助手** | 推推日报、日报日历、四种模板与本地历史 | [打开原项目](https://weekly-report-assistant.eai.qihoo.net/) |

## 360 周报生成助手

从日常办公中的日报整理需求出发，将“记录 → 汇总 → 编辑 → 交付”做成一个轻量工具：

- 按日历记录与编辑日报，选择一周内容生成周报。
- 无需 API 时，使用简洁清单、目标进展、成果亮点等规则模板。
- 可选本机 WisCode / 推推桥接，连接本人电脑上的账号。
- 日报与周报历史保存在当前浏览器，不跨设备同步。

原项目保留完整的本机桥接能力：推推自动读取与经典模板生成依赖本机登录状态和桥接服务；日报与周报历史保存在当前浏览器。该工具是个人项目，不是 360 官方产品。

## 展示说明

本仓库是静态作品集，通过 GitHub Pages 发布。部分项目提供交互原型或本地样例，真实业务采集、模型调用与业务写入需要对应服务和授权。展示材料与参考语料的来源、功能边界以各项目说明为准。

## 本地预览

使用任意静态 HTTP 服务，例如在仓库目录运行：

```bash
python3 -m http.server 8080
```

在浏览器打开 `http://localhost:8080`。主页为 `index.html`，案例数据与弹窗交互在 `portfolio.js`，样式在 `portfolio.css` 和 `portfolio-media.css`。

## 联系

吴炎斌 · AI 产品与 Agent 实践  
邮箱：wyb18959209440@163.com
