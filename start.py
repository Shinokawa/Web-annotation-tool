#!/usr/bin/env python3
"""
车道线标注工具 - 基于Web的标注界面
专为车道线检测和可行驶区域标注优化
"""

import os
import sys
import webbrowser
import time
from threading import Timer

def open_browser():
    """延迟打开浏览器"""
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    print("车道线标注工具 v1.0.0")
    print("-" * 30)
    
    # 检查必要的目录
    input_dir = 'data/images'
    output_dir = 'data/masks'
    
    if not os.path.exists(input_dir):
        os.makedirs(input_dir, exist_ok=True)
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    # 延迟3秒后打开浏览器
    Timer(3.0, open_browser).start()
    
    # 启动Flask服务器
    from app import app
    import socket
    
    # 获取本机IP地址
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"服务器运行于: http://localhost:5000")
    print(f"网络访问: http://{local_ip}:5000")
    print("按 Ctrl+C 停止服务器\n")
    
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\n服务器已停止")
        sys.exit(0)
