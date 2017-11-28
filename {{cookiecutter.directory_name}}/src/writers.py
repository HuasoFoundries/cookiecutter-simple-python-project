import pandas as pd

def df_writer_excel(df, file_name, engine=None):

    extension = 'xls'

    if engine == 'xlsxwriter':
        extension = 'xlsx'

    output_file = '{file_name}.{extension}'.format(file_name=file_name,
                                                   extension=extension)

    writer = pd.ExcelWriter(output_file)
    
    df.to_excel(writer,
                engine=engine,
                sheet_name='Sheet1',
                index=False)

    writer.save()
