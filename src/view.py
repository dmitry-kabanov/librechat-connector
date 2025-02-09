from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import (
    QWebEngineProfile,
    QWebEnginePage,
)
from sshworker import SSHWorker
from PySide6.QtCore import QThreadPool


_LIBRECHAT_URL = "http://localhost:3080/"


class View(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("LibreChat")

        self.ssh_worker = SSHWorker()
        self.thread_pool = QThreadPool()
        self.thread_pool.start(self.ssh_worker)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.profile = QWebEngineProfile("librechat-connector-app", self)
        self.profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
        )

        self.web_view = QWebEngineView(self.central_widget)
        self.page = QWebEnginePage(self.profile)
        self.web_view.setPage(self.page)
        self.web_view.load(QUrl(_LIBRECHAT_URL))

        self._layout = QVBoxLayout(self.central_widget)
        self._layout.addWidget(self.web_view)

    def closeEvent(self, event):
        super().closeEvent(event)
        self.ssh_worker.stop()
