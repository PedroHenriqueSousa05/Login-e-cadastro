from time import sleep


class opcoes:
    def pergunta(self):
        while True:
            print('''
            [ 1 ] LOGIN
            [ 2 ] CADASTRAR
            [ 3 ] SAIR DO PROGRAMA
            ''')
            try:
                opcao = int(input('Sua opcao:'))
                if opcao == 1:
                    log1 = loginback()
                    log1.login()
                    break
                elif opcao == 2:
                    cad1 = cadastro()
                    cad1.cadast()
                    
                elif opcao == 3:
                    print('Saindo...')
                    sleep(2)
                    break
                else:
                    print('ERRO: Por favor ensira uma opcao valida!')
            except (ValueError):
                print('Erro: Por favor ensira uma opcao valida!')


class cadastro:
    def cadast(self):
        print('-'*30)
        print('CADASTRO')
        print('-'*30)
        log = open('User.txt', 'a')
        senh = open('senha.txt', 'a')
        log.close()
        senh.close
        while True:
            try:
                login = str(input('Username:')).strip()
                senha = input('Password:').strip()
                repetirsenha = input('Repeat the password:').strip()
                

                if repetirsenha != senha:
                    print('As senhas nao coincidem!')
                
                else:
                    log = open('User.txt', 'r')
                    senh = open('senha.txt', 'r')
                    usuarios = log.readlines()
                    senhas = senh.readlines()
                    
                    logado = False
                    
                    usuarios = list(map(lambda x: x.replace('\n', ''), usuarios))
                    senhas = list(map(lambda x: x.replace('\n', ''), senhas))
                    
                    for i in range(len(usuarios)):
                        if login == usuarios[i]:
                            print('Nome de usuario indisponivel!')
                        else:
                            logado = True
            except:
                print('Erro')
            
            if logado:            
                print('CADASTRADO COM SUCESSO')
                log = open('User.txt', 'a')
                log.write(f'{login}\n')
                log.close()
                senh = open('senha.txt', 'a')
                senh.write(f'{senha}\n')
                senh.close()            
                break


class loginback:
    def login(self):
        print('-'*30)
        print('Login')
        print('-'*30)

        while True:   
            login1 = input('Username:')
            senha = input('Password:')
            with open('User.txt', 'r') as arquivosUsuario:
                usuarios = arquivosUsuario.readlines()
            with open('senha.txt', 'r') as arquivosUsuario:
                senhas = arquivosUsuario.readlines()

            usuarios = list(map(lambda x: x.replace('\n', ''), usuarios))
            senhas = list(map(lambda x: x.replace('\n', ''), senhas))
            
            logado =  False
        
            for i in range(len(usuarios)):
                if login1 == usuarios[i] and senha == senhas[i]:
                    print('LOGADO COM SUCESSO!!')
                    logado = True
                    
            if not logado:
                print('USUARIO OU SENHA INCORRETO!')
            
            else:
                break


perg = opcoes()
perg.pergunta()


