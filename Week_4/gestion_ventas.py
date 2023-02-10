from domine import Invoice
from datetime import datetime

invoice_list = []


def create_invoice(invoice_id, invoice_total):

    # Instanciamos
    invoiceObj = Invoice()

    invoiceObj.invoice_id = "INVOICE #00001"
    invoiceObj.invoice_date = datetime.now()
    invoiceObj.invoice_total = 234254
    invoiceObj.calc_iva()
    invoice_list.append(invoiceObj)


def showInvoice():
    for i in invoice_list:
        print(f"Invoice ID: {i.invoice_id}")
        print(f"Monto: {i.invoice_total}")
