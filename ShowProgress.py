import time, sys

class TimeCount:
    phases = ['◑', '◒', '◐', '◓'],['-', '\\', '|', '/'],['◷', '◶', '◵', '◴']
    status = True
    progressing_status = True


    def progressing(self):
        while self.progressing_status:
            if self.i == 3:
                self.i = 0
            else:
                self.i += 1
            point = str('.' * (self.i +1))
            sys.stdout.write('\r  {} progressing {}' .format(self.phases[self.shape][self.i], point))
            sys.stdout.flush()
            time.sleep(0.1)


    def left_mins_count(self):
        while self.status:
            if self.i == 3:
                self.i = 0
            else:
                self.i += 1
            count = self.total_secs / 60
            sys.stdout.write('\r  {} {} minutes left'.format(self.phases[self.shape][self.i], round(count,2)))
            sys.stdout.flush()

            if self.total_secs < 0:
                self.status = False
                sys.stdout.flush()
                sys.stdout.write('\r\n')
                return

            else:
                self.total_secs = self.total_secs - 0.1

            time.sleep(0.1)

    def __init__(self,total_mins,progress_shape):
        self.i = 0
        self.total_secs = total_mins * 60
        if progress_shape:
            self.shape = progress_shape
        else:
            self.shape = 0

