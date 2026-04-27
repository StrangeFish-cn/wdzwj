#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Windows防火墙配置帮助"""

import subprocess
import sys

def add_firewall_rule():
    """添加防火墙规则允许5000端口"""
    try:
        # 使用netsh命令添加防火墙规则
        command = [
            'netsh', 'advfirewall', 'firewall', 'add', 'rule',
            'name=Flask Web Server',
            'dir=in',
            'action=allow',
            'protocol=TCP',
            'localport=5000'
        ]
        
        result = subprocess.run(command, capture_output=True, text=True, encoding='gbk')
        
        if result.returncode == 0:
            print("✅ 防火墙规则添加成功！")
            return True
        else:
            if "已存在" in result.stderr or "already exists" in result.stderr.lower():
                print("ℹ️  防火墙规则已存在")
                return True
            else:
                print(f"❌ 添加防火墙规则失败: {result.stderr}")
                return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def check_firewall_rule():
    """检查防火墙规则是否存在"""
    try:
        command = ['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=Flask Web Server']
        result = subprocess.run(command, capture_output=True, text=True, encoding='gbk')
        
        if "Flask Web Server" in result.stdout:
            print("✅ 防火墙规则已存在")
            return True
        else:
            print("❌ 防火墙规则不存在")
            return False
    except Exception as e:
        print(f"检查失败: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Windows防火墙配置工具")
    print("=" * 60)
    print("\n正在配置防火墙规则（需要管理员权限）...")
    print("如果提示需要管理员权限，请以管理员身份运行此脚本\n")
    
    # 检查是否已存在
    if check_firewall_rule():
        print("\n防火墙已配置，无需重复添加")
    else:
        # 尝试添加规则
        if add_firewall_rule():
            print("\n✅ 配置完成！现在手机应该可以访问网站了")
        else:
            print("\n⚠️  自动配置失败，请手动配置：")
            print("1. 打开'Windows Defender 防火墙'")
            print("2. 点击'高级设置'")
            print("3. 选择'入站规则' → '新建规则'")
            print("4. 选择'端口' → TCP → 端口号: 5000")
            print("5. 选择'允许连接'")
    
    print("\n" + "=" * 60)
    print("手机访问地址: http://192.168.1.5:5000")
    print("=" * 60)

