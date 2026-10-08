from datetime import datetime

food_ordered = []
beverage_ordered = []
add_on_ordered = []
payment_method = ""

food_quantity = []
total_food_quantity = 0
beverage_quantity = []
total_beverage_quantity = 0
add_on_quantity = []
total_add_on_quantity = 0

total_price = 0
price_food_ordered = []
price_beverage_ordered = []
price_add_on_ordered = []

total_food_price = 0
total_beverage_price = 0
total_add_on_price = 0

order_menu_food = [
  "Mie Ayam: 16.500",
  "Nasi Goreng: 15.000",
  "Kwetiau Goreng: 20.000",
  "Ayam Goreng + Nasi: 23.000",
  "Bebek Goreng + Nasi: 25.000",
  "Satay Ayam: 15.000",
  "Soto Ayam: 15.000",
  "Bubur Ayam: 15.000",
  "Bakso: 13.000",
  "Ayam Geprek: 14.000"
]

food_without_price = []

food_result = []


order_menu_beverage = [
  "Air Mineral: 3.000",
  "Teh Tawar: 4.000",
  "Es Teh Manis: 4.000",
  "Es Jeruk: 5.000",
  "Air Kelapa: 10.000",
  "Kopi Susu: 5.000",
  "Es Coklat: 7.000",
  "Jus Alpukat: 15.000",
  "Lemon Tea: 10.000",
  "Teh Tarik: 5.000"
]

beverage_without_price = []

beverage_result = []

order_menu_add_on = [
  "Pangsit Goreng: 3.000",
  "Udang Keju: 5.000",
  "Lumpia: 5.000",
  "Siomay: 5.000"
]

add_on_without_price = []

add_on_result =[]

menu_payment_method = [
  "Cash",
  "Transfer",
  "Qris"
]

