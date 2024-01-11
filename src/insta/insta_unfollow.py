from instapy import InstaPy

# `.unfollow_users` don't give amount more than 10
# see here: https://github.com/timgrossmann/InstaPy#unfollowing
# also, i am assuming this s a account that will be run only for the bot
# so I am not setting `onlyInstapyFollowed` to False, this will follow any 10 users from all the following users

from insta_utils import InstaUtils

try:
    insta_utils = InstaUtils(username="geekodour", password="strongpassword", nogui=True)
    insta_utils.login()
    insta_utils.unfollow_users(amount=10, onlyInstapyFollowed=False)
    insta_utils.end()
except Exception as e:
    print(f"An error occurred: {str(e)}")

insta_utils = InstaUtils(username="geekodour", password="strongpassword", nogui=True)\
  .login()\
  .unfollow_users(amount=10, onlyInstapyFollowed = False ) \
  .end()
