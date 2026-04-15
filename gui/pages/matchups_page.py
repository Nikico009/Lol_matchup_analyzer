from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt



class MatchupsPage(QWidget):
    def __init__(self, on_back):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Matchups Page")
        label.setAlignment(Qt.AlignCenter)

        back = QPushButton("Back")
        back.clicked.connect(on_back)

        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(back, alignment=Qt.AlignCenter)

        self.setLayout(layout)
