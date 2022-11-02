import os

GOOD_HASH = 'e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'
BAD_HASH = 'c1a4be04b972b6c17db242fc37752ad517c29402'
TEST_COMMAND = 'python manage.py test'

if __name__ == '__main__':
    os.system(f'git bisect start {BAD_HASH} {GOOD_HASH}')
    os.system(f'git bisect run {TEST_COMMAND}')
    os.system(f'git bisect reset')
