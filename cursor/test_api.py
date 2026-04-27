#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试API接口"""

import time
import json
import urllib.request
import urllib.parse

# 等待服务器启动
print("等待服务器启动...")
time.sleep(3)

# 测试数据
test_cases = [
    {"current_xinli": 450, "description": "正常情况：450点心力"},
    {"current_xinli": 600, "description": "边界情况：已满心力"},
    {"current_xinli": 0, "description": "边界情况：0点心力"},
    {"current_xinli": 300, "description": "正常情况：300点心力"},
]

print("\n" + "=" * 60)
print("开始测试API接口")
print("=" * 60)

for i, test in enumerate(test_cases, 1):
    print(f"\n测试 {i}: {test['description']}")
    print(f"输入心力点数: {test['current_xinli']}")
    
    try:
        # 准备请求数据
        data = json.dumps({"current_xinli": test['current_xinli']}).encode('utf-8')
        req = urllib.request.Request(
            'http://localhost:5000/api/calculate',
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        
        # 发送请求
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"状态码: {response.status}")
            print(f"响应结果:")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            
    except urllib.error.URLError as e:
        print(f"❌ 连接错误: {e}")
        print("请确保Flask服务器正在运行 (python app.py)")
        break
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    time.sleep(0.5)

print("\n" + "=" * 60)
print("测试完成！")
print("=" * 60)
print("\n提示：在浏览器中访问 http://localhost:5000 查看Web界面")

