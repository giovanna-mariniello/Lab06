from database.DB_connect import DBConnect
from model.retailer import Retailer

class RetailersDao:

    @staticmethod
    def get_retailers():

        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Errore di connessione")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT *
                        FROM go_retailers gr"""
            cursor.execute(query)
            rows = cursor.fetchall()

            result = {}

            for row in rows:
                retailer = Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"])
                result[retailer.retailer_code] = retailer

            cursor.close()
            cnx.close()


            return result

    @staticmethod
    def get_retailer(product_code) -> Retailer | None:
        """
        Function that reads the retailers present in the database and returns them.
        :param product_code: The identifying code of the product we want to retrieve
        :return: A set of Retailers, or None if there are connection errors.
        """
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gr.*
                    FROM go_retailers gr
                    WHERE gr.retailer_code =%s"""
            cursor.execute(query, (product_code,))
            row = cursor.fetchone()
            row_retailer = Retailer(row["Retailer_code"],
                                    row["Retailer_name"],
                                    row["Type"],
                                    row["Country"])
            cursor.close()
            cnx.close()
            return row_retailer
        else:
            print("Errore nella connessione")
            return None
    #if __name__ == "__main__":
        #print(get_retailers())