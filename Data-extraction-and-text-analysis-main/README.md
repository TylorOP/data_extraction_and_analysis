# Data-extraction-and-text-analysis.
The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables from url

The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables from url

Here i have done some additional work like saving the text file 111(3 file were 404 not fond) and you can see the content in folder

overview: from Excel file (which contain 114 links ) neeed to visit each single website and extract header and the content of that website and the do some text analysis and score each wesite and do this for all website (114) and export it in a csv file .

Steps:

Read input.xlsx to get the list of URLs and their corresponding URL_IDs

Loop through each row in df_input to extract article content and save in text files

Save the article content in a text file

Read the content from the text file

Clean the text using stop words

Calculate the positive and negative scores

Calculate the total words after cleaning

Calculate the polarity score and subjectivity score

Calculate the average sentence length

Calculate the percentage of complex words

Calculate the Fog Index

Calculate the average number of words per sentence

Calculate the complex word count

Calculate the word count

Calculate the syllable count per word

Calculate the personal pronouns count

Calculate the average word length

Create a dictionary to store the derived variables for this URL

Append the dictionary to the output_data list

Output Data to Excel

Create a DataFrame from the output_data list

Save the DataFrame to an Excel file
