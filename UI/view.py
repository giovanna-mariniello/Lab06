import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "LAB06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_top_vendite = None
        self.btn_analizza_vendite = None
        self.lst_result = None


    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self.dd_anno = ft.Dropdown(label="anno", width=130, options=[ft.dropdown.Option(key="None", text="Nessun filtro")], on_change=self._controller.leggi_dd_anno)
        self._controller.popola_dd_anno()

        self.dd_brand = ft.Dropdown(label="brand", width=200, options=[ft.dropdown.Option(key="None", text="Nessun filtro")], on_change=self._controller.leggi_dd_brand)
        self._controller.popola_dd_brand()

        self.dd_retailer = ft.Dropdown(label="retailer", width=230, options=[ft.dropdown.Option(key="None", text="Nessun filtro")], on_change=self._controller.leggi_dd_retailer)
        self._controller.popola_dd_retailer()

        self.btn_top_vendite = ft.ElevatedButton(text="Top vendite", width=200, on_click=self._controller.get_top_vendite)
        self.btn_analizza_vendite = ft.ElevatedButton(text="Analizza vendite", width=200, on_click=self._controller.get_analisi_vendite)

        row1 = ft.Row(controls=[self.dd_anno, self.dd_brand, self.dd_retailer], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        row2 = ft.Row(controls=[self.btn_top_vendite, self.btn_analizza_vendite], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.lst_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lst_result)

        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
