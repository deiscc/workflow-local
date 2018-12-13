yum install -y epel-release
yum install -y python36 git
python36 -m venv /usr/local/kubespray-venv
source /usr/local/kubespray-venv/bin/activate
git clone -b master --depth 1 https://github.com/kubernetes-sigs/kubespray /usr/local/kubespray
cd /usr/local/kubespray && pip install -r requirements.txt
sed -i 's/helm_enabled: false/helm_enabled: true/g' inventory/local/group_vars/k8s-cluster/addons.yml 
ansible-playbook -i inventory/local/hosts.ini --become --become-user=root cluster.yml
