from dotenv import load_dotenv
from os import listdir, getenv

load_dotenv()

settlement_nas = getenv('NAS_SHARE')

def reading_nas_share():

    count = 0
    for file in listdir(settlement_nas):
        count += 1
    print('There are {} files in this NAS share path'.format(count))


if __name__ == '__main__':
    reading_nas_share()