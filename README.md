# Django-svn-revision

Creates a template tag called ``{% revision %}`` that returns the current svn version.

## Usage:
1.  Include the app in your ``settings.py`` file
2.  Add PROJECT_PATH to your ``settings.py`` file. ``os.path.abspath(os.path.dirname(__file__))`` works great.
3.  Load the templatetag: ``{% load revision %}``
4.  Include ``{% revision %}`` in your template file.

## Notes:
* Requires ``svnversion`` to be installed.
