import os

base_path = os.path.abspath(os.path.dirname(__name__))
script_path = os.path.join(base_path, "scripts")

def install_k8s():
    os.system(os.path.join(script_path, "install-k8s.sh"))

def install_charts():
    os.system(os.path.join(script_path, "install-charts.sh"))


if __name__ == "__main__":
    install_k8s()
    install_helm()
    install_charts()
