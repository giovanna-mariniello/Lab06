from database.DB_connect import DBConnect
from model.sale import Sale


class SalesDao:
    @staticmethod
    def get_anni():

        cnx = DBConnect.get_connection()


        if cnx is None:
            print("Errore di connessione")
            return None
        else:
            cursor = cnx.cursor()
            query = ("""SELECT DISTINCT YEAR(gds.Date)
                        FROM go_daily_sales gds""")
            cursor.execute(query)

            rows = cursor.fetchall()

            cursor.close()
            cnx.close()

            return rows

    def get_filtered_sales(self, anno, brand, retailer_code) -> list[Sale]:
        """
            Function that reads the database and returns the sales with the constraints specified by the input
            parameters
            anno: the year used as filter. If year is None, no filter is applied
            retailer: the retailer used as filter. If retailer is None, no filter is applied
            brand: the brand used as filter. If brand is None, no filter is applied.
            return: a collection containing sales retrieved from the database. It returns None if
            there are connection errors
        """
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gds.*, gds.Unit_sale_price*gds.Quantity AS Ricavo
                FROM go_daily_sales gds, go_retailers gr, go_products gp 
                WHERE gds.Retailer_code  = gr.Retailer_code  
                AND gds.Product_number = gp.Product_number 
                AND (YEAR(gds.Date)=COALESCE(%s,YEAR(gds.Date)))
                AND (gp.Product_brand =COALESCE(%s,gp.Product_brand))
                AND (gr.Retailer_code =COALESCE(%s,gr.Retailer_code))"""
            cursor.execute(query, (anno, brand, retailer_code,))
            result = []
            for row in cursor:
                result.append(Sale(row["Date"],
                                   row["Quantity"],
                                   row["Unit_price"],
                                   row["Unit_sale_price"],
                                   row["Retailer_code"],
                                   row["Product_number"],
                                   row["Order_method_code"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None


