import requests
import json
from packaging.version import Version, parse
import zipfile
import wget
import os
import sys

# Define the TF realese to download
product = sys.argv[1]
print('installing {0}'.format(product))
install_path = '/usr/local/bin/'
osys = 'linux'                                                                                                                                                                                                                   
arch = 'amd64'

# Get the versions data from HC release service
request = requests.get('https://releases.hashicorp.com/{0}/index.json'.format(product))

# Find the latest stable relese
tf_release_data = json.loads(request.content)
tf_versions = tf_release_data["versions"].keys()
tf_latest_ver = Version("0.0.0")

for ver in tf_versions :
    parsed_ver = parse(ver)
    if not parsed_ver.is_prerelease :
        if parsed_ver > tf_latest_ver :
            tf_latest_ver = parsed_ver

tf_latest_ver_builds = tf_release_data["versions"][tf_latest_ver.public]["builds"]

# Get the URL for the required binnary type
tf_latest_ver_url = ''
tf_latest_ver_filename = ''
for build in tf_latest_ver_builds :
    if build["os"] == osys and build["arch"] == arch :
        tf_latest_ver_url = build["url"]
        tf_latest_ver_filename = build["filename"]
        break

# download the terraform archive
dwnld_path = "/tmp/{0}".format(tf_latest_ver_filename)
wget.download(tf_latest_ver_url,dwnld_path)

# extract archive
zip_file = zipfile.ZipFile(dwnld_path)
zip_file.extractall(install_path)

# set file permissions
binpath = os.path.join(install_path, product)
fd = os.open(binpath, os.O_RDWR)
os.fchmod(fd, 755)
os.close(fd)
