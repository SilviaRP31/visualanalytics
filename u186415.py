import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

# 4: Add a title and subheader
st.title('This is an example of title')
st.subheader("This is an example of subheader")
st.write("This is an example of a sentence")

# 7: Add sidebar and emoticons
st.write("This streamlit app adds *different formats* and icons like :sunglasses: and :snow_cloud:")
st.sidebar.header("The header of the sidebar")
st.sidebar.write("*Hello*")

# 8: Create a dataframe and plot charts
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.write("This is a line chart")
st.line_chart(chart_data)
st.write("This is an area chart")
st.area_chart(chart_data)
st.write("This is a bar chart")
st.bar_chart(chart_data)

# 9: Matplotlib and Seaborn plots
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.write("Example 1 of a plot with Matplotlib")
st.pyplot(fig)

penguins = sns.load_dataset("penguins")
st.dataframe(penguins[["species", "flipper_length_mm"]].sample(6))
fig = plt.figure(figsize=(9, 7))
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plt.title("Hello Penguins!")
st.write("Example of a plot with Seaborn library")
st.pyplot(fig)

# 11: Create maps and Plotly plots
df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.write("Example of a plot with a map")
st.map(df)

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
st.write("Example of a plot with Plotly")
st.plotly_chart(fig, use_container_width=True)

# 14: Add widgets (buttons, checkboxes, sliders)
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# 15: Text and number input widgets
title = st.text_input('Name of your favorite movie')
st.write('The current movie title is', title)

number = st.number_input('Insert a number')
st.write('The current number is ', number)

# 15: Date input
d = st.date_input("When's your birthday", date(2019, 7, 6))
st.write('Your birthday is:', d)

#18: Caching and session state
@st.cache_data()
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    t.sleep(10)
    return a * b + 1

a = 3
b = 210
res = expensive_computation(a, b)
st.write("Result:", res)

# 21-22: Session state with callbacks
if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input('Enter a value', value=0, step=1)

def increment_counter(increment_value):
    st.session_state.count += increment_value

st.button('Increment', on_click=increment_counter, args=(increment_value,))
st.write('Count =', st.session_state.count)
