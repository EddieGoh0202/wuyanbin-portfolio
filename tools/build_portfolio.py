"""Regenerate the 16-page portfolio using vector text and compressed screenshots.
Usage: bundled Python tools/build_portfolio.py [output.pdf]
Requires reportlab, Pillow and Chinese TrueType fonts (Microsoft YaHei/SimSun on Windows).
"""
from pathlib import Path
from io import BytesIO
import sys,json,html,shutil
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'portfolio-assets';B=ASSETS/'banxiaozhi'
OUT=Path(sys.argv[1]) if len(sys.argv)>1 else ASSETS/'吴炎斌_作品集_2026.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
for name,path in [('Sans','C:/Windows/Fonts/msyh.ttc'),('Bold','C:/Windows/Fonts/msyhbd.ttc'),('Serif','C:/Windows/Fonts/simsun.ttc'),('Mono',str(ASSETS/'fonts/dm-mono-400.ttf'))]:
 pdfmetrics.registerFont(TTFont(name,path))
W,H=960,675;M=44;TOTAL=16
INK='#18302b';MUTED='#65756d';PAPER='#f4f2eb';LINE='#d6dcd2';LIME='#c9ef79';GREEN='#17312b';WHITE='#fffefa';BLUE='#e5eafa';ORANGE='#b46e37'
SITE='https://eddiegoh0202.github.io/wuyanbin-portfolio/'
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle('吴炎斌 | AI 产品与 Agent 作品集 | 2026');c.setAuthor('吴炎斌');c.setSubject('7 个项目样本，含班小智智能排班助手')
PAGE=0;warnings=[];images={}
def color(v):return HexColor(v)
def rect(x,y,w,h,fill,stroke=None,r=0):
 c.setFillColor(color(fill));c.setStrokeColor(color(stroke or fill));c.setLineWidth(.6)
 if r:c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=bool(stroke))
 else:c.rect(x,H-y-h,w,h,fill=1,stroke=bool(stroke))
def line(x,y,x2,y2,col=LINE,lw=.7):
 c.setStrokeColor(color(col));c.setLineWidth(lw);c.line(x,H-y,x2,H-y2)
def text(value,x,y,size=13,font='Sans',col=INK):
 value=value.replace('—','-').replace('–','-').replace('−','-');c.setFillColor(color(col));c.setFont(font,size);c.drawString(x,H-y-size*.83,value)
 if x+pdfmetrics.stringWidth(value,font,size)>W-25:warnings.append((PAGE,'text-right',value))
 if y+size>625 and y<635:warnings.append((PAGE,'text-bottom',value))
def para(value,x,y,w,size=13,col=MUTED,font='Sans',leading=None,maxh=None):
 value=value.replace('—','-').replace('–','-').replace('−','-')
 style=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.65,textColor=color(col),wordWrap='CJK')
 p=Paragraph(html.escape(value).replace('\n','<br/>'),style);pw,ph=p.wrap(w,1000)
 if maxh and ph>maxh:warnings.append((PAGE,'paragraph-height',value[:25],ph,maxh))
 if y+ph>615:warnings.append((PAGE,'paragraph-bottom',value[:25],y+ph))
 p.drawOn(c,x,H-y-ph);return ph

def label(value,x,y,col=MUTED):text(value,x,y,9,'Sans' if any(ord(ch)>127 for ch in value) else 'Mono',col)
def frame(path,x,y,w,h,bg=WHITE,border=True,pad=9):
 path=Path(path)
 if not path.exists():raise FileNotFoundError(path)
 key=(str(path),1800)
 if key not in images:
  im=Image.open(path).convert('RGB');im.thumbnail((1800,1800),Image.Resampling.LANCZOS);buf=BytesIO();im.save(buf,'JPEG',quality=87,optimize=True);images[key]=(ImageReader(buf),im.size)
 ir,(iw,ih)=images[key];rect(x,y,w,h,bg,LINE if border else None)
 scale=min((w-pad*2)/iw,(h-pad*2)/ih);dw=iw*scale;dh=ih*scale
 c.drawImage(ir,x+(w-dw)/2,H-y-(h+dh)/2,dw,dh,mask='auto')
