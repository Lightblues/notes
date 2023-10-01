""" 
自动根据目录生成 docsify 的 _sidebar.md 文件

"""
import os,sys
from easonsi.util.leetcode import *
from easonsi import utils
os.chdir('docs')

dir = os.path.dirname(os.path.abspath(__file__))

forbidden = ['README.md', 'README_CN.md', 'media', 'resources']
def test_forbid(fn):
    if fn in forbidden: return True
    if fn.startswith('_'): return True
    return False

def build(dir):
    # if dir does not has README.md, then create one
    if not os.path.exists(os.path.join(dir, 'README.md')):
        with open(os.path.join(dir, 'README.md'), 'w') as f:
            f.write('\n\n')
    dlist, flist = [], []
    for f in os.listdir(dir if dir else '.'):
        if test_forbid(f): continue
        if os.path.isdir(os.path.join(dir, f)):
            dlist.append(f)
            # iterate
            build(os.path.join(dir, f))
        elif f.endswith('.md'):
            flist.append(f)
    # generate the markdown sidebar content
    if not dlist and not flist: return
    with open(os.path.join(dir, '_sidebar.md'), 'w') as f:
        for d in dlist:
            f.write(f'* [{d}]({dir}/{d}/README.md)\n')
        for ff in flist:
            f.write(f'* [{ff[:-3]}]({dir}/{ff})\n')

build('')


