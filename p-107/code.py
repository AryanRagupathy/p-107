import csv
import pandas as pd
import plotly.express as px

px.defaults.template = "plotly_dark"

df = pd.read_csv("data.csv")

grouped_mean = df.groupby(["Student ID", "Level"], as_index = False)["Attempt"].mean()


chart = px.scatter(grouped_mean,
                x = "Student ID",
                y = "Level",
                size = "Attempt",
                color = "Attempt",
                title = "Performance of Students in each Chapter",
                )

chart.update_layout(
                font_family="Papyrus, fantasy",
                title_x = 0.5,
                font_size = 20,
                title_font_size = 30,
               
                )



chart.show()
