import xlsxwriter
import datetimer

max_col = 6


def createExcel(arr, name, surplusUSD):
    columns = ["Legajo", "Part number", "Part name", "Cantidad", "Fecha", "Cost $USD"]
    
    fileName ='excel/'+name+'.xlsx' 




    workbook = xlsxwriter.Workbook(fileName)
    #workbook.set_custom_property('surplus',       surplusUSD)
    worksheet = workbook.add_worksheet('Surplus')
    worksheet.set_column('A:F', 20) 
    rows_str = str(len(arr)+1)
    #currency_format = workbook.add_format({'num_format': '$#,##0'})
    
    # Create a list of column headers, to use in add_table().
    column_settings = [{'header': column} for column in columns]

    
    # Add a table to the worksheet.
    worksheet.add_table('A1:F' + rows_str, {'data': arr, 'columns': column_settings})
    

    cell_format_red = workbook.add_format({'bold':True, 'font_color': 'white'})
    cell_format_red.set_bg_color('red')


    
    #i = fila x= current value[array 1d]
    for i, x in enumerate(arr):     
        #print("evaluating: ind(",i,", 4) ", x[4])  
        if datetimer.passedSevenDays(x[4]):    
            #print("writing on : (",i,",4)")        
            worksheet.write(i+1 , 4, x[4], cell_format_red )
            
          

    #adding extra information about surplus
    cell= [(len(arr)+4), 0]
    cell_format = workbook.add_format({'bold':True, 'font_color': 'red', 'font_size':20})
    worksheet.write(cell[0],cell[1], surplusUSD + ' máx tolerable 7 days: $250', cell_format )
    worksheet.set_row(cell[0], 25) 

    worksheet.row_col_headers
    


    #workbook.set_custom_property('Date completed',   date.today)
    workbook.read_only_recommended()
    workbook.close()
   
    
   
