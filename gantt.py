import plotly.figure_factory as ff
import plotly.io as pio
from plotly.offline import plot
import plotly.express as px
import os
from html2image import Html2Image

import urllib.request as req

hti = Html2Image()
path = os.path.dirname(os.path.abspath(__file__))


class Gantt:
    def __init__(self):
        self.data = []
        
    def create_gantt(self,data, ver):
        self.data = data
        #labels = self.data.keys()
        df = []
        annots = []

        for pid, time in self.data.items():
            d = {}
            annot_d = {}
            if isinstance(time, list):
                for nested in time:
                    d = dict(Task = "Gantt", Subtask = pid, Start = nested[0], Finish = nested[1], Resource= pid)
                    df.append(d)
                    d = {}
                    annot_d = dict(x=(nested[0]+nested[1])/2, text = pid, showarrow=False, font = dict(color = 'black', size = 54))
                    annots.append(annot_d)
                    annot_d = {}
            else : 
                d = dict(Task = "Gantt", Subtask = pid, Start = time[0], Finish = time[1], Resource = pid)
                df.append(d)
                annots.append(annot_d)
        self.fig = ff.create_gantt(df, index_col = 'Subtask', group_tasks = True)
        self.fig.update_layout(xaxis_type = 'linear', showlegend = True)
        self.fig['layout']['annotations'] = annots
        
        #self.fig.show()
        filepath = os.path.join(path, 'html/image_' +ver+'.html')
        pio.write_html(self.fig, filepath)
        filename = os.path.join(path,'image/'+ver+'.png')

        with open(filepath) as f:
            if ver == 'FCFS':
                hti.screenshot(f.read(), save_as = 'image_FCFS.png')
                f.close()
            elif ver == 'PP' :
                hti.screenshot(f.read(), save_as = 'image_PP.png')
                f.close() 
            elif ver == 'PPRR' :
                hti.screenshot(f.read(), save_as = 'image_PPRR.png')
                f.close() 
            elif ver == 'Priority' :
                hti.screenshot(f.read(), save_as = 'image_Priority.png')
                f.close() 
            elif ver == 'RR' :
                hti.screenshot(f.read(), save_as = 'image_RR.png')
                f.close() 
            elif ver == 'SJF' :
                hti.screenshot(f.read(), save_as = 'image_SJF.png')
                f.close() 

    def figure(self):
        return self.fig
    
    def create_image(self, ver):
        #filename = os.path.join(path,'html/image_'+ver+'.html')
        
        filepath = os.path.join(path, 'html/image_' +ver+'.html')
        with open(filepath) as f:
            filename = os.path.join(path,'image/'+ver+'.png')
            hti.screenshot(f.read(), save_as = filename)
            f.close()
           
        


'''
if __name__ == '__main__':
    data = {'pid': [[0, 2], [3,6]], 'pid2' : [[2,3]]}
    app = Gantt()
    app.create_gantt(data)
    app.create_image('gantt_test')
'''    
    