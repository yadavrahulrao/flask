class restaurant :
  def __init__(self):
    self.menu = []
    self.table = []
    self.order = []
  def add_item_to_menu(self, item):
    self.menu.append(item)

  def book_table(self,table_no ,customer_name ) :
    self.table.append((table_no,customer_name))

  def customer_order(self,items , customer_name):
    self.order.append((items,customer_name))

  def print_menu(self):
    print("Menu:")
    for item in self.menu :
      print(item)
  
  def reserve_table(self):
    print("Reserved Table:")
    for table_no , customer_name in self.table:
      print("Table No.",table_no,"Name",customer_name)  
  
  def take_order(self):
    print("Order:")
    for customer_name,items in self.order:
      print("Name:",customer_name,"Order Items:",items)
  
hotel = restaurant()

hotel.add_item_to_menu("pizza")
hotel.add_item_to_menu("burger")
hotel.add_item_to_menu("franclie")
hotel.add_item_to_menu("yogurt")

hotel.book_table(1,"Rahul")
hotel.book_table(2,"Ritika")

hotel.customer_order("Rohit","pizza")
hotel.customer_order("Varun","burger")

hotel.print_menu()
hotel.reserve_table()
hotel.take_order()