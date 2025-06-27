# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader
# from utils import clean_text
# from portfolio import Portfolio
# from chains import Chain


# def create_streamlit_app(chain, portfolio, clean_text):
#     st.title("Cold Email Generator")
#     url_input = st.text_input("Enter a URL: ")
#     submit_button  =st.button("Submit")

#     if submit_button:
#         try:
#             loader = WebBaseLoader([url_input])
#             data = clean_text(loader.load().pop().page_content)
#             portfolio.load_portfolio()
#             jobs = chain.extract_data_from_description(data[:4000])

#             for job in jobs:
#                 skills = job.get('skills', [])
#                 portfolio_urls = portfolio.query_links(skills)
#                 email = chain.write_mail(job, portfolio_urls)
#                 st.code(email, language="markdown")
#         except Exception as e:
#             st.error(f"An Error occured: {e}")


# if __name__ == "__main__":
#     chain= Chain()
#     portfolio = Portfolio("sample_portfolio.csv")
#     st.set_page_config(layout="wide", page_title="Cold Email Generator") #, page_icon="E")
#     create_streamlit_app(chain, portfolio, clean_text)


import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text
from portfolio import Portfolio
from chains import Chain


def create_streamlit_app(chain, portfolio, clean_text):
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="✉️")
    st.title("✉️ Cold Email Generator")
    st.markdown("Generate personalized cold emails from job postings — powered by LLMs and vector search.")

    st.markdown("### 🔗 Enter a Job Posting URL")
    url_input = st.text_input("Paste job URL here", placeholder="https://example.com/job-posting")

    submit_button = st.button("🚀 Generate Email")

    if submit_button and url_input:
        with st.spinner("Processing... Please wait."):
            try:
                # Load and clean job data
                loader = WebBaseLoader([url_input])
                raw_data = loader.load().pop().page_content
                cleaned_data = clean_text(raw_data)

                # Load portfolio and extract job info
                portfolio.load_portfolio()
                jobs = chain.extract_data_from_description(cleaned_data[:4000])

                # Display results
                if not jobs:
                    st.warning("No jobs were extracted from the content.")
                for job in jobs:
                    skills = job.get('skills', [])
                    portfolio_urls = portfolio.query_links(skills)
                    email = chain.write_mail(job, portfolio_urls)

                    st.markdown("#### 📬 Generated Email")
                    st.markdown(email.replace("\n", "  \n"))

                st.success("✅ Email(s) generated successfully!")

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
    elif submit_button and not url_input:
        st.warning("⚠️ Please enter a valid URL before submitting.")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio("sample_portfolio.csv")
    create_streamlit_app(chain, portfolio, clean_text)
