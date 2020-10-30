pipelineJob('Ansible_DSL_Demo') {

    def repo = 'https://github.com/asha-keta/Ansible-Docker.git'
   
    triggers {
        scm('*/15 * * * *')
    }
    
    definition {
        cpsScm {
          scm {
            git(repo, 'master', { node -> node / 'extensions' << '' } )
            }
            scriptPath('linux_server_discovery/Pipeline/Jenkinsfile')
        }
    }
}
