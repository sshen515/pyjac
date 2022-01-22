import plotly.express as px

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# pie chart
with open("../transcript/tmp/tmp.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    grades_list = []
    courses = {}
    gpa = {}
    for line in lines:
        if "-----" in line or not line:
            continue
        elif "gpa" in line.lower():
            gpa_list = line.split(" ")
            gpa_list = [x for x in gpa_list if x != '' and x != 'GPA']
            if 'Sessional' not in gpa:
                gpa["Sessional"] = [gpa_list[1]]
            else:
                gpa["Sessional"].append(gpa_list[1])
            if 'Annual' in gpa_list:
                if 'Annual' not in gpa:
                    gpa["Annual"] = [gpa_list[3]]
                else:
                    gpa["Annual"].append(gpa_list[3])
                if 'Cumulative' not in gpa:
                    gpa["Cumulative"] = [gpa_list[5]]
                else:
                    gpa["Cumulative"].append(gpa_list[5])
            else:
                if 'Cumulative' not in gpa:
                    gpa["Cumulative"] = [gpa_list[3]]
                else:
                    gpa["Cumulative"].append(gpa_list[3])
        else:
            grades_list = line.split(" ")
            grades_list = [x for x in grades_list if x != '']
            if grades_list[0][:3] not in courses:
                courses[grades_list[0][:3]] = 1
            else:
                courses[grades_list[0][:3]] += 1

print(gpa, courses)

specs=[[{"type": "xy"}, {"type": "xy"}, {"type": "xy"}],
           [{"colspan": 3, "type": "pie"}, None, None]]

# specs=[[{'type':'scatter'}, {'type':'scatter'}, {'type':'scatter'}], [None, {'type':'pie'}, None]]
fig = make_subplots(rows=2, cols=3, specs=specs, subplot_titles=("Cumualtive GPA", "Annual GPA", "Sessional GPA", "CourseWise Breakdown"))

fig.add_trace(go.Scatter(x=[i for i in range(1,len(list(gpa['Sessional'])))], y=list(gpa['Sessional']), name='Sessional GPA', mode='lines+markers'), 1, 3)

fig.add_trace(go.Scatter(x=[i for i in range(1,len(list(gpa['Annual'])))], y=list(gpa['Annual']), name='Annual GPA', mode='lines+markers'), 1, 2)

fig.add_trace(go.Scatter(x=[i for i in range(1,len(list(gpa['Cumulative'])))], y=list(gpa['Cumulative']), name='Cumulative GPA', mode='lines+markers'), 1, 1)

fig.add_trace(go.Pie(labels=list(courses.keys()), values=list(courses.values()), name="Coursewise Breakdown"), 2, 1)

# fig.update_layout(height=1080, width=1920, title_text="CourseWise Breakdown")
fig.update_layout(autosize=True, title_text="Transcript Visualized")
fig.write_html("../visualizer/file.html", default_width='100%', default_height='100%', include_plotlyjs='cdn', include_mathjax='cdn')
        