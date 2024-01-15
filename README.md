
# Python Docker Environment

A minimalistic **Discord Bot Application** which one can reply to the user depending on user message.


## Setup Instruction 

* Clone this repo to your local machine and go to your project directory.

```bash
cd my-project
```
* Before run you should be maintain **.env** file inside the src directory.
* Go to the [Discord Developer Portal](https://discord.com/developers/applications) and make a new application as you want.It will give you secret token to create **CLIENT** in your script. Copy and past it in **.env** file as named **DISCORD_TOKEN**

* Build docker image
```bash
docker-compose up --build
docker-compose up --build -d [Optional: If you want to build in detach mode ]
```

## Development Instruction 
Very first problem what you will get that no virtual environment and python intellisense work in your first setup so far and that's why we have to run this project in docker container.

* Extensions you need to install : **Docker**, **Dev Container**,  
* Open dialog box of remote machine clicking bottom left **Remot Window** button and select your container what you build previously.It will open **new window** of **VSCODE**.
* For the first time you may don't get intellisense support of python.If you don't get any support please install again **Python Extension** again . For this time install this extension inside your container. After that you don't need to install it again and again.
