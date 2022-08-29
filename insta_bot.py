from instabot import Bot

my_bot= Bot()
#Firstly login to the account
#type the required credentials below
my_bot.login (username="itachi_legemd",password="Mani@123")
#Account logs In
my_bot.follow("_itsnoriana")
#it follows single user
my_bot.follow_users(["arianagrande","jogia","gabi"])
#enter the user_ids to follow them
my_bot.unfollow_non_followers()
#it unfollows all the non-followers
#now uploading an image
my_bot.upload_photo("810254.jpe",captions="pubg")
#mss dm
my_bot.send_message("kimguuuu","monkey_dluffy06")
#liking
my_bot.like_user("___iam_mk___",amount=50,filtration=False)
#comment
user_id=my_bot.get_user_id_from_username("___iam_mk___")
media_id=my_bot.get_last_user_medias(user_id,1)
my_bot.comment(media_id[0],"awesome bro")
#get followers list
followers_list=my_bot.get_user_followers("fuku.ro31")
following_list=my_bot.get_user_following("fuku.ro31")
for count,each_follower in enumerate(followers_list):

    print(my_bot.get_user_followers(each_follower))
for each_follow in following_list:
    print(my_bot.get_username_from_user_id(each_follow))
