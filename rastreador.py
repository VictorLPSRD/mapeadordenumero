# Rastrado de números.
# Utilizando a biblioteca phonenumbers para fazer esse rastreio de número.
# Com a utlização da função DEF 'def() para chamar a função e inicia automaticamente.


import phonenumbers # biblioteca.

 #vl
def rastre(): # para cria um loop
    print('='*30)
    print('coloque seu numero dessa forma TUDO JUNTO') # Informação de como se deve colocar o número.
    print('       +55DD9numero') # explo de como se colocar.
    print('='*30)
    print()
    telefone= input('Digite seu numero abaixo\n') # local para pegar o numero
    print('='*30)
    print()

    telefone_ajustado= phonenumbers.parse(telefone,'pt-br')# Eu utilizo esse perse para formata o número para a biblioteca pode funcionar. 
    print(telefone_ajustado)# Exibi o número não formatado.
#vl
    telefone_formatado=telefone
    telefone_formatado_ajustado=phonenumbers.parse(telefone_formatado,'BR') #onde realmente formata 
    telefone_formatado=phonenumbers.format_number(telefone_formatado_ajustado,# Onde é formatdo o númeor do usuario  usando função format_nunber.
                                              phonenumbers.PhoneNumberFormat.NATIONAL) # phonenunberformat.national é um modelo de formatação de número e tamos usando o nacional(NATIONAL).
    print(f'O número é formatado :{telefone_formatado}')# Exibir o númeor formatdo.

    from phonenumbers import carrier # eu inportei do phonenumber o  carrier para acha a operadora do numero.
    operadora=carrier.name_for_number(telefone_ajustado,'pt-br')#  usei  a função carrier e o metodo do carrie.
    print(f'A operadora desse número: {operadora}')# oara exibir a operadora.


    from phonenumbers import geocoder # Inportei da phonenumber o geocoder para acha o ESTADO que é o número.
    local=geocoder.description_for_number(telefone_ajustado,'pt-br') # usei a função do  geocoder e o metodo dele.
    print(f'O local desse núnumero : {local}') # para exibir o local.
    
    from phonenumbers import timezone
    area_local=phonenumbers.parse(telefone,'GB')
    timezone.time_zones_for_number(area_local)
    print(area_local)                             #vl
    print('')
    rastre() #chamei a função para inicia que der o resultado.
rastre() #hamei novamente para iniciar o looping.

                        # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
                        # ⣿⣿⣿⣿⠉⣹⣿⠋⠉⠉⠁⠄⠄⠄⠄⣤⣤⣤⣤⣤⣍⣉⠉⣿⡏⠙⣿⣿⣿⣿ 
                        # ⣿⣿⡄⠁⠰⣿⣿⠄⠄⢤⠄⠄⠠⠄⠄⣿⣿⣿⠉⣿⣿⣿⠄⣿⣿⠦⠁⢠⣿⣿ 
                        # ⣿⣇⠁⠄⠰⣿⣿⠄⠄⢸⠄⠄⠄⠄⠄⣿⡏⠉⠄⠉⠙⣿⠄⣿⣿⠆⠄⠈⣹⣿ 
                        # ⣿⣿⠄⠄⢀⣿⣿⠄⠄⢸⠄⠄⠄⠄⠄⣿⣷⠚⠄⠑⣾⣿⠄⣿⣿⡀⠄⠐⣿⣿ 
                        # ⣿⣿⣄⠄⢸⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣤⣿⣿⣿⠄⣿⣿⠃⠄⣠⣿⣿        #vl
                        # ⣿⣿⡇⠄⠸⣿⣿⠄⣤⣤⣤⣤⣤⣤⣤⠛⠛⠛⠛⠛⠛⠛⠄⣿⣿⠆⠄⢺⣿⣿ 
                        # ⣿⣿⣧⡀⠁⢸⣿⠄⣿⣿⢛⠁⠩⠻⣿⠄⠄⠄⠄⡀⠄⠄⠄⣿⡇⠄⢀⣼⣿⣿ 
                        # ⣿⣿⣿⡅⠄⠈⢿⠄⢿⡍⠱⠄⠄⢹⣿⠄⠄⠄⠤⡁⠄⠄⠄⡟⠁⠄⢸⣿⣿⣿ 
                        # ⣿⠿⣿⣷⣤⠄⠄⣷⡈⢿⠁⢀⣈⣻⣿⠄⠄⠄⠄⠐⠄⢀⣾⠄⠄⣤⣾⣿⢿⣿ 
                        # ⣿⣧⡈⣉⣩⠤⠤⠌⠑⣄⠁⣾⣿⣿⣿⠄⠄⠉⠉⠄⣠⠊⠡⠤⠤⣍⣉⢁⣼⣿ 
                        # ⣿⡿⠷⢂⣽⠈⣉⡁⠄⠉⠄⠄⠙⢿⣿⠄⠄⠄⠄⠈⠉⠄⢈⣉⠄⣯⡐⠾⢿⣿ 
                        # ⣿⣿⣶⣦⣤⢀⡇⠋⠋⠛⠛⠟⠒⠒⡖⠒⡒⠒⠛⠛⠋⢩⠙⢹⡀⣤⣶⣶⣿⣿ 
                        # ⣿⣿⣿⣿⣿⣦⣭⣭⣙⣛⣓⣓⡒⠒⠷⠶⠓⢒⣒⣛⣛⣋⣭⣭⣴⣿⣿⣿⣿⣿ 
                        # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
