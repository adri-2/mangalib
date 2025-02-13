from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from allapps.mangalib.models import Category, Author, Manga  # Assurez-vous que c'est le bon chemin d'import

import random

UserModel = get_user_model()

CATEGORIES = [
    {
        'name': 'Shonen',
        'description': 'Mangas pour jeunes garçons',
        'mangas': [
            {'title': 'One Piece', 'volume': 1, 'author': 'Eiichiro Oda', 'date': '1997-07-22', 'cover_image': 'mangas/one_piece.jpg'},
            {'title': 'Naruto', 'volume': 1, 'author': 'Masashi Kishimoto', 'date': '1999-09-21', 'cover_image': 'mangas/naruto.jpg'},
            {'title': 'Dragon Ball', 'volume': 1, 'author': 'Akira Toriyama', 'date': '1984-11-20', 'cover_image': 'mangas/dragon_ball.jpg'},
            {'title': 'Bleach', 'volume': 1, 'author': 'Tite Kubo', 'date': '2001-08-07', 'cover_image': 'mangas/bleach.jpg'},
            {'title': 'Hunter x Hunter', 'volume': 1, 'author': 'Yoshihiro Togashi', 'date': '1998-03-03', 'cover_image': 'mangas/hxh.jpg'}
        ]
    },
    {
        'name': 'Seinen',
        'description': 'Mangas pour jeunes adultes',
        'mangas': [
            {'title': 'Berserk', 'volume': 1, 'author': 'Kentaro Miura', 'date': '1989-08-25', 'cover_image': 'mangas/berserk.jpg'},
            {'title': 'Vagabond', 'volume': 1, 'author': 'Takehiko Inoue', 'date': '1998-09-16', 'cover_image': 'mangas/vagabond.jpg'},
            {'title': 'Tokyo Ghoul', 'volume': 1, 'author': 'Sui Ishida', 'date': '2011-09-08', 'cover_image': 'mangas/tokyo_ghoul.jpg'},
            {'title': 'Monster', 'volume': 1, 'author': 'Naoki Urasawa', 'date': '1994-12-05', 'cover_image': 'mangas/monster.jpg'},
            {'title': 'Vinland Saga', 'volume': 1, 'author': 'Makoto Yukimura', 'date': '2005-07-15', 'cover_image': 'mangas/vinland_saga.jpg'}
        ]
    },
    {
        'name': 'Shojo',
        'description': 'Mangas destinés aux jeunes filles',
        'mangas': [
            {'title': 'Fruits Basket', 'volume': 1, 'author': 'Natsuki Takaya', 'date': '1998-07-18', 'cover_image': 'mangas/fruits_basket.jpg'},
            {'title': 'Sailor Moon', 'volume': 1, 'author': 'Naoko Takeuchi', 'date': '1992-07-06', 'cover_image': 'mangas/sailor_moon.jpg'},
            {'title': 'Cardcaptor Sakura', 'volume': 1, 'author': 'CLAMP', 'date': '1996-05-25', 'cover_image': 'mangas/ccs.jpg'},
            {'title': 'Ouran High School Host Club', 'volume': 1, 'author': 'Bisco Hatori', 'date': '2002-08-05', 'cover_image': 'mangas/ouran.jpg'},
            {'title': 'Nana', 'volume': 1, 'author': 'Ai Yazawa', 'date': '2000-05-26', 'cover_image': 'mangas/nana.jpg'}
        ]
    }
]

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'


class Command(BaseCommand):
    help = 'Initialisation des catégories et mangas'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        # Suppression des anciennes données
        Manga.objects.all().delete()
        Category.objects.all().delete()
        Author.objects.all().delete()

        for data_category in CATEGORIES:
            category, _ = Category.objects.get_or_create(
                name=data_category['name'],
                defaults={'description': data_category['description'], 'slug': slugify(data_category['name'])}
            )

            for data_manga in data_category['mangas']:
                author, _ = Author.objects.get_or_create(name=data_manga['author'])

                Manga.objects.create(
                    title=data_manga['title'],
                    slug=slugify(f"{data_manga['title']}-vol{data_manga['volume']}"),
                    volume=data_manga['volume'],
                    author=author,
                    category=category,
                    description=f"{data_manga['title']} est un manga célèbre de {data_manga['author']}.",
                    date=data_manga['date'],
                    isbn=self.generate_isbn(),
                    cover_image=data_manga['cover_image']
                )

        # Création du superutilisateur
        if not UserModel.objects.filter(username=ADMIN_USERNAME).exists():
            UserModel.objects.create_superuser(ADMIN_USERNAME, 'admin@example.com', ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS("Données initialisées avec succès !"))

    @staticmethod
    def generate_isbn():
        """ Génère un ISBN fictif aléatoire """
        return f"978-{random.randint(100000000, 999999999)}"
