import streamlit as st
from utils import icon

st.set_page_config("All column types", "🏛️")
icon("🏛️")
"""
# All column types

This page shows all column types with some examples. Please also look at [the docs](https://docs.streamlit.io/library/api-reference/data/st.column_config).

"""
st.header("Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "widgets": st.column_config.Column(
                "Streamlit Widgets",
                help="Streamlit **widget** commands 🎈",
                width="medium",
                required=True,
            )
        },
        hide_index=True,
        num_rows="dynamic",
    )


st.header("Text Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "widgets": st.column_config.TextColumn(
                "Widgets",
                help="Streamlit **widget** commands 🎈",
                default="st.",
                max_chars=50,
                validate="^st\.[a-z_]+$",
            )
        },
        hide_index=True,
    )

st.header("Number Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "price": [20, 950, 250, 500],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "price": st.column_config.NumberColumn(
                "Price (in USD)",
                help="The price of the product in USD",
                min_value=0,
                max_value=1000,
                step=1,
                format="$%d",
            )
        },
        hide_index=True,
    )

st.header("Checkbox Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
            "favorite": [True, False, False, True],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "favorite": st.column_config.CheckboxColumn(
                "Your favorite?",
                help="Select your **favorite** widgets",
                default=False,
            )
        },
        disabled=["widgets"],
        hide_index=True,
    )

st.header("Selectbox Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "category": [
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
                "📊 Data Exploration",
            ],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "category": st.column_config.SelectboxColumn(
                "App Category",
                help="The category of the app",
                width="medium",
                options=[
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "🤖 LLM",
                ],
            )
        },
        hide_index=True,
    )


st.header("Datetime Column")
with st.echo():
    from datetime import datetime

    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "appointment": [
                datetime(2024, 2, 5, 12, 30),
                datetime(2023, 11, 10, 18, 0),
                datetime(2024, 3, 11, 20, 10),
                datetime(2023, 9, 12, 3, 0),
            ]
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "appointment": st.column_config.DatetimeColumn(
                "Appointment",
                min_value=datetime(2023, 6, 1),
                max_value=datetime(2025, 1, 1),
                format="D MMM YYYY, h:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )


st.header("Time Column")
with st.echo():
    from datetime import time

    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "appointment": [
                time(12, 30),
                time(18, 0),
                time(9, 10),
                time(16, 25),
            ]
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "appointment": st.column_config.TimeColumn(
                "Appointment",
                min_value=time(8, 0, 0),
                max_value=time(19, 0, 0),
                format="hh:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )

st.header("Date Column")
with st.echo():
    from datetime import date

    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "birthday": [
                date(1980, 1, 1),
                date(1990, 5, 3),
                date(1974, 5, 19),
                date(2001, 8, 17),
            ]
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "birthday": st.column_config.DateColumn(
                "Birthday",
                min_value=date(1900, 1, 1),
                max_value=date(2005, 1, 1),
                format="DD.MM.YYYY",
                step=1,
            ),
        },
        hide_index=True,
    )

st.header("Link Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "apps": [
                "https://roadmap.streamlit.app",
                "https://extras.streamlit.app",
                "https://issues.streamlit.app",
                "https://30days.streamlit.app",
            ],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.LinkColumn(
                "Trending apps",
                help="The top trending Streamlit apps",
                validate="^https://[a-z]+\.streamlit\.app$",
                max_chars=100,
            )
        },
        hide_index=True,
    )

st.header("List Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "sales": [
                [0, 4, 26, 80, 100, 40],
                [80, 20, 80, 35, 40, 100],
                [10, 20, 80, 80, 70, 0],
                [10, 100, 20, 100, 30, 100],
            ],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.ListColumn(
                "Sales (last 6 months)",
                help="The sales volume in the last 6 months",
                width="medium",
            ),
        },
        hide_index=True,
    )

st.header("Line Chart Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "sales": [
                [0, 4, 26, 80, 100, 40],
                [80, 20, 80, 35, 40, 100],
                [10, 20, 80, 80, 70, 0],
                [10, 100, 20, 100, 30, 100],
            ],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.LineChartColumn(
                "Sales (last 6 months)",
                width="medium",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )

st.header("Bar Chart Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "sales": [
                [0, 4, 26, 80, 100, 40],
                [80, 20, 80, 35, 40, 100],
                [10, 20, 80, 80, 70, 0],
                [10, 100, 20, 100, 30, 100],
            ],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.BarChartColumn(
                "Sales (last 6 months)",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )


st.header("Progress Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "sales": [200, 550, 1000, 80],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.ProgressColumn(
                "Sales volume",
                help="The sales volume in USD",
                format="$%f",
                min_value=0,
                max_value=1000,
            ),
        },
        hide_index=True,
    )

st.header("Image Column")
with st.echo():
    import pandas as pd
    import streamlit as st

    data_df = pd.DataFrame(
        {
            "apps": [
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
            ],
        }
    )

    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots"
            )
        },
        hide_index=True,
    )
