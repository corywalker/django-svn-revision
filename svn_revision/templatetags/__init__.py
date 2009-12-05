def get_revision():
    from subprocess import Popen, PIPE
    import re, os

    try:
        stdio = Popen(['svnversion', os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../")], stdout=PIPE, stderr=PIPE)
        comm = stdio.communicate()
        stdout = comm[0].strip()
        matched = re.match(':?(\d*).*[MS]?$', stdout)
        stderr = comm[1].strip()
        stdio.stdout.close()
        stdio.stderr.close()

        if stderr:
            return stderr
        if matched:
            return matched.group(1) or ' '
    except:
        return 'Versioning Unavailable'

REVISION = get_revision()
