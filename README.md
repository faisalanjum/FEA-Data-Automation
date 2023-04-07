# FEA-Data-Automation
This repository contains scripts for automating the retrieval and storage of economic data for a financial firm. The scripts are designed to pull data from the Federal Reserve Economic Data (FRED) API, process it, and store it in a PostgreSQL database for later use.

## Installation
- Clone the repository: git clone https://github.com/faisalanjum/FEA-Data-Automation.git.
- Install the required Python libraries: pip install -r requirements.txt.
## Configuration
- The following environmental variables must be set in order to use the scripts:

-- API_KEY: your FRED API key.
-- API_ROOT_URL: the root URL for the FRED API (usually https://api.stlouisfed.org).
-- DB_HOST: the hostname for the PostgreSQL database.
-- DB_PORT: the port number for the PostgreSQL database.
-- DB_NAME: the name of the PostgreSQL database.
-- DB_USER: the username for the PostgreSQL database.
-- DB_PASSWORD: the password for the PostgreSQL database.
## Usage
- The main script for pulling and storing data is populate.py. This script takes a number of command-line arguments that specify the data to be pulled and the time period to be covered. For example, to pull quarterly data for the Gross Domestic Product (GDP) from 2000 to 2020, use the following command:
-- python populate.py GDP Q 2000-01-01 2020-01-01
-- This will retrieve the data, process it, and store it in the PostgreSQL database. The data can then be accessed using the models defined in the models.py file.





