class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def write_lines(self, strings):
        self.file.writelines(strings)
        print(f'wrote {len(strings)} lines')


    def __getattr__(self, item):
        return getattr(self.__dict__['file'], item)


    def  __iter__(self):
        return self.file.__iter__()


    def  __next__(self):
        return self.file.__next__()



    def __setattr__(self, key, value):
        if key == 'file':
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['file'], key , value)


    def __delattr__(self, item):
        delattr(self.__dict__['file'], item )


if __name__ == '__main__':
    file = FileWithLogging(open('hello.txt', 'w'))
    file.write_lines(['hello', 'world'])
    #file.write('hello')
    file.type = 'txt'
    print(file.type)
    del file.type
    print(file.type)
    file.close()

