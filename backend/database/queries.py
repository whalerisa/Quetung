#Function Query พื้นฐาน (CRUD)

from .connection import get_connection

#CUSTOMER
def get_customer():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT CustomerNo,Name,PricingLevel FROM Customer")
    rows = cursor.fetchall()
    conn.close()
    return [{"CustomerNo": r[0],"Name": r[1],"PricingLvel": r[2]} for r in rows ]

def add_customer(customer):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Customer (CustomerNo, Name, PricingLevel, FirstPurchaseDate, PurchaseFrequency,Tel.)
        VALUES (?, ?, ?, ?, ?)
    """, (customer["CustomerNo"], customer["Name"], customer["PricingLevel"],
          customer["FirstPurchaseDate"], customer["PurchaseFrequency"],customer["Tel."]))
    conn.commit()
    conn.close()


#PRODUCT
def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ProductNo, Name, Price, Stock FROM Product")
    rows = cursor.fetchall()
    conn.close()
    return [{"ProductNo": r[0], "Name": r[1], "Price": r[2], "Stock": r[3]} for r in rows]

#SALE
def add_sale(sale):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Sale (CustomerNo, SellerNo, ProductNo, Quantity, PricePerProduct, TotalPrice, PurchaseDate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (sale["CustomerNo"], sale["SellerNo"], sale["ProductNo"], sale["Quantity"],
          sale["PricePerProduct"], sale["TotalPrice"], sale["PurchaseDate"]))
    conn.commit()
    conn.close()
