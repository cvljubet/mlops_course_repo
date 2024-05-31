# MLOps zoomcamp
This is a repo for the MlOps zoomcamp course.

Link of the course:\
https://github.com/DataTalksClub/mlops-zoomcamp

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

**Install anaconda in VM**\
After connecting to virtual machine write in the terminal:\
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh (go to the website to copy the corresponding link)\
bash Anaconda3-2022.05-Linux-x86_64.sh

Update existing packages:\
sudo apt update

**Install Docker and Docker-compose**\
* Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

* Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

* Install the Docker packages
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

* To run docker without sudo:
sudo groupadd docker
sudo usermod -aG docker $USER

* Run Docker
docker run hello-world

**Note:** If you get It is required that your private key files are NOT accessible by others. This private key will be ignored. error, you should change permits on the downloaded file to protect your private key:
chmod 400 name-of-your-private-key-file.pem





**Connecting to VM from VS Code**
