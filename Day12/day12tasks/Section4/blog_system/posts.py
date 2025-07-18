from users import get_user
def get_post(): return f'Post by {get_user()['name']}'
