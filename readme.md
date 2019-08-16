这个是我自己的单词记录器(用于win10)
this is my customized helper for recording new English words(for windows 10).

它的功能非常简单,当然也没啥太大的作用
its use is really simple,which of course is really limited

按以下方式使用
use this following steps listed

        配置path环境变量
        configure path environment
            you have to set a environment named "WR_HOME"
                WR_HOME={your repository path}
            and then:
                path=%path%;WR_HOME/bin
        添加新单词,你可以在后面加注释(command: put)
        add a new word,and you can add a annotation after the word
            egg1:
                put hi
            egg2:
                put hello "你好"
            egg3:
                put transient "短暂的" "转瞬即逝的"

        删除新单词(command: delete)
        delete a wold(normally it is the last word)
            egg:
                delete

        获取今天记录的所有新单词(command: get)
        get all words you recorded today.
            egg:
                get