def button(value,url,x,y,w=180,dark=False):
 rect(x,y,w,34,LIME if dark else WHITE,None if dark else LINE,r=3);text(value,x+12,y+10,11,'Sans',INK)
 c.linkURL(url,(x,H-y-34,x+w,H-y),relative=0,thickness=0)
def metric(x,y,number,name,detail='',w=190):
 text(number,x,y,38,'Bold');text(name,x,y+49,12,'Bold');para(detail,x,y+70,w,10,maxh=55)
def note(value,y=598):para(value,M,y,W-M*2,8.5,col=MUTED,leading=13,maxh=27)
def base(section,dark=False,bookmark=None):
 global PAGE
 PAGE+=1;rect(0,0,W,H,GREEN if dark else PAPER);fg='#b3c3b1' if dark else MUTED;ln='#3a5144' if dark else LINE
 label('WYB / PORTFOLIO',M,25,fg);label(section,520,25,fg);line(M,49,W-M,49,ln)
 line(M,631,W-M,631,ln);label('WU YANBIN / AI PRODUCT & AGENT',M,649,fg);label(f'{PAGE:02} / {TOTAL:02}',870,649,fg)
 if bookmark:c.bookmarkPage(bookmark);c.addOutlineEntry(section,bookmark,level=0,closed=False)
def end():c.showPage()
def heading(kicker,title,summary):
 label(kicker,M,77,ORANGE);text(title,M,101,32,'Bold');para(summary,M,147,870,13,maxh=42)
def block(x,y,kicker,title,body,w=267):
 label(kicker,x,y,ORANGE);text(title,x,y+24,20,'Bold');return para(body,x,y+59,w,13,maxh=105)
# 01 / COVER
base('SELECTED WORK / 2024-2026',True,'cover')
for rr in [160,220,280]:
 c.setStrokeColor(color('#405744'));c.setLineWidth(.5);c.circle(750,H-310,rr,stroke=1,fill=0)
label('AI PRODUCT / AGENT BUILDER',M,97,LIME);text('吴炎斌',M,139,65,'Serif',WHITE)
text('把复杂业务流程，',M,249,30,'Serif',WHITE);text('做成可交付的智能服务。',M,301,30,'Serif',LIME)
para('连接业务理解、智能体编排、Prompt 评测与前端 MVP，\n把想法推进到可用、可评估、可展示。',M,373,425,14,'#b3c3b1',maxh=63)
frame(B/'workspace.jpg',528,162,387,287,bg='#52664d',border=False,pad=11)
rect(641,426,275,92,LIME);label('FROM INSIGHT TO DELIVERY',657,440,INK);text('07',657,463,43,'Bold');text('个项目样本',741,481,15)
label('PERSONAL PORTFOLIO',M,508,LIME);text('AI 产品与 Agent 作品集',M,540,25,'Serif',WHITE)
text('中国农业大学 · 农艺与种业硕士',M,587,11,'Sans','#b3c3b1');text('2026',800,558,39,'Mono','#b3c3b1');end()
# 02 / PROFILE + INDEX
base('PROFILE / CONTENTS',bookmark='profile');heading('PROFILE','业务理解 × 智能体产品化','农学背景让我习惯在复杂约束中找规律，计算机辅修和产品实践让我把规律变成工具。')
block(M,224,'EDUCATION','中国农业大学','农艺与种业硕士\nGPA 3.54/4.00 · 预计 2027.06 毕业',345)
block(M,362,'EXPERIENCE','360 安全科技','AI 产品实习生 · 舆情方向\n2025.09-至今 · 参与 SaaS 向 Agent Teams 升级',345)
para('AI 产品设计 / Agent Workflow / Prompt 评测\nFigma / Axure / Python / React / Vite',M,522,385,12,maxh=48)
label('SELECTED PROJECTS',510,195)
items=[('07','班小智 · 智能排班助手','03-06','scheduler'),('01','智能舆情系统 MVP','07-08','mvp'),('02','舆情分析与监测 Agent','09','opinion'),('03','实验室设备管理','10','lab'),('04','学生反馈洞察工作流','11-12','feedback'),('05','公众号文章仿写 Agent','13','writing'),('06','360 周报生成助手','14','weekly')]
for i,(num,title,pages,dest) in enumerate(items):
 y=224+i*50;line(510,y+38,916,y+38);label(num,510,y+8,ORANGE);text(title,546,y+5,14,'Bold');label(pages,864,y+9);c.linkRect('',dest,(510,H-y-35,916,H-y+5),relative=0,thickness=0)
