"""
This module contains code used to create plot with clubs 
that are increasing value of football players most . 
"""
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_plot_club_increasing_value_at(position):
    df = pd.read_csv("data/club_value_increase.csv")
    df = df.sort_values(by="value_increase", ascending=False)

    df_att = df[df["position"] == "Attack"]

    df = pd.read_csv("data/club_value_increase.csv")
    df = df.sort_values(by="value_increase", ascending=False)

    df_att = df[df["position"] == "Attack"]

    fig = make_subplots(
        rows=1, cols=3, specs=[[{}, {}, {}]], shared_yaxes=False, vertical_spacing=0.001
    )


    

    fig.add_trace(
        go.Bar(
            x=df_att["value_increase"],
            y=list(range(10, 0, -1)),
            name="att",
            marker=dict(
                color="green",
                line=dict(color="green", width=1),
            ),
            orientation="h",
        ),
        1,
        1,
    )

    fig.update_layout(
        title="Top Football Clubs for Aspiring Young Attackers",
        title_font_size=30,
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            domain=[0, 0.95],
        ),
        yaxis2=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            domain=[0, 0.95],
        ),
        yaxis3=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            domain=[0, 0.95],
        ),
        xaxis=dict(
            zeroline=False,
            showline=False,
            showticklabels=False,
            showgrid=True,
            domain=[0, 0.3],
        ),
        xaxis2=dict(
            zeroline=False,
            showline=False,
            showticklabels=False,
            showgrid=True,
            domain=[0.33, 0.63],
        ),
        xaxis3=dict(
            zeroline=False,
            showline=False,
            showticklabels=False,
            showgrid=True,
            domain=[0.66, 0.96],
        ),
        showlegend=False,
        plot_bgcolor="white",
    )

    # add annotations
    for i in range(0, 10):
        for j, df in enumerate([df_att]):
            idx = 10 - i - 1
            fig.add_annotation(
                dict(
                    xref="x",
                    yref="y",
                    x=0,
                    y=i + 1,
                    text=df["club_name"].iloc[idx][:20],
                    font=dict(family="Arial", size=12, color="black"),
                    showarrow=False,
                    align="right",
                    xanchor="right",
                ),
                row=1,
                col=j + 1,
            )
            # add value to each bar
            fig.add_annotation(
                dict(
                    xref="x",
                    yref="y",
                    x=df["value_increase"].iloc[idx],
                    y=i + 1,
                    text=str(round(df["value_increase"].iloc[idx], 2)),
                    font=dict(family="Arial", size=12, color="black"),
                    showarrow=False,
                    align="left",
                    xanchor="left",
                ),
                row=1,
                col=j + 1,
            )

    return fig

if __name__ == "__main__":
    fig = create_plot_club_increasing_value_at("Attacker")
    fig.show()
    # save as html
    fig.write_html("images/attacker.html")