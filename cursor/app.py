#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
燕云心力计算器 - Web版本
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)


def calculate_full_xinli_time(current_xinli):
    """
    计算下次满心力的时间
    
    参数:
        current_xinli: 当前心力点数
    
    返回:
        包含计算结果的字典
    """
    # 心力上限
    MAX_XINLI = 600
    
    # 恢复速度：每8分钟恢复1点
    RECOVERY_RATE = 8  # 分钟/点
    
    # 获取当前时间
    current_time = datetime.now()
    
    # 检查当前心力是否已满
    if current_xinli >= MAX_XINLI:
        return {
            "success": False,
            "message": "当前心力已满，无需恢复！",
            "current_xinli": current_xinli,
            "current_time": current_time.strftime("%H:%M:%S")
        }
    
    # 计算需要恢复的点数
    points_needed = MAX_XINLI - current_xinli
    
    # 计算需要的时间（分钟）
    minutes_needed = points_needed * RECOVERY_RATE
    
    # 计算下次满心力的时间
    full_xinli_time = current_time + timedelta(minutes=minutes_needed)
    
    # 格式化时间
    hours = minutes_needed // 60
    minutes = minutes_needed % 60
    
    # 获取星期几（中文）
    weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    weekday = weekdays[full_xinli_time.weekday()]
    
    return {
        "success": True,
        "current_xinli": current_xinli,
        "current_time": current_time.strftime("%H:%M:%S"),
        "points_needed": points_needed,
        "minutes_needed": minutes_needed,
        "hours": hours,
        "minutes": minutes,
        "full_xinli_time": full_xinli_time.strftime("%H:%M:%S"),
        "full_xinli_datetime": full_xinli_time.strftime("%Y-%m-%d %H:%M:%S"),
        "weekday": weekday
    }


@app.route('/')
def index():
    """主页"""
    return render_template('index.html')


@app.route('/api/calculate', methods=['POST'])
def calculate():
    """计算API接口"""
    try:
        data = request.get_json()
        current_xinli = int(data.get('current_xinli', 0))
        
        # 验证输入
        if current_xinli < 0 or current_xinli > 600:
            return jsonify({
                "success": False,
                "message": "心力点数必须在0-600之间！"
            }), 400
        
        # 计算结果
        result = calculate_full_xinli_time(current_xinli)
        return jsonify(result)
    
    except ValueError:
        return jsonify({
            "success": False,
            "message": "请输入有效的数字！"
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"计算错误：{str(e)}"
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

