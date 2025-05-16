import pandas as pd
import easygui 
import os 


def main():
    df_csv()

def df_csv():
    current_path = os.getcwd()

    print('Please select the Excel File: ')
    path = easygui.fileopenbox('Please Select the file')
    csv_path= easygui.diropenbox('Please select the location to save the CSV file')

    while True:
        try:
            xl = pd.ExcelFile(path)

            sheet_names = xl.sheet_names

            break 

        except Exception:
            print('Please select an Excel File')


    file_name = path.split('\\')


    if len(sheet_names) == 1:

        df= pd.read_excel(path)

        df.to_csv(rf'{current_path}\{file_name[-1].split('.')[0]}.csv', index=False)
        
    else:

        # this is where we'll hold all the DF
        combined_df = pd.DataFrame()

        for sheet in sheet_names:

            # excel_file opens the excel file, and here we're reading it 
            df = xl.parse(sheet)

            df['Sheet Name'] = sheet
            
            # Combining the sheets 
            combined_df = pd.concat([combined_df, df], ignore_index=True)
            
            combined_df.to_csv(rf'{current_path}\{file_name[-1].split('.')[0]}.csv', index=False)


    print("The file has been converted to a CSV file ")


if __name__ == '__main__':
    main()