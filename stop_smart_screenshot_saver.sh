#!/bin/bash

# smart_screenshot_saver.py のプロセスIDを取得し、各PIDに対してkillコマンドを実行
ps aux | grep 'smart_screenshot_saver.py' | grep -v 'grep' | awk '{print $2}' | while read PID; do
    if kill $PID > /dev/null 2>&1; then
        echo "プロセス（PID: $PID）を停止しました。"
    else
        echo "プロセス（PID: $PID）の停止に失敗しました。"
    fi
done