note('新增重点案例置于前部；项目编号与个人网站一致。更新：2026-10-14。');end()
# 03 / SCHEDULER OVERVIEW
base('CASE 07 / AGENT PRODUCT',bookmark='scheduler');heading('07 / BANXIAOZHI · NEW','班小智 · 智能排班助手','让门店的每次排班，成为一份有依据、可确认、能交付的安排。')
rect(M,196,270,26,BLUE,r=3);text('个人项目 / 2026.10 / React + TypeScript',M+10,204,10)
block(M,250,'THE PROBLEM','多种约束，一张班表','人数、岗位技能、请假、可用时间与工时上限相互影响；临时变化又让手工改表反复返工。')
block(M,417,'MY CONTRIBUTION','把需求落成运行闭环','完成业务规则拆解、交互设计、Agent 计划协议、约束求解、校验解释与结果导出。')
frame(B/'workspace.jpg',350,196,566,366,pad=9);label('PRODUCT / 对话与每周排班同屏',350,574)
button('直接体验本地规则版',SITE+'portfolio-assets/banxiaozhi/demo/index.html',M,555,240,True)
note('真实产品截图，20 名虚构员工；静态体验使用本地模板理解，模型版由作者安排演示。');end()
# 04 / ARCHITECTURE
base('CASE 07 / UNDERSTANDING TO EXECUTION');heading('07 / SYSTEM DESIGN','需求先确认，班表再求解。','将理解、写入、求解和校验分开，让管理员始终看得见系统将做什么。')
steps=[('01','理解需求','自然语言 / 结构化编辑','整理员工、日期、班次与人数技能要求'),('02','确认计划','白名单与语义校验','变更摘要明确；确认后原子保存'),('03','约束求解','Worker 多轮启发式搜索','满足硬规则，再兼顾偏好与原安排'),('04','核验交付','独立规则校验','解释依据、量化缺口、导出结果')]
for i,(n,t,tag,body) in enumerate(steps):
 x=M+i*223;rect(x,213,205,209,WHITE,LINE);label(n,x+15,229,ORANGE);text(t,x+15,259,21,'Bold');text(tag,x+15,307,11,'Bold');para(body,x+15,340,175,12,maxh=64)
 if i<3:text('>',x+210,299,13,'Mono',MUTED)
