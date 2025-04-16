#!/bin/bash
echo "🔧 [MAC] 正在使用 PyInstaller 打包..."
pyinstaller --noconfirm --onefile --windowed --name "DiagApp" --add-data ".env:." main.py
echo "✅ 打包完成，文件在 dist/DiagApp 或 dist/main.app"
