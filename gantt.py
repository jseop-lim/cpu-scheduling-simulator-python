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
        
    def create_gantt(self, data, ver):
        """
        scheduler log를 data로 입력받아 image 파일을 생성
        ver: scheduler 이름
        """
        self.data = data
        #labels = self.data.keys()
        df = []
        annots = []
        ticks = []
        for pid, time in self.data.items():
            d = {}
            annot_d = {}
            tick = {}
            if isinstance(time, list):
                for nested in time:
                    d = dict(Task = "Gantt", Subtask = pid, Start = nested[0], Finish = nested[1], Resource= pid)
                    df.append(d)
                    d = {}
                    annot_d = dict(x=(nested[0]+nested[1])/2, text = pid, showarrow=False, font = dict(color = 'black', size =40))
                    annots.append(annot_d)
                    annot_d = {}
                    tick = dict(x=nested[1], y = -0.5,  text = str(nested[1]), showarrow = False, font = dict(color='red',size = 32 ) )
                    annots.append(tick)
                    tick = {}
                    
            else : 
                d = dict(Task = "Gantt", Subtask = pid, Start = time[0], Finish = time[1], Resource = pid)
                df.append(d)
                annots.append(annot_d)
                annots.append(tick)
               
        annots.append(dict(x=0, y = -0.5, text = '0',  showarrow = False, font = dict(color='red',size = 32 )))
        self.fig = ff.create_gantt(df, index_col = 'Subtask', group_tasks = True)
        self.fig.update_layout(
            xaxis_type = 'linear', 
            showlegend = True, 
            xaxis = dict(
                showticklabels = True,
                showgrid = True,
                gridcolor = 'gray',
                linecolor = 'gray',
            )
        )
        
        self.fig.layout.xaxis['tickfont'] = {'size': 40}

        self.fig['layout'].update(
            annotations= annots
        )
        
        #self.fig.show()
        if not os.path.exists(os.path.join(path, 'html')):
            os.makedirs(os.path.join(path, 'html'))

        filepath = os.path.join(path, 'html/image_' + ver +'.html')
        pio.write_html(self.fig, filepath)
        filename = os.path.join(path,'image/'+ ver +'.png')

        with open(filepath) as f:
            if ver == 'FCFS':
                hti.screenshot(f.read(), save_as = 'image_FCFS.png')
                f.close()
            elif ver == 'PP' :
                hti.screenshot(f.read(), save_as = 'image_PP.png')
                f.close() 
            elif ver == 'PRR' :
                hti.screenshot(f.read(), save_as = 'image_PRR.png')
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
            elif ver == 'SRTF':
                hti.screenshot(f.read(), save_as = 'image_SRTF.png')
                f.close()
