import csv

"""
All the engineering tables and data gathering scripts
"""

def class_data():

    """
    To get the pressure and temp associated with each class
    """

    file_name = rf'csv_files\Flange_class.csv'

    try:

        with open(file_name, newline='') as file:

            reader= csv.DictReader(file)

            i = 1
            for row in reader:
                
                i += 1

                # for 100 C value 
                if i == 4: # CHANGE THIS TO CHANGE THE REQUIRED TEMP (4: 100C, 3: 50C, 2:38C, 1:-29C)
                    return row

    
    except FileNotFoundError:
        print("Error: Flange Class CSV does not exist")
        return None
    

def flange_details():

    """
    To get the flange details 
    """

    file_name = rf'csv_files\Flange_data.csv'

    try:

        flange_sizes=[] # All Available flange sizes 
        flanges= [] # details about all flanges 

        with open(file_name, newline='') as file:

            reader= csv.DictReader(file)

            for row in reader:

                flange_sizes.append(float(row['NPS']))
                flanges.append(row)

        flange_sizes=list(set(flange_sizes))
        
        flange_sizes = sorted(flange_sizes)

        return flanges, flange_sizes
    
    except FileNotFoundError:
        print("Error: Flange Detail CSV does not exist")
        return None
            

def tensioner(bolt_size):

    """
    Tensioner details based on bolt size
    """

    file_name = rf'csv_files\tensioner_size.csv'

    with open(file_name) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if float(row['bolt_size']) == bolt_size:

                return row
            
def bolt_pitch(bolt_dia):
    """
    Bolt threads based on bolt size
    """

    with open(rf'csv_files\bolt_sizes.csv') as file:
        
        reader = csv.DictReader(file)

        for row in reader:
            if float(row['Nominal Diameter (inches)']) == bolt_dia:
                return row['Threads per Inch (TPI)']
            


def clamp_details(file_name):

    details=[]

    with open(file_name) as file:
    
        reader = csv.DictReader(file)

        for row in reader:
            details.append(row)

    return file_name