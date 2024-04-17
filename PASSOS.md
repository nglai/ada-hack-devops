# Passos para resolução do case

## Tecnologias

Foi proposto o uso de três tecnologias:
1. CloudFormation
2. AWS
3. GitHub Actions

## Lista de tarefas

Foi proposto uma lista de tarefas a serem seguidas para melhor andamento do projeto.
- [X] Subir local manualmente no Docker.
- [X] Testar os endpoints.
- [X] Entender como a aplicação funciona
- [X] Subir em uma EC2 da AWS com Docker.
- [X] Subir no CloudFormation da AWS.
- [X] Fazer o CI/CD no Github Actions.
- [X] Melhorias

## Subir local manualmente

Primeiramente foi proposto subir o projeto manualmente local sem automação.
A API fornecida já possuia um [Dockerfile](Dockerfile).
Então, para ver o funcionamento da API, subimos no Docker.
Os passos foram:
1. Ter o Docker instalado na máquina.
2. Buildar a imagem do Dockerfile. 
   ```bash
   docker build -t nglai/adahack .
   ```
* Observação: o arquivo Dockerfile deve estar na mesma pasta do caminho do terminal. Se não estiver, deve substituir o . (ponto final) pelo caminho do arquivo Dockerfile.
3. Verificar a Image Id da imagem.
   ```bash
   docker images
   ```
4. Rodar a imagem.
   ```bash
   docker run -p 8000:8000 -d ImageID
   ```
Dessa forma, a porta 8000 local expõe a porta 8000 do docker.
A API estará rodando em `http://127.0.0.1:8000`.
Para mais informações, verificar a documentação da [API](API.md).
5. Subir a imagem para o Docker Hub.
   ```bash
   docker push nglai/adahack
   ```
6. Outra forma de testar foi criando um [docker-compose](docker-compose.yaml) pegando a imagem do Docker Hub do passo 5 e subir.
   ```bash
   docker compose up
   ```

## Subir em uma EC2 da AWS

Após subir local, a segunda parte foi subir em uma EC2 da AWS, instalar o Docker na EC2 e rodar a aplicação.
Os passos foram:
1. Logar na conta da AWS.
2. Ir no servico EC2:Security Groups e criar um novo grupo de segurança.
Nome do grupo de segurança: sg_adahack
Descrição: Security group for Ada Hack
Regras de entrada:
   - 80 - HTTP
   - 8000
3. Ir no serviço EC2.
4. Criar uma instância nova.
Nome: adahack
AMI: Amazon Linux (Amazon Linux 2023 AMI)
Tipo de instância: t2.micro.
Par de chaves: Prosseguir sem um par de chaves (não recomendado).
Configurações de rede: 
   - Usar grupo de segurança criado acima.
Em detalhes avançados:
   - User data:
   ```bash
   #!/bin/bash
   sudo yum update -y
   sudo yum install docker -y
   sudo yum install git -y
   sudo service docker start
   sudo systemctl enable docker
   sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   sudo git clone https://github.com/nglai/ada-hack-devops /path/to/your/folder
   cd /path/to/your/folder
   sudo docker-compose up -d
   ```
5. Acessar a api em `IPPublicoDaInstancia:8000`.
Para mais informações, verificar a documentação da [API](API.md).

## Github Actions

A terceira parte foi fazer uma pipeline no GitHub Actions com as seguintes funções:
- Fazer os testes da API
- Mandar a imagem atualizada para o Docker hub
- Realizar o deploy do cloud formation na AWS

* Foi necessário corrigir os testes da aplicação para todos os testes passarem.
* As secrets foram colocadas localmente no repositório. Isso garante segurança.