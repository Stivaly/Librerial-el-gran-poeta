import csv

csv_file = r'scripts-bd\migracion\editorial.csv'
sql_script = 'scripts-bd\migracion\editorial.sql'

with open(csv_file, 'r', encoding='utf-8-sig', errors='ignore') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    with open(sql_script, 'w') as script:
        line_count = 0
        for row in reader:
            id_editorial = row[0]
            editorial = row[1]
            
            insert_statement = f"INSERT INTO inventario_editorial (id_editorial, editorial) VALUES ({id_editorial}, '{editorial}');\n"
            script.write(insert_statement)
            
            line_count += 1
            print(f"Line {line_count} written.")