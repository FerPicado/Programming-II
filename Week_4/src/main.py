from domine import Invoice
import gestion_ventas as gv


def invoiceRegister():
    amount = float(input("Amount: "))
    gv.create_invoice(amount)


def showInvoice():
    gv.showInvoice()


def main():

    while True:
        opt = int(input("Escoge una opcion: "))
        if (opt == 1):
            invoiceRegister()
        elif (opt == 2):
            showInvoice()
        else:
            continue


if __name__ == "__main__":
    main()
