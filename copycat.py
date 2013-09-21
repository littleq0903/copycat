#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__ = ['copy', 'paste', 'list', 'delete']
import pyclip
import os
import json


DEFAULT_COPYCAT_STORE = os.path.join(os.path.expanduser("~"), '.copycat_store')
DEFAULT_CONFIG_FILE = os.path.join(os.path.expanduser("~"), '.copycat')

def readfile(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return None

SOURCE = readfile(DEFAULT_CONFIG_FILE) or "{}"
CONFIG = json.loads(SOURCE)
COPY_STORE = CONFIG.get('COPY_STORE') or DEFAULT_COPYCAT_STORE

class Storage(object):
    stack_len = 10

    def __init__(self, path=COPY_STORE):    
        source = readfile(path) or "{}"
        data = json.loads(source)
        self._reg = data.get('reg', {})
        self._stack = data.get('stack', [None]*self.stack_len)[:self.stack_len]
        self._path = path

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        data = {}
        data['reg'] = self._reg
        data['stack'] = list(self._stack)[:self.stack_len]
        with open(self._path, 'w+') as f:
            f.write(json.dumps(data))

    def save(self, value, name=None):
        if not name:
            self._stack.insert(0, value)
        elif name and name.isdigit() and int(name) < self.stack_len:
            self._stack[int(name)] = value
        else:
            self._reg[name] = value

    def get(self, name=None):
        if not name:
            return self._stack[0]
        elif name and name.isdigit() and int(name) < self.stack_len:
            return self._stack[int(name)]
        else:
            return self._reg.get(name, None)

    def delete(self, name):
        try:
            del self._reg[name]
        except:
            print 'no reg {}'.format(name)

    def list(self):
        template = "{}:{}"
        for i, v in enumerate(self._stack):
            print template.format(i, v)
        for i, v in self._reg.items():
            print template.format(i, v)


def paste(name=None):
    with Storage() as storage:
        if not name:
            data = pyclip.paste() or storage.get()
        else:
            data = storage.get(name)
        pyclip.copy(data)
        return data
    
def copy(name=None, value=None):
    with Storage() as storage:
        storage.save(value, name=name)
        if not name:
            pyclip.copy(value)

def delete(name):
    with Storage() as storage:
        storage.delete(name)

def view():
    with Storage() as storage:
        storage.list()


if __name__ == '__main__':
    __all__ = ['copycat']
    import sys
    def copycat(value=None, name=None, paste=False, list=False, delete=False):
        '''
        option:
        -p, --paste
        -d, --delete
        -l, --list
        -n=<str>, --name=<str>
        '''
        
        if paste:
            print globals()['paste'](name)
        elif delete:
            globals()['delete'](name)
        elif list:
            globals()['view']()
        else:
            globals()['copy'](name, value)

    import clime.now
