"""
Scripts related to getting user inputs and validating the inputs 
"""

def class_input(flange_data):
    """
    To get the class from the user
    """

    # first element is temp 
    classes = list(flange_data.keys())[1:]

    while True:
        try:
            cl = input('Please Enter the Class: ')

            if cl in classes:
                return float(flange_data[cl]), float(flange_data['Temp']), cl
            
            else:
                print('Please Enter a Valid Class')

        except (ValueError, TypeError):
            print('Please Enter a Valid Class')


def pipeWT():
    """
    To get the WT of the pipe as an Input 
    """

    while True:
        
        try:

            pipe_wt = float(input('Enter the Pipe WT in mm: '))

            if pipe_wt > 0.01:
                return pipe_wt
            else:
                print('Enter a valid number')
        
        
        except (ValueError, TypeError):
            print('Enter a valid number')



def size_input(selected_class, flanges, flange_sizes):

    """
    To get the size of the pipe and return the respective class dims 
    """

    while True:

        nps = round(float(input("Please enter the NPS size in inch: ")),1)

        if nps in flange_sizes:
            for i in range(len(flanges)):

                if nps == float(flanges[i]['NPS']) and selected_class == flanges[i]['Sheet Name']:
                    selected_flange = {'Flange_Dia':float(flanges[i]['Flange_Dia']),
                                'No._bolts':float(flanges[i]['No._bolts']),
                                'Bolt_Dia':float(flanges[i]['Bolt_Dia']),
                                'Bolthole_Dia':float(flanges[i]['Bolthole_Dia']),
                                'Bolt_Circle':float(flanges[i]['Bolt_Circle']),
                                    }
                    
                    return nps, selected_flange
                
        else:
            print("Please Enter a Valid Pipe size in Inches")


def cavity_dims(nps, cavity_length):

    """
    To calculate the cavity dims for validation 
    """

    # Constant Values
    W_seal = 28
    Seal_gap = 20
    Sealedge_gap = 42
    Pipe_edge = 15
    nps = nps *25.4

    Din_L = cavity_length
    Din_L2 = Din_L+(2*W_seal)
    Dout_L = Din_L2+(2*Seal_gap)
    Dout_L2 = Dout_L+(2*W_seal)
    Dcavity= nps +(2*Pipe_edge)
    Din_R=Dcavity+(2*Sealedge_gap)
    Din_R2=Din_R+(2*W_seal)
    Dout_R=Din_R2+(2*Seal_gap)
    Dout_R2=Dout_R+(2*W_seal)

    cavity_dims = {
        "l_cavity":round(cavity_length,2),
        "Din_L2":round(Din_L2,2),
        "Dout_L":round(Dout_L,2),
        "Dout_L2":round(Dout_L2,2),
        "Dcavity":round(Dcavity,2),
        "Din_R":round(Din_R,2),
        "Din_R2":round(Din_R2,2),
        "Dout_R":round(Dout_R,2),
        "Dout_R2":round(Dout_R2,2)
    }

    return cavity_dims
        

def cav_len(nps):

    while True:

        try:
            l_cavity = float(input("l_cavity mm: "))
            break
        
        except ValueError as e:
            print("Enter a valid number")


    if l_cavity < (nps*25.4)*1.5:# converting from inches to mm 
        l_cavity = (nps*25.4)*1.5

    Din_L = l_cavity

    return Din_L
