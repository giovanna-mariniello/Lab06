import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._anno = None
        self._brand = None
        self._retailer_code = None

    def leggi_dd_anno(self, e):
        if e.control.value == "Nessun filtro":
            self._anno = None
        else:
            self._anno = e.control.value

    def popola_dd_anno(self):
        anni = self._model.get_anni()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def leggi_dd_brand(self, e):
        if e.control.value == "Nessun filtro":
            self._brand = None
        else:
            self._brand = e.control.value

    def popola_dd_brand(self):
        brands = self._model.get_brands()
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand[0]))
        self._view.update_page()

    def leggi_dd_retailer(self, e):
        if e.control.data is None:
            self._retailer_code = None
        else:
            self._retailer_code = e.control.data.retailer_code

    def popola_dd_retailer(self):
        retailers = self._model.get_retailers()
        for retailer in retailers.values():
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.retailer_code, text=retailer.retailer_name, data=retailer, on_click=self.leggi_dd_retailer))
        self._view.update_page()

    def get_top_vendite(self, e):
        top_vendite = self._model.get_top_vendite(self._anno, self._brand, self._retailer_code)
        self._view.lst_result.controls.clear()
        if len(top_vendite) == 0:
            self._view.lst_result.controls.append(ft.Text("Nessuna vendita con i filtri selezionati"))
        else:
            for vendita in top_vendite:
                self._view.lst_result.controls.append(ft.Text(vendita))
        self._view.update_page()


    def get_analisi_vendite(self, e):
        statistiche_vendite = self._model.get_sales_stats(self._anno, self._brand, self._retailer_code)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("Satistiche vendite:"))
        self._view.lst_result.controls.append(ft.Text(f"Giro d'affari: {statistiche_vendite[0]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero vendite: {statistiche_vendite[1]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero retailers coinvolti: {statistiche_vendite[2]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {statistiche_vendite[3]}"))
        self._view.update_page()
