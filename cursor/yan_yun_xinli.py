#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
燕云心力计算器
心力上限：600点
恢复速度：每8分钟恢复1点
"""

from datetime import datetime, timedelta


def calculate_full_xinli_time(current_xinli, current_time):
    """
    计算下次满心力的时间
    
    参数:
        current_xinli: 当前心力点数
        current_time: 当前时间 (datetime对象)
    
    返回:
        下次满心力的时间字符串
    """
    # 心力上限
    MAX_XINLI = 600
    
    # 恢复速度：每8分钟恢复1点
    RECOVERY_RATE = 8  # 分钟/点
    
    # 检查当前心力是否已满
    if current_xinli >= MAX_XINLI:
        return "当前心力已满，无需恢复！"
    
    # 计算需要恢复的点数
    points_needed = MAX_XINLI - current_xinli
    
    # 计算需要的时间（分钟）
    minutes_needed = points_needed * RECOVERY_RATE
    
    # 计算下次满心力的时间
    full_xinli_time = current_time + timedelta(minutes=minutes_needed)
    
    # 格式化输出
    time_str = full_xinli_time.strftime("%H:%M:%S")
    datetime_str = full_xinli_time.strftime("%Y-%m-%d %H:%M:%S")
    current_time_str = current_time.strftime("%H:%M:%S")
    
    # 获取星期几（中文）
    weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    weekday = weekdays[full_xinli_time.weekday()]
    
    return f"当前心力：{current_xinli}点\n" \
           f"当前时间：{current_time_str}\n" \
           f"需要恢复：{points_needed}点\n" \
           f"恢复时间：{minutes_needed}分钟 ({minutes_needed // 60}小时{minutes_needed % 60}分钟)\n" \
           f"下次满心力时间：{time_str}\n" \
           f"完整时间：{datetime_str}\n" \
           f"星期几：{weekday}"


def main():
    """主函数"""
    print("=" * 50)
    print("燕云心力计算器")
    print("=" * 50)
    print("心力上限：600点")
    print("恢复速度：每8分钟恢复1点")
    print("=" * 50)
    
    # 自动获取当前系统时间
    current_time = datetime.now()
    current_time_str = current_time.strftime("%H:%M:%S")
    print(f"当前系统时间：{current_time_str}")
    print("=" * 50)
    
    # 获取当前心力点数
    while True:
        try:
            current_xinli = int(input("请输入当前心力点数（0-600）："))
            if 0 <= current_xinli <= 600:
                break
            else:
                print("心力点数必须在0-600之间，请重新输入！")
        except ValueError:
            print("请输入有效的数字！")
    
    # 计算并显示结果
    result = calculate_full_xinli_time(current_xinli, current_time)
    print("\n" + "=" * 50)
    print("计算结果：")
    print("=" * 50)
    print(result)
    print("=" * 50)


if __name__ == "__main__":
    main()

