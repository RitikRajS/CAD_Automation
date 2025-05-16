from MathcadPy import Mathcad
import easygui
import os 
import csv

"""
To access MATHCAD and get the outputs from it 
"""

def mathCadapp():

    """
    To acess MATHCAD 
    """

    mathCad= Mathcad()

    file_path =  os.path.abspath('mathcad_cals/bolt_calculations.mcdx')

    mathCad_file = mathCad.open(file_path)

    return mathCad_file

def input_var(mathcad):
    '''
    Getting Inputs and Outputs from the Mathcad
    '''
    # provides a list of inouts and output variables 
    in_variables = mathcad.inputs()
    out_variables = mathcad.outputs()

    inputs ={}
    outputs={}

    for variable in in_variables:
        inputs[variable]=mathcad.get_input(variable)

        
    for variable in out_variables:
        outputs[variable]=mathcad._get_output(variable)


    return inputs, outputs


def clamp_overall(mathcad,
            pressure, 
            temp, 
            nps, 
            pipe_wt,
            L_cavity,
            Db,
            Dbolthole,
            thread,
            tensioner_cap, 
            tensioner_width, 
            tensioner_sideC,
            nut_hole,
            nut_depth
            ):
    """
    Will link to the mathcad to provide the inputs
    And obtain the number of bolts required 
    """
    print(f"{pressure},\n{temp},\n{nps},\n{pipe_wt},\n{L_cavity},\n {Db},\n {thread},")

    pressure = float(pressure)*10**5
    temp =float(temp) + 273.15
    nps = float(nps) * 0.0254
    pipe_wt =float(pipe_wt)* 0.001
    L_cavity =float(L_cavity)* 0.001
    Db = float(Db) * 0.0254
    thread= float(thread)
    Dbolthole= float(Dbolthole) * 0.0254
    tensioner_cap= float(tensioner_cap)*1000 # from used tensioner 
    tensioner_width = float(tensioner_width)*0.0254
    tensioner_sideC = float(tensioner_sideC)*0.0254
    nut_hole = float(nut_hole)*0.001
    nut_depth = float(nut_depth)*0.001

    mathcad.set_real_input('Pi', pressure)
    mathcad.set_real_input('Tmax', temp)
    mathcad.set_real_input('Dopipe', nps)
    mathcad.set_real_input('t', pipe_wt)
    mathcad.set_real_input('Lcavity', L_cavity)
    mathcad.set_real_input('DB', Db)
    mathcad.set_real_input('np', thread)
    mathcad.set_real_input('Dbolthole', Dbolthole)
    mathcad.set_real_input('Ftensioner', tensioner_cap)
    mathcad.set_real_input('Tensionerwidth', tensioner_width)
    mathcad.set_real_input('Tensionerc', tensioner_sideC)
    mathcad.set_real_input('nut_hole', nut_hole)
    mathcad.set_real_input('nut_depth', nut_depth)
    out_variables = mathcad.outputs()

    in_variables=mathcad.inputs()

    outputs={}

    inputs={}

    for variable in out_variables:
        outputs[variable]=mathcad._get_output(variable)

    
    for variable in in_variables:
        inputs[variable]=mathcad.get_input(variable)

    # print('MathCAD Outputs', sorted(outputs.items()))
    # print('MathCAD Inputs', sorted(inputs.items()))

    return outputs


def save_results(selected_class, nps, results, cavity_length):

    """
    To get the mathcad results as a csv output
    """

    data=[]

    dims ={}
    
    out_to_var = {
    'out': 'Dout_wid',
    'out_0': 'Din_wid',
    'out_1': 'LO1AE_l',
    'out_10': 'Do_AE',
    'out_11': 'DIC',
    'out_14': 'Dcav1',
    'out_15': 'nut_depth',
    'out_16': 'nut_hole',
    'out_18': 'DB',
    'out_19': 'Din_L',
    'out_2': 'LO1AE_w',
    'out_22': 'Dcavout',
    'out_24': 'Dbolthole',
    'out_25': 'Dcav',
    'out_26': 'Din_R',
    'out_27': 'Dorad_seal',
    'out_28': 'Din_L2',
    'out_29': 'Din_R2',
    'out_3': 'LI1AE_l',
    'out_30': 'Dout_L',
    'out_31': 'Dout_R',
    'out_32': 'Dout_L2',
    'out_33': 'Dout_R2',
    'out_34': 'Gapbolt',
    'out_35': 'Gapedge',
    'out_36': 'ri.clamp',
    'out_37': 'Gapouter',
    'out_39': 'ro.clamp',
    'out_4': 'LI1AE_w',
    'out_40': 'Lec2',
    'out_41': 'Wc',
    'out_42': 'thickness',
    'out_43': 'Refp',
    'out_44': 'Refp1',
    'out_45': 'Nb',
    'out_5': 'LO2AE_l',
    'out_6': 'LO2AE_w',
    'out_7': 'LI2AE_l',
    'out_8': 'LI2AE_w',
    'out_9': 'Le'
}
    print('before saving')

    if len(results) == len(out_to_var):

        for key, values in results.items():

            item = {
                'Name': out_to_var[key],
                'Value': round(float(values[0]), 4),
                'Unit': values[1]
            }
            data.append(item)

            
            dims[out_to_var[key]]=round(float(values[0]),4)

        dims['NPS']= nps
        dims['Class']= selected_class
        dims['cavity']=cavity_length

    else:
        print('Check the Variable Field name list')

    
    file_name = f'C{selected_class}_NPS{nps}_L{round(cavity_length)}.csv'
    file_path = rf'results/'

    file= file_path+file_name

    with open(file, 'w', newline='') as file:
        writer = csv.DictWriter(file, data[0].keys(), delimiter=" ")
        writer.writeheader()
        writer.writerows(data)

    return file.name, dims

