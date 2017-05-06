class playChess(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, voice_command):
        move = voice_command.replace(self.keyword, '', 1) 
        self.say("ok, you played," + move)

        p = subprocess.Popen(["/usr/games/gnuchess","-x"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        p.stdin.write(bytes(move + '\n', 'utf-8'))
        p.stdin.flush()

        newmove = ""
        while ("move" not in newmove):
           newmove = p.stdout.readline().decode("utf-8")

        self.say(newmove)

        p.stdin.write(bytes('quit\n', 'utf-8'))
        p.stdin.flush()

actor.add_keyword(_('chess'), playChess(say,_('chess')))
