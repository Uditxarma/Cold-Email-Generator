from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.1,
            max_tokens=3000,
            max_retries=2,
        )
    
    def extract_data_from_description(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template("""
            I will give you scraped text from the job posting. 
            Your job is to extract the job details & requirements in a JSON format containing the following keys: 'role', 'experience', 'skills', and 'description'. 
            Only return valid JSON. No preamble, please.
            Here is the scraped text: {cleaned_text}
        """)

        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke(input={'cleaned_text': cleaned_text})

        try:
            parser = JsonOutputParser()
            response = parser.parse(response.content[:2000])
        except OutputParserException:
            raise OutputParserException('Content is too big, unable to parse jobs')

        return response if isinstance(response, list) else [response]                       # If it's not a list (e.g., a dictionary or a string), wrap it in a list and then return it.
    

    def write_mail(self, job_description, portfolio_urls):
        prompt_email = PromptTemplate.from_template(
            """
            I will give you a role and a task that you have to perform in that specific role.
            Your Role: Your name is Udit Sharma, You are an incredible business development officer who knows how to get clients. You work for Kush_venture, your firm works with all sorts of IT clients and provide solutions in the domain of Data Science and AI. 
            Kush Venture focuses on efficient tailored solutions for all clients keeping costs down.Your contact number is 7906619557. 
            Your Job: Your Job is to write cold emails to clients regarding the Job openings that they have advertised. Try to pitch your clients with an email hook that opens a conversation about a possibility of working with them. Add the most relevant portfolio URLs from
            the following (shared below) to showcase that we have the right expertise to get the job done. If client name and resource missing, find a good way to address.
            Don't do things:
                1. Only use available information
                3. If infomation is missing, find alternate way to present, but don't make it noticeble in occured way
            I will now provide you with the Job description and the portfolio URLs:
            JOB DESCRIPTION: {job_description}
            ------
            PORTFOLIO URLS: {portfolio_urls}
            """
        )

        chain_email = prompt_email | self.llm
        response = chain_email.invoke(input={
            "job_description": str(job_description),
            "portfolio_urls": portfolio_urls
        })

        return response.content