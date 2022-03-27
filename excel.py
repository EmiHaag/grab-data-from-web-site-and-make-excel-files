import xlsxwriter
import datetimer

#set global max excel columns 
max_col = 6

#excel file creator with custom employee data
def createExcel(arr, name, surplusUSD):
    
    #set names for excel template
    columns = ["Legajo", "Part number", "Part name", "Cantidad", "Fecha", "Cost $USD"]
    
    #set filename
    fileName ='excel/'+name+'.xlsx' 
    
    #create workbook with sxlswriter
    workbook = xlsxwriter.Workbook(fileName)
    
    #add worksheet
    worksheet = workbook.add_worksheet('Surplus')
    worksheet.set_column('A:F', 20) 
    rows_str = str(len(arr)+1)
    
    # Create a list of column headers, to use in add_table().
    column_settings = [{'header': column} for column in columns]

    
    # Add a table to the worksheet with the custom employee data.
    worksheet.add_table('A1:F' + rows_str, {'data': arr, 'columns': column_settings})
    
    #add fonts format 
    cell_format_red = workbook.add_format({'bold':True, 'font_color': 'white'})
    cell_format_red.set_bg_color('red')


    #add the font format if condition is true, in this case the value 'date' is passed over seven days
    for i, x in enumerate(arr):     
        #call custom function to check if it's value is 7 days passed 
        if datetimer.passedSevenDays(x[4]):    
            worksheet.write(i+1 , 4, x[4], cell_format_red )
     
          

    #adding extra line information about employee
    cell= [(len(arr)+4), 0]
    cell_format = workbook.add_format({'bold':True, 'font_color': 'red', 'font_size':20})
    worksheet.write(cell[0],cell[1], surplusUSD + ' máx tolerable 7 days: $250', cell_format )
    worksheet.set_row(cell[0], 25) 

    worksheet.row_col_headers
    
    #add read only property to excel file
    workbook.read_only_recommended()
    
    #close file, once finished 
    workbook.close()
   
    
   
