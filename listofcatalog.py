from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Catalog, Base, CatalogItem, User

engine = create_engine('sqlite:///catalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543' +
             '/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# catagories  for Soccer
catalog1 = Catalog(user_id=1, name="Soccer")

session.add(catalog1)
session.commit()

catalogItem1 = CatalogItem(user_id=1,
                           name="Shinguard",
                           description="Shinguard for Soccer",
                           catalog=catalog1)

session.add(catalogItem1)
session.commit()


catalogItem2 = CatalogItem(user_id=1,
                           name="Soccer Cleats",
                           description="Soccer Cleats for Soccer",
                           catalog=catalog1)

session.add(catalogItem2)
session.commit()


# Menu for Super Stir Fry
catalog2 = Catalog(user_id=1, name="Snow Boarding")

session.add(catalog2)
session.commit()


catalogItem1 = CatalogItem(user_id=1,
                           name="Snowboard",
                           description="Snowboard for sking",
                           catalog=catalog2)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1,
                           name="Goggles",
                           description="Goggles for sking",
                           catalog=catalog2)

session.add(catalogItem2)
session.commit()

print "added menu items!"
