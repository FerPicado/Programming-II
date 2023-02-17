from domine import Invoice
from datetime import datetime

invoice_list = []
cons_invoice_format = "INV{0}"
cons_invoice = 1


def create_invoice(invoice_total):

    # Instanciamos
    try:
        global cons_invoice
        invoiceObj = Invoice()
        num_invoice = str(cons_invoice).rjust(3, '0')

        invoiceObj.invoice_id = cons_invoice_format.format(num_invoice)
        invoiceObj.invoice_date = datetime.now()
        invoiceObj.invoice_total = 234254
        invoiceObj.calc_iva()
        invoice_list.append(invoiceObj)
        cons_invoice += 1
    except UnboundLocalError:
        print("Error")


def showInvoice():
    for i in invoice_list:
        print(f"Invoice ID: {i.invoice_id}")
        print(f"Monto: {i.invoice_total}")
