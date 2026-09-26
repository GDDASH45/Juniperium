import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QToolBar,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Juniperium")
        self.setGeometry(100, 100, 1200, 800)

        # The browser widget (Chromium-based)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.browser.urlChanged.connect(self.update_url_bar)

        # Navigation Toolbar
        nav_bar = QToolBar("Navigation")
        self.addToolBar(nav_bar)

        # Back Button
        back_btn = QPushButton("←")
        back_btn.clicked.connect(self.browser.back)
        nav_bar.addWidget(back_btn)

        # Forward Button
        forward_btn = QPushButton("→")
        forward_btn.clicked.connect(self.browser.forward)
        nav_bar.addWidget(forward_btn)

        # Reload Button
        reload_btn = QPushButton("⟳")
        reload_btn.clicked.connect(self.browser.reload)
        nav_bar.addWidget(reload_btn)

        # URL / Address Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        # Go Button
        go_btn = QPushButton("Go")
        go_btn.clicked.connect(self.navigate_to_url)
        nav_bar.addWidget(go_btn)

        # Set central widget layout
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def navigate_to_url(self):
        url_text = self.url_bar.text()
        # If the user didn't type a protocol, default to HTTPS
        if not url_text.startswith("http://") and not url_text.startswith(
            "https://"
        ):
            # Simple check if it looks like a domain or search query
            if "." in url_text and " " not in url_text:
                url_text = "https://" + url_text
            else:
                # Fallback to Google search if it's just words
                url_text = (
                    "https://www.google.com/search?q="
                    + url_text.replace(" ", "+")
                )

        self.browser.setUrl(QUrl(url_text))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Python Browser")
    window = Browser()
    window.show()
    sys.exit(app.exec())