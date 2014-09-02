from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from margot.database import Base


wallpaper_tags = Table('wallpaper_tags', Base.metadata,
    Column('wallpaper_id', Integer, ForeignKey('wallpapers.id')),
    Column('tag', String, ForeignKey('tags.tag'))
)


class Wallpaper(Base):
    __tablename__ = 'wallpapers'

    id = Column(Integer, primary_key=True)
    image_id = Column(String, nullable=False)

    # Image metadata
    resx = Column(Integer, nullable=False)
    resy = Column(Integer, nullable=False)
    filetype = Column(String)

    tags = relationship('Tag', secondary=wallpaper_tags, backref='wallpapers')
