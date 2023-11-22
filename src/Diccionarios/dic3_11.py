def main(): 

    info_cliente = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

    lineas = info_cliente.split ("\n")

    nombres_campos = lineas[0].split(";")

    directorio_clientes = {}
    
    for linea in lineas[1:]:
        if linea:
            valores = linea.split(";")

            cliente_info = {}

            if len(nombres_campos) == len (valores):
                for i in range(len(nombres_campos)):
                    cliente_info[nombres_campos[i]] = valores[i]
            
            directorio_clientes[valores[0]] = cliente_info

    print(directorio_clientes)

if __name__ == "__main__":
    main()