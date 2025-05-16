from cals import calculations
from inventor import inventor_app

def main():

    details = calculations() # sample details for all the clamp

    print(details)

    inventor = inventor_app(details)


if __name__ == "__main__":
    main()
