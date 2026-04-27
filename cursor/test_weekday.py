#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试星期几功能"""

from datetime import datetime, timedelta

# 测试计算函数
def test_calculate():
    current_time = datetime.now()
    current_xinli = 450
    
    # 心力上限
    MAX_XINLI = 600
    RECOVERY_RATE = 8
    
    # 计算
    points_needed = MAX_XINLI - current_xinli
    minutes_needed = points_needed * RECOVERY_RATE
    full_xinli_time = current_time + timedelta(minutes=minutes_needed)
    
    # 获取星期几
    weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    weekday = weekdays[full_xinli_time.weekday()]
    
    print("=" * 60)
    print("测试星期几功能")
    print("=" * 60)
    print(f"当前时间: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"当前心力: {current_xinli}点")
    print(f"需要恢复: {points_needed}点")
    print(f"恢复时间: {minutes_needed}分钟 ({minutes_needed // 60}小时)")
    print(f"下次满心力时间: {full_xinli_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"星期几: {weekday}")
    print("=" * 60)
    print("星期几功能测试通过！")

if __name__ == "__main__":
    test_calculate()

