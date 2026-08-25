"""Виджет прозрачного прицела."""

from __future__ import annotations

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QWidget


class CrosshairOverlay(QWidget):
    """Прозрачный прицел поверх всех окон."""

    def __init__(
        self,
        size: int = 48,
        thickness: int = 100,
        gap: int = 8,
        color: QColor | None = None,
        parent: QWidget | None = None,
    ) -> None:
        """Создаёт прицел.
        size — размер окна прицела
        thickness — толщина линий
        gap — зазор в центре
        color — цвет прицела
        """
        super().__init__(parent)

        self._size = size
        self._thickness = thickness
        self._gap = gap
        self._color = color or QColor(0, 255, 0, 220)

        self.setFixedSize(size, size)
        self._setup_window()
        self._center_on_screen()

    def _setup_window(self) -> None:
        """Настраивает окно: без рамок, поверх всех, клик-сквозь."""
        flags = (
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
            | Qt.WindowType.WindowTransparentForInput
        )
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

    def _center_on_screen(self) -> None:
        """Ставит прицел точно в центр основного монитора."""
        screen = QApplication.primaryScreen()
        if screen is None:
            return


        center = screen.geometry().center()
        print(center)
        top_left = center - QPoint((self._size // 2) - 1, (self._size // 2) - 1)
        self.move(top_left)

    def paintEvent(self, event) -> None:  # noqa: N802
        """Рисует крестик."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(self._color)
        pen.setWidth(self._thickness)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)

        half = self._size // 2
        gap = self._gap

        # Вертикаль
        painter.drawLine(half, 0, half, half - gap)
        painter.drawLine(half, half + gap, half, self._size)

        # Горизонталь
        painter.drawLine(0, half, half - gap, half)
        painter.drawLine(half + gap, half, self._size, half)