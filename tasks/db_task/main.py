from tasks.db_task.dao.genre_dao import GenreDAO
from tasks.db_task.dao.platform_dao import PlatformDAO
from tasks.db_task.models.genre import Genre
from tasks.db_task.models.platform import Platform

if __name__ == '__main__':
    new_pl = Platform(platform_name="XboxOne")
    new_pl2 = Platform(platform_name="XboxOne1")
    new_pl3 = Platform(platform_name="XboxOne3")

    pl_from_db = PlatformDAO.add_records(new_pl, new_pl2, new_pl3)
    print(pl_from_db)
    for pl in pl_from_db:
        found_pl = PlatformDAO.get_records_by_attributes(pl.__dict__)[0]
        print(pl, found_pl, pl == found_pl)
        PlatformDAO.delete_record(pl.__dict__)

    new_genre1 = Genre("Fighting")
    new_genre2 = Genre("Strategy")

    genres_from_db = GenreDAO.add_records(new_genre1, new_genre2)
    print(genres_from_db)
    for genre in genres_from_db:
        found_genre = GenreDAO.get_records_by_attributes(genre.__dict__)[0]
        print(genre, found_genre, genre == found_genre)
        GenreDAO.delete_record(genre.__dict__)
