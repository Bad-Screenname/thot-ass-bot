table_name = 'insults'

def read_query():
    return f'SELECT insult FROM {table_name}'

def create_row_query(insult):
    return f"""
    INSERT INTO {table_name} (insult)
    VALUES ({insult});
    """

def update_rows_query(column_value_pair, filter_expression):
    return f"""
    UPDATE {table_name}
    SET {column_value_pair}
    WHERE {filter_expression};
    """

def delete_rows_query(filter_expression):
    return f"""
    DELETE FROM {table_name}
    WHERE {filter_expression};
    """
