## Retrieving Corresponding Content In Massive Text

### Abstract

Flight maintenance is very tedious and accurate work, even the most experienced engineers need to refer to a vast number of repair documents for related operations. After identifying the name of the corresponding parts, it is necessary to find the corresponding manual content for reference operation.

However, in the maintenance manual, the names of many parts of the same type are very close and difficult to distinguish, which brings considerable troubles to the maintenance work. The maintenance-matching algorithm needs to match the closest result set for selection after the engineer identifies the image or inputs keywords manually.

After the user chooses the relevant content summary, the application can automatically jump to the corresponding page according to the pre-read PDF file directory (refer to the PDF Process section for implementation). This function enables our software to work as a search engine, providing sufficient convenience for maintenance staff.

Text retrieval is an eternal proposition in the field of data processing. Whether it is SQL database or Solr or Sphinx, it has its own unique features, and the processing and segmentation technology of natural language is also being explored. Beginning with a database search, we will continue to optimize and gradually solve the high-order functions of fuzzy search, correlation ranking, search prediction, and so on.

### Structure

#### Fulltext Index

Use Mysql database (InnoDB engine) to add Fulltext index to related columns after storing data. After that, the "Like", "contains" and "against" statements in SQL statements are synthetically used, and the optimal results are returned to the front end after judgment.

By using fulltext index, the retrieval efficiency is greatly improved under the huge data scale, and the results can be displayed instantly in general.

#### Search Engine

We use Apache Luence information retrieval library to achieve higher-order functions. (In development)

Luence is already a standard fulltext search program in the Java world, which provides a complete query engine and index engine.
### Explanation

#### Relevance Ranking
e.g
SELECT column_name
FROM table_name 
WHERE CONTAINS(column_name, 'ISABOUT (keyword1 weight (.8), keyword2 weight (.4))' )

Weight specifies a number between 0 and 1, similar to weight coefficients

Or we can use BooleanQuery and Wildcard Query in Luence Later.

#### Fuzzy Search

We intend to use Fuzzy Query in Luence.



**Contact:** 1753344@tongji.edu.cn  

**Author:** Mac