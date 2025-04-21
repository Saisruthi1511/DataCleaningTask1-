# Data Cleaning and Preprocessing Task

This repository contains the code and data used for the Data Cleaning and Preprocessing task.

## Task Description

The task was to clean and prepare a raw dataset. This involved handling missing values, removing duplicates, standardizing text, converting date formats, renaming columns, and fixing data types. 
## Dataset

The dataset used is the "Mall Customer Segmentation Data" obtained from Kaggle.


## Code

The Python code for the data cleaning process is in the file `data_cleaning.py`.

## Cleaning Steps Performed

1.  **Missing Values:** Checked for missing values using `isnull()` and handled them by filling numerical columns with the mean and categorical columns with the mode. 
2.  **Duplicate Rows:** Removed duplicate rows using `drop_duplicates()`. 
3.  **Standardized Text Values:** Standardized the 'Gender' column by converting all values to lowercase and removing extra spaces.
4.  **Date Formats:** *This dataset did not contain dates, so this step was not applicable.*
5.  **Renamed Column Headers:** Renamed columns to lowercase and replaced spaces with underscores for consistency (e.g., 'CustomerID' to 'customer\_id').
6.  **Fixed Data Types:** Checked and converted the 'customer\_id' column to integer type.
## Summary of Changes

* No missing values were found in the dataset.
* No duplicate rows were found in the dataset.
* The 'Gender' column was standardized.
* Column names were made consistent.
* The 'customer\_id' column was verified to be of integer type.

## How to Run the Code

1.  Make sure you have Python 3 and Pandas installed (`pip install pandas`).
2.  Place the `Mall_Customers.csv` file in the `data` subfolder.
3.  Run the `data_cleaning.py` script.

## Contact

[Saisruthi]
[saisruthivasudevan6@gmail.com]
