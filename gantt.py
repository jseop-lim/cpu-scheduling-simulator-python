
import plotly.figure_factory as ff
import plotly.io as pio
import os
path = os.path.dirname(os.path.abspath(__file__))

class Gantt:
    def __init__(self, data):
        self.data = data
        
    def create_gantt(self):
        labels = self.data.keys()
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
                    annot_d = dict(x=(nested[0]+nested[1])/2, text = pid, showarrow=False)
                    annots.append(annot_d)
                    annot_d = {}
            else:
                d = dict(Task = "Gantt", Subtask = pid, Start = time[0], Finish = time[1], Resource = pid)
                df.append(d)
                annots.append(annot_d)
        
        self.fig = ff.create_gantt(df, index_col = 'Subtask', group_tasks = True)
        self.fig.update_layout(xaxis_type = 'linear')

        self.fig['layout']['annotations'] = annots
        #self.fig.show()
    
    def create_image(self, ver):
        filename = os.path.join(path,'image/'+ver+'.png')
        #pio.write_image(self.fig, os.path.join(path, filename))
        pio.write_image(self.fig, filename)
"""
labels = data.keys()
df = []
annots = []
for pid, time in data.items():
    d = {}
    annot_d = {}
    if isinstance(time, list):
        for nested in time:
            d = dict(Task = "Gantt", Subtask = pid, Start = nested[0], Finish = nested[1], Resource = pid)
            df.append(d)
            d = {}
            annot_d = dict(x=(nested[0]+nested[1])/2, text = pid,showarrow =False)
            annots.append(annot_d)
            annot_d = {}
    else:
        d = dict(Task = "Gantt", Subtask = pid, Start = time[0], Finish = time[1], Resource = pid)
        df.append(d)
        annot_d = dict(x=(nested[0]+nested[1])/2, text = pid,showarrow =False)
        annots.append(annot_d)


fig = ff.create_gantt(df, index_col = 'Subtask', group_tasks = True)
fig.update_layout(xaxis_type = 'linear')

fig['layout']['annotations'] = annots
fig.show()
"""