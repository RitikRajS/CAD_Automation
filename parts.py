"""
RETURNS A LIST OF ALL THE PARTS DETAILS 
INCLUDED IN THE ASSEMBLY
"""
import os 


def all_parts():

    path= os.getcwd()
    # all the parts that we've got in our assembly
    #LONGITUDINAL SEALS 
    long_outer_seal = {
        'id':'LOS',
        'name':'l_outer_seal',
        'model_no': 'P0003021.ipt',
        'drawing_no': 'P0003021.idw',
        'model_path':f"{path}//ref_model//parts//P0003021.ipt",
        'drawing_path': f"{path}//ref_drawings//P0003021.idw"
    }

    long_inner_seal = {
        'id':'LIS',
        'name':'l_inner_seal',
        'model_no': 'P0003356.ipt',
        'drawing_no': 'P0003356.idw',
        'model_path':f"{path}//ref_model//parts//P0003356.ipt",
        'drawing_path': f"{path}//ref_drawings//P0003356.idw"
    }

    # RADIAL SEALS 
    rad_seal = {
        'id':'RAS',
        'name':'rad_seal',
        'model_no': 'P0003022.ipt',
        'drawing_no': 'P0003022.idw',
        'model_path':f"{path}//ref_model//parts//P0003022.ipt",
        'drawing_path': f"{path}//ref_drawings//P0003022.idw"
    }

    # LONGITUDINAL AE
    long_out_ae1={
        'id':'LOAE1',
        'name':'long_out_ae1',
        'model_no': 'P0006083.ipt',
        'drawing_no': 'P0006083.idw',
        'model_path':f"{path}//ref_model//parts//P0006083.ipt",
        'drawing_path': f"{path}//ref_drawings//P0006083.idw"
    }

    long_out_ae2={
        'id':'LOAE2',
        'name':'long_out_ae2',
        'model_no': 'P0006084.ipt',
        'drawing_no': 'P0006084.idw',
        'model_path':f"{path}//ref_model//parts//P0006084.ipt",
        'drawing_path': f"{path}//ref_drawings//P0006084.idw"
    }

    long_out_ae3={
        'id':'LOAE3',
        'name':'long_out_ae3',
        'model_no': 'P0006085.ipt',
        'drawing_no': 'P0006085.idw',
        'model_path':f"{path}//ref_model//parts//P0006085.ipt",
        'drawing_path': f"{path}//ref_drawings//P0006085.idw"
    }

    long_out_ae4={
        'id':'LOAE4',
        'name':'long_out_ae4',
        'model_no': 'P0006086.ipt',
        'drawing_no': 'P0006086.idw',
        'model_path':f"{path}//ref_model//parts//P0006086.ipt",
        'drawing_path': f"{path}//ref_drawings//P0006086.idw"
    }

    # INNER LONG SEAL AE     
    long_in_ae1={
        'id':'LIAE1',
        'name':'long_in_ae1',
        'model_no': 'P0006087.ipt',
        'drawing_no': 'P0006087.idw',
        'model_path':f"{path}//ref_model//parts//P0006087.ipt",
        'drawing_path': f"{path}//ref_drawings//P0006087.idw"
    }

    long_in_ae2={
        'id':'LIAE2',
        'name':'long_in_ae2',
        'model_no': 'P0006088.ipt',
        'drawing_no': 'P0006088.idw',
        'model_path':f"{path}//ref_model//parts//P0006088.ipt",
        'drawing_path': f"{path}//ref_drawings//P0006088.idw"
    }

    long_in_ae3={
        'id':'LIAE3',
        'name':'long_in_ae3',
        'model_no': 'P0006089.ipt',
        'drawing_no': 'P0006089.idw',
        'model_path':f"{path}//ref_model//parts//P0006089.ipt",
        'drawing_path': f"{path}//ref_drawings//P0006089.idw"
    }

    long_in_ae4={
        'id':'LIAE4',
        'name':'long_in_ae4',
        'model_no': 'P0006090.ipt',
        'drawing_no': 'P0006090.idw',
        'model_path':f"{path}//ref_model//parts//P0006090.ipt",
        'drawing_path': f"{path}//ref_drawings//P0006090.idw"
    }

    #RADIAL AE 
    rad_ae1={
        'id':'RDAE1',
        'name':'rad_ae1',
        'model_no': 'P0003025.ipt',
        'drawing_no': 'P0003025.idw',
        'model_path':f"{path}//ref_model//parts//P0003025.ipt",
        'drawing_path': f"{path}//ref_drawings//P0003025.idw"
    }

    rad_ae2={
        'id':'RDAE2',
        'name':'rad_ae2',
        'model_no': 'P0003026.ipt',
        'drawing_no': 'P0003026.idw',
        'model_path':f"{path}//ref_model//parts//P0003026.ipt",
        'drawing_path': f"{path}//ref_drawings//P0003026.idw"
    }

    rad_ae3={
        'id':'RDAE3',
        'name':'rad_ae3',
        'model_no': 'P0003027.ipt',
        'drawing_no': 'P0003027.idw',
        'model_path':f"{path}//ref_model//parts//P0003027.ipt",
        'drawing_path': f"{path}//ref_drawings//P0003027.idw"
    }

    rad_ae4={
        'id':'RDAE4',
        'name':'rad_ae4',
        'model_no': 'P0003028.ipt',
        'drawing_no': 'P0003028.idw',
        'model_path':f"{path}//ref_model//parts//P0003028.ipt",
        'drawing_path': f"{path}//ref_drawings//P0003028.idw"
    }

    # Fabrications 
    fab1={
        'id':'FAB1',
        'name':'fab1',
        'model_no': 'CF00000563-01.ipt',
        'drawing_no': 'CF00000563-01.idw',
        'model_path':f"{path}//ref_model//fabrications//CF00000563-01.ipt",
        'drawing_path': f"{path}//ref_drawings//CF00000563-01.idw"
    }

    incon1={
        'id':'INC1',
        'name':'inco1',
        'model_no': 'CF00000563-02.ipt',
        'drawing_no': 'CF00000563-02.idw',
        'model_path':f"{path}//ref_model//fabrications//CF00000563-02.ipt",
        'drawing_path': f"{path}//ref_drawings//CF00000563-02.idw"
    }

    fab2={
        'id':'FAB2',
        'name':'fab2',
        'model_no': 'CF00000563-03.ipt',
        'drawing_no': 'CF00000563-03.idw',
        'model_path':f"{path}//ref_model//fabrications//CF00000563-03.ipt",
        'drawing_path': f"{path}//ref_drawings//CF00000563-03.idw"
    }

    incon2={
        'id':'INC2',
        'name':'inco2',
        'model_no': 'CF00000563-04.ipt',
        'drawing_no': 'CF00000563-04.idw',
        'model_path':f"{path}//ref_model//fabrications//CF00000563-04.ipt",
        'drawing_path': f"{path}//ref_drawings//CF00000563-04.idw"
    }

    # Assembly Models 
    rad_seal_assembly={
        'id':'rsa',
        'name':'rad_seal_assembly',
        'model_no': 'A0000008.iam',
        'drawing_no': 'A0000008.idw',
        'model_path':f"{path}//ref_model//assembly//A0000008.iam",
        'drawing_path': f"{path}//ref_drawings//A0000008.idw"
    }

    long_seal_assembly={
        'id':'lsa',
        'name':'long_seal_assembly',
        'model_no': 'A0000009.iam',
        'drawing_no': 'A0000009.idw',
        'model_path':f"{path}//ref_model//assembly//A0000009.iam",
        'drawing_path': f"{path}//ref_drawings//A0000009.idw"
    }    
    part_list = [
                long_outer_seal, long_inner_seal, rad_seal, long_out_ae1,
                 long_out_ae2, long_out_ae3, long_out_ae4, long_in_ae1, long_in_ae2,
                 long_in_ae3, long_in_ae4, rad_ae1, rad_ae2, rad_ae3, rad_ae4,
                 ]
    
    assembly_list=[rad_seal_assembly, long_seal_assembly]

    return part_list, assembly_list