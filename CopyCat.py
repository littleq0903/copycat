#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyclip
import os
import json
import clime


DEFAULT_COPYCAT_STORE = os.path.join(os.path.expanduser("~"), '.copycat_store')
CONFIG_FILE = os.path.join(os.path.expanduser("~"), '.copycat')


def readfile(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return 

class Storage(object):
    stack_len = 10

    def __init__(self, path):    
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

    def show(self):
        template = "{}:{}"
        for i, v in enumerate(self._stack):
            print template.format(i, v)
        for i, v in self._reg.items():
            print template.format(i, v)


class CopyCat(object):
    
    def __init__(self):
        source = readfile(CONFIG_FILE) or "{}"
        data = json.loads(source)
        self.storage_file = data.get('COPY_STORE') or DEFAULT_COPYCAT_STORE
    
    def paste(self, name=None):
        with Storage(self.storage_file) as storage:
            if not name:
                data = pyclip.paste() or storage.get()
            else:
                data = storage.get(name)
            pyclip.copy(data)
            return data
        
    def copy(self, data, name=None):
        with Storage(self.storage_file) as storage:
            storage.save(data, name=name)
            if not name:
                pyclip.copy(data)
