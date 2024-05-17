import pandas as pd
import plotly.express as px
import streamlit as st

Df=pd.read_csv(r'C:\Users\kesav\Guvi\guvi main\Airbnb_data.csv')

Df['listing_id']=Df['listing_id'].astype(str)
Df['host_id']=Df['host_id'].astype(str)
# Using columns layout to display select boxes adjacent to each other

def data():
    col1, col2, col3,col4 = st.columns(4)
    # Select Country
    with col1:
        country=st.selectbox('select Country',Df['country'].unique())
    # Select Property Type
    with col2:   
        property=st.selectbox('select property type',Df['property_type'].unique())
    # Select Room Type
    with col3:
        room_type=st.selectbox('select  room type',Df['room_type'].unique())
    with col4:
# Price range slider
        min_price= Df['price'].min()
        max_price = Df['price'].max()
        price_range = st.slider('Select price range:', min_value=min_price, max_value=max_price, value=(9.0,48842.0), step=50.0)
        st.write(price_range)

    d1=Df[(Df['property_type']==property) & 
          (Df['room_type']==room_type) & 
          (Df['country']==country) & 
          (Df['price'] >= price_range[0]) & 
          (Df['price'] <= price_range[1])].reset_index(drop=True)
    st.write(d1)
    

def World_map():
    fig = px.scatter_geo(Df, lat=Df['latitude'], lon=Df['longitude'], hover_name=Df['country'],
                         color=Df['price'], color_continuous_scale='Viridis')
    
# Display the map in Streamlit
    st.plotly_chart(fig)

# Creating a function for map visualisation
def map():
    col1, col2, col3 = st.columns(3)
    # Select Country
    with col1:
        country=st.selectbox('select Country',Df['country'].unique())
    # Select Property Type
    with col2:   
        property=st.selectbox('select property type',Df['property_type'].unique())
    # Select Room Type
    with col3:
        room_type=st.selectbox('select  room type',Df['room_type'].unique())
    d1=Df[(Df['property_type']==property) & (Df['room_type']==room_type) & (Df['country']==country)].reset_index(drop=True)
    fig = px.scatter_geo(d1, lat=d1['latitude'], lon=d1['longitude'], hover_name=d1['country'],color=d1['price'], color_continuous_scale='Viridis',projection='natural earth')
    
    # Display the map in Streamlit
    st.plotly_chart(fig)
# Creating a function for bar chart visualisation   
def chart():
    col1, col2 = st.columns(2)
    # Select Country
    #with col1:
        #country=st.selectbox('select Country',Df['country'].unique())
    # Select Property Type
    with col1:   
        property=st.selectbox('select property type',Df['property_type'].unique())
    # Select Room Type
    with col2:
        room_type=st.selectbox('select  room type',Df['room_type'].unique())
        #(Df['country']==country) & 
    d2=Df[(Df['property_type']==property) & (Df['room_type']==room_type)] .reset_index(drop=True)

    # Calculate average price for each country
    avg_prices = d2.groupby('country')['price'].mean().reset_index().sort_values(by='price', ascending=False)

    # Plot bar chart
    bar = px.bar(avg_prices, x='country', y='price', labels={'x': 'Country', 'y': 'Average Price'}, title='Country vs Average Price')
    st.plotly_chart(bar)
    
# Create a list of items
def visual():
    items = ['Table', 'Map', 'Chart','World_map']

    # Display a selectbox to choose an item
    selected_item = st.sidebar.selectbox('Select the type of data to visualize:', items)

    # Define content for each item
    item_content = {
        'Table':data,
        'Map':map,
        'Chart':chart,
        'World_map':World_map
    }

    # Display the content corresponding to the selected item

    st.write('Selected the type of data to view:',selected_item)
    item_content[selected_item]()
def home():
    
    st.image(r'C:\Users\kesav\Guvi\guvi main\airbnb_logo.jpeg', caption='logo', use_column_width=True)
    st.title('Project done by KESAVAPRASAD')
def about():
    st.title('History of airbnb')
    st.image(r'C:\Users\kesav\Guvi\guvi main\AIRBNB-history.webp')
    st.image(r'C:\Users\kesav\Guvi\guvi main\Why-Is-It-Called-Airbnb-.webp')
    st.title("Business model of Airbnb")
    st.image(r"C:\Users\kesav\Guvi\guvi main\airbnb-business-model-2.webp")

page = ['home','About airbnb','visual']
selected_page = st.sidebar.selectbox('Select a page:', page)
page_details = {
        'home':home,
        'visual':visual,
        'About airbnb':about
        
    }

page_details[selected_page]()


