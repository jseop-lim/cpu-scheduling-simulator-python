import plotly.figure_factory as ff
data = {
    "P0" : [(0,2) ,(10,15)],
    "P1" : [(2,3),(4,7)],
    "P2" : [(3,4)],
    "P3" : [(7,10)]
}

"""
df = [
    dict(Task = "Gantt", Subtask = "P0", Start=0, Finish = 2, Resource = "P0"),
    dict(Task = "Gantt", Subtask = "P1", Start=2, Finish = 3, Resource = "P1"),
    dict(Task = "Gantt", Subtask = "P2", Start=3, Finish = 4, Resource = "P2"),
    dict(Task = "Gantt", Subtask = "P1", Start=4, Finish = 7, Resource = "P1"),
    dict(Task = "Gantt", Subtask = "P3", Start=7, Finish = 10, Resource = "P3"),
    dict(Task = "Gantt", Subtask = "P0", Start=10, Finish = 15, Resource = "P0")
]
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

