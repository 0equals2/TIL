from django import template

register = template.Library()

@register.filter
def hashtag_link(post):
    content = post.content
    hashtags = post.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(
            f'{hashtag.content}',
            f'<a href="/posts/hashtags/{hashtag.id}/">{hashtag.content}</a>'
        )

    return content