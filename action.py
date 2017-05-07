# =========================================
# Makers! Implement your own actions here.
# =========================================

p = None
class playChess(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, voice_command):

        move = voice_command.replace(self.keyword, '', 1)

        global p
        if (p == None):
           p = subprocess.Popen(["/usr/games/gnuchess","-q"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)

        p.stdin.write(bytes(move.lower() + '\n', 'utf-8'))
        p.stdin.flush()

        response = ""
        if all(x.isalpha() or x.isspace() for x in move):
           # no numbers (d2d4) so its a command like new,undo,remove
           response = p.stdout.readline().decode("utf-8")
           response = "ok," + move
        else:
            self.say("ok, you played," + move)

            while ("move" not in response):
              response = p.stdout.readline().decode("utf-8")
              logging.info("Chess log: %s", response)

        logging.info("Chess: %s", response)
        self.say(response)

    # =========================================
    # Makers! Add your own voice commands here.
    # =========================================

    actor.add_keyword(_('chess'), playChess(say,_('chess')))
