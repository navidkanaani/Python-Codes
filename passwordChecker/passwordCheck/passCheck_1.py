import requests
import hashlib
import sys

# send request to api


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error: {res.status_code}, check the api')
    return res


# split passwords which returned from api
def seperate_password(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


# convert password to hash code
def pwned_check(password):
    # check the password if exist or not
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return seperate_password(response, tail)


# give passwords from user and send it to converter func
def main(args):
    for password in args:
        count = pwned_check(password)
        if count:
            print(f'{password} was found {count} times...')
        else:
            print(f'{password} was NOT found. It is Safe')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
