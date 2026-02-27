#!/bin/bash
# 清理GitHub仓库 - 删除所有个人文件

cd ~/.openclaw/workspace

# 删除个人配置文件
git rm -f .bilibili_cookie .env.twitter .skill-install-status*.json .skillsmp_all_skills.json .skillsmp_cookie .skillsmp_session.json 2>/dev/null || true
git rm -f AGENTS.md BOOTSTRAP.md COOKIE_EOF EOF HEARTBEAT.md IDENTITY.md MEMORY.md SOUL.md TOOLS.md USER.md 2>/dev/null || true

# 删除截图和敏感图片
git rm -f bilibili-account.png debug_search.png google_login.png login_error.png qiuzhi_profile_385670211.png search-*.png search-result.png skills_fetched.png skills_homepage.png skillsmp*.png step*.png test_*.png 2>/dev/null || true

# 删除个人脚本
git rm -f api-comparison.md auto-login.js crawl-bilibili.js debug_skills.js download-prompts*.js fetch-*.js gemini-flash-prompts-detailed.md github_skills_db.md learn-skill*.js login-*.js manager-system.md nanobanana2-experiment.md openclaw-automation-templates.md openclaw-extension-fix.md openclaw-skills-library.md qiuzhi_analysis_385670211.json save-cookie.js skill-video-script-learning.md skills-install-plan.md skills-learning-log.json skills-learning-plan.md video-demo.sh video-script.md 2>/dev/null || true

# 删除特殊文件
git rm -f "学习时间:" "搜索词:" "状态:" 2>/dev/null || true

# 删除目录
git rm -rf backup data debug logs managers memory mission-control playwright-env prompts qiuzhi_analysis tools video-learning video-scripts 2>/dev/null || true

# 删除个人skills（保留框架）
# 注意：skills/ 保留，但可能需要选择性删除

echo "✅ GitHub清理完成"
