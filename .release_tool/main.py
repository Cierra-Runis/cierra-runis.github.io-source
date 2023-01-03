'''
发布用 py 脚本
'''

import os

if __name__ == '__main__':
    os.system('cls')
    print('-- main.py --')

    print('> 清除旧构建')
    os.system('hexo clean')

    print('> 获取最新 bangumi 资讯')
    os.system('hexo bangumi -u')

    print('> 构建中')
    os.system('hexo generate')

    print('> 发布中')
    os.system('hexo deploy')

    print('> 同步本仓库中')
    os.system('git add .')
    print('> 请输入一段信息: ')
    release_str = input().replace('\n', ' ')
    os.system(f'git commit -m "{release_str}"')
    os.system('git push')
    print(f'> 已发布携带信息为 "{release_str}" 的仓库, 请检查发布情况')
