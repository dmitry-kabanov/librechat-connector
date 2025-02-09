import sys


from view import View
from PySide6.QtWidgets import QApplication


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    app = QApplication(argv)
    app.setApplicationName("LibreChat Connector")
    app.setOrganizationName("com.dmitrykabanov")

    view = View()
    view.showMaximized()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
