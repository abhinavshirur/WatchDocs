This folder contains all the json files of the database collections. Download all the files and import the file, collection in your mongodb database.
Collection name should be kept same as the file name.

Command to import a collection from a file into the database:

mongoimport --db mongotest --collection keywords --file keywords.json

where _mongotest_ is the database, _keywords_ is the collection we want to create from the file _keywords.json_
