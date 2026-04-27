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
            print("Firewall rule added successfully!")
            return True
        else:
            if "已存在" in result.stderr or "already exists" in result.stderr.lower():
                print("Firewall rule already exists")
                return True
            else:
                print(f"Failed to add firewall rule: {result.stderr}")
                return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_firewall_rule():
    """检查防火墙规则是否存在"""
    try:
        command = ['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=Flask Web Server']
        result = subprocess.run(command, capture_output=True, text=True, encoding='gbk')
        
        if "Flask Web Server" in result.stdout:
            print("Firewall rule exists")
            return True
        else:
            print("Firewall rule does not exist")
            return False
    except Exception as e:
        print(f"Check failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Windows Firewall Configuration Tool")
    print("=" * 60)
    print("\nConfiguring firewall rule (may require admin privileges)...")
    print("If prompted, please run as administrator\n")
    
    # 检查是否已存在
    if check_firewall_rule():
        print("\nFirewall is already configured")
    else:
        # 尝试添加规则
        if add_firewall_rule():
            print("\nConfiguration complete! Mobile devices should now be able to access the website")
        else:
            print("\nAutomatic configuration failed. Please configure manually:")
            print("1. Open 'Windows Defender Firewall'")
            print("2. Click 'Advanced Settings'")
            print("3. Select 'Inbound Rules' -> 'New Rule'")
            print("4. Select 'Port' -> TCP -> Port: 5000")
            print("5. Select 'Allow the connection'")
    
    print("\n" + "=" * 60)
    print("Mobile access URL: http://192.168.1.5:5000")
    print("=" * 60)

