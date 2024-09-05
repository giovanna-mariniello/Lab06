from database.DB_connect import DBConnect
from model.product import Product
class ProductsDao:

    @staticmethod
    def get_brands():

        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Errore di connessione")
            return None
        else:
            cursor = cnx.cursor()
            query = """ SELECT DISTINCT gp.Product_brand
                        FROM go_products gp"""
            cursor.execute(query)
            rows = cursor.fetchall()

            cursor.close()
            cnx.close()

            return rows

    @staticmethod
    def get_brand(product_number):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gp.*
                            FROM go_products gp
                            WHERE Product_number =%s"""
            cursor.execute(query, (product_number,))
            row = cursor.fetchone()
            row_product = Product(row["Product_number"],
                                  row["Product_line"],
                                  row["Product_type"],
                                  row["Product"],
                                  row["Product_brand"],
                                  row["Product_color"],
                                  row["Unit_cost"],
                                  row["Unit_price"])
            cursor.close()
            cnx.close()
            return row_product
        else:
            print("Errore nella connessione")
            return None

    if __name__=="__main__":
        print(get_brand(1110))