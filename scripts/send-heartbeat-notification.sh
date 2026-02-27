#!/bin/bash
# Heartbeat通知发送脚本

HEARTBEAT_STATE="/home/zzyuzhangxing/.openclaw/workspace/data/heartbeat-state.json"
NOTIFICATION_FILE="/home/zzyuzhangxing/.openclaw/workspace/data/heartbeat-notification.txt"

# 检查是否有通知文件
if [ -f "$NOTIFICATION_FILE" ]; then
    # 读取通知内容
    NOTIFICATION=$(cat "$NOTIFICATION_FILE")
    
    # 发送飞书消息
    # 使用OpenClaw的message工具
    cd /home/zzyuzhangxing/.openclaw/workspace
    
    # 记录发送日志
    echo "[$(date)] 发送Heartbeat通知: $NOTIFICATION" >> /home/zzyuzhangxing/.openclaw/workspace/logs/heartbeat-notification.log
    
    # 删除通知文件（已发送）
    rm -f "$NOTIFICATION_FILE"
fi
