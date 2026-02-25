#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
X(Twitter) AI热门推文抓取脚本
抓取泛AI类热门推文，按点赞数排序

频率: 每天4次 (06:00, 12:00, 18:00, 00:00)
输出: data/x-ai-trending/x_trending_YYYYMMDD_HH.json

技术方案: 直接爬虫 (无需API Key)
注意: X有反爬机制，需处理登录/限流/验证
"""

import os
import sys
import json
import time
import random
from datetime import datetime
from urllib.parse import quote

# 尝试导入requests
# 如需selenium: pip install selenium webdriver-manager
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("[WARN] requests/beautifulsoup4 未安装")
    print("[INFO] 如需使用: pip install requests beautifulsoup4")
    requests = None

DATA_DIR = os.path.expanduser("~/.openclaw/workspace/data/x-ai-trending")

# 监控关键词 (英文为主，X上AI内容多为英文)
AI_KEYWORDS = [
    "AI",
    "ArtificialIntelligence", 
    "AIGC",
    "ChatGPT",
    "GPT4",
    "ClaudeAI",
    "Midjourney",
    "StableDiffusion",
    "ComfyUI",
    "Runway",
    "PikaLabs",
    "OpenAI",
    "Anthropic",
    "Llama",
    "AIModel"
]

# 请求头模拟
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
}

def fetch_via_nitter(keyword):
    """
    通过Nitter实例搜索推文
    Nitter是Twitter的开源镜像，无需登录
    """
    # Nitter实例列表 (部分可能失效)
    nitter_instances = [
        "https://nitter.net",
        "https://nitter.it", 
        "https://nitter.cz",
        "https://nitter.privacydev.net"
    ]
    
    tweets = []
    encoded_keyword = quote(keyword)
    
    for instance in nitter_instances:
        try:
            url = f"{instance}/search?f=tweets&q={encoded_keyword}&since={datetime.now().strftime('%Y-%m-%d')}"
            print(f"[INFO] Trying {instance} for '{keyword}'...")
            
            response = requests.get(url, headers=HEADERS, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                timeline = soup.find('div', class_='timeline')
                
                if timeline:
                    items = timeline.find_all('div', class_='timeline-item')
                    for item in items[:5]:  # 每个关键词取前5条
                        tweet = parse_nitter_tweet(item, keyword)
                        if tweet:
                            tweets.append(tweet)
                    
                    print(f"[SUCCESS] Got {len(tweets)} tweets from {instance}")
                    break  # 成功则跳出
                    
            elif response.status_code == 429:
                print(f"[WARN] {instance} rate limited")
                continue
                
        except Exception as e:
            print(f"[ERROR] {instance} failed: {e}")
            continue
            
        time.sleep(random.uniform(1, 3))  # 随机延迟
    
    return tweets

def parse_nitter_tweet(item, keyword):
    """解析Nitter页面中的推文数据"""
    try:
        # 提取推文内容
        content_div = item.find('div', class_='tweet-content')
        if not content_div:
            return None
            
        text = content_div.get_text(strip=True)
        
        # 提取作者
        author_elem = item.find('a', class_='username')
        author = author_elem.text if author_elem else "unknown"
        
        # 提取时间
        time_elem = item.find('span', class_='tweet-date')
        tweet_time = time_elem.find('a')['title'] if time_elem else ""
        
        # 提取互动数据 (Nitter可能不显示准确数字)
        stats = item.find_all('div', class_='tweet-stat')
        likes = 0
        retweets = 0
        
        for stat in stats:
            stat_text = stat.get_text()
            if 'likes' in stat_text.lower() or 'favorite' in stat_text.lower():
                try:
                    likes = int(stat_text.split()[0].replace(',', ''))
                except:
                    pass
            elif 'retweets' in stat_text.lower():
                try:
                    retweets = int(stat_text.split()[0].replace(',', ''))
                except:
                    pass
        
        return {
            'keyword': keyword,
            'author': author,
            'text': text[:280],  # 限制长度
            'time': tweet_time,
            'likes': likes,
            'retweets': retweets,
            'url': f"https://twitter.com{author}/status/...",  # 需提取真实ID
            'fetched_at': datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"[ERROR] Parse failed: {e}")
        return None

def fetch_x_ai_trending():
    """
    抓取X上泛AI类热门推文
    方案: 通过Nitter镜像站点 (无需API Key)
    """
    print("[INFO] X AI trending fetch started...")
    print(f"[INFO] Keywords: {', '.join(AI_KEYWORDS[:5])}...")
    
    if not requests:
        print("[ERROR] requests library not available")
        return {
            'fetch_time': datetime.now().isoformat(),
            'status': 'error',
            'error': 'Missing dependencies',
            'tweets': []
        }
    
    all_tweets = []
    
    # 每个关键词抓取
    for keyword in AI_KEYWORDS[:3]:  # 先测试前3个关键词
        print(f"\n[INFO] Searching keyword: {keyword}")
        tweets = fetch_via_nitter(keyword)
        all_tweets.extend(tweets)
        time.sleep(random.uniform(2, 5))  # 请求间隔
    
    # 按点赞数排序
    all_tweets.sort(key=lambda x: x.get('likes', 0), reverse=True)
    
    # 去重 (同一作者相似内容)
    seen = set()
    unique_tweets = []
    for t in all_tweets:
        key = f"{t['author']}:{t['text'][:50]}"
        if key not in seen:
            seen.add(key)
            unique_tweets.append(t)
    
    result = {
        'fetch_time': datetime.now().isoformat(),
        'status': 'success',
        'keywords': AI_KEYWORDS,
        'total_fetched': len(all_tweets),
        'unique_count': len(unique_tweets),
        'tweets': unique_tweets[:20]  # 返回Top 20
    }
    
    print(f"\n[SUCCESS] Total: {len(all_tweets)}, Unique: {len(unique_tweets)}")
    return result

def save_data(data):
    """保存数据到文件"""
    os.makedirs(DATA_DIR, exist_ok=True)
    
    timestamp = datetime.now()
    filename = f"x_trending_{timestamp.strftime('%Y%m%d_%H')}.json"
    filepath = os.path.join(DATA_DIR, filename)
    
    # 同时更新latest
    latest_path = os.path.join(DATA_DIR, "x_trending_latest.json")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    with open(latest_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"[INFO] Data saved to: {filepath}")
    return filepath

def main():
    """主函数"""
    print("=" * 60)
    print("X(Twitter) AI Trending Fetch (Direct Scraping)")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    try:
        data = fetch_x_ai_trending()
        filepath = save_data(data)
        print(f"\n[SUCCESS] Fetch completed: {filepath}")
        return 0
    except Exception as e:
        print(f"\n[ERROR] Fetch failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

