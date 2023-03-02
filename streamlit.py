import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similrity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similrity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommerder System")

select_movie_name=st.selectbox(
    "Do you want to watch movie?? I am here to recommend!",
    movies["title"].values
)

if st.button('Recommend'):
    recommendations=recommend(select_movie_name)
    for i in recommendations:
        st.write(i)