# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_navigation.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

from component.button.switch_button import SwitchButton
from component.label.head_label import HeadLabel
from component.scroll_area.smooth_scroll_area import SmoothScrollArea
import images_rc

class Ui_Navigation(object):
    def setupUi(self, Navigation):
        if not Navigation.objectName():
            Navigation.setObjectName(u"Navigation")
        Navigation.resize(290, 578)
        Navigation.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Navigation)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Navigation)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.picLabel = HeadLabel(self.widget)
        self.picLabel.setObjectName(u"picLabel")
        self.picLabel.setMinimumSize(QSize(100, 100))
        self.picLabel.setMaximumSize(QSize(100, 100))
        self.picLabel.setPixmap(QPixmap(u":/png/icon/placeholder_avatar.png"))
        self.picLabel.setScaledContents(True)

        self.verticalLayout.addWidget(self.picLabel, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.nameLabel = QLabel(self.widget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.verticalLayout.addWidget(self.nameLabel)

        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(150, 0))

        self.verticalLayout.addWidget(self.titleLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.expLabel = QLabel(self.widget)
        self.expLabel.setObjectName(u"expLabel")

        self.horizontalLayout.addWidget(self.expLabel)

        self.levelLabel = QLabel(self.widget)
        self.levelLabel.setObjectName(u"levelLabel")

        self.horizontalLayout.addWidget(self.levelLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.proxyName = QLabel(self.widget)
        self.proxyName.setObjectName(u"proxyName")

        self.horizontalLayout_6.addWidget(self.proxyName)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.proxyImgName = QLabel(self.widget)
        self.proxyImgName.setObjectName(u"proxyImgName")

        self.horizontalLayout_7.addWidget(self.proxyImgName)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.offlineButton = SwitchButton(self.widget)
        self.offlineButton.setObjectName(u"offlineButton")

        self.horizontalLayout_4.addWidget(self.offlineButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.scrollArea = SmoothScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -336, 253, 654))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 9)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.collectButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup = QButtonGroup(Navigation)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.collectButton)
        self.collectButton.setObjectName(u"collectButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.collectButton.sizePolicy().hasHeightForWidth())
        self.collectButton.setSizePolicy(sizePolicy1)
        self.collectButton.setMinimumSize(QSize(150, 40))
        self.collectButton.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/images/menu/Contact.png", QSize(), QIcon.Normal, QIcon.Off)
        self.collectButton.setIcon(icon)
        self.collectButton.setIconSize(QSize(32, 32))
        self.collectButton.setCheckable(True)
        self.collectButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.collectButton)

        self.localCollectButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.localCollectButton)
        self.localCollectButton.setObjectName(u"localCollectButton")
        sizePolicy1.setHeightForWidth(self.localCollectButton.sizePolicy().hasHeightForWidth())
        self.localCollectButton.setSizePolicy(sizePolicy1)
        self.localCollectButton.setMinimumSize(QSize(150, 40))
        self.localCollectButton.setFocusPolicy(Qt.NoFocus)
        self.localCollectButton.setIcon(icon)
        self.localCollectButton.setIconSize(QSize(32, 32))
        self.localCollectButton.setCheckable(True)
        self.localCollectButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.localCollectButton)

        self.myCommentButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.myCommentButton)
        self.myCommentButton.setObjectName(u"myCommentButton")
        sizePolicy1.setHeightForWidth(self.myCommentButton.sizePolicy().hasHeightForWidth())
        self.myCommentButton.setSizePolicy(sizePolicy1)
        self.myCommentButton.setMinimumSize(QSize(150, 40))
        self.myCommentButton.setFocusPolicy(Qt.NoFocus)
        self.myCommentButton.setIcon(icon)
        self.myCommentButton.setIconSize(QSize(32, 32))
        self.myCommentButton.setCheckable(True)
        self.myCommentButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.myCommentButton)

        self.historyButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.historyButton)
        self.historyButton.setObjectName(u"historyButton")
        sizePolicy1.setHeightForWidth(self.historyButton.sizePolicy().hasHeightForWidth())
        self.historyButton.setSizePolicy(sizePolicy1)
        self.historyButton.setMinimumSize(QSize(150, 40))
        self.historyButton.setFocusPolicy(Qt.NoFocus)
        self.historyButton.setIcon(icon)
        self.historyButton.setIconSize(QSize(32, 32))
        self.historyButton.setCheckable(True)
        self.historyButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.historyButton)

        self.remoteHistoryButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.remoteHistoryButton)
        self.remoteHistoryButton.setObjectName(u"remoteHistoryButton")
        sizePolicy1.setHeightForWidth(self.remoteHistoryButton.sizePolicy().hasHeightForWidth())
        self.remoteHistoryButton.setSizePolicy(sizePolicy1)
        self.remoteHistoryButton.setMinimumSize(QSize(150, 40))
        self.remoteHistoryButton.setFocusPolicy(Qt.NoFocus)
        self.remoteHistoryButton.setIcon(icon)
        self.remoteHistoryButton.setIconSize(QSize(32, 32))
        self.remoteHistoryButton.setCheckable(True)
        self.remoteHistoryButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.remoteHistoryButton)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.indexButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.indexButton)
        self.indexButton.setObjectName(u"indexButton")
        sizePolicy1.setHeightForWidth(self.indexButton.sizePolicy().hasHeightForWidth())
        self.indexButton.setSizePolicy(sizePolicy1)
        self.indexButton.setMinimumSize(QSize(150, 40))
        self.indexButton.setFocusPolicy(Qt.NoFocus)
        self.indexButton.setIcon(icon)
        self.indexButton.setIconSize(QSize(32, 32))
        self.indexButton.setCheckable(True)
        self.indexButton.setChecked(True)
        self.indexButton.setPopupMode(QToolButton.DelayedPopup)
        self.indexButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.indexButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.indexButton)

        self.searchButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.searchButton)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy1.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy1)
        self.searchButton.setMinimumSize(QSize(150, 40))
        self.searchButton.setFocusPolicy(Qt.NoFocus)
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QSize(32, 32))
        self.searchButton.setCheckable(True)
        self.searchButton.setPopupMode(QToolButton.DelayedPopup)
        self.searchButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.searchButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.searchButton)

        self.categoryButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.categoryButton)
        self.categoryButton.setObjectName(u"categoryButton")
        sizePolicy1.setHeightForWidth(self.categoryButton.sizePolicy().hasHeightForWidth())
        self.categoryButton.setSizePolicy(sizePolicy1)
        self.categoryButton.setMinimumSize(QSize(150, 40))
        self.categoryButton.setFocusPolicy(Qt.NoFocus)
        self.categoryButton.setIcon(icon)
        self.categoryButton.setIconSize(QSize(32, 32))
        self.categoryButton.setCheckable(True)
        self.categoryButton.setPopupMode(QToolButton.DelayedPopup)
        self.categoryButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.categoryButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.categoryButton)

        self.commentButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.commentButton)
        self.commentButton.setObjectName(u"commentButton")
        sizePolicy1.setHeightForWidth(self.commentButton.sizePolicy().hasHeightForWidth())
        self.commentButton.setSizePolicy(sizePolicy1)
        self.commentButton.setMinimumSize(QSize(150, 40))
        self.commentButton.setFocusPolicy(Qt.NoFocus)
        self.commentButton.setIcon(icon)
        self.commentButton.setIconSize(QSize(32, 32))
        self.commentButton.setCheckable(True)
        self.commentButton.setPopupMode(QToolButton.DelayedPopup)
        self.commentButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.commentButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.commentButton)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.downloadButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.downloadButton)
        self.downloadButton.setObjectName(u"downloadButton")
        sizePolicy1.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy1)
        self.downloadButton.setMinimumSize(QSize(150, 40))
        self.downloadButton.setFocusPolicy(Qt.NoFocus)
        self.downloadButton.setIcon(icon)
        self.downloadButton.setIconSize(QSize(32, 32))
        self.downloadButton.setCheckable(True)
        self.downloadButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.downloadButton)

        self.localReadButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.localReadButton)
        self.localReadButton.setObjectName(u"localReadButton")
        sizePolicy1.setHeightForWidth(self.localReadButton.sizePolicy().hasHeightForWidth())
        self.localReadButton.setSizePolicy(sizePolicy1)
        self.localReadButton.setMinimumSize(QSize(0, 40))
        self.localReadButton.setFocusPolicy(Qt.NoFocus)
        self.localReadButton.setIcon(icon)
        self.localReadButton.setIconSize(QSize(32, 32))
        self.localReadButton.setCheckable(True)
        self.localReadButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.localReadButton)

        self.waifu2xButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.waifu2xButton)
        self.waifu2xButton.setObjectName(u"waifu2xButton")
        sizePolicy1.setHeightForWidth(self.waifu2xButton.sizePolicy().hasHeightForWidth())
        self.waifu2xButton.setSizePolicy(sizePolicy1)
        self.waifu2xButton.setMinimumSize(QSize(150, 40))
        self.waifu2xButton.setFocusPolicy(Qt.NoFocus)
        self.waifu2xButton.setIcon(icon)
        self.waifu2xButton.setIconSize(QSize(32, 32))
        self.waifu2xButton.setCheckable(True)
        self.waifu2xButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.waifu2xButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.helpButton = QToolButton(self.widget)
        self.buttonGroup.addButton(self.helpButton)
        self.helpButton.setObjectName(u"helpButton")
        sizePolicy1.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy1)
        self.helpButton.setMinimumSize(QSize(0, 40))
        self.helpButton.setFocusPolicy(Qt.NoFocus)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QSize(32, 32))
        self.helpButton.setCheckable(True)
        self.helpButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.helpButton)

        self.settingButton = QToolButton(self.widget)
        self.buttonGroup.addButton(self.settingButton)
        self.settingButton.setObjectName(u"settingButton")
        sizePolicy1.setHeightForWidth(self.settingButton.sizePolicy().hasHeightForWidth())
        self.settingButton.setSizePolicy(sizePolicy1)
        self.settingButton.setMinimumSize(QSize(150, 40))
        self.settingButton.setFocusPolicy(Qt.NoFocus)
        self.settingButton.setStyleSheet(u"")
        self.settingButton.setIcon(icon)
        self.settingButton.setIconSize(QSize(32, 32))
        self.settingButton.setCheckable(True)
        self.settingButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.settingButton.setAutoRaise(False)

        self.verticalLayout.addWidget(self.settingButton)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(Navigation)

        QMetaObject.connectSlotsByName(Navigation)
    # setupUi

    def retranslateUi(self, Navigation):
        Navigation.setWindowTitle(QCoreApplication.translate("Navigation", u"\u5bfc\u822a", None))
        self.picLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("Navigation", u"\u767b\u5f55", None))
        self.nameLabel.setText("")
        self.titleLabel.setText("")
        self.expLabel.setText("")
        self.levelLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("Navigation", u"API\u5206\u6d41\uff1a", None))
        self.proxyName.setText("")
        self.label_7.setText(QCoreApplication.translate("Navigation", u"\u56fe\u7247\u5206\u6d41\uff1a", None))
        self.proxyImgName.setText("")
        self.label_5.setText(QCoreApplication.translate("Navigation", u"\u79bb\u7ebf\u6a21\u5f0f\uff1a", None))
        self.label.setText(QCoreApplication.translate("Navigation", u"\u7528\u6237", None))
        self.collectButton.setText(QCoreApplication.translate("Navigation", u"\u6211\u7684\u6536\u85cf", None))
        self.localCollectButton.setText(QCoreApplication.translate("Navigation", u"\u672c\u5730\u6536\u85cf", None))
        self.myCommentButton.setText(QCoreApplication.translate("Navigation", u"\u6211\u7684\u8bc4\u8bba", None))
        self.historyButton.setText(QCoreApplication.translate("Navigation", u"\u672c\u5730\u8bb0\u5f55", None))
        self.remoteHistoryButton.setText(QCoreApplication.translate("Navigation", u"\u89c2\u770b\u8bb0\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("Navigation", u"\u5bfc\u822a", None))
        self.indexButton.setText(QCoreApplication.translate("Navigation", u"\u9996\u9875", None))
        self.searchButton.setText(QCoreApplication.translate("Navigation", u"\u641c\u7d22", None))
        self.categoryButton.setText(QCoreApplication.translate("Navigation", u"\u5206\u7c7b\u4e0e\u6392\u884c", None))
        self.commentButton.setText(QCoreApplication.translate("Navigation", u"\u8bc4\u8bba", None))
        self.label_3.setText(QCoreApplication.translate("Navigation", u"\u5176\u4ed6", None))
        self.downloadButton.setText(QCoreApplication.translate("Navigation", u"\u4e0b\u8f7d", None))
        self.localReadButton.setText(QCoreApplication.translate("Navigation", u"\u672c\u5730\u6f2b\u753b", None))
        self.waifu2xButton.setText(QCoreApplication.translate("Navigation", u"Waifu2x", None))
        self.helpButton.setText(QCoreApplication.translate("Navigation", u"\u5e2e\u52a9", None))
        self.settingButton.setText(QCoreApplication.translate("Navigation", u"\u8bbe\u7f6e", None))
    # retranslateUi