rect(M,454,416,117,BLUE);label('MODEL / 理解边界',M+16,469);para('模型输出结构化工具计划，不直接决定员工在哪天上班；存在歧义或未支持要求时，先澄清。',M+16,493,382,12,maxh=60)
rect(480,454,436,117,LIME);label('RULES / 决策依据',496,469);para('每日单班、请假禁排、人数与技能下限、工时、连续工作及晚接早由求解器处理，并再次独立检查。',496,493,404,12,col=INK,maxh=60)
note('实现参考：当前工程架构与 Agent 调用文档。多轮启发式搜索不保证全局最优；当前只校验本周配置。');end()
# 05 / TEMPORARY CHANGE
base('CASE 07 / CHANGE WITH CONFIRMATION');heading('07 / SCENARIO VALIDATION','临时变化，只改它影响的班次。','“制冰机故障，本周五白班停业，不安排任何员工，晚班正常，请重新排班。”')
frame(B/'confirmation.jpg',M,202,546,369,pad=8);label('PRODUCT / 明确日期与班次的待确认计划',M,583)
block(624,208,'01 / INTERPRET','定位具体影响','2026-10-16 早 / 白班关闭；其他日期与晚班照常营业。',285)
block(624,343,'02 / CONFIRM','管理员核对后执行','将变化展示成待确认计划；确认后保存，旧班表标记过期，再求解。',285)
rect(624,491,292,82,LIME);text('64 → 60',639,507,30,'Bold');text('全周人次 / 关闭 1 个平日班',639,549,11)
note('2026-10-13 留档案例：周五白班 0 人、晚班 4 人，本周硬错误 0。恢复营业后重新排班。');end()
# 06 / OUTPUT + EVALUATION
base('CASE 07 / DELIVERY & EVIDENCE');heading('07 / SHIP & VERIFY','结果带得走，依据查得到。','按人展示班次与工时，按班次检查人数与技能覆盖，提供 PDF / CSV 和安排说明。')
frame(B/'schedule-report.png',M,196,485,338,pad=6);label('DELIVERY / 2026-10-12 至 10-18 示例周',M,544)
for x,y,n,name,detail in [(569,201,'64','安排人次','20 名虚构员工的示例周'),(763,201,'512h','本周工时','本周硬冲突与覆盖缺口 0'),(569,352,'74','自动回归','2026-10-13 留档测试'),(763,352,'14','真实模型场景','首轮 13/14，超时项重试通过')]:metric(x,y,n,name,detail,w=155)
para('缺口存在时交付明确标记的候选方案，并给出借调、补员或需求协商建议；加班需要员工同意与管理员确认。',569,508,347,12,maxh=65)
button('下载完整排班样例',SITE+'portfolio-assets/banxiaozhi/schedule-sample.pdf',M,560,215,True)
note('数字对应特定样例与留档范围。当前无跨周历史校验、多人同步或劳动法规认证；静态体验不调用模型。',y=602);end()
# 07 / MVP
base('CASE 01 / PRODUCT MVP',bookmark='mvp');heading('01 / PRODUCT TRANSFORMATION','智能舆情系统 MVP','围绕“自然语言入口 + 动态工作区”，把监测、事件、风险与报告组织成一条交付链。')
block(M,211,'THE PROBLEM','用户需要业务结果','传统 SaaS 功能与页面较多，用户仍需自己理解流程、配置任务并拼接结果。')
block(M,393,'MY CONTRIBUTION','重组场景与交付路径','参与转型方向、核心场景优先级、Agent 工作流与动态工作区设计。')
frame(B/'reference-mvp.png',350,202,566,352,pad=8);label('PRODUCT DEMO / 日常监测与风险卡片',350,568)
button('打开在线原型',SITE+'智能服务版-双视角-Agent Teams的副本.html?demo=1',M,560,208,True)
note('前端演示原型。线索、事件与研判内容使用样例材料；素材沿用原版作品集与个人网站。');end()
# 08 / MVP EXPERIENCE
base('CASE 01 / EXPERIENCE SYSTEM');heading('01 / FROM TOOLS TO SERVICES','一句话需求，成为一条任务链。','将系统能力组织在同一条路径上，让用户看见依据、参与确认，并带走完整结果。')
for i,(n,title,tag,body) in enumerate([('01','理解任务','自然语言输入','识别用户意图与业务约束'),('02','组织执行','Supervisor 编排','将任务分配给专业 Worker'),('03','形成判断','证据与风险同屏','展示来源、研判与关键线索'),('04','交付结果','动态工作区','承接方案、事件与报告')]):
 x=M+i*223;label(n,x,228,ORANGE);text(title,x,268,23,'Bold');text(tag,x,318,12,'Bold');para(body,x,350,195,13,maxh=58)
