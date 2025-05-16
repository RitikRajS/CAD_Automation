from data import class_data, flange_details, tensioner, bolt_pitch, clamp_details
from user_inputs import class_input, size_input, cav_len, cavity_dims, pipeWT
from mathCAD import mathCadapp, clamp_overall, save_results


classes = class_data() # pressure & temp for each class
flanges, flange_sizes = flange_details() # available flange size and details for each flange 


def calculations():

    """
    Final output from the mathcad 
    which will be used for inventor modeling
    """
    # getting info
    pressure, temp, selected_class= class_input(classes)
    nps, selected_flange = size_input(selected_class, flanges, flange_sizes)
    pipe_wt = pipeWT()
    bolt_thread = bolt_pitch(selected_flange['Bolt_Dia'])
    tensioner_details = tensioner(selected_flange['Bolt_Dia'])
    print(tensioner_details)
    print(tensioner_details['load_capacity'])
    cavity_length = cav_len(nps)

    # mathcad section

    mathcad = mathCadapp()

    clampDims = clamp_overall(mathcad,
            pressure, 
            temp, 
            nps, 
            pipe_wt,
            cavity_length,
            selected_flange['Bolt_Dia'],
            selected_flange['Bolthole_Dia'],
            bolt_thread,
            tensioner_details['load_capacity'],
            tensioner_details['tensioner_width'],
            tensioner_details['c_dim'],
            tensioner_details['nut_hole'],
            tensioner_details['nuthole_depth '],
            )
    
    
    results, data = save_results(selected_class, nps, clampDims, cavity_length)

    file_name = clamp_details(results)

    return data


if __name__ == "__main__":
    calculations()
