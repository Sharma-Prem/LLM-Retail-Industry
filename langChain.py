import os
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mssql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from fewShots import fewShots

load_dotenv()

def get_few_shot_db_chain():
    llm = GooglePalm(google_api_key=os.getenv("google_api_key"), temperature=0.1)

    server = os.getenv("server")
    database = 't_shirts_store'
    driver = os.getenv("driver")
    db = SQLDatabase.from_uri(f'mssql://@{server}/{database}?driver={driver}', sample_rows_in_table_info=3)
    
    embeddings = HuggingFaceEmbeddings()
    toVectorize = [" ".join(item.values()) for item in fewShots]
    vectorStore = Chroma.from_texts(toVectorize, embedding=embeddings, metadatas=fewShots)

    exampleSelector = SemanticSimilarityExampleSelector(
        vectorstore=vectorStore,
        k=2
    )

    examplePrompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )

    fewShotPrompt = FewShotPromptTemplate(
        example_selector=exampleSelector,
        example_prompt=examplePrompt,
        prefix=_mssql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"] 
    )

    Chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=fewShotPrompt)
    return Chain


if __name__ == "__main__":
    chain = get_few_shot_db_chain()
    print(chain.run("What are the unique brands in the dataset?"))