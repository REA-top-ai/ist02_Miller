from sqlalchemy.orm import Session, joinedload
from models import Author, Post, Comment
from sqlalchemy import func, desc, cast, Date
from datetime import datetime, date
def create_author(session: Session, name: str, email: str) -> Author:
    new_author = Author(name=name, email=email)
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author

def get_author_by_email(session: Session, email: str) -> Author | None:
    return session.query(Author).filter(Author.email == email).first()

def create_post(session: Session, title: str, content: str,
                author_id: int, published: bool = False) -> Post:
    new_post = Post(
        title = title,
        content=content,
        author_id=author_id,
        published=published
    )
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post

def get_published_posts(session: Session, limit: int=10) -> list[Post]:
    return session.query(Post).filter(Post.published == True).limit(limit).all()

def get_posts_by_author(session: Session, author_id: int, limit: int=10) -> list[Post]:
    return session.query(Post).filter(Post.author_id == author_id).limit(limit).all()

def update_post_status(session: Session, post_id: int, published: bool) -> bool:
    post = session.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return False
    post.published = published
    session.commit()
    return True

def add_comment(session: Session, post_id: int, author_name: str, text:str) -> Comment:
    new_comment = Comment(
        post_id = post_id,
        author_name=author_name,
        text = text
    )
    session.add(new_comment)
    session.commit()
    session.refresh(new_comment)
    return new_comment

def get_top_authors_by_posts(session: Session, limit: int = 3) -> list[tuple[str, int]]:
    from sqlalchemy import func, desc
    result = (session.query(
        Author.name,
        func.count(Post.id).label('post_count')
    )
        .join(Post)
        .group_by(Author.id)
        .order_by(desc('post_count'))
        .limit(limit)
        .all())
    return result

# Самостоятельная работа
def get_author_by_name(session: Session, name: str,) -> Author | None:
    return session.query(Author).filter(Author.name == name).first()

def get_published_posts_by_date(session: Session, target_date: date) -> list[Post]:
    return session.query(Post).filter(
        Post.published == True,
        cast(Post.created_at, Date) == target_date).all()

def create_authors_bulk(session: Session, authors_data: list[tuple[str, str]]) -> list[Author]:
    created_authors = []
    for name, email in authors_data:
        existing = session.query(Author).filter((Author.email == email) | (Author.name == name)).first()
        if existing:
            print(f"Автор {name} уже существует, пропускаем...")
            continue
        author = Author(name=name, email=email)
        session.add(author)
        created_authors.append(author)
    session.commit()
    for author in created_authors:
        session.refresh(author)
    return created_authors

def get_post_with_comments(session: Session, post_id: int) -> dict | None:
    post = session.query(Post).options(joinedload(Post.author),joinedload(Post.comments)).filter(Post.id == post_id).first()
    if not post:
        return None
    comments_list = []
    for comment in post.comments:
        comments_list.append({'id': comment.id, 'author_name': comment.author_name, 'text': comment.text, 'created_at': comment.created_at})
    result = {'post': {'id': post.id,
                       'title': post.title,
                       'content': post.content,
                       'published': post.published,
                       'created_at': post.created_at,
                       'author_name': post.author.name if post.author else 'Unknown'
                },
                'comments': comments_list,
                'comments_count': len(comments_list)
            }
    return result