line(M,427,916,427);label('WORKSPACES',M,452)
for i,(title,desc) in enumerate([('日常监测','持续看见线索'),('专项监测','围绕任务配置'),('事件研判','追踪事件进展'),('成果中心','沉淀可交付材料')]):
 x=M+i*223;rect(x,482,205,82,WHITE,LINE);text(title,x+15,498,20,'Bold');text(desc,x+15,535,11)
note('设计提炼基于原版作品集、网站介绍与公开原型；该页呈现产品结构。');end()
# 09 / OPINION
base('CASE 02 / AGENT ENGINEERING',bookmark='opinion');heading('02 / SUPERVISOR + WORKERS','舆情智能分析与监测 Agent','React + Python 工程：用对话调度用户画像、监测方案编辑、事件研判与报告工作区。')
metric(M,208,'16','个 Worker','后端默认注册数量，沿用已核实的项目记录。',240)
text('让任务可追踪、可接管',M,365,22,'Bold');para('围绕业务需求组织对话入口与协同工作区，串起编辑、确认、研判与交付。\n\n画像提取 / 意图识别\n风险扫描 / 专家配置\n事件分析 / 结构化报告',M,408,270,12,maxh=150)
frame(B/'reference-opinion.png',350,202,566,357,pad=9);label('PRODUCT / 监测方案编辑与双栏协作',350,573)
note('公开展示版复用真实前端并使用固定本地样例；采集、模型分析与业务写入依赖后端及授权。');end()
# 10 / LAB
base('CASE 03 / MINI PROGRAM',bookmark='lab');heading('03 / SCENARIO-BASED PRODUCT','实验室设备时空地理围栏管理','将预约、到场签到、超时释放和通知串成闭环，减少共享设备管理中的人工追踪。')
metric(M,216,'300m','到场签到规则','梳理状态与异常分支，设计定位校验、防作弊、释放与通知流程。',300)
label('STATE MACHINE',M,406)
for i,s in enumerate(['预约中','待签到','使用中','已释放']):
 x=M+i*98;rect(x,441,84,33,WHITE,LINE,r=3);text(s,x+13,451,12)
para('到场校验通过后进入使用；超时则释放设备并提醒。',M,499,365,13,maxh=65)
frame(B/'reference-lab.png',455,206,208,373,pad=8);label('DEMO / 预约成功',455,586)
for y,n,t in [(212,'+42%','设备利用率'),(345,'-95%','资源冲突'),(478,'0%','值日遗漏')]:metric(714,y,n,t,w=160)
note('效果数字沿用原网站项目记录；统计周期与样本口径未披露。300 米为设计规则参数。');end()
# 11 / WORKFLOW
base('CASE 04 / WORKFLOW DESIGN',bookmark='feedback');heading('04 / MULTI-BRANCH ANALYSIS','学生反馈洞察工作流','把反馈原话与公众号材料，整理成可以阅读、讨论与分工的图文洞察。')
for i,(n,t) in enumerate([('90','条测试反馈'),('3','篇公众号材料'),('17','个设计节点'),('4','条分析支路')]):
 x=M+i*223;text(n,x,205,35,'Bold');text(t,x,252,11)
rect(M,309,169,228,BLUE);label('INPUTS',M+15,325);text('问卷反馈',M+15,365,21,'Bold');para('读取表格\n清洗与脱敏',M+15,409,140,12,maxh=50);text('公众号材料',M+15,477,17,'Bold')
rows=[('A','分词与词频','高频词整理','词云生成'),('B','情感分析','情绪统计','情绪饼图'),('C','主题归类','问题聚合','问题与建议'),('D','读取公众号','校园事件提取','每周事件总结')]
for i,(n,a,b,d) in enumerate(rows):
 y=309+i*62;label(n,235,y+18,ORANGE)
 for j,value in enumerate([a,b,d]):
  x=265+j*159;rect(x,y,142,44,WHITE,LINE,r=3);text(value,x+12,y+15,11.5)
  if j<2:text('>',x+145,y+17,11,'Mono',MUTED)
