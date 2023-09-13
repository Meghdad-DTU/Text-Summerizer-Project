# Text-Summerizer-Project with Deploymnet

### Workflows

- 1- Update config.yaml
- 2- Update params.yaml
- 3- Update entity
- 4- Update the configuration manager in src config
- 5- Update the conponents
- 6- Uupdate the pipeline
- 7- Update the main.py
- 8- Update the app.py

### How to run?
#### STEP 01- Clone the repository

```bash
https://github.com/Meghdad-DTU/Text-Summerizer-Project.git
```

#### STEP 02- Create a python virtual environmet

```bash
virtualenv venv --python=python3.8
```

```bash
Source venv/bin/activate
```

#### STEP 03- Install the requirements

```bash
pip install -r requirements.txt
```

#### STEP 04- Run the application

```bash
python app.py
```

#### STEP 05- Open up you local host and port




### AWS-CICD-Deployment-with-Github-Actions

#### STEP 01- Login to AWS console

#### STEP 02- Create IAM user for deployment

Withe specific access

- 1- EC2 access : It is virtual machine

- 2- ECR: Elastic Container registry to save your docker image in aws


Description: About the deployment

- 1- Build docker image of the source code

- 2- Push your docker image to ECR

- 3- Launch Your EC2 

- 4- Pull Your image from ECR in EC2

- 5- Lauch your docker image in EC2

Policy:

- 1- AmazonEC2ContainerRegistryFullAccess

- 2- AmazonEC2FullAccess

#### STEP 03- Create ECR repo to store/save docker image
```example >>  566373416292.dkr.ecr.ap-south-1.amazonaws.com/text-summarizer```

#### STEP 04- Create EC2 machine (Ubuntu)

#### STEP 05- Open EC2, connect and install docker in EC2 Machine
```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
#### STEP 06- Configure EC2 as self-hosted runner
```setting>actions>runner>new self hosted runner> choose os> then run command one by one```

#### STEP 07- Setup github secrets
```bash
AWS_ACCESS_KEY_ID= ....

AWS_SECRET_ACCESS_KEY= ....

AWS_REGION = .... 

AWS_ECR_LOGIN_URI = example >>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = text-summarizer
```
