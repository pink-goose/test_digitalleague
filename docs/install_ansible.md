# Install ansible

if on Windows: run WSL Ubuntu and do
```
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
# sudo apt-get install ansible
sudo apt install python3-pip
sudo pip3 install pywinrm
sudo pip3 install pyvmomi
sudo pip3 install ansible
sudo pip3 install ansible[azure]
```

on Ubuntu:
```
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
python3 -m pip install --user ansible
```

run /mnt/c/Users/Mikhail/MyProjects/ansible/playbook.yml on localhost:
```
cd /mnt/c/Users/Mikhail/MyProjects/ansible
ansible-playbook playbook.yml -i localhost
```