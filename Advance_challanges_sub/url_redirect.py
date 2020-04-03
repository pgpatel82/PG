import requests
import xlrd
import xlwt
import xlutils.copy
import certifi

if __name__ == '__main__':
    import sys
    rb = xlrd.open_workbook("C:\\Prahlad\\Project\\Redirect_17oct19.xlsx") 
    sheet = rb.sheet_by_index(0)
    wb = xlutils.copy.copy(rb)
    sheet1 = wb.get_sheet(0)
    for row in range(1,sheet.nrows):
        current_url = sheet.cell_value(row, 0) 
        #print(current_url)
        new_url = sheet.cell_value(row, 1)
        #print(new_url)
        #resolve_url(current_url)
        #r = requests.get(current_url)
        r = requests.get(current_url, auth=('XXX', 'XXX'))
        sheet1.write(row, 2, r.url)
        sheet1.write(row, 3, r.status_code)
        wb.save("C:\\Prahlad\\Project\\Redirect_17oct19_output.xls")
        #print(r.url)
        if (new_url+"/".casefold() == r.url.casefold()) or (new_url.casefold() == r.url.casefold()):
            sheet1.write(row, 4, "YES")
        else:
            sheet1.write(row, 4, "NO")
    wb.save("C:\\Prahlad\\Project\\Redirect_17oct19_output.xls")
