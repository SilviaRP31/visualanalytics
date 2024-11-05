
def expensive_computation(a, b):
st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
time.sleep(10) # 👈 This makes the function take 10s to run
return a * b+1
a = 3
b = 210
res = expensive_computation(a, b)
st.write("Result:", res)

@st.cache_data()
def expensive_computation_3(a, b):
st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
time.sleep(5) # This makes the function take 2s to run
return a * b
a = 2
b = st.slider("Pick a number", 0, 10) # 👈 Changed this


res = expensive_computation_3(a, b)
st.write("Result:", res)