while True: 
  print("="*10 + " " + "Umami Resto" + " " + "="*10)
  print("Main Menu: ")
  print("1. Order")
  print("2. Exit Menu")

  choose = input("Please Select Main Menu [1 - 2]: ")
  print("\n")
  match choose:
    case "1":
      print("="*10 + " " + "Selamat Datang di Umami Resto" + " " + "="*10)
      while True:
        is_reorder = False

        print("-"*5 + " " + "Silahkan Pilih Menu yang tersedia" + " " + "-"*5)
        
        print("~"*3 + "List of food" + "~"*3)
        for food in order_menu_food:
          print(food)
          food_split = food.split(":")
          food_name = food_split[0]
          food_without_price.append(food_name)
        print("-"*40)
        _menu_food = input("Your food Order [Type 'None' if you don't want to order food]: ").title()
        if _menu_food == "None":
          break
        elif _menu_food in food_without_price:
          food_ordered.append(_menu_food)
          match _menu_food:
            case "Mie Ayam":
              price = 16500
              price_food_ordered.append(price) 
      
            case "Nasi Goreng":
              price = 15000
              price_food_ordered.append(price)
        
            case "Kwetiau Goreng":
              price = 20000
              price_food_ordered.append(price)
        
            case "Ayam Goreng + Nasi":
              price = 23000
              price_food_ordered.append(price)
        
            case "Bebek Goreng + Nasi":
              price = 25000
              price_food_ordered.append(price)
        
            case "Satay Ayam":
              price = 15000
              price_food_ordered.append(price)
        
            case "Soto Ayam":
              price = 15000
              price_food_ordered.append(price)
        
            case "Bubur Ayam":
              price = 15000
              price_food_ordered.append(price)
        
            case "Bakso":
              price = 13000
              price_food_ordered.append(price)
        
            case "Ayam Geprek":
              price = 14000
              price_food_ordered.append(price)
          _food_quantity = int(input("Number of Items [Number]: "))
          food_quantity.append(_food_quantity)
          break
        print("Invalid input, Please only input food in menu")
      print("\n")
      

      while True:
        print("-"*5 + " " + "Silahkan Pilih Menu yang tersedia" + " " + "-"*5)
        
        print("~"*3 + "List of Beverage" + "~"*3)
        for beverage in order_menu_beverage:
          print(beverage)
          beverage_split = beverage.split(":")
          beverage_name = beverage_split[0]
          beverage_without_price.append(beverage_name)
        print("-"*40)
        _menu_beverage = input("Your Beverage Order [Type 'None' if you don't want to order food]: ").title()
        if _menu_beverage == "None":
          break
        elif _menu_beverage in beverage_without_price:
          beverage_ordered.append(_menu_beverage)
          match _menu_beverage:
            case "Air Mineral":
              price = 3000
              price_beverage_ordered.append(price)
            case "Teh Tawar":
              price = 4000
              price_beverage_ordered.append(price)
            case "Es Teh Manis":
              price = 4000
              price_beverage_ordered.append(price)
            case "Es Jeruk":
              price = 5000
              price_beverage_ordered.append(price)
            case "Air Kelapa":
              price = 10000
              price_beverage_ordered.append(price)
            case "Kopi Susu":
              price = 5000
              price_beverage_ordered.append(price)
            case "Es Coklat":
              price = 7000
              price_beverage_ordered.append(price)
            case "Jus Alpukat":
              price = 15000
              price_beverage_ordered.append(price)
            case "Lemon Tea":
              price = 10000
              price_beverage_ordered.append(price)
            case "Teh Tarik":
              price = 5000
              price_beverage_ordered.append(price)
          _beverage_quantity = int(input("Number of Items [Number]: "))
          beverage_quantity.append(_beverage_quantity)
          print(beverage_quantity)
          break
        print("Invalid input, Please only input Beverage in menu")
      print("\n")
        

      while True:
        print("-"*5 + " " + "Silahkan Pilih Menu yang tersedia" + " " + "-"*5)
  
        print("~"*3 + "List of Add-On" + "~"*3)
        for add_on in order_menu_add_on:
          print(add_on)
          add_on_split = add_on.split(":")
          add_on_name = add_on_split[0]
          add_on_without_price.append(add_on_name)
        print("-"*40)
        _menu_add_on = input("Your Add-On Order [Type 'None' if you don't want to order food]: ").title()
        if _menu_add_on == "None":
          break
        elif _menu_add_on in add_on_without_price:
          add_on_ordered.append(_menu_add_on)
          match _menu_add_on:
            case"Pangsit Goreng":
              price = 3000
              price_add_on_ordered.append(price)
            case"Udang Keju":
              price = 5000
              price_add_on_ordered.append(price)
            case"Lumpia":
              price = 5000
              price_add_on_ordered.append(price)
            case "Siomay":
              price = 5000
              price_add_on_ordered.append(price)
          _add_on_quantity = int(input("Number of Items [Number]: "))
          add_on_quantity.append(_add_on_quantity)
          break
        print("Invalid input, Please only input Add-On in menu")
      print("\n")
        

      while True:
        _reorder = input("Do you want to add your order [y/n]: ")
        print("\n")
        if _reorder == "y" or _reorder == "Y":
          is_reorder = True
          break      
        elif _reorder == "n" or _reorder == "N":
            break 
        else:
          print("Invalid Input, Please only input [y/n]")
          continue

      if is_reorder == True:
        continue

      while True:
        print("-"*5 + " " + "Silahkan Pilih Metode Pembayaran yang tersedia" + " " + "-"*5)
        for i in range(len(menu_payment_method)):
          print("~"*3 + "List of Payment Method" + "~"*3)
          for payment in menu_payment_method:
            print(payment)
          print("-"*40)
          _input_payment_method = input("Your Payment Method: ").title()
          if _input_payment_method in menu_payment_method:
            payment_method = _input_payment_method
            break
          print("Invalid input, Please only input Add-On in menu")
          print("\n")
          break
        break

      for sum_food_qty in food_quantity:
        total_food_quantity += sum_food_qty
      
      for sum_beverage_qty in beverage_quantity:
        total_beverage_quantity += sum_beverage_qty

      for sum_add_on_qty in add_on_quantity:
        total_add_on_quantity += sum_add_on_qty

      for n in range(len(food_quantity)):
        result_total=price_food_ordered[n] * food_quantity[n]
        food_result.append(result_total)

      for food_total in food_result:
        total_food_price += food_total

      for p in range(len(beverage_quantity)):
        result_total=price_beverage_ordered[p] * beverage_quantity[p]
        beverage_result.append(result_total)

      for beverage_total in beverage_result:
        total_beverage_price += beverage_total

      for n in range(len(add_on_quantity)):
        result_total=price_add_on_ordered[n] * add_on_quantity[n]
        add_on_result.append(result_total)

      for add_on_total in add_on_result:
        total_add_on_price += add_on_total
      
      total_items = total_food_quantity + total_beverage_quantity + total_add_on_quantity
      total_price = total_price + (total_food_price + total_beverage_price + total_add_on_price)
      
      print("\n")
      print("="*30 + " " + "RINCIAN PEMESANAN" + " "+ "="*30)
      print("\n")
      print("Order Date: ", datetime.now())
      print("\n")
      print("-"*5 + " Food Ordered "+"-"*5)
      if food_ordered == []:
        print("No Food Ordered")
        print("\n")
      else:
        for f in range(len(food_ordered)):
          name_food = food_ordered[f] 
          price_food = price_food_ordered[f]
          qty_food = food_quantity[f] 
          print(f"{name_food}: {price_food} : {qty_food}")
        print("\n")
      print("-"*5 + " Beverage Ordered "+"-"*5)
      if beverage_ordered == []:
        print("No Beverage Ordered")
        print("\n")
      else:
        for b in range(len(beverage_ordered)):
          name_beverage = beverage_ordered[b]
          price_beverage = price_beverage_ordered[b]
          qty_beverage = beverage_quantity[b] 
          print(f"{name_beverage}: {price_beverage} : {qty_beverage}")
        print("\n")
      print("-"*5 + " Add-On Ordered "+"-"*5)
      if add_on_ordered == []: 
        print("No Add On Ordered")
        print("\n")
      else:
        for a in range(len(add_on_ordered)):
          name_add_on = add_on_ordered[a]
          price_add_on = price_add_on_ordered[a]
          qty_add_on = add_on_quantity[a] 
          print(f"{name_add_on}: {price_add_on} : {qty_add_on}")
        print("\n")
      print("-"*10) 
      print("Total Items: ", total_items)
      print("Total Price: Rp. ", format(total_price, ","))
      print("-"*10)
      print("Payment Method: ", payment_method)
      print("\n")
    case "2":
      print("Thank You  - Umami Resto")
      exit()
    case _:
      print("Please Input Valid Menu [1 or 2]")