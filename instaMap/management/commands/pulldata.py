from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import fromstr
from instaMap.models import Post
import requests


class Command(BaseCommand):
    if __name__ == '__main__':
        help = 'Gathers the assigned users recent instagram data.' \
               'Checks against old data to avoid duplicate data.'\
               'Accepts a string argument for the file path to a ' \
               'txt file with the first line being the access token.'

    def add_arguments(self, parser):
        parser.add_argument('token_path', type=str)

    def handle(self, *args, **options):
        access_token = open(options['token_path'], 'r').readline()
        request_url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=%s' % access_token
        user_data = requests.get(request_url).json()
        if 'data' in user_data:
            data = user_data['data']
            data_list = []
            id_list = Post.objects.all().values_list('id_code', flat=True)
            for data in data:
                if data['id'] in id_list:
                    self.stdout.write('Duplicate item found: ' + data.get('location', {}).get('name'))
                else:
                    if data['location'] is not None:
                        post_id = data['id']
                        post_link = data['link']
                        image = data.get('images', {}).get('standard_resolution', {}).get('url')
                        location_name = data.get('location', {}).get('name')
                        post_tags = data['tags']
                        post_location = data['location']
                        post_content = data.get('caption', {}).get('text')
                        data_list.append({'id': post_id,
                                          'image': image,
                                          'loc_name': location_name,
                                          'tags': post_tags,
                                          'location': post_location,
                                          'link': post_link,
                                          'content': post_content})
            for entry in data_list:
                Post(content=entry.get('content'),
                     id_code=entry.get('id'),
                     tags=entry.get('tags'),
                     link=entry.get('link'),
                     image_url=entry.get('image'),
                     loc_name=entry.get('loc_name'),
                     loc_point=fromstr('POINT(%s %s)' % (entry.get('location', {}).get('longitude'),
                                                         entry.get('location', {}).get('latitude')), srid=4326))\
                    .save()
                self.stdout.write('Location added: ' + entry.get('loc_name'))
        self.stdout.write('Sequence completed!')

