# Text Similarity ETL
Text similarity explores an algorithm that detects and measures the similarities between text bodies and documents.

### **What it does**
This python application is designed as a mini-ETL operation to create tables in a PostgreSQL database and ingest raw txt files in the *input_texts* table. It also compares 2 texts and calculates the jaccard similarity and cosine similarity. A score closer to 0 means more dissimilar whereas a score nearer to 1 showcases a higher degree of similarity. The scores of each individual comparison between 2 texts is ingested as a record in the *textsim_metrics* table.

### **Design Choice**
Considering the scope of the challenge I chose to wrap this challenge as a basic ETL operation as it simulates the transformation and load process of stored raw data files.

### **Getting Started**
Before you start, make sure you have a recent version of Python 3, pip and PostgreSQL installed. 

#### <u>*Setting up the database in PostgreSQL*</u>
You can download PostgreSQL [here](https://www.postgresql.org/download/) for your OS and follow the setup instructions. 

Once you have PostgreSQL installed and are connected to a DB server you can use your favorite IDE (pgAdmin, DBeaver, Azure Data Studio etc.) to create a database. Open a query window and execute the following:
```SQL
CREATE DATABASE textsimilarity;
```
#### <u>*Setting up the virtual environment*</u>
Open a terminal and clone this repository.
```git
git clone <repository_name>
```
Navigate to the cloned directory from your terminal with cd. Then set up your virtual environment in python. If you don't have a virtual environment package on your system, you can install it as such:
```
pip install virtualenv
```
Create it as such:
```
virtualenv tsenv
```
and then activate it:
```
source tsenv/bin/activate
```
To deactivate, simply type ```deactivate``` in your terminal.

#### <u>*Installing packages*</u>
- cd into the directory where **requirements.txt** is located.
- Make sure your virtual environment is activated
- run this command in your terminal: 
```
pip install -r requirements.txt
```
#### <u>*Environment variables*</u>
In your main directory create a .env file using this terminal command:
```
touch .env
```
The next step is to open the .env file and add your postgreSQL credentials. You'll need the host, database name, user name and password. You won't need quotes to stringify. 

```
PGHOST=
PGDBNAME=
PGUSERNAME=
PGPASSWORD=
```
#### <u>*Running the ETL*</u>
Once all previous steps are completed, you can start running the ETL from the terminal. 

1. In your terminal run command below. This will create the tables in your database.
```
python create_tables.py
```
2. Then run:
```
python ingest.py
```
If everything is correct, you'll find the results in your database by querying the tables as such:
```SQL
SELECT * FROM  input_texts;

SELECT * FROM textsim_metrics;
```

### Resources
- [NLTK](https://github.com/nltk/nltk)
- Geeks for Geeks: Measuring the document similarity in Python [link](https://www.geeksforgeeks.org/measuring-the-document-similarity-in-python/)
- Jaccard Index [link](https://www.statisticshowto.com/jaccard-index/)