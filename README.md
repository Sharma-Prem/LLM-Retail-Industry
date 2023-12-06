# KRaZy Boys Tees: Talk to a Database  

This is an end to end LLM project based on Google Palm and Langchain. It is a system that can talk to MSSQL database. 
User asks questions in a natural language and the system generates answers by converting those questions to an SQL query and
then executing that query on MSSQL database. 
KRaZy Boys Tees is a T-shirt store where they maintain their inventory, sales and discounts data in MSSQL database. A store manager 
will may ask questions such as,
- How many white color Adidas t shirts do we have left in the stock?
- How much sales our store will generate if we can sell all extra-small size t shirts after applying discounts?
The system is intelligent enough to generate accurate queries for given question and execute them on MSSQL database

## Project Highlights

- KRaZy Boys Tees is a t shirt store that sells Adidas, Nike, Van Heusen and Levi's t shirts 
- Their inventory, sales and discounts data is stored in a MSSQL database
- We will build an LLM based question and answer system that will use following,
  - Google Palm LLM
  - Hugging face embeddings
  - Streamlit for UI
  - Langchain framework
  - Chromadb as a vector store
  - Few shot learning
- In the UI, store manager will ask questions in a natural language and it will produce the answers

## Sample Questions
  - How many total t shirts are left in total in stock?
  - How many t-shirts do we have left for Nike in XS size and white color?
  - How much is the total price of the inventory for all S-size t-shirts?
  - How much sales amount will be generated if we sell all small size adidas shirts today after discounts?
  - What are the unique brands in the dataset?
  - What is the total stock quantity for each brand?
  - Which brand has the highest stock quantity?
  - Which brand has the lowest stock quantity?
  - What are the unique colors available in the stock?
  - How many items are available for each color?
  - What are the unique sizes available in the stock?
  - How many items are available for each size?
  - What is the average price of the items?
  - Which item has the highest price?
  - Which item has the lowest price?
  - What is the overall stock quantity in the store?
  - What is the average stock quantity for each brand?
  - Which item has the highest price-to-stock quantity ratio?
  - How many white color Levi T-shirt we have available?
  - How many t-shirts have associated discounts?
  - What is the average discount percentage?
  - What is the brand-color-size combination that has the highest average discount percentage?
  - What is the total value of the current stock, considering both original prices and applied discounts?
  - Is there a correlation between the size of a t-shirt and the average discount percentage applied?


## Project Structure

- main.py: The main Streamlit application script.
- langChain.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- fewShots.py: Contains few shot prompts
- .env: Configuration file for storing your Google API key, server name and driver name.But added in gitignore.
