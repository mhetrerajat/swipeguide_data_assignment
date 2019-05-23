import json
import click


class StorageManager(object):
    """This class interacts with storage. It takes path of JSON file as input and reads the 
    data in it
    """

    def __init__(self, path, **kwargs):
        """
        Arguments:
            path {str} -- Path of JSON file
        """
        self.path = path

    def fetch(self):
        """Reads the JSON file and loads it as list of dict
        
        Returns:
            list -- Data in the form of list of dicts
        """

        click.echo('Reading: %s' % click.format_filename(self.path))

        try:
            f = open(self.path, 'r')
            data = json.loads(f.read())
            return data
        except FileNotFoundError as e:
            click.secho(str(e), fg='red')
            raise
