# Passos para resolução do case

## Tecnologias

Foi proposto o uso de três tecnologias:
1. CloudFormation
2. AWS
3. GitHub Actions

## Lista de tarefas

Foi proposto uma lista de tarefas a serem seguidas para melhor andamento do projeto.
- [x] Subir local manualmente.
- [ ] Subir em uma EC2 da AWS.
- [ ] Subir no CloudFormation da AWS.
- [ ] Fazer o CI/CD no Github Actions.
- [ ] Melhorias

## Subir local manualmente

Primeiramente foi proposto subir o projeto manualmente local sem automação.
A API fornecida já possuia um [Dockerfile](Dockerfile).
Então, para ver o funcionamento da API, subimos no Docker.
Os passos foram:
1. Ter o Docker instalado na máquina.
2. Buildar a imagem do Dockerfile. 
   ```bash
   docker build -t adahack .
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