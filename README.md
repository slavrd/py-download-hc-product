# Download HashiCorp product

A simple python script to download the latest version of an HashiCorp product.

# Requirements

Python2.7 and the prerequisite packages described in `requirements.txt` / `Pipfile`.

# Usage

Script is not interactive. Except for the product the other build parameters need to be defined by setting the appropriate variable in the beginning of the script.

Running the script would usually require `sudo` to be able to install the binary. For example:

`sudo python download-hc-product.py terraform`
