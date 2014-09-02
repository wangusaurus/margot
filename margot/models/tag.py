"""
There's a many-to-many relationship between wallpapers and tags.

I know, this violates normal form. I like each tag having its own row, though,
in case we need to append metadata to them.
"""
from sqlalchemy import Column, String

from margot.database import Base


class Tag(Base):
    __tablename__ = 'tags'

    tag = Column(String, primary_key=True)
    # wallpapers attr created by many-to-many in wallpaper.py
