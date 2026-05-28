from database import SessionLocal, engine, Base
from models import Author, Post, Comment
from crud import *

def main():
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        print("Начинаем тестирование...\n")

        print("Создаем авторов...")
        author1 = create_author(session, "Анна Петрова", "anna@example.com")
        author2 = create_author(session, "Иван Сидоров", "ivan@example.com")
        print(f"{author1.name} (id={author1.id})")
        print(f"{author2.name} (id={author2.id})")

        print("Создаем посты...")
        post1 = create_post(session, "Первый пост", "Это содержание первого поста. Оно достаточно длинное.",
                            author1.id, published=True)
        post2 = create_post(session, "Черновик", "Этот пост пока не опубликован.",
                            author1.id, published=False)
        post3 = create_post(session, "Пост Ивана", "Текст от Ивана.", author2.id,
                            published=True)
        print(f"'{post1.title}' (опубликован)")
        print(f"'{post2.title}' (черновик)")
        print(f"'{post3.title}' (опубликова)\n")

        print("Добавляем комментарии...")
        add_comment(session, post1.id, "Читатель1", "Отличная статья, очень полезно!")
        add_comment(session, post1.id, "Читатель2", "Спасибо за материал, жду продолжения.")
        add_comment(session, post1.id, "Аноним", "Коротко.")
        print("3 комментария добавлены к первому посту\n")
        print("Публикуем черновик...")
        success = update_post_status(session, post2.id, published=True)
        if success:
            print(f"'{post2.title}' теперь опубликован\n")
        print("Все опубликованные посты:")
        published = get_published_posts(session)
        for post in published:
            print(f"'{post.title}' - автор: {post.author.name}")
        print()

        print("Топ авторов по количеству постов:")
        top_authors = get_top_authors_by_posts(session, limit=3)
        for rank, (name, count) in enumerate(top_authors, 1):
            print(f"{rank}. {name}: {count} пост(ов)")
        print()

        print("Поиск автора по email...")
        found = get_author_by_email(session, "anna@example.com")
        if found:
            print(f"Найдено: {found.name}")
        else:
            print("Автор не найден")

        print("Поиск автора по имени...")
        author_by_name = get_author_by_name(session, "Иван Сидоров")
        if author_by_name:
            print(f"Найден автор: {author_by_name.name}, email: {author_by_name.email}")
        else:
            print("Автор не найден")

        today = datetime.now()
        post_by_date = get_published_posts_by_date(session, today)
        print(f"Посты, опубликованные {today.strftime('%Y-%m-%d')}:")
        if post_by_date:
            for post in post_by_date:
                print(f"'{post.title}' - автор: {post.author.name}")
        else:
            print("Нет опубликованных постов за эту дату")

        authors_bulk = [
            ("Алина Бабаева", "alina@example.com"),
            ("Тимур Бабаев", "timur@example.com"),
            ("Даша Линкина", "dasha@example.com")
        ]
        new_authors = create_authors_bulk(session, authors_bulk)
        for author in new_authors:
            print(f"{author.name} (email: {author.email})")

        post_with_comments = get_post_with_comments(session, post1.id)
        if post_with_comments:
            print(f"Пост: '{post_with_comments['post']['title']}'")
            print(f"Автор: {post_with_comments['post']['author_name']}")
            print(f"Содержание: {post_with_comments['post']['content'][:50]}...")
            print(f"Комментарии ({post_with_comments['comments_count']}):")
            for comment in post_with_comments['comments']:
                print(f" {comment['author_name']}: {comment['text']}")
        else:
            print("Пост не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
        session.rollback()
    finally:
        session.close()
        print("\nТестирование завершено. Сессия закрыта.")


if __name__ == "__main__":
    main()