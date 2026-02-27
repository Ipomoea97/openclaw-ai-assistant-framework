# 清理敏感文件 - 只保留框架

# 需要删除的文件列表（敏感/个人数据）
DELETE_FILES=(
    ".bilibili_cookie"
    ".env.twitter"
    ".skill-install-status.json"
    ".skill-install-status-v2.json"
    ".skill-install-status-v3.json"
    ".skillsmp_all_skills.json"
    ".skillsmp_cookie"
    ".skillsmp_session.json"
    "AGENTS.md"
    "BOOTSTRAP.md"
    "COOKIE_EOF"
    "EOF"
    "HEARTBEAT.md"
    "IDENTITY.md"
    "MEMORY.md"
    "SOUL.md"
    "TOOLS.md"
    "USER.md"
    "api-comparison.md"
    "auto-login.js"
    "bilibili-account.png"
    "crawl-bilibili.py"
    "debug_search.png"
    "debug_skills.js"
    "download-prompts-auto.js"
    "download-prompts.js"
    "fetch-homepage.js"
    "fetch-skills.js"
    "gemini-flash-prompts-detailed.md"
    "github_skills_db.md"
    "google_login.png"
    "learn-cron.log"
    "learn-skill-github.py"
    "learn-skill-official.py"
    "learn-skill-openclaw.py"
    "learn-skill-v2.js"
    "learn-skill.js"
    "login-google-full.js"
    "login-google.js"
    "login-skillsmp.js"
    "login-visual.js"
    "login_error.png"
    "manager-system.md"
    "nanobanana2-experiment.md"
    "openclaw-automation-templates.md"
    "openclaw-extension-fix.md"
    "openclaw-skills-library.md"
    "qiuzhi_analysis_385670211.json"
    "qiuzhi_profile_385670211.png"
    "save-cookie.js"
    "search-*.png"
    "search-result.png"
    "skill-video-script-learning.md"
    "skills-install-plan.md"
    "skills-learning-log.json"
    "skills-learning-plan.md"
    "skills_fetched.png"
    "skills_homepage.png"
    "skillsmp.png"
    "skillsmp2.png"
    "skillsmp_home.png"
    "skillsmp_stealth.png"
    "step*.png"
    "test*.js"
    "test*.png"
    "test*.py"
    "video-demo.sh"
    "video-script.md"
)

# 需要删除的目录
DELETE_DIRS=(
    "backup"
    "data"
    "logs"
    "managers"
    "memory"
    "mission-control"
    "playwright-env"
    "prompts"
    "skills"
    "tools"
    "video-learning"
    "video-scripts"
)

echo "开始清理敏感文件..."

# 删除文件
for file in "${DELETE_FILES[@]}"; do
    if [ -f "$file" ]; then
        git rm -f "$file" 2>/dev/null || rm -f "$file"
        echo "✅ 已删除: $file"
    fi
done

# 删除目录
for dir in "${DELETE_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        git rm -rf "$dir" 2>/dev/null || rm -rf "$dir"
        echo "✅ 已删除目录: $dir"
    fi
done

# 只保留框架相关脚本
KEEP_SCRIPTS=(
    "smart-backup.sh"
    "auto-restore.sh"
    "model-health-check.py"
    "daily-evolution.py"
    "heartbeat-check.py"
)

# 删除其他脚本
for script in scripts/*; do
    basename=$(basename "$script")
    if [[ ! " ${KEEP_SCRIPTS[@]} " =~ " ${basename} " ]]; then
        git rm -f "$script" 2>/dev/null || rm -f "$script"
        echo "✅ 已删除脚本: $script"
    fi
done

echo ""
echo "清理完成！"
echo ""
echo "剩余文件:"
ls -la
echo ""
echo "提交更改:"
echo "git add ."
echo "git commit -m 'chore: 清理敏感文件，只保留框架'"
echo "git push origin main --force"
