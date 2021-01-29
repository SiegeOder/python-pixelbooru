from django.contrib.auth.models import User
from comments.models import Comment
from posts.models import Post
from profiles.models import Profile
from tags.models import Tag

from random import choice, randint
from string import ascii_letters

USERNAMES = ('ЪуЪ', 'Taught', 'MeJk', 'Hikiri', 'leonsksk', 'Sechga', 'Ṧℰℵẳℜ7', 'KOTYANYA', 'Сабрина', 'KillerSenpai',
             'Kalerija', 'FearlessP', 'Einstein', 'Айка', 'Mabel Duck', 'kiwami', 'アニメワンラブ', 'Max Wolf',
             'ReZeroOfficial', 'ConqueroR', 'Blue', 'Ведьмочка', '_Kresh_', 'イタチうちは', 'ArisTocraT', 'AnyGrief',
             '•ahegao•', 'Trap', 'brusee', 'anm', 'Super_Tortik121', 'Slen’s Ellebru', 'Sakagari', 'ANIMESHNIK',
             'YING YUE ㊚', 'Makino', 'sandoffer', 'Tetsu_Kun', 'Суицидальный', 'Queen', 'Weersel', 'Shingetsu',
             'ILIa3174', 'Knoxann', 'Makiavelly', 'BloodSigh†', 'loxmatiy_losos', 'Hirxmi', 'ZiKAY:3', 'Zaur_Sizo',
             'SCReech', 'x_O', 'Nillie', 'General Blue', 'Clark_Gonzales', 'Anteyko', 'Subject', 'Akionai', 'Reivu',
             '.N.E.E.T.', 'Dark', 'Bastbis', 'Demonenok', 'Ellebru', 'Чаёчеканимешник', 'TheMeror', 'KimiKota',
             'Stranger568', 'miakemri', 'Денис Иманити', 'MaxWell', 'Nuwhekq', 'wisgoth', 'lostp1ayer', 'ELGD',
             'tahhattoo', '-Morrie-', 'DanialPhanToM', 'ToniHyon', 'Loki13666', 'Rapidous', 'clan life 2.0', 'Drobash',
             'USB4.0', 'Atlantean', 'anish.', 'Вокалоид Мейко', '強力INTERNET', 'ren elric', 'MiguelitoS2', 'Fishel',
             'KILYD', 'Zyris', 'ẮℝℂℍÌ', 'SheepSinner', 'MEGAMIA', 'Boolikot', 'Greatve', '_Тихая_Мишель_', 'Breinat',
             'HuLu', 'Delight', 'Silestiya', 'Naganen', 'Murasaki-dono', 'OConnell', 'StoryDark', 'usubaru', 'Hikori',
             'G1TLER', 'Full_bek_165', 'Димедролыч', 'Fumoffu', 'Aichii', 'God_Ganster', 'RUStalker33',
             'Path to Pleasure', 'Alucard', 'Hiroshima', 'Voriol', 'Chroma', 'Elarmy', 'allrightttt', 'Korii',
             'Feriss.Argyle', 'Rmon', 'kun', 'Night Kawaii', 'Äℍúℳ€ŴℍúĶ', 'YRek', 'rayderxxx', 'bezzer',
             'Кошка Мишель', 'qweerty351', 'Dragonk', 'Meurse1L', 'LifeIsNice', 'Mavili', 'AlexKun', 'senpachi',
             'ArtoriaChan', 'Spuffyffin', 'MichiKio', 'Blue ConqueroR', 'Sukoru', 'Stivirys', 'MosTape', 'shouto',
             'VktrSansara', 'Nofference強力', 'AsuNa)', '๖ۣۣۜYegativ', 'Дыбенко!!!', 'Voricai')
PICTURE_COUNT = 54
COMMENT_COUNT = 200
TAGS_COUNT = 40
TAG_TYPES = ('general', 'artist', 'copyright', 'character')
TAG_RELATIONS_COUNT = 500
USERS = 66  # max: 150


def run():
    print('seeding users table', end='...')
    seed_users_table()
    print('complete')
    print('seeding posts table', end='...')
    seed_posts_table()
    print('complete')
    print('seeding comments table', end='...')
    seed_comments_table()
    print('complete')
    print('seeding tags table', end='...')
    seed_tags_table()
    print('complete')
    print('seeding relations table', end='...')
    seed_relations_table()
    print('complete')


# Seed functions
def seed_users_table():
    Profile.objects.create(
        user=User.objects.get(id=1),
        image=f'images/users/SODA.png',
        note='ore wa admin desuyo',
    )
    for user_id in range(2, USERS + 2):
        username = USERNAMES[user_id - 2]
        user = User.objects.create_user(
            username=username,
            password=username
        )
        Profile.objects.create(
            user=user,
            image=f'images/users/{user_id}.png',
            note=rand_str(128),
        )


def seed_posts_table():
    author = Profile.objects.get(id=1)
    for i in range(1, PICTURE_COUNT + 1):
        Post.objects.create(
            image=f'images/posts/{i}.png',
            author=author
        )


def seed_comments_table():
    posts = Post.objects.all()
    users = Profile.objects.all()
    for i in range(COMMENT_COUNT):
        Comment.objects.create(
            text=rand_str(randint(11, 256)),
            post=choice(posts),
            author=choice(users)
        )


def seed_tags_table():
    for number in range(TAGS_COUNT):
        Tag.objects.create(
            name=rand_str(randint(1, 2) * 10).replace(' ', '_'),
            type=choice(TAG_TYPES),
            definition=rand_str(randint(5, 25) * 10)
        )


def seed_relations_table():
    posts = Post.objects.all()
    tags = Tag.objects.all()
    for _ in range(TAG_RELATIONS_COUNT):
        choice(posts).tags.add(choice(tags))


# Utils
def rand_str(max_length=200):
    words = max_length // 10
    string = ''
    for word in range(words):
        string += ''.join(choice(ascii_letters) for i in range(randint(1, 10))) + ' '
    return string[:-1]
