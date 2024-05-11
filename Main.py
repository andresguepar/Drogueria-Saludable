
from Services import Services


def main():
    
    services = Services()
    while True:
        print("\nMenú:")
        print("1. Prototype")
        print("2. Singleton")
        print("3. Builder")
        print("4. Exit")

        option = input("Select an option: ")

        if option == "1":
            services.prototype()
        elif option == "2":
             services.singleton()
        elif option == "3":
             services.builder()
        elif option == "4":
            print("Exiting...")
            break
        else:
            print("Invalid Option")
    
if __name__ == '__main__':
    main()