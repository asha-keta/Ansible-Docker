#!/bin/bash

sed --in-place '/build_number/d' /root/migrationpod/configuration/linux_server_discovery.yml
sudo echo "build_number: $1" >> /root/migrationpod/configuration/linux_server_discovery.yml

cd "/var/lib/jenkins/workspace/linux_server_discovery/linux_server_discovery/Playbooks/"
sudo ansible-playbook -i "/root/migrationpod/configuration/inventory" --vault-password-file "/root/migrationpod/configuration/vault_pass" linux_discovery.yml 
