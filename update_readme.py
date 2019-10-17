import os
import re


def update(directory, problems):
    '''
    根据directory下新解决题目的.md,.py，在readme文档中更新
    :param directory: str，为'easy','medium','hard'
    :problems: list 题目名（文件名)
    :return:
    '''
    tags = []
    for problem in problems:
        tags.append(r'[{name}](./{level}/{name}.md)|[{name}.py](./{level}/{name}.py)'
                    .format(name=problem, level=directory)
                    + '\n')

    with open('README.md', 'r', encoding='UTF-8') as readme:
        content = readme.readlines()

    aim = '### ' + directory.capitalize()  # as the level written in README is in capitalized form
    flag = False
    for index, line in enumerate(content):
        if aim in line:
            flag = True
        if flag is True and line == '\n':
            # index += 3  # markdown列表的两行跳过
            for tag in tags:
                content.insert(index, tag)
                index += 1
                print('successfully insert')
            break

    with open('README.md', 'w', encoding='UTF-8') as readme:
        readme.writelines(content)

def get_problem_names(directory):
    '''
    返回对应难度下全部的题目名称（无后缀）
    :param directory: str 对应难度的文件夹名
    :return: list
    '''
    names=[]
    for file in os.listdir(r'./{directory}'.format(directory=directory)):
        if file[-2:]=='md':
            names.append(file[:-3])

    return names

if __name__ == '__main__':
    directory = 'medium'
    # problems=get_problem_names(directory)
    problems=['015_3Sum']
    update(directory, problems)
