import sys
import time
import argparse
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer, QCoreApplication

def show_message(message):
    app = QApplication(sys.argv)
    
    # Create the message box
    msg_box = QMessageBox()
    msg_box.setText(message)
    msg_box.setIcon(QMessageBox.Warning)
    
    # Use Windows' yellow triangle warning icon
    msg_box.setWindowTitle("p")
    
    # Set up the interval if specified
    if args.interval:
        def display_message():
            result = msg_box.exec_()
            if result == QMessageBox.Ok:
                QTimer.singleShot(args.interval * 1000, display_message)
        display_message()
    else:
        msg_box.exec_()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display a message box with a custom message using PyQt5.')
    parser.add_argument('-m', '--message', required=True, help='The message to be displayed.')
    parser.add_argument('-i', '--interval', type=int, help='Interval in seconds to show the message repeatedly.')

    args = parser.parse_args()
    show_message(args.message)
