"""
Used to form a connection with inventor 
"""

from win32com.client import  gencache, Dispatch, constants, DispatchEx, CastTo
import pandas as pd
import os 
from parts import all_parts
from datetime import datetime


def date():
    x = datetime.today().strftime('%d/%m/%Y')
    return x

def update_mass(doc):
    """
    ACCEPTS A MODEL OBJECT, AND UPDATES THE MASS
    """
    mass = doc.ComponentDefinition.MassProperties.Mass

    return mass


def inch_cm(number):

    """ CONVERTS FROM INCHES TO CM """

    number = float(number)*2.54

    return number

def mm_cm(number):

    """ CONVERTS FROM MM TO CM """

    number = float(number)*0.1

    return number

def m_cm(number):

    """ CONVERTS FROM MM TO CM """

    number = float(number)*100

    return number

def m_mm(number):

    """ CONVERTS FROM MM TO MM """

    number = float(number)*1000

    return number


def parts(invApp, path, sample, part_list):

    """
    CREATES A COPY OF THE REFERENCE PART 
    AND SAVES A COPY IN THE DESIGNATED LOCATION
    """
    new_parts={}

    longAE_out = ['long_out_ae1', 'long_out_ae2', 'long_out_ae3', 'long_out_ae4']
    longAE_in = ['long_in_ae1', 'long_in_ae2', 'long_in_ae3', 'long_in_ae4']
    radAE = ['rad_ae1', 'rad_ae2', 'rad_ae3', 'rad_ae4']

    for part in part_list:
    # opening the part
        part_doc = invApp.Documents.Open(part['model_path'])

        for document in invApp.Documents:

            if document.DisplayName.lower()==part['model_no'].lower():

                part_doc=document

                break

        # casting the document to a part document (letting the document know that it is a part document)
        part_document=CastTo(part_doc, "PartDocument")

        parameters = part_document.ComponentDefinition.Parameters
        #Access the user parameters
        user_parameters = parameters.UserParameters

        #access the mass of the part 
        mass = part_document.ComponentDefinition.MassProperties.Mass

        print('Before updating Mass: ', mass)

        
    #All user parameters
        for i in range(user_parameters.Count):
            param = user_parameters.Item(i+1)  
            print(f"Parameter Name: {param.Name}, Value: {param.Value}, Units: {param.Units}")

            # FOR SEALS AND AE PLATES
            if part['name'] == 'l_outer_seal':
                user_parameters.Item("Dout_wid").Value = m_cm(sample['Dout_wid'])
                user_parameters.Item("Dout_L2").Value = m_cm(sample['Dout_L2'])

            elif part['name'] == 'l_inner_seal':
                user_parameters.Item("Din_wid").Value = m_cm(sample['Din_wid'])
                user_parameters.Item("Dout_L2").Value = m_cm(sample['Dout_L2'])

            elif part['name'] == 'rad_seal':
                user_parameters.Item("Dorad_seal").Value = m_cm(sample['Dorad_seal'])

            elif part['name'] in longAE_out:
                if part['name'] == 'long_out_ae1' or part['name'] == 'long_out_ae2':
                    user_parameters.Item("LO1AE_l").Value = m_cm(sample['LO1AE_l'])
                    user_parameters.Item("LO1AE_w").Value = m_cm(sample['LO1AE_w'])
                else:
                    user_parameters.Item("LI1AE_w").Value = m_cm(sample['LI1AE_w'])
                    user_parameters.Item("LI1AE_l").Value = m_cm(sample['LI1AE_l'])

            elif part['name'] in longAE_in:
                if part['name'] == 'long_in_ae1' or part['name'] == 'long_in_ae2':
                    user_parameters.Item("LO2AE_l").Value = m_cm(sample['LO2AE_l'])
                    user_parameters.Item("LO2AE_w").Value = m_cm(sample['LO2AE_w'])
                else:
                    user_parameters.Item("LI2AE_l").Value = m_cm(sample['LI2AE_l'])

            elif part['name'] in radAE:

                user_parameters.Item("Do_AE").Value = m_cm(sample['Do_AE'])/2

        #updating the part mass 
        mass = update_mass(part_document)

        # Access the PropertySets to update the Mass property
        prop_sets = part_doc.PropertySets

        for prop in prop_sets:
            print(prop.Name)

        # updating the part 
        part_doc.Update()

        # saving new part 

        name= f"N_{part['name']}"
        
        file_path= f"{path}//new_models//Clamp-{sample['NPS']}-{sample['Class']}//{part['id']}-{sample['NPS']}-{sample['Class']}.ipt"

        new_parts[name] = file_path

        part_doc.SaveAs(file_path, True)

        part_doc.Close(True)

    return new_parts


