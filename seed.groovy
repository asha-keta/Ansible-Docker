pipelineJob('Ansible_DSL_Demo')     
    
    parameters {
        stringParam('Playbook_Name', 'linux_server_discovery', 'Playbook to trigger')
        stringParam('Playbook_Name1', 'linux_server_discovery1', 'Playbook to trigger1')
    }
    definition {
        cps {
         script(readFileFromWorkspace('linux_server_discovery/Pipeline/Jenkinsfile'))
        }
    }


pipelineJob('Ansible_DSL_Demo1') {

    def repo = 'https://github.com/asha-keta/Ansible-Docker.git'
    parameters {
        stringParam('Playbook_Name', 'linux_server_discovery', 'Playbook to trigger')
        stringParam('Playbook_Name1', 'linux_server_discovery1', 'Playbook to trigger1')
    }
     
    definition {
        cpsScm {
          scm {
            git(repo, 'master', { node -> node / 'extensions' << '' } )
              configure { git ->
                git / 'extensions' / 'hudson.plugins.git.extensions.impl.SparseCheckoutPaths' / 'sparseCheckoutPaths' {
                    ['linux_server_discovery'].each { mypath ->
                        'hudson.plugins.git.extensions.impl.SparseCheckoutPath' {
                            path("${mypath}")
                }
            }
        }
	}
            }
            scriptPath('linux_server_discovery/Pipeline/Jenkinsfile')
        }
    }
}

job("free-style-ansible") {
    description "Trigger test Ansible Playbook"
    parameters {
        stringParam('Playbook_Name', 'linux_server_discovery', 'Playbook to trigger')
        stringParam('Playbook_Name1', 'linux_server_discovery1', 'Playbook to trigger1')
    }
    
    steps {
        shell "docker exec trusting_lovelace sh -c 'ansible-playbook /ansible_playbooks/workspace/Sonar_Scanner/linux_server_discovery/Playbooks/linux_discovery.yml'"
    }
}
