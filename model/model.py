from database.sales_dao import SalesDao
from database.products_dao import ProductsDao
from database.retailers_dao import RetailersDao

class Model:

    def __init__(self):
        self._sales_dao = SalesDao()

    def get_anni(self):
        return SalesDao.get_anni()

    def get_brands(self):
        return ProductsDao.get_brands()

    def get_retailers(self):
        return RetailersDao.get_retailers()



    def get_top_vendite(self, anno, brand, retailer_code):
        filtered_sales = self._sales_dao.get_filtered_sales(anno, brand, retailer_code)
        filtered_sales.sort(reverse=True)
        return filtered_sales[0:5]

    def get_sales_stats(self, anno, brand, retailer_code):
        """
            Funzione che legge dal dal dao le vendite con i filtri selezionati,
            e ne restituisce le prime 5 (se presenti) ordinate per ricavo decrescente
        """
        filtered_sales = self._sales_dao.get_filtered_sales(anno, brand, retailer_code)
        ricavo_totale = sum([sale.ricavo for sale in filtered_sales])
        retailers_involved = set([sale.retailer_code for sale in filtered_sales])
        product_involved = set([sale.product_number for sale in filtered_sales])
        return ricavo_totale, len(filtered_sales), len(retailers_involved), len(product_involved)