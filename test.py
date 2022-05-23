import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import os
from PyQt5.QtCore import pyqtSlot
from processes import BaseProcess
from input import Model 
from main import Handler
from processes import BaseProcess
from gantt import Gantt

ui_path = os.path.dirname(os.path.abspath(__file__))
form_class= uic.loadUiType(os.path.join(ui_path, "mainwindow.ui"))[0]


class myApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(os.path.join(ui_path, "mainwindow.ui"),self)
        #self.setupUi(self)
        self.setWindowTitle("My Scheduler")
        self.model = Model()
        self.handler = Handler()
        self.handler.model = self.model
        lineEdit_list = [self.ui.lineEdit_arrival, 
                         self.ui.lineEdit_burst,
                         self.ui.lineEdit_pid,
                         self.ui.lineEdit_priority,
                         self.ui.lineEdit_timeslice]
        
        #self.ui.lineEdit_priority.setInputMask("00") #99개까지만?
        #for lineEdit in lineEdit_list:
        #    lineEdit.setValidator() # #pid는 string, arrival, burst 등은 숫자로 제한. 
        btn_list = [self.ui.pushButton_add, 
                    self.ui.pushButton_run,
                    self.ui.pushButton_deleteall]
    
        for btn in btn_list:
            btn.clicked.connect(lambda x, button = btn: self.button_func(x, button))
    
    
    
    @pyqtSlot()

    def fill_in_results(self, tab):
        if tab == 'FCFS':
            response = self.handler.outputs[0][0] # FCFS' waiting time
            turnaround = self.handler.outputs[0][1] # FCFS' turnaround time
            waiting = self.handler.outputs[0][2]  # FCFS' waiting time

            self.ui.results_fcfs.setRowCount(len(response))
            pid = sorted(response.keys())
            
            for i, id in enumerate(pid):
                self.ui.results_fcfs.setItem(i, 0, QTableWidgetItem(id))
                self.ui.results_fcfs.setItem(i,1,QTableWidgetItem(str(response[id])))
                self.ui.results_fcfs.setItem(i,2,QTableWidgetItem(str(turnaround[id])))
                self.ui.results_fcfs.setItem(i,3,QTableWidgetItem(str(waiting[id])))
        
            item = QGraphicsRectItem()
            item.setRect(10,10,50,50)
            item.setBrush(Qt.yellow)
            item.setPen(QPen(Qt.red, 5))

            scene = QGraphicsScene()
            scene.addItem(item)

            view = QGraphicsView()
            view.setScene(scene)
            view.show()

        elif tab == 'RR':
            response = self.handler.outputs[1][0] # RR's waiting time
            turnaround = self.handler.outputs[1][1] # RR's turnaround time
            waiting = self.handler.outputs[1][2]  # RR's waiting time

            self.ui.results_rr.setRowCount(len(response))
            pid = sorted(response.keys())
            
            for i, id in enumerate(pid):
                self.ui.results_rr.setItem(i, 0, QTableWidgetItem(id))
                self.ui.results_rr.setItem(i,1,QTableWidgetItem(str(response[id])))
                self.ui.results_rr.setItem(i,2,QTableWidgetItem(str(turnaround[id])))
                self.ui.results_rr.setItem(i,3,QTableWidgetItem(str(waiting[id])))
        
        elif tab == 'Priority':
            response = self.handler.outputs[2][0] # Priority's waiting time
            turnaround = self.handler.outputs[2][1] # Priority's turnaround time
            waiting = self.handler.outputs[2][2]  # Priority's waiting time

            self.ui.results_priority.setRowCount(len(response))
            pid = sorted(response.keys())
            
            for i, id in enumerate(pid):
                self.ui.results_priority.setItem(i, 0, QTableWidgetItem(id))
                self.ui.results_priority.setItem(i,1,QTableWidgetItem(str(response[id])))
                self.ui.results_priority.setItem(i,2,QTableWidgetItem(str(turnaround[id])))
                self.ui.results_priority.setItem(i,3,QTableWidgetItem(str(waiting[id])))

        elif tab == 'PP':
            response = self.handler.outputs[3][0] # PP's waiting time
            turnaround = self.handler.outputs[3][1] # PP's turnaround time
            waiting = self.handler.outputs[3][2]  # PP's waiting time
            self.ui.results_pp.setRowCount(len(response))
            pid = sorted(response.keys())
            
            for i, id in enumerate(pid):
                self.ui.results_pp.setItem(i, 0, QTableWidgetItem(id))
                self.ui.results_pp.setItem(i,1,QTableWidgetItem(str(response[id])))
                self.ui.results_pp.setItem(i,2,QTableWidgetItem(str(turnaround[id])))
                self.ui.results_pp.setItem(i,3,QTableWidgetItem(str(waiting[id])))
            
                
        elif tab == 'PPRR':
            response = self.handler.outputs[4][0] # PPRR's waiting time
            turnaround = self.handler.outputs[4][1] # PPRR's turnaround time
            waiting = self.handler.outputs[4][2]  # PPRR's waiting time

            self.ui.results_pprr.setRowCount(len(response))
            pid = sorted(response.keys())
            
            for i, id in enumerate(pid):
                self.ui.results_pprr.setItem(i, 0, QTableWidgetItem(id))
                self.ui.results_pprr.setItem(i,1,QTableWidgetItem(str(response[id])))
                self.ui.results_pprr.setItem(i,2,QTableWidgetItem(str(turnaround[id])))
                self.ui.results_pprr.setItem(i,3,QTableWidgetItem(str(waiting[id])))
        
        elif tab == 'SJF':
            response = self.handler.outputs[5][0] # SJF's waiting time
            turnaround = self.handler.outputs[5][1] # SJF's turnaround time
            waiting = self.handler.outputs[5][2]  # SJF's waiting time

            self.ui.results_sjf.setRowCount(len(response))
            pid = sorted(response.keys())
            
            for i, id in enumerate(pid):
                self.ui.results_sjf.setItem(i, 0, QTableWidgetItem(id))
                self.ui.results_sjf.setItem(i,1,QTableWidgetItem(str(response[id])))
                self.ui.results_sjf.setItem(i,2,QTableWidgetItem(str(turnaround[id])))
                self.ui.results_sjf.setItem(i,3,QTableWidgetItem(str(waiting[id])))
        
        elif tab == 'SRTF':
            response = self.handler.outputs[6][0] # SRTF's waiting time
            turnaround = self.handler.outputs[6][1] # SRTF's turnaround time
            waiting = self.handler.outputs[6][2]  # SRTF's waiting time

            self.ui.results_srtf.setRowCount(len(response))
            pid = sorted(response.keys())
            
            for i, id in enumerate(pid):
                self.ui.results_srtf.setItem(i, 0, QTableWidgetItem(id))
                self.ui.results_srtf.setItem(i,1,QTableWidgetItem(str(response[id])))
                self.ui.results_srtf.setItem(i,2,QTableWidgetItem(str(turnaround[id])))
                self.ui.results_srtf.setItem(i,3,QTableWidgetItem(str(waiting[id])))

    @pyqtSlot()
    def button_func(self, x, button):
        # 없는거 확인 validation
        exp = button.text()
        if(exp =='add'):
            input1 = self.ui.lineEdit_pid.text()
            input2 = self.ui.lineEdit_arrival.text()
            input3 = self.ui.lineEdit_burst.text()
            input4 = self.ui.lineEdit_priority.text()

            ##validation!! 비어있는 것이 있는가?
            if (not input1 or not input2 or not input3 or not input4):
                QMessageBox.warning(self, 'ERROR', 'You missed something!\nPlease Enter ALL')
            
            # validation!! 옳은 형식인가? (priority : int, pid : string, arrival : float, burst : float)

            # validation Pid 같은거 확인. 

            

            inputs = [input1, input2, input3, input4]

            #inputs넘기기?
            #표에 저장하고 한번에 넘기기?
            row = self.ui.tableWidget_processes.rowCount()
            self.ui.tableWidget_processes.setRowCount(row+1)
    
            for j in range(4):
                item = QTableWidgetItem()
                text = inputs[j]
                item.setText(text)

                self.ui.tableWidget_processes.setItem(row, j, item)
            
            append_row = input1 + " " + input2 + " " + input3 + " " + input4
            
            self.model.add_input(append_row)
            
        elif(exp =='Delete All'):
            self.ui.tableWidget_processes.clear()
            self.ui.tableWidget_processes.setRowCount(0)

        elif(exp =='Run'):
            if(len(self.model.base_process_list)<=0) :
                QMessageBox.warning(self, "ERROR","No entry! Please ENTER the inputs")
            
            timeslice = self.ui.lineEdit_timeslice.text()
            if not timeslice:
                # timeslice 숫자? 확인하기!!
                QMessageBox.warning(self, "ERROR", "You missed timeslice!\nPlease enter TIMESLICE")
            else:
                self.model.sort_inputs(timeslice)
                self.handler.main()
                #self.print_outputs()
                #print('test:', self.handler.output[3])
                #for i in range(7):
                    #self.handler.outputs[i][2].sort(key=lambda p: p.pid)
                    #print(self.handler.outputs[i][2])
                self.fill_in_results('FCFS')
                self.fill_in_results('RR')
                self.fill_in_results('Priority')
                self.fill_in_results('PP')
                self.fill_in_results('PPRR')
                self.fill_in_results('SJF')
                #self.fill_in_results('SRTF')
                #img = self.gantt[0].create_gantt()
                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp()
    ex.show()
    sys.exit(app.exec_())