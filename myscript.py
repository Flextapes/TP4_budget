import os

GOOD_HASH = 'e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'
BAD_HASH = 'c1a4be04b972b6c17db242fc37752ad517c29402'
TEST_COMMAND = 'python manage.py test'

def execute(command: str):
    print(f'{command} :')
    print(os.system(command))

if __name__ == '__main__':
    execute(f'git bisect start {BAD_HASH} {GOOD_HASH}')
    execute(f'git bisect run {TEST_COMMAND}')
    execute(f'git bisect reset')