rect(763,309,153,228,LIME);text('结果汇总',783,391,21,'Bold');text('统一排版',783,433,13);text('图文报告',783,474,13)
note('Coze 风格方案整理，共 17 节点。本页按四支路重绘；为方案设计，非平台运行截图或可导入配置。');end()
# 12 / REPORT
base('CASE 04 / REPORT AS EVIDENCE');heading('04 / FROM FEEDBACK TO ACTION','让输出成为行动依据。','不仅展示统计结果，也保留代表性原话，让问题、证据与建议保持对应。')
for i in range(3):
 x=M+i*177;frame(ASSETS/f'report-pages/page-{i+1}.png',x,213,162,342,pad=5);label(f'REPORT / {i+1:02}',x,566)
for y,n,title,body in [(216,'01','高频问题','系统卡顿、退款异常、校园生活配套不足。'),(347,'02','原话与建议','将具体反馈与扩容监控、对账响应、配套优化等建议对应。'),(489,'03','图文汇总','情绪分布、负面反馈词云与校园事件总结。')]:
 label(n,615,y,ORANGE);text(title,615,y+23,20,'Bold');para(body,615,y+62,301,12,maxh=70)
note('图文来自原站示例报告；测试反馈与图表数字用于方案展示，不代表经核实的校园事件或已完成处置。');end()
# 13 / WRITING
base('CASE 05 / CONTENT AGENT',bookmark='writing');heading('05 / CONTENT SYSTEM','公众号文章仿写 Agent','学习体裁、论证骨架与段落功能，建立从参考样本到可审阅成稿的内容流程。')
metric(M,216,'63','篇参考语料','整理样本索引，抽取体裁、论证主线与适用场景。',225);metric(M,394,'02','篇生成成稿','每篇保留正文、写作说明、参考资料与质量核查。',225)
for x,title,body,url in [(329,'公共议题评论','盲杖被要求收起：\n辅助器具何以成了\n“待报备物品”','disney-commentary.html'),(631,'科技议题评论','“欢迎来到 AGI 时代”，\n宏大叙事何以\n先于安全落地？','ai-commentary.html')]:
 rect(x,208,285,357,WHITE,LINE);label('CONTENT / GENERATED SAMPLE',x+18,229);text(title,x+18,260,22,'Bold');para(body,x+18,315,249,19,col=INK,font='Serif',leading=32,maxh=105);para('正文 / 写作说明\n参考资料 / 事实核查\n质量核查记录',x+18,445,249,12,maxh=72);button('阅读完整成稿',SITE+'portfolio-assets/writing-results/'+url,x+18,518,249,True)
note('两篇为生成示例；外部事实以原稿核查记录及进一步核实为准。流程：选样 / 学习 / 检索 / 写作 / 核查。');end()
# 14 / WEEKLY
base('CASE 06 / PRODUCTIVITY TOOL',bookmark='weekly');heading('06 / LOCAL-FIRST PRODUCT','360 周报生成助手','把分散在日期与消息中的日报，整理为可编辑、可复制、可保存的工作周报。')
block(M,216,'MY CONTRIBUTION','记录 → 汇总 → 交付','设计日报日历、工作日编辑、周报模板、历史记录与本机桥接，让记录和交付留在同一工作台。')
for y,n,t,d in [(404,'01','日历','按工作日记录与修正日报'),(465,'02','模板','规则模板或可选 AI 生成'),(526,'03','历史','编辑、复制并保存周报')]:label(n,M,y,ORANGE);text(t,M+35,y-2,16,'Bold');text(d,M+90,y+1,11)
frame(B/'reference-weekly.png',350,204,566,355,pad=8);label('PRODUCT / 日报日历工作台',350,573)
note('个人项目，非 360 官方产品。资料保存在当前浏览器；推推读取及部分生成功能依赖本机桥接和授权。');end()
# 15 / METHOD
base('METHOD / EVALUATION',bookmark='method');heading('HOW I WORK','从问题现场开始，用证据推进。','把项目拆成可验证的假设，用原型、测试集、用户反馈和结果指标逐步收敛。')
for i,(n,t,b) in enumerate([('01','理解业务','从业务流程与用户原话开始，识别需要交付的结果。'),('02','定义系统','明确 Agent 角色、输入输出、状态与质量门。'),('03','建立评测','用人工测试集与错误分类，把效果转成产品决策。'),('04','交付迭代','用 MVP 或可运行工具，让方案进入反馈回路。')]):
 x=M+i*223;label(n,x,218,ORANGE);text(t,x,254,23,'Bold');para(b,x,305,195,13,maxh=86)
