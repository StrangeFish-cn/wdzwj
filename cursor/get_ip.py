#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""获取本机IP地址，用于手机访问"""

import socket

def get_local_ip():
    """获取本机局域网IP地址"""
    try:
        # 连接到一个远程地址（不会实际发送数据）
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None

def get_all_ips():
    """获取所有网络接口的IP地址"""
    import socket
    hostname = socket.gethostname()
    ips = []
    try:
        # 获取所有IP地址
        for ip in socket.gethostbyname_ex(hostname)[2]:
            if not ip.startswith("127."):
                ips.append(ip)
    except:
        pass
    return ips

if __name__ == "__main__":
    print("=" * 60)
    print("获取本机IP地址 - 用于手机访问网站")
    print("=" * 60)
    
    local_ip = get_local_ip()
    all_ips = get_all_ips()
    
    if local_ip:
        print(f"\n主要IP地址: {local_ip}")
        print(f"\n手机访问地址: http://{local_ip}:5000")
    else:
        print("\n无法自动获取IP地址")
    
    if all_ips:
        print(f"\n所有可用IP地址:")
        for ip in all_ips:
            print(f"  - http://{ip}:5000")
    
    print("\n" + "=" * 60)
    print("使用说明:")
    print("=" * 60)
    print("1. 确保手机和电脑连接在同一个WiFi网络")
    print("2. 在手机浏览器中输入上面的IP地址")
    print("3. 如果无法访问，请检查Windows防火墙设置")
    print("4. 确保Flask服务器正在运行 (python app.py)")
    print("=" * 60)

