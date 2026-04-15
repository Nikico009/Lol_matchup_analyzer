from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt


class MenuPage(QWidget):
    def __init__(self, on_matches, on_matchups, on_config):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("LoL Matchup Analyzer")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: bold;")

        btn1 = QPushButton("Matches")
        btn2 = QPushButton("Matchups")
        btn3 = QPushButton("Configuration")

        btn1.setFixedWidth(250)
        btn1.setFixedHeight(50)
        btn2.setFixedWidth(250)
        btn2.setFixedHeight(50)
        btn3.setFixedWidth(250)
        btn3.setFixedHeight(50)


        btn1.clicked.connect(on_matches)
        btn2.clicked.connect(on_matchups)
        btn3.clicked.connect(on_config)

        layout.addWidget(title, alignment=Qt.AlignCenter)
        layout.addSpacing(50)
        layout.addWidget(btn1, alignment=Qt.AlignCenter)
        layout.addWidget(btn2, alignment=Qt.AlignCenter)
        layout.addWidget(btn3, alignment=Qt.AlignCenter)

        self.setLayout(layout)
