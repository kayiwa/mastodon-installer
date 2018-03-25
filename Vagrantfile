# vim: set syntax=ruby:
# rubocop:disable Metrics/BlockLength
Vagrant.configure('2') do |config|
  config.vm.define 'bare' do |bare|
    bare.vm.box = 'ubuntu/xenial64'
    bare.vm.network 'private_network', type: 'dhcp'
    bare.vm.provision 'ansible' do |ansible|
      ansible.playbook = 'site.yml'
      ansible.extra_vars = {
        mastodon_db_password: 'CHANGEME'
      }
      ansible.verbose = true
    end

  end

end
