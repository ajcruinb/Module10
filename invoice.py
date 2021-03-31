"""
Program: invoice.py
Author: AJ Crusinberry
Last date modified: 3/30/2021
Program description:
Declares a invoice class and create and prints an object from that class.
"""


class Invoice:
    """Invoice Class"""
    def __init__(self, inv_id, cust_id, l_name, f_name, phone, add, item_cost={}):
        """
        :param inv_id: Invoice ID (required)
        :param cust_id: Customer ID (required)
        :param l_name: Customer Last Name (required)
        :param f_name: Customer First Name (required)
        :param phone: Customer Phone Number (required)
        :param add: Customer Address (required)
        :param item_cost: Dictionary with items and cost (optional)
        """
        # Constructor
        phone_number_characters = set("1234567890-()")
        if not inv_id:
            raise ValueError
        self._invoice_id = inv_id
        if not cust_id:
            raise ValueError
        self._customer_id = cust_id
        if not l_name:
            raise ValueError
        self._last_name = l_name
        if not f_name:
            raise ValueError
        self._first_name = f_name
        if not phone_number_characters.issuperset(phone):
            raise ValueError
        self._phone_number = phone
        if not add:
            raise ValueError
        self._address = add
        self._items_with_price = item_cost
        self._tax_rate = 0.07

    def set_invoice_id(self, inv_id):
        """
        Updates the the invoice number
        :param inv_id: Updates the Customer's invoice number
        :return:
        """
        if not inv_id:
            raise ValueError
        self._invoice_id = inv_id

    def set_customer_id(self, cust_id):
        """
        Updates customer's ID
        :param cust_id: updates the customer's customer ID
        """
        if not cust_id:
            raise ValueError
        self._customer_id = cust_id

    def set_last_name(self, l_name):
        """
        Updates customer's last name
        :param l_name: Customer's Last Name
        """
        if not l_name:
            raise ValueError
        self._last_name = l_name

    def set_first_name(self, f_name):
        """
        Updates the customer's first name
        :param f_name: Customer's First Name
        """
        if not f_name:
            raise ValueError
        self._first_name = f_name

    def set_phone_number(self, phone):
        """
        updates the phone number
        :param phone: Customer Phone Number
        """
        if not phone:
            raise ValueError
        phone_number_characters = set("1234567890-()")
        if not phone_number_characters.issuperset(phone):
            raise ValueError
        self._phone_number = phone

    def set_address(self, add):
        """
        updates the address
        :param add: Customer Address
        """
        if not add:
            raise ValueError
        self._address = add

    def add_item(self, item):
        """
        adds item to the invoice
        :param item: dictionary item to add
        """
        self._items_with_price.update(item)

    def __str__(self):
        """
        function creates a printable version of the object
        :return: string of invoice object
        """
        sp = ' '
        nl = '\n'
        for i in range(0, len(self._address)):
            if self._address[i] == ':':
                res = i
        return "Name:" + str(self._first_name) + sp + str(self._last_name) + nl + "Address: " + str(self._address[0:res]) + nl + str(self._address[res+2:]) + nl + "Phone: " + str(self._phone_number) + nl + 'Invoice Number: ' + str(self._invoice_id) + nl + 'Customer ID: ' + str(self._customer_id) + nl

    def __repr__(self):
        """
        function creates a printable version of the object
        :return: string of invoice object
        """
        sp = ' '
        nl = '\n'
        for i in range(0, len(self._address)):
            if self._address[i] == ':':
                res = i
        return "Name:" + str(self._first_name) + sp + str(self._last_name) + nl + "Address: " + str(self._address[0:res]) + nl + str(self._address[res+2:]) + nl + "Phone: " + str(self._phone_number) + nl + 'Invoice Number: ' + str(self._invoice_id) + nl + 'Customer ID: ' + str(self._customer_id) + nl

    def create_invoice(self):
        """
        this function prints all the items and their costs along with the tax on the invoice.
        """
        total = 0
        if self._items_with_price:
            for key, values in self._items_with_price.items():
                total = values + total
                print("{}: ${}".format(key, values))
            tax = total * self._tax_rate
            total = total + tax
            print("Tax: ${n:.{digits}f}".format(n=tax, digits=2))
            print("Total: ${n:.{digits}f}".format(n=total, digits=2))
        else:
            print("your invoice is empty")


# Driver Code
invoice = Invoice(1, 123, 'Mouse', 'Minnie', '555-867-5309', '1313 Disneyland Dr: Anaheim, CA 92802')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
