import sys
import subprocess
import os
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox

class ScreenshotSaverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.config_items = {
            'interval': {'label': 'Interval（秒）:', 'value': '3'},
            'limit_similarity_val': {'label': '類似度の閾値（%）:', 'value': '95'}
            # 今後新しい設定項目を追加する場合は、ここに追加
        }
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Smart Screenshot Saver')
        layout = QVBoxLayout()

        # 設定項目の動的生成
        self.inputs = {}
        for key, item in self.config_items.items():
            label = QLabel(item['label'], self)
            layout.addWidget(label)

            line_edit = QLineEdit(self)
            line_edit.setText(item['value'])
            layout.addWidget(line_edit)
            self.inputs[key] = line_edit

        self.start_button = QPushButton('スクリーンショット取得を開始', self)
        self.start_button.clicked.connect(self.start_screenshot_saver)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('スクリーンショット取得を停止', self)
        self.stop_button.clicked.connect(self.stop_screenshot_saver)
        layout.addWidget(self.stop_button)

        self.update_button = QPushButton('設定を更新', self)
        self.update_button.clicked.connect(self.update_settings)
        layout.addWidget(self.update_button)

        self.setLayout(layout)

    def start_screenshot_saver(self):
        QMessageBox.information(self, 'Info', 'スクリーンショットの取得を開始しました。')
        subprocess.Popen(['python', 'smart_screenshot_saver.py'], cwd=os.getcwd())

    def stop_screenshot_saver(self):
        subprocess.run(['bash', 'stop_smart_screenshot_saver.sh'], cwd=os.getcwd())
        QMessageBox.information(self, 'Info', 'スクリーンショットの取得を停止しました。')

    def update_settings(self):
        config = {}
        try:
            for key in self.config_items:
                config[key] = int(self.inputs[key].text())
            self.save_config(config)
            QMessageBox.information(self, 'Info', '設定を更新しました。')
        except ValueError:
            QMessageBox.critical(self, 'Error', '無効な値です。整数を入力してください。')

    def save_config(self, config):
        with open('config.json', 'w') as file:
            json.dump(config, file, indent=4)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScreenshotSaverApp()
    ex.show()
    sys.exit(app.exec_())
