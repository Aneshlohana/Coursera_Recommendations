import streamlit as st
import pickle
import pandas as pd 

def recommend(course):
    course_index = courses[courses['course_name'] == course].index[0]
    distances = similarity[course_index]
    course_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    
    recommend_courses = []
    for i in course_list:
        recommend_courses.append(courses.iloc[i[0]].course_name)

    return recommend_courses    


courses_dict = pickle.load(open('courses_dict.pkl', 'rb'))
courses  = pd.DataFrame(courses_dict)# create streamlit app

similarity = pickle.load(open('similiarity.pkl', 'rb'))

st.title('Course Recommendation System :)')

selected_course_name = st.selectbox('Select a course', courses['course_name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_course_name)
    for i in recommendations:
        st.write(i)