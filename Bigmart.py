import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')


# loading the saved model
loaded_model = pickle.load(open('C:/Users/ankit/OneDrive/Desktop/streamlit_dashboard/trained_model_big.pkl'
                                , 'rb'))

def main():

    # giving a title
    st.title('Big Mart Sales Prediction')

    # getting the input data from the user

    Item_wgt = st.text_input('Weight of the Product')
    Item_fat = st.text_input('product is low on fat or not')
    Item_Visibility = st.text_input('percentage of total display area')
    Item_MRP = st.text_input('Maximum Retail Price of the product')

    Outlet_Size = st.text_input('Outlet Size')
    Outlet_Location_Type = st.text_input('Location Type of Outlet')
    Outlet_Type = st.text_input('Type of Outlet')
    Item_Type_Combined = st.text_input('Type of Item')
    Outlet = st.text_input('Outlet')

    # creating a button for Prediction

    if st.button('Outlet Sales Result'):
        price_prediction = loaded_model.predict(
            [[Item_wgt,Item_fat,Item_Visibility,Item_MRP,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Type_Combined,Outlet]])

        output = round(price_prediction[0], 2)
        st.success("Price of Product is {}".format(output))


if __name__ == '__main__':
    main()

