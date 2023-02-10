#  Tuesday Class

class Invoice:

    def __init__(self) -> None:
        self.invoice_id = None
        self.invoice_date = None
        self.iva_invoice = None
        self.invoice_total = None

    def calc_iva(self):
        self.iva_invoice = self.invoice_total * 0.13
        return self.iva_invoice


invoice_list = []
