from pre_process import pre_process

# pre-process the docs.csv file
docs_csv_file = '../Query_Doc/docs.csv'
out_docs_csv_file = '../Query_Doc/pre_processed_docs.csv'

pre_process(docs_csv_file, out_docs_csv_file, 'doc_text')

# pre-process the queries.csv file
queries_csv_file = '../Query_Doc/queries.csv'
out_queries_csv_file = '../Query_Doc/pre_processed_queries.csv'

pre_process(queries_csv_file, out_queries_csv_file, 'query_text')