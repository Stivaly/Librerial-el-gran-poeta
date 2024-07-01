import csv
import random

csv_file = r'scripts-bd/migracion/autor.csv'
sql_script = 'scripts-bd/migracion/autor.sql'

with open(csv_file, 'r', encoding='utf-8-sig', errors='ignore') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    with open(sql_script, 'w') as script:
        line_count = 0
        for row in reader:
            id_pais_min = 1
            id_pais_max = 240
            
            id_autor = row[0]
            autor_genero = row[1]
            nombre_autor = row[2]
            autor_rating_promedio = row[3]
            cantidad_rating_autor = row[4]
            cantidad_comentarios = row[5]
            id_pais_id = random.randint(id_pais_min, id_pais_max)
            
            insert_statement = f"""INSERT INTO inventario_autor (id_autor, autor_genero, nombre_autor, autor_rating_promedio, cantidad_rating_autor, cantidad_comentarios, id_pais_id) 
                                    VALUES ({id_autor}, '{autor_genero}', '{nombre_autor}', {autor_rating_promedio}, {cantidad_rating_autor}, {cantidad_comentarios}, {id_pais_id} );\n"""
            script.write(insert_statement)
            
            line_count += 1
            print(f"Line {line_count} written.")