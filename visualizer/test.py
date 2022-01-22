import plotly.express as px

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# pie chart
with open("C:/UTM/Winter2022/pyjac/transcript/tmp/tmp.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    grades_list = []
    courses = {}
    for line in lines:
        if "-----" in line:
            continue
        grades_list = line.split(" ")
        grades_list = [x for x in grades_list if x != '']
        if grades_list[0][:3] not in courses:
            courses[grades_list[0][:3]] = 1
        else:
            courses[grades_list[0][:3]] += 1


fig = make_subplots(rows=1, cols=1, specs=[[{"type": "pie"}]])
print(list(courses.keys()), list(courses.values()))

fig.add_trace(go.Pie(labels=list(courses.keys()), values=list(courses.values()), name="Coursewise Breakdown"),
              1, 1)

fig.update_layout(height=600, width=800, title_text="CourseWise Breakdown")
fig.write_html("C:/UTM/Winter2022/test/file.html")
        