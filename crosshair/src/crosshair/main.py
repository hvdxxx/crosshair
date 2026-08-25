"""Точка входа приложения."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from crosshair.overley import CrosshairOverlay


def main() -> int:
    """Запускает приложение."""
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    overlay = CrosshairOverlay(
        size=32,
        thickness=2,
        gap=4,
        # color=QColor(255, 50, 50, 230),  # можно поменять цвет
    )
    overlay.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())