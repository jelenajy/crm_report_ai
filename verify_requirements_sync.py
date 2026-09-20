from pathlib import Path
import sys

root = Path(__file__).parent
html = (root / "客质月报交互设计v2.html").read_text(encoding="utf-8")
doc = (root / "客质月报AI知识问答需求文档.md").read_text(encoding="utf-8")

required_doc = [
    "文档版本 | V2.1",
    "C Hive Sage｜指标顾问",
    "当前实现基线",
    "单一入口",
    "当前报表",
    "Customer Type知识包",
    "Product 知识包",
    "Member Tier 知识包",
    "Binding 知识包",
    "NPS 知识包",
    "请基于所选报表进行相关的逻辑问询",
    "收起/展开",
    "提问时所选报表",
    "查看知识依据",
    "有帮助/没帮助",
    "问题编号",
    "后台提交为模拟效果",
    "不会真实提交",
    "Enter",
    "Escape",
    "500",
    "650ms",
    "1800ms",
    "contextSnapshot",
    "Base64 Data URL",
    "原型行为—需求映射表",
]

forbidden_doc = [
    "C Hive Lens",
    "全局悬浮入口 + 指标级快捷入口",
    "AI 指标助手",
    "产品名称、知识状态、最小化、清空和关闭",
    "当前页面、指标、关键筛选条件",
    "请基于该报表进行相关的逻辑问询",
    "展示问题编号、负责人和状态",
    "“没帮助”可选择",
    "当前报表上下文",
]

missing = [item for item in required_doc if item not in doc]
stale = [item for item in forbidden_doc if item in doc]

if missing:
    print("FAIL: requirements missing current prototype behavior: " + ", ".join(missing))
    sys.exit(1)
if stale:
    print("FAIL: requirements retain obsolete behavior: " + ", ".join(stale))
    sys.exit(1)

html_contracts = {
    "openAssistant": "打开助手",
    "closeAssistant": "关闭助手",
    "renderContext": "同步更新知识包名称、知识状态和快捷问题",
    "renderQuickQuestions": "动态快捷问题",
    "toggleContext": "收起/展开",
    "sendQuestion": "发送问题",
    "createTicket": "生成模拟问题编号",
    "renderReportRecommendation": "推荐报表卡片",
    "getCitationLabel": "知识依据名称随提问时所选报表动态展示",
    "toggleCitation": "查看知识依据",
    "submitFeedback": "有帮助/没帮助",
    "clearConversation": "清空对话",
    "showToast": "非阻塞提示",
    "handleReportChange": "切换报表",
}

unmapped = [behavior for function, behavior in html_contracts.items() if function in html and behavior not in doc]
if unmapped:
    print("FAIL: HTML interactions lack requirement mapping: " + ", ".join(unmapped))
    sys.exit(1)

print("PASS: requirements document matches the current HTML interaction contract")
