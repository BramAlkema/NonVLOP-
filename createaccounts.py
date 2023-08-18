import subprocess
import re
from faker import Faker
import random
import os
import argparse
import time
import base64

parser = argparse.ArgumentParser(description='Create random bots to be used in a scenario.')
parser.add_argument('--num',required=True)
parser.add_argument('--country', required=False)
parser.add_argument('--dest',required=True)
parser.add_argument('--domain',required=True)

args = parser.parse_args()


fake = None
if args.country:
        fake = Faker(args.country)
else:
        fake = Faker()

numberofaccounts = int(args.num)
id = 0
while id < numberofaccounts:
        time.sleep(5)
        
        profile = fake.profile()
        displayname = profile['name']
        email = profile['mail']
        username = profile['username']
        
        print(displayname)
        print(username)
        print(email)

        note = subprocess.getoutput('motivate --no-colors').splitlines()[0]
        print(note)
        
        # create a random avatar
        imagefile = base64.b64encode(str.encode(username)).hex() + ".jpg"
        subprocess.getoutput("curl 'https://thispersondoesnotexist.com/image' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:75.0) Gecko/20100101 Firefox/75.0' -H 'Accept: image/webp,*/*' -H 'Accept-Language: nl,en-US;q=0.7,en;q=0.3' --compressed -H 'Connection: keep-alive' -H 'Referer: https://thispersondoesnotexist.com/' -H 'Cookie: __cfduid=db38cb5d4bab72bdbabdf512c8123ddca1588168831' -H 'If-Modified-Since: Wed, 29 Apr 2020 14:00:31 GMT' -H 'If-None-Match: \"5ea9887f-ce0ac\"' -H 'Cache-Control: max-age=0, no-cache' -H 'TE: Trailers' -H 'Pragma: no-cache' --output /home/mastodon/avatars/"+imagefile)
        avatar = imagefile
        subprocess.getoutput("convert -resize 256x256 /home/mastodon/avatars/%s /home/mastodon/avatars/%s" % (imagefile,imagefile))
        print(avatar)
        
        
        output = subprocess.getoutput('RAILS_ENV=production /home/mastodon/live/bin/tootctl accounts create '+username+' --email "' + email + '" --confirmed --role user --reattach --force')
        print(output)

        # verify that account is created
        if re.search("OK",output):
                print("success")

                # extract the password
                password = re.findall('New password: ([a-z0-9]+)',output)[0]
                print(password)

                # confirm the account
                output = subprocess.getoutput('RAILS_ENV=production /home/mastodon/live/bin/tootctl accounts modify '+username+' --approve ')
                print(output)

                
                # create login credentials for the bot
                output = subprocess.getoutput('/usr/bin/madonctl config dump -i %s -L %s -P %s > %s/%s.yaml' % (args.domain,email,password,args.dest,username))
                print(output)
        
        
	        # configure the account
                output = subprocess.getoutput('/usr/bin/madonctl --config %s/%s.yaml account update --avatar /home/mastodon/avatars/%s --display-name "%s"' % (args.dest,username,avatar,displayname))
                print(output)
        else:
                print("failed to create account")
        id = id + 1
