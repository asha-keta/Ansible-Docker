pipelineJob('Ansible_DSL_Demo') {

    def repo = 'https://github.com/asha-keta/Ansible-Docker.git'
   
    triggers {
        scm('*/15 * * * *')
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
