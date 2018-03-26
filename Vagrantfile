# vim: set syntax=ruby:
Vagrant.configure('2') do |config|
  config.vm.define 'mastodon' do |mastodon|
    mastodon.vm.box = 'ubuntu/xenial64'
    mastodon.vm.network 'private_network', type: 'dhcp'
    mastodon.vm.provision 'ansible' do |ansible|
      ansible.playbook = 'site.yml'
      ansible.extra_vars = {
        mastodon_db_password: 'CHANGEME'
      }
      ansible.verbose = 'vvv'
    end

  end

end
