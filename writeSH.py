# topics = ['three', 'average', 'support', 'business', 'america', 'romney', 'congress', 'nearly', 'governor', 'child', 'program', 'nation', 'increase', 'office', 'democrat', 'house', 'national', 'county', 'dollar', 'medicare', 'public', 'senate', 'florida', 'money', 'spending', 'united', 'insurance', 'wisconsin', 'first', 'school', 'country', 'barack', 'voted', 'since', 'texas', 'republican', 'government', 'every', 'billion', 'budget', 'federal', 'american', 'would', 'people', 'million', 'president', 'health', 'obama', 'percent', 'state']

# for t in topics:
#     f=open('fakeBulkScripts/'+t+'.sh', 'w')
#     line=['nohup python scweet.py --words "'+t+'" --until 2017-07-28 --since 2014-07-26 --limit 5 --interval 1 --display_type Latest --lang="en" --headless True >all_dir_log/fake_dir_log/log_'+t+'.txt>&1 &']
#     f.writelines(line)
#     f.close()

# f = open('fakeBulkCommand.sh', 'w')
# astr=''
# for t in topics:
#     astr = astr + 'sh fakeBulkScripts/'+t+'.sh & '
# astr = astr[:-2]
# f.writelines([astr])
# print(astr)


# topics = ['always', 'bitch', 'check', 'great', 'listen', 'location', 'mention', 'someone', 'today', 'brown', 'followback', 'senior', 'light', 'opening', 'really', 'thanks', 'friday', 'listening', 'morning', 'tonight', 'tweet', 'would', 'first', 'class', 'spotify', 'united', 'please', 'service', 'friend', 'never', 'remix', 'thing', 'following', 'people', 'right', 'going', 'heart', 'still', 'looking', 'think', 'world', 'engineer', 'bbtweetmedia', 'hiring', 'album', 'justinbieber', 'night', 'manager', 'follow', 'follower']
# for t in topics:
#     f=open('hashBulkScripts/'+t+'.sh', 'w')
#     line=['nohup python scweet.py --words "'+t+'" --until 2011-11-30 --since 2011-09-01 --limit 40 --interval 1 --display_type Latest --lang="en" --headless True >all_dir_log/hash_dir_log/log_'+t+'.txt>&1 &']
#     f.writelines(line)
#     f.close()

# f = open('hashBulkCommand.sh', 'w')
# astr=''
# for t in topics:
#     astr = astr + 'sh hashBulkScripts/'+t+'.sh & '
# astr = astr[:-2]
# f.writelines([astr])
# print(astr)



topics = ['start', 'working', 'great', 'nomaskonme', 'political', 'socialdistancing', 'testing', 'freedom', 'place', 'question', 'stayhome', 'control', 'djitchyfingazz', 'first', 'hospital', 'listenliveon', 'ourapponplaystore', 'spinning', 'total', 'websiteonbio', 'saying', 'house', 'india', 'openamericanow', 'enough', 'thank', 'american', 'closetheschools', 'masksoff', 'person', 'store', 'social', 'vaccine', 'better', 'another', 'covid_19', 'quarantine', 'spread', 'wearamasksavealife', 'quarantinelife', 'schoolreopening', 'anyone', 'positive', 'getting', 'realdonaldtrump', 'around', 'business', 'others', 'someone', 'family', 'masksdontwork', 'protect', 'child', 'mandatory', 'month', 'never', 'covidー19', 'really', 'could', 'number', 'without', 'every', 'maskssavelives', 'world', 'nomask', 'government', 'public', 'health', 'staysafestayhome', 'country', 'state', 'corona', 'everyone', 'pandemic', 'please', 'firefauci', 'thing', 'today', 'trump', 'still', 'covid', 'wearamask', 'covid-19', 'right', 'think', 'death', 'fauci', 'going', 'would', 'virus', 'drfauci', 'school', 'stayhomestaysafe', 'wearing', 'wearadamnmask', 'nomasks', 'people', 'coronavirus', 'covid19', 'lockdown']
for t in topics:
    f=open('stanceBulkScripts/'+t+'.sh', 'w')
    line=['python scweet.py --words "'+t+'" --until 2020-08-21 --since 2020-07-15 --limit 100 --interval 1 --display_type Latest --lang="en" --headless True']
    #line=['nohup python scweet.py --words "'+t+'" --until 2020-08-21 --since 2020-07-15 --limit 100 --interval 1 --display_type Latest --lang="en" --headless True >all_dir_log/stance_dir_log/log_'+t+'.txt>&1 &']
    f.writelines(line)
    f.close()

f = open('stanceBulkCommand.sh', 'w')
astr=''
for t in topics:
    astr = astr + 'sh stanceBulkScripts/'+t+'.sh & '
astr = astr[:-2]
f.writelines([astr])
print(astr)





# topics = ['everyone', 'stupid', 'always', 'world', 'supremacist', 'friend', 'could', 'money', 'around', 'saying', 'someone', 'child', 'going', 'asian', 'called', 'thing', 'alien', 'every', 'trump', 'american', 'lesbian', 'trash', 'retard', 'never', 'racist', 'violence', 'still', 'really', 'right', 'ghetto', 'refugee', 'would', 'queer', 'country', 'think', 'retarded', 'illegal', 'immigrant', 'raped', 'faggot', 'black', 'fucking', 'muslim', 'nigger', 'woman', 'nigga', 'people', 'bitch', 'number', 'white']

# for t in topics:
#     f=open('hateBulkScripts/'+t+'.sh', 'w')
#     line=['nohup python scweet.py --words "'+t+'" --until 2020-01-09 --since 2019-09-30 --limit 20 --interval 1 --display_type Latest --lang="en" --headless True >all_dir_log/hate_dir_log/log_'+t+'.txt>&1 &']
#     f.writelines(line)
#     f.close()

# f = open('hateBulkCommand.sh', 'w')
# astr=''
# for t in topics:
#     astr = astr + 'sh hateBulkScripts/'+t+'.sh & '
# astr = astr[:-2]
# f.writelines([astr])
# print(astr)
