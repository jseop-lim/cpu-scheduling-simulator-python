# importing module
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

"""
input은 dictionary형태로.
ex) 
data = {
    "P0" : [(0,2) ,(10,5)],
    "P1" : [(2,1),(4,3)],
    "P2" : [(3,1)],
    "P3" : [(7,3)]
}
이 때, 리스트 내의 튜플은 (시작시간, 실행시간) form.

"""
fig, gnt = plt.subplots()
gnt.set_ylim(0,10)

#테스트용 데이터
data = {
    "P0" : [(0,2),(10,5)],
    "P1" : [(2,1),(4,3)],
    "P2" : [(3,1)],
    "P3" : [(7,3)]
}

bar_input = []
bar_color = []

labels = list(data.keys())

category_colors = plt.get_cmap('Pastel1')(
    np.linspace(0.15, 0.85, len(labels))
)

colors_dict= {}
for (i, label) in enumerate(labels):
    colors_dict[label] = category_colors[i]

for pid, time in data.items():
    if isinstance(time, list):
        for nested in time:
            bar_input.append(nested)
            bar_color.append(colors_dict[pid])
    else:
        bar_input.append(time)
        bar_color.append(colors_dict[pid])


gnt.broken_barh(bar_input, (3,4), facecolors = tuple(bar_color))
# broken_barh의 경우 input과 facecolors가 리스트/튜플형태로 한 번에 주어져야 함. 
plt.show()

"""
def ganttChart(self):
    fig, gnt = plt.subplots()
    gnt.set_ylim(0,10)
    gnt.set_xlabel("Prcocess Time")
    bar_input = []
    bar_color = []

    labels = list(data.keys())

    category_colors = plt.get_cmap('Pastel1')(
        np.linspace(0.15, 0.85, len(labels))
    )

    colors_dict= {}
    for (i, label) in enumerate(labels):
        colors_dict[label] = category_colors[i]

    for pid, time in data.items():
        if isinstance(time, list):
            for nested in time:
                bar_input.append(nested)
                bar_color.append(colors_dict[pid])
        else:
            bar_input.append(time)
            bar_color.append(colors_dict[pid])

    #for i, (pid, color) in enumerate(zip(labels, category_colors)):
    #    gnt.broken_barh(bar_input, (3,4),  label = pid, facecolors = tuple(bar_color))

    gnt.broken_barh(bar_input, (3,4), facecolors = tuple(bar_color))
    plt.show()
    #plt.savefig('gantChart.png')
"""