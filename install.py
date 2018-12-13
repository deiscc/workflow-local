import os

base_path = os.path.abspath(os.path.dirname(__name__))
script_path = os.path.join(base_path, "scripts")

def install_minikube():
    os.system(os.path.join(script_path, "install-microk8s.sh"))

def install_helm():
    os.system(os.path.join(script_path, "install-helm.sh"))


if __name__ == "__main__":
    install_minikube()
    install_helm()