def assembly(invApp, path, samples, part_list, new_parts, assembly_list):
    
    """
    CREATES A COPY FOR THE ASSEMBLY 
    AND REPLACES THE PARTS IN THE ASSEMBLY
    """

    new_assembly={}

    for assembly_model in assembly_list:

        assembly_doc = invApp.Documents.Open(assembly_model['model_path'])

        for document in invApp.Documents:

            if document.DisplayName.lower()==assembly_model['model_no'].lower():

                assembly_doc=document

                break

        assembly_document=CastTo(assembly_doc, "AssemblyDocument") 

        #access the mass of the part 
        mass = assembly_document.ComponentDefinition.MassProperties.Mass

        assembly_def = assembly_document.ComponentDefinition

        occurences = assembly_def.Occurrences

        for occurence in occurences:

            component_Name = occurence.Name.split(':')[0]

            if assembly_model['id'] =='rsa': # Radial Seal 

                for part in part_list:

                    part_no = part['model_no'].split('.')[0]
                    part_name = part['name']
                    
                    if component_Name.lower() == part_no.lower():

                        occurence.Replace(new_parts[f'N_{part_name}'], True)

                
            elif assembly_model['id'] =='lsa': # logitudinal Seal 

                for part in part_list:

                    part_no = part['model_no'].split('.')[0]
                    part_name = part['name']
                    
                    if component_Name.lower() == part_no.lower():

                        occurence.Replace(new_parts[f'N_{part_name}'], True)

        assembly_doc.Update()

        # NEED TO UPDATE THE DESCRIPTION OF THE NEWLY CREATED ASSEMBLY 

        prop = assembly_doc.PropertySets.Item("Design Tracking Properties")

        if assembly_model['id'] =='rsa':
            prop('Description').Value = f"{samples['NPS']} INCH RADIAL SEAL"

        elif assembly_model['id'] =='lsa':
            prop('Description').Value = f"{samples['NPS']} INCH LONGITUDINAL SEAL"

        #updating the part mass 
        mass = update_mass(assembly_document)

        if assembly_model['id'] =='rsa':
            file_path = f"{path}//new_models//Clamp-{samples['NPS']}-{samples['Class']}//RS-{samples['NPS']}-{samples['Class']}.iam"  
            new_assembly['rsa'] = file_path
        
        elif assembly_model['id'] =='lsa':
            file_path = f"{path}//new_models//Clamp-{samples['NPS']}-{samples['Class']}//LS-{samples['NPS']}-{samples['Class']}.iam"  
            new_assembly['lsa'] = file_path

        assembly_doc.SaveAs(file_path, True) 

        assembly_doc.Close(True)

    return new_assembly



def drawing(invApp, path, sample, new_parts, new_assembly, part_list, assembly_list):
    """
    CREATES A DRAWING FOR THE NEWLY CREATED ASSEMBLY 
    AND PART  
    """
    # First focus on the parts 

    for part in part_list:
        draw_doc = invApp.Documents.Open(part['drawing_path'])

        for document in invApp.Documents:
            
           if document.DisplayName.lower()==part['drawing_no'].lower():

               draw_doc=document

               break
               
        draw_doc =CastTo(draw_doc, "Document") 

        refdocs = draw_doc.ReferencedDocumentDescriptors

        for refpart in refdocs:

            if refpart.DisplayName == part['model_no']:

                new_path = new_parts[f'N_{part['name']}']

                refpart.ReferencedFileDescriptor.ReplaceReference(new_path)

        draw_doc.Update()

        new_drawing = f"{path}//new_drawings//Clamp-{sample['NPS']}-{sample['Class']}//{part['id']}-{sample['NPS']}-{sample['Class']}.idw"   

        draw_doc.SaveAs(new_drawing, True) 

        new_drawing_name = new_drawing.split('//')[-1]

        for document in invApp.Documents:

            if document.DisplayName.lower()==new_drawing_name.lower():

                draw_doc=document

                break

        
            draw_doc =CastTo(draw_doc, "Document") 

        prop = draw_doc.PropertySets.Item("Design Tracking Properties")

        prop('Description').Value = f"{sample['NPS']} INCH {part['id']}"
        prop('Designer').Value = "RR"
        prop('Checked By').Value = ""
        prop('Engr Approved By').Value = ""
        prop('Date Checked').Value = date()
        prop('Creation Time').Value = date()
        prop('Part Number').Value = F"{part['id'].upper()}-{sample['NPS']}-{sample['Class']}"
        
        draw_doc.Update()
        draw_doc.Save()
        draw_doc.Close(False)


def inventor_app(samples):

    """
    Establish connection with Inventor 
    """

    # dispatch will connect to inventor and set the visibility of the app to true 
    invApp = Dispatch("Inventor.Application")
    invApp.Visible = True

    Cast2 = gencache.EnsureModule('{D98A091D-3A0F-4C3E-B36E-61F62068D488}', 0, 1, 0)
    invApp = Cast2.Application(invApp)


    path= os.getcwd()

    # all the parts that we've got in our assembly

    part_list, assembly_list = all_parts()

    # For Parts 
    new_parts = parts(invApp, path, samples, part_list)

    print(new_parts)
    
    new_assembly= assembly(invApp, path, samples, part_list, new_parts, assembly_list)

    new_drawings = drawing(invApp, path, samples, new_parts, new_assembly, part_list, assembly_list)
