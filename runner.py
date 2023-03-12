from brands import brands
from parser import Parser
import logging
import schedule
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

schedule.every().day.at("13:00").do(Parser(brands["5.11 Tactical"], "5.11 Tactical").run)
schedule.every().day.at("13:00").do(Parser(brands["Addax"], "Addax").run)
schedule.every().day.at("13:00").do(Parser(brands["Adidas"], "Adidas").run)
schedule.every().day.at("13:00").do(Parser(brands["Armani Exchange"], "Armani Exchange").run)
schedule.every().day.at("13:00").do(Parser(brands["Asics"], "Asics").run)
schedule.every().day.at("13:00").do(Parser(brands["Bad Bear"], "Bad Bear").run)
schedule.every().day.at("13:00").do(Parser(brands["Bebe Plus"], "Bebe Plus").run)
schedule.every().day.at("13:00").do(Parser(brands["Bershka"], "Bershka").run)
schedule.every().day.at("13:00").do(Parser(brands["Bianco Lucci"], "Bianco Lucci").run)
schedule.every().day.at("13:00").do(Parser(brands["Mudo"], "Mudo").run)
schedule.every().day.at("13:00").do(Parser(brands["Colin’s"], "Colin’s").run)
schedule.every().day.at("13:00").do(Parser(brands["Columbia"], "Columbia").run)
schedule.every().day.at("13:00").do(Parser(brands["Diesel"], "Diesel").run)
schedule.every().day.at("13:00").do(Parser(brands["Ecko Unltd"], "Ecko Unltd").run)
schedule.every().day.at("13:00").do(Parser(brands["Emporio Armani"], "Emporio Armani").run)
schedule.every().day.at("13:00").do(Parser(brands["Ferraro"], "Ferraro").run)
schedule.every().day.at("13:00").do(Parser(brands["Franko Armondi"], "Franko Armondi").run)
schedule.every().day.at("13:00").do(Parser(brands["GAP"], "GAP").run)
schedule.every().day.at("13:00").do(Parser(brands["Guess"], "Guess").run)
schedule.every().day.at("13:00").do(Parser(brands["Gymlegend"], "Gymlegend").run)
schedule.every().day.at("13:00").do(Parser(brands["Gymwolves"], "Gymwolves").run)
schedule.every().day.at("13:00").do(Parser(brands["Harley Davidson"], "Harley Davidson").run)
schedule.every().day.at("13:00").do(Parser(brands["Helly Hansen"], "Helly Hansen").run)
schedule.every().day.at("13:00").do(Parser(brands["Hugo Boss"], "Hugo Boss").run)
schedule.every().day.at("13:00").do(Parser(brands["HUMMEL"], "HUMMEL").run)
schedule.every().day.at("13:00").do(Parser(brands["Jack & Jones"], "Jack & Jones").run)
schedule.every().day.at("13:00").do(Parser(brands["Jack Wolfskin"], "Jack Wolfskin").run)
schedule.every().day.at("13:00").do(Parser(brands["Jimmy Key"], "Jimmy Key").run)
schedule.every().day.at("13:00").do(Parser(brands["Karaca"], "Karaca").run)
schedule.every().day.at("13:00").do(Parser(brands["Karl Lagerfeld"], "Karl Lagerfeld").run)
schedule.every().day.at("13:00").do(Parser(brands["Lacoste"], "Lacoste").run)
schedule.every().day.at("13:00").do(Parser(brands["Lanvin"], "Lanvin").run)
schedule.every().day.at("13:00").do(Parser(brands["LC Waikiki"], "LC Waikiki").run)
schedule.every().day.at("13:00").do(Parser(brands["Lescon"], "Lescon").run)
schedule.every().day.at("13:00").do(Parser(brands["Levi's"], "Levi's").run)
schedule.every().day.at("13:00").do(Parser(brands["Lotto"], "Lotto").run)
schedule.every().day.at("13:00").do(Parser(brands["Ltb"], "Ltb").run)
schedule.every().day.at("13:00").do(Parser(brands["Mango"], "Mango").run)
schedule.every().day.at("13:00").do(Parser(brands["Markova"], "Markova").run)
schedule.every().day.at("13:00").do(Parser(brands["Massimo Dutti"], "Massimo Dutti").run)
schedule.every().day.at("13:00").do(Parser(brands["Mavi"], "Mavi").run)
schedule.every().day.at("13:00").do(Parser(brands["MORREZ"], "MORREZ").run)
schedule.every().day.at("13:00").do(Parser(brands["New Balance"], "New Balance").run)
schedule.every().day.at("13:00").do(Parser(brands["Nike"], "Nike").run)
schedule.every().day.at("13:00").do(Parser(brands["North Pacific"], "North Pacific").run)
schedule.every().day.at("13:00").do(Parser(brands["Paul&Shark"], "Paul&Shark").run)
schedule.every().day.at("13:00").do(Parser(brands["Penti"], "Penti").run)
schedule.every().day.at("13:00").do(Parser(brands["Pierre Cardin"], "Pierre Cardin").run)
schedule.every().day.at("13:00").do(Parser(brands["Pull & Bear"], "Pull & Bear").run)
schedule.every().day.at("13:00").do(Parser(brands["Puma"], "Puma").run)
schedule.every().day.at("13:00").do(Parser(brands["Quiksilver"], "Quiksilver").run)
schedule.every().day.at("13:00").do(Parser(brands["QUO"], "QUO").run)
schedule.every().day.at("13:00").do(Parser(brands["Ralph Lauren"], "Ralph Lauren").run)
schedule.every().day.at("13:00").do(Parser(brands["RE DESIGN"], "RE DESIGN").run)
schedule.every().day.at("13:00").do(Parser(brands["Reebok"], "Reebok").run)
schedule.every().day.at("13:00").do(Parser(brands["Roxy"], "Roxy").run)
schedule.every().day.at("13:00").do(Parser(brands["Salomon"], "Salomon").run)
schedule.every().day.at("13:00").do(Parser(brands["Scalpers"], "Scalpers").run)
schedule.every().day.at("13:00").do(Parser(brands["Speedlife"], "Speedlife").run)
schedule.every().day.at("13:00").do(Parser(brands["Staff"], "Staff").run)
schedule.every().day.at("13:00").do(Parser(brands["Superfly"], "Superfly").run)
schedule.every().day.at("13:00").do(Parser(brands["Timberland"], "Timberland").run)
schedule.every().day.at("13:00").do(Parser(brands["Tommy Hilfiger"], "Tommy Hilfiger").run)
schedule.every().day.at("13:00").do(Parser(brands["Tommy Jeans"], "Tommy Jeans").run)
schedule.every().day.at("13:00").do(Parser(brands["Tony Montana"], "Tony Montana").run)
schedule.every().day.at("13:00").do(Parser(brands["TSHIRT35"], "TSHIRT35").run)
schedule.every().day.at("13:00").do(Parser(brands["U.S. Polo Assn."], "U.S. Polo Assn.").run)
schedule.every().day.at("13:00").do(Parser(brands["United Colors of Benetton"], "United Colors of Benetton").run)
schedule.every().day.at("13:00").do(Parser(brands["Vans"], "Vans").run)
schedule.every().day.at("13:00").do(Parser(brands["W Collection"], "W Collection").run)
schedule.every().day.at("13:00").do(Parser(brands["Zühre"], "Zühre").run)
schedule.every().day.at("13:00").do(Parser(brands["Under Armour"], "Under Armour").run)

if __name__ == '__main__':
    while True:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        )
        schedule.run_pending()
        time.sleep(1)




