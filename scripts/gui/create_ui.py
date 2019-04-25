import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class CreateUI(object):
    def create_ui(self, MainWindow):
        # Initialize Object Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)

        # Set Sizing Requirements
        MainWindow.resize(955, 757)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1680, 767))

        ##################################################
        #
        # Spacer items for alignment corrections
        #
        ##################################################
        spacer_item = QtWidgets.QSpacerItem(
            40,
            5,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        spacer_item_1 = QtWidgets.QSpacerItem(
            40,
            5,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        spacer_item_2 = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        spacer_item_3 = QtWidgets.QSpacerItem(
            50,
            20,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Minimum
        )

        ##################################################
        #
        # Icon data
        #
        ##################################################
        sync_to_local_icon = QtGui.QIcon()
        sync_to_local_icon.addPixmap(
            QtGui.QPixmap("./images/icons/arrow-back_white.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        sync_to_remote_icon = QtGui.QIcon()
        sync_to_remote_icon.addPixmap(
            QtGui.QPixmap("./images/icons/arrow-forward_white.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        sync_to_both_icon = QtGui.QIcon()
        sync_to_both_icon.addPixmap(
            QtGui.QPixmap("./images/icons/swap_white.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        refresh_icon = QtGui.QIcon()
        refresh_icon.addPixmap(
            QtGui.QPixmap("./images/icons/sync_white.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )

        ##################################################
        #
        # Connection Components
        #
        ##################################################

        # Initialize primary container widget
        self.primary_widget = QtWidgets.QWidget(MainWindow)
        self.primary_widget.setObjectName("primary_widget")
        self.grid_layout = QtWidgets.QGridLayout(self.primary_widget)
        self.grid_layout.setObjectName("grid_layout")

        # Initialize Connection styling and positioning
        self.connection_layout = QtWidgets.QGridLayout()
        self.connection_layout.setObjectName("connection_layout")

        # Create Username and Password form
        self.un_pw_layout = QtWidgets.QFormLayout()
        self.un_pw_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.un_pw_layout.setLabelAlignment(
            QtCore.Qt.AlignLeading |
            QtCore.Qt.AlignLeft |
            QtCore.Qt.AlignVCenter
        )
        self.un_pw_layout.setObjectName("un_pw_layout")

        # Create Host Info form
        self.host_info_layout = QtWidgets.QFormLayout()
        self.host_info_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.host_info_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.host_info_layout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.host_info_layout.setLabelAlignment(
            QtCore.Qt.AlignLeading |
            QtCore.Qt.AlignLeft |
            QtCore.Qt.AlignVCenter
        )
        self.host_info_layout.setObjectName("host_info_layout")

        # Hostname Label and ComboBox Dropdown
        self.hostname_label = QtWidgets.QLabel(self.primary_widget)
        self.hostname_label.setObjectName("hostname_label")
        self.host_info_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.hostname_label)
        self.hostname = QtWidgets.QComboBox(self.primary_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.hostname.sizePolicy().hasHeightForWidth())
        self.hostname.setSizePolicy(size_policy)
        self.hostname.setMinimumSize(QtCore.QSize(0, 33))
        self.hostname.setEditable(True)
        self.hostname.setCurrentText("")
        self.hostname.setObjectName("hostname")
        self.host_info_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hostname)

        # IP Address Label and Text Field
        self.address_label = QtWidgets.QLabel(self.primary_widget)
        self.address_label.setObjectName("address_label")
        self.host_info_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.ip_address = QtWidgets.QLineEdit(self.primary_widget)
        self.ip_address.setObjectName("ip_address")
        self.host_info_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ip_address)

        # SSH Key Label and Text Field
        self.sshkey_label = QtWidgets.QLabel(self.primary_widget)
        self.sshkey_label.setObjectName("sshkey_label")
        self.host_info_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sshkey_label)
        self.ssh_key = QtWidgets.QLineEdit(self.primary_widget)
        self.ssh_key.setObjectName("ssh_key")
        self.host_info_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ssh_key)

        # SSH Key Find File Dialogue Button
        self.ssh_key_find = QtWidgets.QToolButton(self.primary_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.ssh_key_find.sizePolicy().hasHeightForWidth())
        self.ssh_key_find.setSizePolicy(size_policy)
        self.ssh_key_find.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ssh_key_find.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.ssh_key_find.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.ssh_key_find.setAutoRaise(False)
        self.ssh_key_find.setArrowType(QtCore.Qt.NoArrow)
        self.ssh_key_find.setObjectName("ssh_key_find")
        self.host_info_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ssh_key_find)

        # Username Label and Text Field
        self.username_label = QtWidgets.QLabel(self.primary_widget)
        self.username_label.setObjectName("username_label")
        self.un_pw_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username = QtWidgets.QLineEdit(self.primary_widget)
        self.username.setObjectName("username")
        self.un_pw_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)

        # Password Label and Text Field
        self.password_label = QtWidgets.QLabel(self.primary_widget)
        self.password_label.setObjectName("password_label")
        self.un_pw_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password = QtWidgets.QLineEdit(self.primary_widget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.un_pw_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)

        # Apply Spacer for Alignment correction
        self.un_pw_layout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacer_item_2)

        # Remember Checkbox
        self.remember = QtWidgets.QCheckBox(self.primary_widget)
        self.remember.setToolTip("")
        self.remember.setObjectName("remember")
        self.un_pw_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.remember)

        # Connect Button
        self.connect = QtWidgets.QPushButton(self.primary_widget)
        self.connect.setObjectName("connect")
        self.un_pw_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.connect)

        ##################################################
        #
        # TreeView file directory components
        #
        ##################################################

        # Initialize Local styling and positioning
        self.local_layout = QtWidgets.QVBoxLayout()
        self.local_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.local_label = QtWidgets.QLabel(self.primary_widget)
        self.local_label.setAlignment(QtCore.Qt.AlignCenter)
        self.local_label.setObjectName("local_label")
        self.local_layout.addWidget(self.local_label)
        self.local_layout.addItem(spacer_item)
        self.local_tree = QtWidgets.QTreeView(self.primary_widget)
        self.local_tree.setMinimumSize(QtCore.QSize(0, 500))
        self.local_tree.setObjectName("local_tree")
        self.local_layout.addWidget(self.local_tree, 0, QtCore.Qt.AlignTop)

        # Initialize Remote styling and positioning
        self.remote_layout = QtWidgets.QVBoxLayout()
        self.remote_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.remote_layout.setObjectName("remote_layout")
        self.remote_label = QtWidgets.QLabel(self.primary_widget)
        self.remote_label.setAlignment(QtCore.Qt.AlignCenter)
        self.remote_label.setObjectName("remote_label")
        self.remote_layout.addWidget(self.remote_label)
        self.remote_layout.addItem(spacer_item_1)
        self.remote_tree = QtWidgets.QTreeView(self.primary_widget)
        self.remote_tree.setMinimumSize(QtCore.QSize(0, 500))
        self.remote_tree.setObjectName("remote_tree")
        self.remote_layout.addWidget(self.remote_tree, 0, QtCore.Qt.AlignTop)

        ##################################################
        #
        # Button Components
        #
        ##################################################

        # Sync to Remote Button
        self.sync_to_remote = QtWidgets.QPushButton(self.primary_widget)
        self.sync_to_remote.setText("")
        self.sync_to_remote.setIcon(sync_to_remote_icon)
        self.sync_to_remote.setObjectName("sync_to_remote")

        # Sync to Local Button
        self.sync_to_local = QtWidgets.QPushButton(self.primary_widget)
        self.sync_to_local.setText("")
        self.sync_to_local.setIcon(sync_to_local_icon)
        self.sync_to_local.setObjectName("sync_to_local")

        # Sync to Both Button
        self.sync_to_both = QtWidgets.QPushButton(self.primary_widget)
        self.sync_to_both.setText("")
        self.sync_to_both.setIcon(sync_to_both_icon)
        self.sync_to_both.setObjectName("sync_to_both")

        # Refresh Button
        self.refresh = QtWidgets.QPushButton(self.primary_widget)
        self.refresh.setText("")
        self.refresh.setIcon(refresh_icon)
        self.refresh.setObjectName("refresh")

        ##################################################
        #
        # Place Components into Grid
        #
        ##################################################

        # Insert Host Info into forms
        self.connection_layout.addLayout(self.host_info_layout, 0, 0, 1, 1)
        self.connection_layout.addItem(spacer_item_3, 0, 1, 1, 1)
        self.connection_layout.addLayout(self.un_pw_layout, 0, 2, 1, 1)

        # Insert forms into Grid
        self.grid_layout.addLayout(self.connection_layout, 0, 0, 1, 3)
        self.grid_layout.addLayout(self.local_layout, 1, 0, 6, 1)
        self.grid_layout.addLayout(self.remote_layout, 1, 2, 6, 1)
        self.grid_layout.addWidget(self.sync_to_remote, 2, 1, 1, 1)
        self.grid_layout.addWidget(self.sync_to_local, 3, 1, 1, 1)
        self.grid_layout.addWidget(self.sync_to_both, 4, 1, 1, 1)
        self.grid_layout.addWidget(self.refresh, 5, 1, 1, 1)

        ##################################################
        #
        # Menubar & Statusbar Components
        #
        ##################################################
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_configuration = QtWidgets.QAction(MainWindow)
        self.action_configuration.setObjectName("action_configuration")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_file.addAction(self.action_exit)
        self.menu_settings.addAction(self.action_configuration)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.status_bar)

        ##################################################
        #
        # Place Primary widget into
        #
        ##################################################
        MainWindow.setCentralWidget(self.primary_widget)

        self.retranslate_UI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_UI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MySync"))
        self.local_label.setText(_translate("MainWindow", "Local"))
        self.remote_label.setText(_translate("MainWindow", "Remote"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.username.setToolTip(_translate("MainWindow", "Username for connection to server"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.password.setToolTip(_translate("MainWindow", "Password for connection to server"))
        self.remember.setText(_translate("MainWindow", "Remember"))
        self.connect.setToolTip(_translate("MainWindow", "Connect to server"))
        self.connect.setText(_translate("MainWindow", "Connect"))
        self.hostname_label.setText(_translate("MainWindow", "Hostname"))
        self.address_label.setText(_translate("MainWindow", "IP Address"))
        self.ip_address.setToolTip(_translate("MainWindow", "Enter IP Address to connect to"))
        self.sshkey_label.setText(_translate("MainWindow", "SSH Key"))
        self.ssh_key.setToolTip(_translate("MainWindow", "Path to SSH Key"))
        self.ssh_key_find.setToolTip(_translate("MainWindow", "Open SSH Key"))
        self.ssh_key_find.setText(_translate("MainWindow", "..."))
        self.hostname.setToolTip(_translate("MainWindow", "Enter a Hostname to save as"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_settings.setTitle(_translate("MainWindow", "Settings"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_configuration.setText(_translate("MainWindow", "Configuration"))
        self.action_about.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CreateUI()
    ui.create_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
else:
    from scripts.gui import tree_controller as TC

    TC.TreeController()
