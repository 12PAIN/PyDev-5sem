import pytest

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from application import MyWidget

@pytest.fixture
def app(qtbot):
    test_app = MyWidget()
    qtbot.addWidget(test_app)
    return test_app


def test_initial_state(app):
    assert not app.hideButton.isChecked()
    assert not app.disableButton.isChecked()
    assert not app.enlargeFontOnButton.isChecked()
    assert not app.paintButton.isChecked()
    assert not app.changeText.isChecked()
    assert not app.pushButton.isVisible()
    assert app.pushButton.isEnabled()
    assert app.pushButton.text() == "Button"


def test_hide_button(app, qtbot):
    qtbot.mouseClick(app.hideButton, Qt.LeftButton)
    assert app.pushButton.isHidden()


def test_show_button(app, qtbot):
    app.hideButton.setChecked(True)
    qtbot.mouseClick(app.hideButton, Qt.LeftButton)
    assert not app.pushButton.isHidden()


def test_disable_button(app, qtbot):
    qtbot.mouseClick(app.disableButton, Qt.LeftButton)
    assert not app.pushButton.isEnabled()


def test_enable_button(app, qtbot):
    app.disableButton.setChecked(True)
    qtbot.mouseClick(app.disableButton, Qt.LeftButton)
    assert app.pushButton.isEnabled()


def test_enlarge_text_button(app, qtbot):
    qtbot.mouseClick(app.enlargeFontOnButton, Qt.LeftButton)
    assert app.pushButton.font().toString() == QFont('Times', 18).toString()


def test_normal_size_button(app, qtbot):
    app.enlargeFontOnButton.setChecked(True)
    qtbot.mouseClick(app.enlargeFontOnButton, Qt.LeftButton)
    assert app.pushButton.font().toString() == QFont('Times', 12).toString()


def test_change_button_color(app, qtbot):
    qtbot.mouseClick(app.paintButton, Qt.LeftButton)
    assert "background-color: red" in app.pushButton.styleSheet()


def test_reset_button_color(app, qtbot):
    app.paintButton.setChecked(True)
    qtbot.mouseClick(app.paintButton, Qt.LeftButton)
    assert not "background-color: yellow" in app.pushButton.styleSheet()


def test_change_button_text(app, qtbot):
    qtbot.mouseClick(app.changeText, Qt.LeftButton)
    assert app.pushButton.text() == "Текст изменён"


def test_reset_button_text(app, qtbot):
    app.changeText.setChecked(True)
    qtbot.mouseClick(app.changeText, Qt.LeftButton)
    assert app.pushButton.text() == "Button"
