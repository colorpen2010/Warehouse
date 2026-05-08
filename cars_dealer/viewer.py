from rich.table import Table

def table_creator(table_name,column_name_list):
    table = Table(title=table_name)
    for i in column_name_list:
        table.add_column(i)
    return table

def table_filler(content,table:Table):
    # column_count = len(content[0])
    for i in content:
        table.add_row(*i)