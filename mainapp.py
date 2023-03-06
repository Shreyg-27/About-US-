import streamlit as st
from st_functions import st_button, load_css

st.title(':blue[OUR TEAM]')


st.header('**:black[FOUNDERS]**')

col1, col2, col3, col4 = st.columns(4)

icon_size = 20

with col1:
    st.image("Images/poojadinew.png")
    st.caption("Pooja Gera")
    st_button('linkedin', 'https://www.linkedin.com/in/pooja-gera/', 'LinkedIn', icon_size)


with col2:
    st.image("Images/NishthaDinew.png")
    st.caption("Nishtha Goyal")
    st_button('linkedin', 'https://www.linkedin.com/in/nishtha0801/', 'LinkedIn', icon_size)


with col3:
    st.image("Images/GaurishaDinew.png")
    st.caption("Gaurisha R Srivastava")
    st_button('linkedin', 'https://www.linkedin.com/in/gaurisha-r-srivastava/', 'LinkedIn', icon_size)

with col4:
    st.image("Images/AbhigyaDi.png")
    st.caption("Abhigya Verma")
    st_button('linkedin', 'https://www.linkedin.com/in/abhigya02/', 'LinkedIn', icon_size)



st.write("Celestial Biscuit is here to carry forward the ideology of problem solving and innovation with technology for the "
         "greater good in our minds, hearts and souls. We are a bunch of enthusiastic people from IGDTUW who are passionate "
         "about what we do and take pride in our university, our work and our profession. We are the people who believe in the "
         "fact that change is something that doesn't come just by dreaming about it but comes by working hard for it to make it "
         "a true reality.")

st.header('**:black[MEMBERS]**')

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.image("Images/ShreyaGanjoo.jpeg")
    st.caption("Shreya Ganjoo")
    st_button('linkedin', 'https://www.linkedin.com/in/shreya-ganjoo-30563822b/', 'LinkedIn', icon_size)

    st.image("Images/ShreyaGanjoo.jpeg")
    st.caption("Khyati Gupta")
    st_button('linkedin', 'https://www.linkedin.com/in/khyatigupta369/', 'LinkedIn', icon_size)

with col6:
    st.image("Images/KashikaDi.jpg")
    st.caption("Kashika Jain")
    st_button('linkedin', 'https://www.linkedin.com/in/kashika18/', 'LinkedIn', icon_size)

    st.image("Images/ShreyaGanjoo.jpeg")
    st.caption("Khushi Jain")
    st_button('linkedin', 'https://www.linkedin.com/in/abhigya02/', 'LinkedIn', icon_size)

with col7:
    st.image("Images/JahnaviDi.jpg")
    st.caption("Jahnavi Malhotra")
    st_button('linkedin', 'https://www.linkedin.com/in/jahnavi2k/', 'LinkedIn', icon_size)

    st.image("Images/ShreyaGanjoo.jpeg")
    st.caption("Khushi Sinha")
    st_button('linkedin', 'https://www.linkedin.com/in/khushi-sinha-91731b202/', 'LinkedIn', icon_size)

with col8:
    st.image("Images/AnushkaAggarwal.png")
    st.caption("Anushka Agarwal")
    st_button('linkedin', 'https://www.linkedin.com/in/anushka-aggarwal-26963b228/', 'LinkedIn', icon_size)



