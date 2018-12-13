sudo snap install microk8s --classic
sudo microk8s.enable dns storage registry
sudo snap alias microk8s.docker docker
sudo snap alias microk8s.kubectl kubectl

