import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, on_matches_click, on_matchups_click, on_config_click):
        super().__init__()

        self.setWindowTitle("LoL Matchup Analyzer")

        layout = QVBoxLayout()

        # empuja contenido hacia el centro
        layout.addStretch()

        # título
        title = QLabel("LoL Matchup Analyzer")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: bold;")

        # botones
        btn_matches = QPushButton("Matches")
        btn_matchups = QPushButton("Matchups")
        btn_config = QPushButton("Configuration")

        btn_matches.clicked.connect(on_matches_click)
        btn_matchups.clicked.connect(on_matchups_click)
        btn_config.clicked.connect(on_config_click)

        # centrado de botones
        btn_matches.setFixedWidth(250)
        btn_matches.setFixedHeight(50)
        btn_matchups.setFixedWidth(250)
        btn_matchups.setFixedHeight(50)
        btn_config.setFixedWidth(250)
        btn_config.setFixedHeight(50)

        # agregar widgets
        layout.addWidget(title)
        layout.addSpacing(200)
        layout.addWidget(btn_matches, alignment=Qt.AlignCenter)
        layout.addWidget(btn_matchups, alignment=Qt.AlignCenter)
        layout.addWidget(btn_config, alignment=Qt.AlignCenter)

        # empuja desde abajo → centra vertical
        layout.addStretch()

        self.setLayout(layout)

