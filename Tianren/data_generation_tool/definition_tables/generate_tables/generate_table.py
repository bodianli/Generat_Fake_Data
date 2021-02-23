from ..models import ColumnConfig, TableConfig
import pyodbc

#   Connect to Local Server for test      ----> You can change to Mirai Server
database = 'AdventureWorksDW2012'
server = 'DESKTOP-TAHGBP9\BODIAN_LI'
tcon = 'yes'


def generate_tables():
    conn = pyodbc.connect(driver='{SQL Server}', host=server, database=database, Trusted_Connection=tcon)
    cursor = conn.cursor()

    # get table config list from table_definition
    for table_config in TableConfig.objects.all():
        create_table(table_config, cursor)
        # Step 5: generate fake data(table_name)
    # conn.commit()
    pass


def create_table(table_config, cursor):
    column_sql = ''
    # get column config list of this table from column_definition
    for column_config in ColumnConfig.objects.filter(table_config=table_config.id):
        column_sql += '{name} {type}({length}), '.format(name=column_config.name, type=column_config.type,
                                                        length=column_config.length)
    # create SQL string with arguments
    sql = "CREATE TABLE {table_name} ({column_sql}".format(table_name=table_config.name, column_sql=column_sql)
    print(sql)
    # cursor.execute(sql)
    # run sql command
