# OpenClaw AI Assistant Framework

> 一个专业、高效、自主成长的AI助手框架


## ✨ 框架简介

OpenClaw AI Assistant Framework 是一个专业、高效、自主成长的AI助手框架，基于OpenClaw构建，适用于各种AI应用场景。

### 核心特性

**🚀 OpenClaw深度使用7步法**
1. **智能备份机制** - 24小时/10K文件变化触发，7天轮换
2. **四层模型池体系** - 高速池、智能池、文本池、视觉池
3. **会话识别规则** - 自动选择合适的模型池
4. **上下文压缩** - 节省22% tokens
5. **任务铁律** - 5轮尝试，20,000 Token上限
6. **陌生任务处理** - ClawHub优先，自动学习
7. **自我进化** - 每日22:00生成进化报告

**🧠 三层记忆体系**
- **L1 工作记忆** - 当前会话临时记忆
- **L2 短期记忆** - 每日记忆文件（memory/YYYY-MM-DD.md）
- **L3 长期记忆** - 永久记忆文件（MEMORY.md）

**🔄 Heartbeat记忆维护机制**
- 每30分钟：检查紧急事项、整理记忆、清理日志
- 每日：提取重要决策到MEMORY.md
- 每周：回顾MEMORY.md，清理30天前记忆

**📚 AI自我成长机制**
- Skill深度学习：不只是安装，而是深度理解
- 经验总结：每30分钟反思，记录经验教训
- 知识整合：发现关联，创造新能力

---

## 🎯 24小时定向学习

框架采用时段化学习策略，根据不同时间段自动学习相关技能：

### 前12小时（00:00-12:00）- 创作时段 🎨
- **00:00-04:00**：图像生成、提示词工程
- **04:00-08:00**：视频制作、剪辑工具
- **08:00-12:00**：视觉优化、设计工具

### 中间2小时（12:00-14:00）- 财务时段 📱
- **12:00-14:00**：行业、财经消息获取、持有基金形势分析

### 后10小时（14:00-24:00）- 科研进展学习时段 📱
- **12:00-16:00**：新闻获取、论文获取
- **16:00-20:00**：论文分析、领域知识分析
- **20:00-24:00**：数据分析、报告生成

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/Ipomoea97/openclaw-ai-assistant-framework.git
cd openclaw-ai-assistant-framework
```

### 2. 运行安装脚本

```bash
chmod +x install.sh
./install.sh
```

**安装脚本会：**
- ✅ 创建目录结构
- ✅ 创建核心文件（不会覆盖已有文件）
- ✅ 安装ClawHub CLI
- ✅ 安装核心技能
- ✅ 配置定时任务

### 3. 配置模型池

编辑 `config/model-pools.json`：

```json
{
  "version": 2,
  "pools": {
    "fast": {
      "name": "高速池",
      "primary": "qwen3.5-plus",
      "fallback": "qwen3.5-plus"
    },
    "smart": {
      "name": "智能池",
      "primary": "kimi-k2.5",
      "fallback": "kimi-k2.5"
    },
    "text": {
      "name": "文本池",
      "primary": "glm-5",
      "fallback": "glm-5"
    },
    "vision": {
      "name": "视觉池",
      "primary": "qwen3.5-plus",
      "fallback": "qwen3.5-plus"
    }
  }
}
```

### 4. 配置24小时学习计划

编辑 `config/skill-learning-schedule.json`：

```json
{
  "hourly_rotation": {
    "00-04": ["image", "prompt", "ai-art", "generation"],
    "04-08": ["artificial intelligence", "ai", "production", "creative"],
    "08-12": ["design", "graphics", "article", "visual"],
    "12-16": ["content", "writing", "copywriting", "research"],
    "16-20": ["catalyst", "biogas", "biomass", "catalysis"],
    "20-24": ["analytics", "automation", "rational design", "machine learning"]
  }
}
```

---

## 📚 文档

### 核心文档
- [完整框架文档](docs/openclaw-ai-assistant-framework.md) - OpenClaw 7步深度使用法
- [AI自我成长计划](docs/ai-self-evolution-plan.md) - 6大成长维度
- [AI自我成长实现](docs/ai-self-evolution-implementation.md) - 实现细节
- [Skill深度学习](docs/skill-deep-learning.md) - 知识提取与整合
- [上下文压缩机制](docs/context-compression-mechanism.md) - 框架固化
- [每日成长报告](docs/daily-growth-report-mechanism.md) - 成长可视化
- [经验总结机制](docs/experience-summary-mechanism.md) - 经验管理

### 配置文档
- [模型池配置](config/model-pools.md) - 4层模型池体系
- [会话路由](config/session-routing.md) - 自动选择模型池
- [任务铁律](config/task-iron-law.md) - 5轮尝试机制
- [上下文压缩](config/context-compression.md) - 压缩规则
- [自我进化](config/self-evolution.md) - 进化机制
- [陌生任务处理](config/unfamiliar-task-handling.md) - 处理流程
- [大脑肌肉配置](config/brain-muscle-config.md) - 行为模式

---

## ⏰ 定时任务体系（8个）

### 维护类
1. **heartbeat-notify** - 每30分钟（记忆维护）
2. **smart-backup** - 每小时（智能备份）
3. **model-health-check** - 每6小时（模型健康）

### 进化类
4. **install-skills-infinite** - 每小时（技能学习）
5. **daily-evolution** - 每天22:00（进化报告）

### 数据类
6. **daily-growth-report** - 每天09:00（成长报告）
7. **daily-report-gen** - 每天09:30（日报生成）

### 迭代类
8. **mission-control-weekly** - 每周一20:00（迭代）

---

## 🔧 核心脚本

### 学习相关
- `scripts/batch-extract-knowledge.py` - 批量知识提取
- `scripts/extract-skill-knowledge.py` - Skill知识提取
- `scripts/extract-skill-knowledge-enhanced.py` - 增强版知识提取
- `scripts/integrate-knowledge.py` - 知识整合

### 维护相关
- `scripts/daily-evolution.py` - 每日进化报告
- `scripts/model-health-check.py` - 模型池健康检查

### 测试相关
- `scripts/test-compression.py` - 上下文压缩测试
- `scripts/test-iron-law.py` - 任务铁律测试
- `scripts/test-session-routing.py` - 会话路由测试
- `scripts/test-unfamiliar-task.py` - 陌生任务测试
sher/openclaw-ai-assistant-framework
