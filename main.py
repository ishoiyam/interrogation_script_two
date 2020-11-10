from getInfo import get_information
from printCard import print_card
from greeting import greetings
from save_to_Db import connect_to_db, insert_one, get_data


def main():
    # connecting to db
    connect_to_db()
    
    # starting program
    greetings()
    fn, ln, emaddr, haddr, origin = get_information()
    print_card(fn, ln, emaddr, haddr, origin)
    insert_one(fn, ln, emaddr, haddr, origin)
    get_data()




if __name__ == "__main__":
    main()
