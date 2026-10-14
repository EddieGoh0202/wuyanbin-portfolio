# 吴炎斌 · AI 产品与 Agent 作品集

围绕真实业务问题，展示从产品设计、Agent 编排、工作流到可交互工具的个人实践。

**[访问个人作品集](https://eddiegoh0202.github.io/wuyanbin-portfolio/)**

## 项目一览

| 项目 | 内容 | 入口 |
| --- | --- | --- |
| **班小智 · 智能排班助手** | 自然语言计划确认、约束求解、独立校验与 PDF / CSV 交付 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=scheduler) |
| 产品转型：智能舆情系统 MVP | 自然语言入口、动态工作区与智能服务流程 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=mvp) |
| 舆情智能分析与监测 Agent | AI 主驾、监测方案、事件研判与报告的交互展示 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=opinion) |
| 实验室设备时空地理围栏管理 | 预约、签到、超时释放与通知流程 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=lab) |
| 学生反馈洞察工作流 | 四路分析、17 个节点与图文示例报告 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=feedback) |
| 公众号文章仿写 Agent | 结构学习、参考语料与两篇生成成稿 | [查看案例](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio.html?project=writing) |
| **360 周报生成助手** | 推推日报、日报日历、四种模板与本地历史 | [打开原项目](https://weekly-report-assistant.eai.qihoo.net/) |

## 班小智 · 智能排班助手

[直接体验本地规则版](https://eddiegoh0202.github.io/wuyanbin-portfolio/portfolio-assets/banxiaozhi/demo/index.html)。使用 20 名虚构员工，固定展示 2026-10-12 开始的示例周，可生成班表、核对变更计划、解释安排并导出 PDF / CSV。

- 完整工程将模型理解、计划确认、原子写入、Worker 求解和独立校验分开。
- GitHub Pages 中的体验版使用本地模板理解，不调用后端或模型服务；不包含 API 密钥、访问码与临时隧道。
- 数据仅保存在当前浏览器的独立工作空间；当前校验范围为一周。
- 案例中的 74 项回归与 14 类模型场景来自 2026-10-13 项目留档。模型理解版由作者安排演示。
- 基准样例为 64 人次、512 小时；周五白班临时停业后为 60 人次、480 小时，晚班照常营业。

静态构建快照来自 `banxiaozhi-demo` 的 `e1f96cb9dd2452fafcced6222166635acf8cab37`。展示版本隔离了存储键、移除了模型网关和访问门控，并以相对路径构建。源工程可继续独立迭代。

## 可下载作品集

[下载新版 PDF](portfolio-assets/吴炎斌_作品集_2026.pdf)：16 页，约 2.30 MB（2,304,652 字节），含 7 个项目、可选择文本、目录书签、在线案例链接与二维码。班小智案例占 4 页。

构建脚本位于 `tools/build_portfolio.py`，使用 ReportLab 和 Pillow。Windows 下需安装微软雅黑、宋体；安装依赖后在仓库根目录运行：

```bash
python tools/build_portfolio.py
```

发布前已检查 16 页渲染、中文文本与链接、文件大小、桌面与 390px 窄屏布局，并实测基准生成、停业计划确认、独立校验和 PDF / CSV 下载。

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
