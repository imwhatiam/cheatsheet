from fabric import Connection

host_list = ('root@demo.seafile.top', 'root@download.seafile.top')

for host in host_list:

    c = Connection(host)

    result = c.run('uname -s', hide=True)
    print("Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}".format(result))

    result = c.put('lian-test', remote='/opt/')
    print("Uploaded {0.local} to {0.remote}".format(result))
