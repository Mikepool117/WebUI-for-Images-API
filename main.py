import streamlit as st
import openai

#Enter Your API Key You Generated here 
openai.api_key = < ENTER YOUR API KEY HERE >

#Setup Page Title
st.set_page_config(
   page_title="DALL·E WebUI",
   initial_sidebar_state="expanded"
)

#UI Components
st.title('DALL·E WebUI')
st.subheader("Generate an image using the Images API")
prompt_text = st.text_input("Enter a prompt : ")

#Stack Two UI Components Together
col1, col2 = st.columns(2)
with col1 :
    #set the max number of images equal to your rate limit
    number_of_images = st.slider('Select the number of images to be generated : ', 1, 5, 1)
with col2 :
    image_size = st.selectbox(
    'Select the size of the image to be generated : ',
    ('256x256', '512x512', '1024x1024'))


#Use a button to initiate API call and use an try except clause to catch any errors
if st.button('Generate Image') :
    try :
        with st.spinner('Generating Image') :
            response = openai.Image.create(
            prompt=prompt_text,
            n=number_of_images,
            size=image_size
            )
            for i in range(number_of_images) :
                with st.expander("View Image") :
                    st.image(response['data'][i]['url'])
    except :
      #show this instead of an error when you hit the rate limit
        st.error("There was a problem with your request, Please try again in a minute.")
