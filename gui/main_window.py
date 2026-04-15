from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.pages.menu_page import MenuPage
from gui.pages.matches_page import MatchesPage
from gui.pages.matchups_page import MatchupsPage
from gui.pages.config_page import ConfigPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LoL Matchup Analyzer")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.show_menu()

    def clear(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

    def set_page(self, page_widget):
        self.clear()
        self.layout.addWidget(page_widget)

    # navegación
    def show_menu(self):
        self.set_page(MenuPage(
            on_matches=self.show_matches,
            on_matchups=self.show_matchups,
            on_config=self.show_config
        ))

    def show_matches(self):
        self.set_page(MatchesPage(on_back=self.show_menu))

    def show_matchups(self):
        self.set_page(MatchupsPage(on_back=self.show_menu))

    def show_config(self):
        self.set_page(ConfigPage(on_back=self.show_menu))
