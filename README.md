# Download HashiCorp product

A simple python script to download the latest version of an HashiCorp product.

# Requirements

Python2.7 and the prerequisite packages described in `requirements.txt` / `Pipfile`.

# Usage

Script is not interactive.

Product and version can be passed as 1st and 2nd argument respectively. If the version argument is ommited the latest version will be installed.

The OS and processor architecture are set as variables inside the script.

Running the script would usually require `sudo` to be able to install the binary. For example:

`sudo python download-hc-product.py terraform`

`sudo python download-hc-product.py terraform 0.11.14`