line(M,431,916,431);label('INTERNSHIP / EVALUATION EXPERIENCE',M,455)
for x,n,t in [(M,'500+','人工测试集'),(350,'94.55%','谣言识别准确率'),(677,'389','条舆情核查')]:metric(x,484,n,t,w=220)
note('实习指标沿用个人网站与原版作品集记录；统计周期与口径未披露，不作为公开演示版性能指标。');end()
# 16 / CONTACT
base('CONTACT / EXPLORE MORE',True,'contact');label('LET’S BUILD SOMETHING USEFUL',M,94,LIME);text('让想法走到可用。',M,137,46,'Serif',WHITE)
para('期待和你聊聊 AI 产品、Agent 与真实业务。',M,210,520,16,'#b3c3b1',maxh=40)
label('CONTACT',M,301,LIME);text('吴炎斌',M,341,27,'Serif',WHITE);text('wyb18959209440@163.com',M,392,15,'Sans',WHITE);c.linkURL('mailto:wyb18959209440@163.com',(M,H-413,420,H-389),relative=0,thickness=0)
button('访问完整个人网站',SITE,M,442,239,True)
q=QrCodeWidget(SITE);bounds=q.getBounds();qw=bounds[2]-bounds[0];qh=bounds[3]-bounds[1];draw=Drawing(90,90,transform=[90/qw,0,0,90/qh,0,0]);draw.add(q);rect(M,503,102,102,WHITE);renderPDF.draw(draw,c,M+6,H-599);para('扫码浏览完整项目\n或点击右侧材料入口',163,535,300,11,'#b3c3b1',maxh=43)
label('PROJECT MATERIALS / CLICK TO OPEN',538,301,LIME)
links=[('班小智 · 本地规则体验','portfolio-assets/banxiaozhi/demo/index.html'),('智能舆情系统 MVP','portfolio.html?project=mvp'),('舆情分析与监测 Agent','portfolio.html?project=opinion'),('实验室设备演示视频','portfolio.html?project=lab'),('学生反馈图文报告','portfolio.html?project=feedback'),('文章仿写案例与成稿','portfolio.html?project=writing'),('360 周报生成助手','portfolio.html?project=weekly')]
for i,(title,url) in enumerate(links):
 y=335+i*38;line(538,y+28,916,y+28,'#3a5144');label(['07','01','02','03','04','05','06'][i],538,y+4,LIME);text(title,573,y+1,13,'Sans',WHITE);text('↗',898,y+1,14,'Sans',LIME);c.linkURL(SITE+url,(538,H-y-28,916,H-y+3),relative=0,thickness=0)
end();c.save()
assert PAGE==TOTAL,(PAGE,TOTAL)
if warnings:print('LAYOUT WARNINGS',json.dumps(warnings,ensure_ascii=False));raise SystemExit(1)
assert OUT.stat().st_size<10_000_000,OUT.stat().st_size
print(json.dumps({'path':str(OUT),'pages':PAGE,'bytes':OUT.stat().st_size,'layoutWarnings':warnings},ensure_ascii=False))
