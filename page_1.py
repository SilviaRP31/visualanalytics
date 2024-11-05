st.set_page_config(
page_title="My first app with Streamlit in Visual Analytics",
page_icon="🧊",
layout="wide",
initial_sidebar_state="expanded",
menu_items={
'Get Help': 'https://upf.edu/help',
'Report a bug': "https://upf.edu/bug",
'About': "# This is a header. This is *my first app*!"
}
)

#Text input
title = st.text_input('Name of your favorite movie')
st.write('The current movie title is', title)


#Number input
number = st.number_input('Insert a number')
st.write('The current number is ', number)


#Date input
import datetime
d = st.date_input(
"When's your birthday",
datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
