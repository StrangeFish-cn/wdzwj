#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试服务器和星期几功能"""

import time
import urllib.request
import json

print("等待服务器启动...")
time.sleep(3)

try:
    # 测试API
    req = urllib.request.Request(
        'http://localhost:5000/api/calculate',
        data=json.dumps({'current_xinli': 450}).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode('utf-8'))
    
    print("\n" + "=" * 60)
    print("服务器测试成功！")
    print("=" * 60)
    print(f"状态码: {response.status}")
    print(f"当前心力: {result.get('current_xinli')}点")
    print(f"当前时间: {result.get('current_time')}")
    print(f"需要恢复: {result.get('points_needed')}点")
    print(f"恢复时间: {result.get('minutes_needed')}分钟")
    print(f"下次满心力时间: {result.get('full_xinli_time')}")
    print(f"完整时间: {result.get('full_xinli_datetime')}")
    print(f"星期几: {result.get('weekday', '未找到')}")
    print("=" * 60)
    print("\n服务器运行正常！")
    print("访问地址: http://localhost:5000")
    print("手机访问: http://192.168.1.5:5000")
    
except urllib.error.URLError as e:
    print(f"\n连接失败: {e}")
    print("请确保服务器正在运行 (python app.py)")
except Exception as e:
    print(f"\n错误: {e}")

