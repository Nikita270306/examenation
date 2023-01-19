import json


def get_posts_all():
    """
    возвращает посты
    """
    with open('./data/posts.json', 'r', encoding='utf-8') as all_file:
        return json.load(all_file)


def get_posts_by_user(user_name):
    """
    возвращает посты определенного пользователя
    """
    result = []
    for i in get_posts_all():
        if i["poster_name"] == user_name:
            result.append(i)
    return result


def get_comments_by_post_id(post_id):
    """
    возвращает комментарии определенного поста
    """
    com_result = []
    with open('./data/comments.json', 'r', encoding='utf-8') as comments:
        comments = json.load(comments)
        for i in comments:
            if i["post_id"] == post_id:
                com_result.append(i)
        return com_result


def search_for_posts(query):
    """
    возвращает список постов по ключевому слову
    """
    result = []
    for i in get_posts_all():
        if query.lower() in i["content"].lower():
            result.append(i)
    return result


def get_post_by_pk(pk):
    """
    возвращает один пост по его идентификатору
    """
    for i in get_posts_all():
        if i["pk"] == pk:
            return i
