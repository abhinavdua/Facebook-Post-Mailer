# Facebook-Post-Mailer script

The script uses a harcoded facebook group id to fetch the last 100 posts in a group, find specific keywords in the messages posted by users and then send a mail to the concerned people alerting them of the same.

The script needs an extended access token which can be generated by finding the short lived access token from the graph API explorer page and then requesting an extended token(valid for 60 days). The data retrieved from facebook is used to construct links for the posts and then send them out to the user in a mail using SMTP connection. The script can be run at fixed intervals using a cronjob.

Example usage: I used the script to filter out posts from the Pre-owned item sale group of my university. I wanted to buy a desk and hence in order to not go through 100s of posts everyday, I decided to make a script to automate the whole process. I ran the script every 2 hours and subsequently got a mail with the links pointing to the facebook posts.
