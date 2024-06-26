# MLOps zoomcamp
This is a repo for the MlOps zoomcamp course.

Link of the course:\
https://github.com/DataTalksClub/mlops-zoomcamp

mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root ./artifacts_local


## Environment set up
I'm gonna use a VM in AWS following the next steps:

1. Create an account in AWS.
2. Create en EC2 instance, that is, a virtual machine. I will create it with Ubuntu as OS.
3. When I create the VM, as I follow the instructions, I'm gonna use a "key pair" to securely connect to my VM. As I don't have yet any key pair I'm gonna create a new one.
4. While creating the key pair select:
   * Key pair type: RSA
   * Private key file format: .pem
5. After clicking on "Create key pair" button the .pem file will be downloaded.
6. Place the key (.pem file) in .ssh folder (ex: /Users/constanzalalala/.ssh/key1.pem.
7. Open a new terminal and write: cd .ssh/
8. To connect to VM write:  ssh -i ~/Users/constanzalalala/.ssh/key1.pem ubuntu@3.23.96.130 --> the IP Address will change every time I start again the VM in AWS
I can get the IP Address going to my instance in AWS and clicking under instance ID > copy the number under Public IPv4 address

I can edit config file to connect more easily to the VM:
* Close connection with "logout"
* Open a new terminal
* Write: nano .ssh/config
* Write:
    Host mlops-course
        HostName 3.23.96.130  --> Every time I start the VM I'm gonna have to change that IP                       
        User ubuntu
        IdentityFile /Users/constanzalalala/.ssh/key1.pem
        StrictHostKeyChecking no
* Save changes
* Connect to VM writing: mlops-course (or the name I decide)

### Install anaconda in VM
After connecting to virtual machine write in the terminal to download Anaconda:\
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh (go to the website to copy the corresponding link)\
Then install:\
bash Anaconda3-2022.05-Linux-x86_64.sh

Update existing packages:\
sudo apt update

**Install Docker and Docker-compose**
* Open a terminal and write:\
  ssh mlops-course (if I'm aleady connected to the VM this line is not necessary)\
  sudo apt install docker.io\
  If previous line doesn't work first run this:\
  sudo apt update\
  Create a folder\
  mkdir soft\
  cd soft\
  Search in explorer for "docker-compose github" and then click on "Releases (latest)"\
  wget https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-linux-x86_64 -O docker-compose # download and give the name docker-compose\
  Make docker-compose executable:\
  chmod +x docker-compose
  
  In order to access to soft folder from any location we do:\
  cd .. # First out from soft folder\
  nano .bashrc\
  At the end of the file that will be opent write:\
  export PATH="${HOME}/soft:${PATH}"    # with thise, everything that is inside soft folder will be in my path and I can execute it from anywhere\
  Run the previous modified file:\
  source .bashrc\
  which docker-compose # I will see location
  
* Trying to run docker:
  docker run hello-world\
  If it doesn't work we have to run it with sudo:\
  sudo docker run hello-world\

  * If I don't want to use "sudo" everytime I run docker I can add my user to dockergroup
  sudo groupadd docker\
  If it already exists we do:\
  sudo usermod -aG docker $USER\ # Then we have to logout and log back to the VM\
  If I get a message like "permission denied while trying to connect to the Docker daemon socket...." I have to do the next OUTSIDE the VM, in my own machine:\
  chmod 400 .ssh/keyname.pem\
  And then restart VM

**NOTE**: The next steps related with Docker were in the course notes but were not mentioned in the video, I based on the video to write the previous steps and I'm not sure in what cases I have to do the next steps, It seems to be a way to do the same but just copying and pasting that code, anyway I'll let them  here in case:
  
* Add Docker's official GPG key:\
sudo apt-get update\
sudo apt-get install ca-certificates curl\
sudo install -m 0755 -d /etc/apt/keyrings\
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc\
sudo chmod a+r /etc/apt/keyrings/docker.asc

* Add the repository to Apt sources:
echo \\
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \\
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \\
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null\
sudo apt-get update

* Install the Docker packages\
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

* To run docker without sudo:\
sudo groupadd docker\
sudo usermod -aG docker $USER

* Run Docker\
docker run hello-world

**Note:** If you get "It is required that your private key files are NOT accessible by others. This private key will be ignored." error, you should change permits on the downloaded file to protect your private key:
chmod 400 name-of-your-private-key-file.pem

### Connecting to VM from VS Code
1. First start the VM, I can use the VSCode integrated terminal instead of the system terminal.
2. Install the Remote-SSH extension.
3. Click on the lower left corner (will be colored green), then in the upper bar of VSCode a list will be displayed.
4. Choose "Connect to Host" > mlops-course (or the name of the connection).
5. I can open the VM home with "open folder" and see all the folders and files that are in my VM.

#### Using Jupyter notebook in VSCode
I have to install the extension for jupyter notebook but must be installed in the VM not in my system, I don't remember exactly but I searched for the extension 
in the VSCode Extensions tab being connected to the virtual machine (maybe install through SSH, something like that).


   
