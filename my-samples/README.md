Clean environment:
```

mkdir acitoolkit-clean
cd acitoolkit-clean
python3 -m venv env
source env/bin/activate

# DO NOT USE that, because has the problem:
# >>> import acitoolkit as ACI
# >>> ACI._interface_from_dn("")
# Traceback (most recent call last):
#  File "<console>", line 1, in <module>
# AttributeError: module 'acitoolkit' has no attribute '_interface_from_dn'
wget https://github.com/datacenter/acitoolkit/archive/refs/tags/v0.4.zip
unzip v0.4.zip
cd acitoolkit-0.4

# Option 1
wget https://github.com/datacenter/acitoolkit/archive/master.zip
unzip master.zip
cd acitoolkit-master
sudo python setup.py install

# Option 2
git clone https://github.com/datacenter/acitoolkit.git
cd acitoolkit
sudo python setup.py install
```