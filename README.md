Tempest Integration of storage tests - cinder , glance , nova, swift and ceph

This directory contains Tempest tests to cover the StorageTest project.

Setup steps:

Prerequisites:

Installed tempest virtual environment.
Cloned tempest repository.
Storage plugin setup:

The tempeset-storage-plugin repository should be cloned near to the main tempest directory.
$ git clone https://github.com/bkopilov/tempest-storage-plugin.git

Activate the tempest virtual env.
Browse to the storage_tempest_plugin directory and install the storage plugin:
$ pip install --upgrade -e .

Test the installed plugin:
$ pip list |grep -i storage

Browse to the main tempest directory and check the newly installed storage plugin:
$ testr list-tests |grep -i storage