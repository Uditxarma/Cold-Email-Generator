import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text
from portfolio import Portfolio
from chains import Chain


def create_streamlit_app(chain, portfolio, clean_text):
    st.title("Cold Email Generator")
    url_input = st.text_input("Enter a URL: ")
    submit_button  =st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = chain.extract_data_from_description(data[:4000])

            for job in jobs:
                skills = job.get('skills', [])
                portfolio_urls = portfolio.query_links(skills)
                email = chain.write_mail(job, portfolio_urls)
                st.code(email, language="markdown")
        except Exception as e:
            st.error(f"An Error occured: {e}")


if __name__ == "__main__":
    chain= Chain()
    portfolio = Portfolio("sample_portfolio.csv")
    st.set_page_config(layout="wide", page_title="Cold Email Generator") #, page_icon="E")
    create_streamlit_app(chain, portfolio, clean_text)