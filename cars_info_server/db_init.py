
import psycopg2
import psycopg2.extras
from loguru import logger


DB_HOST = "db"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "postgres_password"

logger.add('debug.log', format="{time},{level},{message}", level='INFO')
# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

@logger.catch()
def connect_to_db():
    try:
        # Подключаемся к базе данных
        connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,password=DB_PASSWORD, host=DB_HOST, port=5432)
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        logger.info("Testing connection")
        logger.info("You are connected to - {} ", record[0])
        response = "OK"
        return response
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()


def create_tables_in_db():
    try:
        # Подключаемся к базе данных
        connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=5432)
        cur = connection.cursor()

        cur.execute("CREATE TABLE brands (id SERIAL PRIMARY KEY,"
                    " brand_name VARCHAR(64) NOT NULL);")

        connection.commit()
        logger.info("Table brands created successfully in DB ")

        cur.execute("CREATE TABLE models (id SERIAL PRIMARY KEY,"
                           " model VARCHAR(64) NOT NULL,"
                           " year INTEGER NOT NULL,"
                           " brandId INTEGER REFERENCES brands (id) ON DELETE CASCADE)")
        connection.commit()
        logger.info("Table models created successfully in DB ")

        cur.execute("CREATE TABLE price (id SERIAL PRIMARY KEY,"
                    " start_date DATE , end_date DATE,"
                    " price FLOAT NOT NULL,"
                    "modelId INTEGER REFERENCES models (id) ON DELETE CASCADE)")
        connection.commit()
        logger.info("Table prices created successfully in DB ")
        logger.info("Tables created successfully in DB ")

    except (Exception, psycopg2.DatabaseError) as error:
        if (connection):
            logger.error("Error while creating PostgreSQL table {}", error)
    finally:
        if (connection):
            cur.close()
            connection.close()

def insert_data_into_tables():
    try:
        # Подключаемся к базе данных
        connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=5432)
        cur = connection.cursor()

        # Заполняем данными таблицу brands
        insert_query_to_brands = """ INSERT INTO brands (brand_name) VALUES (%s)"""
        records_to_insert_to_brands = [
            ('AUDI',),
            ('BMW',),
            ('HONDA',),
            ('NISSAN',),
            ('SUBARU',),
        ]

        cur.executemany(insert_query_to_brands, records_to_insert_to_brands)
        connection.commit()
        logger.info("insert data into brands")

        # Заполняем данными таблицу models
        insert_query_to_models = """ INSERT INTO models (model,year,brandId) VALUES (%s,%s,%s)"""
        records_to_insert_to_models = [
            ('A4',2019,1),
            ('A6',2018,1),
            ('Q3',2020,1),
            ('X5',2020,2),
            ('X3',2017,2),
            ('M6',2010,2),
            ('Accord',2015,3),
            ('Civic',2010,3),
            ('CR-V',2013,3),
            ('XTrail',2014,4),
            ('Teana',2013,4),
            ('Terrano',2018,4),
            ('Impreza',2008,5),
            ('Forester',2012,5),
            ('Outback',2010,5),

        ]

        cur.executemany(insert_query_to_models,records_to_insert_to_models)
        connection.commit()
        logger.info("insert data into models")

        # Заполняем данными таблицу price
        insert_query_to_price = """ INSERT INTO price (price,modelId) VALUES (%s,%s)"""
        records_to_insert_to_price = [
            (1566600.00, 1),
            (1899600.00, 2),
            (2366600.00, 3),
            (1665500.00, 4),
            (1766600.00, 5),
            (1935900.00, 6),
            (1521300.00, 7),
            (1266600.00, 8),
            (1366600.00, 9),
            (12563400.00, 10),
            (1634000.00, 11),
            (954000.00, 12),
            (866656.00, 13),
            (2455000.00, 14),
            (1857000.00, 15),
        ]

        cur.executemany(insert_query_to_price, records_to_insert_to_price)
        connection.commit()
        logger.info("insert data into prices")

    except (Exception, psycopg2.Error) as error:
        if (connection):
            logger.error("Error {}", error)
    finally:
        if (connection):
            cur.close()
            connection.close()

def select_data(id):
    try:
        # Подключаемся к базе данных
        connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=5432)
        cur = connection.cursor()

        insert_query_to_select = """
        select  b.brand_name, m.model, m.year, p.price
        from brands b
        join models m on b.id = m.brandId
        join price p on m.id = p.modelId
        where m.id = %s
        """
        to_select = (id,)

        cur.execute(insert_query_to_select,to_select)
        info=cur.fetchone()
        logger.info("Test select request {}", info)

    except (Exception, psycopg2.Error) as error:
        if(connection):
            logger.error("Error {}", error)

    finally:
        if (connection):
            cur.close()
            connection.close()


if __name__ == '__main__':
    connect_to_db()
    create_tables_in_db()
    insert_data_into_tables()
    select_data(2)

