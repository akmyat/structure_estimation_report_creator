import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from shear_report.shear_report import ShearReport

class window(QWidget):
    def __init__(self):
        super(window, self).__init__()
        self.resize(620, 200)
        self.setWindowTitle("Structure Estimation Report Creator")

        ### Folder Path Browser###
        self.folder_path_label = QLabel(self)
        self.folder_path_label.setText("Folder Path: ")
        self.folder_path_label.move(20, 20)

        self.folder_path_textbox = QLineEdit(self)
        self.folder_path_textbox.move(150, 15)
        self.folder_path_textbox.resize(350, 32)
        self.folder_path_textbox.setText("/Path/To/Folder/")

        self.browse_btn = QPushButton("Browse", self)
        self.browse_btn.move(500, 15)
        self.browse_btn.resize(100, 32)
        self.browse_btn.clicked.connect(self.browse_folder)

        ### Output Name ###
        self.output_name_label = QLabel(self)
        self.output_name_label.setText("Output Name: ")
        self.output_name_label.move(20, 60)

        self.output_textbox = QLineEdit(self)
        self.output_textbox.move(150, 55)
        self.output_textbox.resize(350, 32)
        self.output_textbox.setText("Output Name")


        ### Create Report Button ###
        self.create_report_btn = QPushButton("Create Report", self)
        self.create_report_btn.move(20, 120)
        self.create_report_btn.resize(580, 32)
        self.create_report_btn.clicked.connect(self.create_report)

        ### Copyright ###
        self.copyright = QLabel(self)
        self.copyright.setText("© 2022, Aung Kaung Myat@LeapTech")
        self.copyright.move(180, 180)

    def browse_folder(self):
            self.folder_path = QFileDialog.getExistingDirectory(self, "Select Directory you want to create report.") + "/"
            self.folder_path_textbox.setText(self.folder_path)
        
    def create_report(self):
        shear_report = ShearReport(self.folder_path, self.output_textbox.text())
        response = shear_report.create_report()
        QMessageBox.about(self, "Report Created", response)
        

def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()