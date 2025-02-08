import streamlit as st
import finnhub
import random

# Path for static images like error messages
image_path = "./static/Error.JPG"

# Link to Finnhub's website for users to create an account
fin_hub_page = "https://finnhub.io/"

def get_financial_news():
    """
    Fetches financial news from the Finnhub API using the provided client.
    Returns a list of financial news articles.
    """
    news = finnhub_client.general_news('general', {'category': 'financial'})
    return news

# Streamlit UI setup
st.title("Financial News Chatbot")

# Sidebar components
finnhub_api = st.sidebar.text_input("Finn Hub API key", type="password")
st.sidebar.markdown(f"[Create an account if you don't have one]({fin_hub_page})")
num_news = st.sidebar.selectbox("Select number of news to be displayed:", list(range(1, 10)))

# Initialize the Finnhub API client using the provided API key
finnhub_client = finnhub.Client(api_key=finnhub_api)

# Fetch and display the latest financial news when the button is pressed
if len(finnhub_api.strip()):
    if st.button('Get Latest Financial News'):
        try:
            # Attempt to fetch financial news
            financial_news = get_financial_news()
        except Exception as e:
            # If an error occurs, display an error message and an image
            st.error("An error occurred while getting financial news.")
            st.image(image_path, "Error Occurred")
            st.write("Error details:", e)  # Display error details
            financial_news = []  # Set financial news to an empty list on error
            num_news = 0  # No news to display
        if financial_news:
            # Randomly select the number of articles requested by the user
            news = random.sample(financial_news, num_news)
            # Display the selected news articles
            for news_item in news:
                title = news_item['headline']
                summary = news_item['summary']
                url = news_item['url']
                
                st.subheader(f"Title: {title}")
                st.write(f"Summary: {summary}")
                st.write(f"Read more: {url}")
                st.write(f"API key used: {finnhub_api}")  # Display API key (for demonstration)
        else:
            st.write("No financial news available.")
else:
    st.write("Please provide a valid API key.")  # Prompt user to enter a valid API key
