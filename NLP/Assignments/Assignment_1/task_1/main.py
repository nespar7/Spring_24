from pre_process import pre_process

# pre-process the docs.csv file
docs_csv_file = '../Query_Doc/docs.csv'

pre_process(docs_csv_file, 'doc_text')

# pre-process the queries.csv file
queries_csv_file = '../Query_Doc/queries.csv'

pre_process(queries_csv_file, 'query_text')