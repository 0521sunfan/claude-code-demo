# Claude Code 入门指南

Claude Code 是 Anthropic 推出的命令行 AI 编程助手，深度集成在你的终端中。

## 核心能力

- **代码理解**：直接读取和分析你的代码库，帮你读懂复杂逻辑
- **代码编写**：一句话描述需求，自动生成、修改代码文件
- **调试定位**：描述问题现象，自动搜索定位并修复 bug
- **Git 操作**：自动生成 commit message、创建 PR、审查代码

## 快速上手

```bash
# 安装
npm install -g @anthropic-ai/claude-code

# 进入项目
cd your-project
claude
```

启动后可直接用中文描述需求，Claude Code 会自主完成任务。

## 常用技巧

- 用 `/init` 初始化项目上下文
- 用 `/review` 审查代码变更
- 用 `/help` 查看所有命令
- 直接粘贴报错日志即可自动排查
