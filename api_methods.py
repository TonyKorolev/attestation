import logging
import requests
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def get_user_token_and_id():
    logging.info('Get user token and id')
    try:
        r = requests.post(testdata['getaway']['login'],
                          data={'username': testdata['username'], 'password': testdata['password']})
        token = r.json()['token']
        user_id = r.json()['id']
    except Exception as e:
        logging.exception(e)
        token = None
        user_id = None
    return token, user_id


def get_my_posts():
    logging.info('Get list with my posts')
    g = requests.get(testdata['api']['posts'],
                     headers={'X-Auth-Token': get_user_token_and_id()[0]})
    if g:
        list_content = [i['content'] for i in g.json()['data']]
        return list_content
    else:
        logging.error('List with my posts is not received')


def get_not_my_posts():
    logging.info('Get list with not my posts')
    g = requests.get(testdata['api']['posts'], headers={'X-Auth-Token': get_user_token_and_id()[0]},
                     params={'owner': 'notMe'})
    if g:
        list_content = [i['content'] for i in g.json()['data']]
        return list_content
    else:
        logging.error('List with not my posts is not received')


def create_post():
    logging.info('Create new post')
    p = requests.post(testdata['getaway']['posts'], headers={'X-Auth-Token': get_user_token_and_id()[0]},
                      data={'title': testdata['create_post']['title'],
                            'description': testdata['create_post']['description'],
                            'content': testdata['create_post']['content']})
    if p:
        return p.json()
    else:
        logging.error('Post is not created')


def find_post():
    logging.info('Find created post')
    d = requests.get(testdata['api']['posts'], headers={'X-Auth-Token': get_user_token_and_id()[0]})
    if d:
        list_description = [i['description'] for i in d.json()['data']]
        return list_description
    else:
        logging.error('Post is not found')


# def get_user_id():
#     logging.info('Get user id')
#     try:
#         userdata = requests.post(testdata['getaway']['login'],
#                                  data={'username': testdata['username'], 'password': testdata['password']})
#         user_id = userdata.json()['id']
#     except:
#         logging.exception('User data is not received')
#         user_id = None
#     return user_id


def get_username():
    logging.info('Get username')
    try:
        data = requests.get(testdata['api']['users'] + str(get_user_token_and_id()[1]),
                            headers={'X-Auth-Token': get_user_token_and_id()[0]})
        username = data.json()['username']
    except Exception as e:
        logging.exception(e)
        username = None
    return username
