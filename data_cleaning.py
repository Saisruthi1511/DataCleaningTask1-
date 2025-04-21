{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b741b098-bb57-4737-8553-7f22d789e5a9",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pandas'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpd\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[38;5;66;03m# Load the dataset\u001b[39;00m\n\u001b[32m      4\u001b[39m data = pd.read_csv(\u001b[33mr\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mC:\u001b[39m\u001b[33m\\\u001b[39m\u001b[33mUsers\u001b[39m\u001b[33m\\\u001b[39m\u001b[33msai surth\u001b[39m\u001b[33m\\\u001b[39m\u001b[33mOneDrive\u001b[39m\u001b[33m\\\u001b[39m\u001b[33mDesktop\u001b[39m\u001b[33m\\\u001b[39m\u001b[33mMall_Customers.csv\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'pandas'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load the dataset\n",
    "data = pd.read_csv(r\"C:\\Users\\sai surth\\OneDrive\\Desktop\\Mall_Customers.csv\")\n",
    "\n",
    "# Display the first 5 rows\n",
    "print(data.head())\n",
    "\n",
    "# Get information about the DataFrame, including data types and non-null values\n",
    "print(data.info())\n",
    "\n",
    "# Get descriptive statistics of the numerical columns\n",
    "print(data.describe())\n",
    "\n",
    "# Check for missing values\n",
    "print(data.isnull().sum())\n",
    "\n",
    "# Display the shape of the DataFrame (number of rows and columns)\n",
    "print(data.shape)\n",
    "\n",
    "# Display the column names\n",
    "print(data.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1492cbfb-83d9-4a4c-b083-84c9886c1a54",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pandas'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'pandas'"
     ]
    }
   ],
   "source": [
    "import pandas\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4a8cdcab-58e5-492a-9a90-c14223bab60c",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pandas'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpd\u001b[39;00m\n\u001b[32m      3\u001b[39m data = pd.read_csv(\u001b[33m\"\u001b[39m\u001b[33mMall_Customers.csv\u001b[39m\u001b[33m\"\u001b[39m) \u001b[38;5;66;03m# Replace with your file path\u001b[39;00m\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'pandas'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = pd.read_csv(\"Mall_Customers.csv\") # Replace with your file path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9f41377e-5416-4b06-b6f5-dc04c39f3b29",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'Mall_Customers.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpd\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m data = \u001b[43mpd\u001b[49m\u001b[43m.\u001b[49m\u001b[43mread_csv\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mMall_Customers.csv\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m  \u001b[38;5;66;03m# Replace with your file path\u001b[39;00m\n\u001b[32m      4\u001b[39m \u001b[38;5;28mprint\u001b[39m(data.head()) \u001b[38;5;66;03m#testing to see if it works\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1026\u001b[39m, in \u001b[36mread_csv\u001b[39m\u001b[34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[39m\n\u001b[32m   1013\u001b[39m kwds_defaults = _refine_defaults_read(\n\u001b[32m   1014\u001b[39m     dialect,\n\u001b[32m   1015\u001b[39m     delimiter,\n\u001b[32m   (...)\u001b[39m\u001b[32m   1022\u001b[39m     dtype_backend=dtype_backend,\n\u001b[32m   1023\u001b[39m )\n\u001b[32m   1024\u001b[39m kwds.update(kwds_defaults)\n\u001b[32m-> \u001b[39m\u001b[32m1026\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_read\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:620\u001b[39m, in \u001b[36m_read\u001b[39m\u001b[34m(filepath_or_buffer, kwds)\u001b[39m\n\u001b[32m    617\u001b[39m _validate_names(kwds.get(\u001b[33m\"\u001b[39m\u001b[33mnames\u001b[39m\u001b[33m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[32m    619\u001b[39m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m620\u001b[39m parser = \u001b[43mTextFileReader\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    622\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[32m    623\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1620\u001b[39m, in \u001b[36mTextFileReader.__init__\u001b[39m\u001b[34m(self, f, engine, **kwds)\u001b[39m\n\u001b[32m   1617\u001b[39m     \u001b[38;5;28mself\u001b[39m.options[\u001b[33m\"\u001b[39m\u001b[33mhas_index_names\u001b[39m\u001b[33m\"\u001b[39m] = kwds[\u001b[33m\"\u001b[39m\u001b[33mhas_index_names\u001b[39m\u001b[33m\"\u001b[39m]\n\u001b[32m   1619\u001b[39m \u001b[38;5;28mself\u001b[39m.handles: IOHandles | \u001b[38;5;28;01mNone\u001b[39;00m = \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m-> \u001b[39m\u001b[32m1620\u001b[39m \u001b[38;5;28mself\u001b[39m._engine = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_make_engine\u001b[49m\u001b[43m(\u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mengine\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1880\u001b[39m, in \u001b[36mTextFileReader._make_engine\u001b[39m\u001b[34m(self, f, engine)\u001b[39m\n\u001b[32m   1878\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode:\n\u001b[32m   1879\u001b[39m         mode += \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m-> \u001b[39m\u001b[32m1880\u001b[39m \u001b[38;5;28mself\u001b[39m.handles = \u001b[43mget_handle\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   1881\u001b[39m \u001b[43m    \u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1882\u001b[39m \u001b[43m    \u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1883\u001b[39m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mencoding\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1884\u001b[39m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mcompression\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1885\u001b[39m \u001b[43m    \u001b[49m\u001b[43mmemory_map\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mmemory_map\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1886\u001b[39m \u001b[43m    \u001b[49m\u001b[43mis_text\u001b[49m\u001b[43m=\u001b[49m\u001b[43mis_text\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1887\u001b[39m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mencoding_errors\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mstrict\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1888\u001b[39m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43moptions\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mstorage_options\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1889\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   1890\u001b[39m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m.handles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m   1891\u001b[39m f = \u001b[38;5;28mself\u001b[39m.handles.handle\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\common.py:873\u001b[39m, in \u001b[36mget_handle\u001b[39m\u001b[34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[39m\n\u001b[32m    868\u001b[39m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[32m    869\u001b[39m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[32m    870\u001b[39m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[32m    871\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m ioargs.encoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mb\u001b[39m\u001b[33m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs.mode:\n\u001b[32m    872\u001b[39m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m873\u001b[39m         handle = \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\n\u001b[32m    874\u001b[39m \u001b[43m            \u001b[49m\u001b[43mhandle\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    875\u001b[39m \u001b[43m            \u001b[49m\u001b[43mioargs\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    876\u001b[39m \u001b[43m            \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[43mioargs\u001b[49m\u001b[43m.\u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    877\u001b[39m \u001b[43m            \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    878\u001b[39m \u001b[43m            \u001b[49m\u001b[43mnewline\u001b[49m\u001b[43m=\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[32m    879\u001b[39m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    880\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m    881\u001b[39m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[32m    882\u001b[39m         handle = \u001b[38;5;28mopen\u001b[39m(handle, ioargs.mode)\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'Mall_Customers.csv'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = pd.read_csv(\"Mall_Customers.csv\")  # Replace with your file path\n",
    "print(data.head()) #testing to see if it works\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5f8ea35f-24aa-4013-ab5d-aab40bf191af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   CustomerID  Gender  Age  Annual Income (k$)  Spending Score (1-100)\n",
      "0           1    Male   19                  15                      39\n",
      "1           2    Male   21                  15                      81\n",
      "2           3  Female   20                  16                       6\n",
      "3           4  Female   23                  16                      77\n",
      "4           5  Female   31                  17                      40\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 200 entries, 0 to 199\n",
      "Data columns (total 5 columns):\n",
      " #   Column                  Non-Null Count  Dtype \n",
      "---  ------                  --------------  ----- \n",
      " 0   CustomerID              200 non-null    int64 \n",
      " 1   Gender                  200 non-null    object\n",
      " 2   Age                     200 non-null    int64 \n",
      " 3   Annual Income (k$)      200 non-null    int64 \n",
      " 4   Spending Score (1-100)  200 non-null    int64 \n",
      "dtypes: int64(4), object(1)\n",
      "memory usage: 7.9+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Use the full file path\n",
    "data = pd.read_csv(\"C:/Users/sai surth/Downloads/Mall_Customers.csv\")  # Using forward slashes\n",
    "\n",
    "# Or, you can use a raw string:\n",
    "# data = pd.read_csv(r\"C:\\Users\\sai surth\\Downloads\\Mall_Customers.csv\")\n",
    "\n",
    "print(data.head())  # Verify that the data is loaded correctly\n",
    "print(data.info())  # Get information about the DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e1e9e362-57f9-4873-a077-5e3d43978938",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First 5 rows:\n",
      "   CustomerID  Gender  Age  Annual Income (k$)  Spending Score (1-100)\n",
      "0           1    Male   19                  15                      39\n",
      "1           2    Male   21                  15                      81\n",
      "2           3  Female   20                  16                       6\n",
      "3           4  Female   23                  16                      77\n",
      "4           5  Female   31                  17                      40\n",
      "\n",
      "Information about the data:\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 200 entries, 0 to 199\n",
      "Data columns (total 5 columns):\n",
      " #   Column                  Non-Null Count  Dtype \n",
      "---  ------                  --------------  ----- \n",
      " 0   CustomerID              200 non-null    int64 \n",
      " 1   Gender                  200 non-null    object\n",
      " 2   Age                     200 non-null    int64 \n",
      " 3   Annual Income (k$)      200 non-null    int64 \n",
      " 4   Spending Score (1-100)  200 non-null    int64 \n",
      "dtypes: int64(4), object(1)\n",
      "memory usage: 7.9+ KB\n",
      "None\n",
      "\n",
      "Descriptive statistics:\n",
      "       CustomerID         Age  Annual Income (k$)  Spending Score (1-100)\n",
      "count  200.000000  200.000000          200.000000              200.000000\n",
      "mean   100.500000   38.850000           60.560000               50.200000\n",
      "std     57.879185   13.969007           26.264721               25.823522\n",
      "min      1.000000   18.000000           15.000000                1.000000\n",
      "25%     50.750000   28.750000           41.500000               34.750000\n",
      "50%    100.500000   36.000000           61.500000               50.000000\n",
      "75%    150.250000   49.000000           78.000000               73.000000\n",
      "max    200.000000   70.000000          137.000000               99.000000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = pd.read_csv(\"C:/Users/sai surth/Downloads/Mall_Customers.csv\")\n",
    "\n",
    "print(\"First 5 rows:\")\n",
    "print(data.head())  # See the first few rows\n",
    "\n",
    "print(\"\\nInformation about the data:\")\n",
    "print(data.info())  # Data types, missing values, etc.\n",
    "\n",
    "print(\"\\nDescriptive statistics:\")\n",
    "print(data.describe())  # Summary statistics for numerical columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "99f69c79-0089-4cb1-98bb-08158c029bfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Missing values per column:\n",
      "CustomerID                0\n",
      "Gender                    0\n",
      "Age                       0\n",
      "Annual Income (k$)        0\n",
      "Spending Score (1-100)    0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nMissing values per column:\")\n",
    "print(data.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "537e842c-66e9-4fa9-a80e-cdbe9565a5ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Number of duplicate rows:\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nNumber of duplicate rows:\")\n",
    "print(data.duplicated().sum())\n",
    "\n",
    "data = data.drop_duplicates()  # Remove duplicate rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ae8b8fe0-f7a8-4cb1-a300-a26f155da6ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Unique values in Gender before standardization:\n",
      "['Male' 'Female']\n",
      "\n",
      "Unique values in Gender after standardization:\n",
      "['male' 'female']\n"
     ]
    }
   ],
   "source": [
    "# Standardize 'Gender'\n",
    "print(\"\\nUnique values in Gender before standardization:\")\n",
    "print(data['Gender'].unique())  # Check unique values\n",
    "\n",
    "data['Gender'] = data['Gender'].str.lower()  # Convert to lowercase\n",
    "\n",
    "print(\"\\nUnique values in Gender after standardization:\")\n",
    "print(data['Gender'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a9a1cc23-dd8c-43b6-9c31-42069b3304f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Column names after renaming:\n",
      "Index(['customer_id', 'gender', 'age', 'annual_income', 'spending_score'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "data = data.rename(columns={'CustomerID': 'customer_id',\n",
    "                            'Gender': 'gender',\n",
    "                            'Age': 'age',\n",
    "                            'Annual Income (k$)': 'annual_income',\n",
    "                            'Spending Score (1-100)': 'spending_score'})\n",
    "\n",
    "print(\"\\nColumn names after renaming:\")\n",
    "print(data.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c05fd6f5-8109-45fd-9f6b-22d3e0424576",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Data types:\n",
      "customer_id        int64\n",
      "gender            object\n",
      "age                int64\n",
      "annual_income      int64\n",
      "spending_score     int64\n",
      "dtype: object\n",
      "\n",
      "Data types after conversion:\n",
      "customer_id        int64\n",
      "gender            object\n",
      "age                int64\n",
      "annual_income      int64\n",
      "spending_score     int64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nData types:\")\n",
    "print(data.dtypes)\n",
    "\n",
    "# 'CustomerID' should be an integer (if it's not already)\n",
    "data['customer_id'] = data['customer_id'].astype(int)\n",
    "\n",
    "print(\"\\nData types after conversion:\")\n",
    "print(data.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "643938c3-b1c0-442c-b34f-d6139da1fc35",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
